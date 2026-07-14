---
source_url: https://github.com/huggingface/transformers/issues/47326
ingested: 2026-07-14
sha256: f118ff36a494787eca5f86a78d622e2f0bc40a04fd871f4aab32ff982fbd4e11
blog_source: github:huggingface/transformers
---
# Issue #47326: Fix assistant tokens mask when a generation span ends at token index 0 or on stripped whitespace

**State:** open | **Author:** sohumt123 | **Created:** 2026-07-14T16:43:33Z

<!-- ci-dashboard-badge:start -->
[![CI](https://transformers-ci.lor-e.huggingface.cool/badge/pr?pr=47326)](https://transformers-ci.lor-e.huggingface.cool/d/pytest-observability-by-pr/pytest-observability-branch?var-pr=47326)
<!-- ci-dashboard-badge:end -->

# What does this PR do?

Fixes #47325.

`apply_chat_template(..., return_assistant_tokens_mask=True)` masks every token from the start of a `{% generation %}` span to the end of the sequence whenever `char_to_token(assistant_end_char - 1)` is falsy without the span being truncated, wrongly labelling later user/system turns as assistant tokens. This PR replaces the truthiness check with an explicit `is None` walk-back so the mask stops at the last real assistant token, while keeping the existing mask-to-end behavior for genuinely truncated spans.

## Problem

The end of each generation span is computed as:

```python
end_token = out.char_to_token(i, assistant_end_char - 1)
...
for token_id in range(start_token, end_token + 1 if end_token else len(input_ids[i])):
```

The ternary tests the truthiness of `end_token`, but `end_token` is legitimately falsy in two non-truncation cases:

1. **`end_token == 0`** — the span's last char maps to token index 0 because the assistant turn is the first content in the sequence. `0` is a valid token index.
2. **`end_token is None`** — the span's last char has no aligned token, e.g. a trailing space inside `{% generation %}` that a WordPiece pre-tokenizer strips.

In both cases the loop falls through to `len(input_ids[i])` and masks the rest of the sequence. Since `assistant_masks` is typically used to build SFT/RLHF loss masks, this silently trains on user/system text.

Minimal repro for case 1 (gpt2):

```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("gpt2")
template = (
    "{% for message in messages %}"
    "{% if message['role'] == 'assistant' %}"
    "{% generation %}{{ message['content'] }}{% endgeneration %}"
    "{% else %}{{ '<|user|>' + message['content'] }}{% endif %}"
    "{% endfor %}"
)
conversation = [
    {"role": "assistant", "content": "A"},
    {"role": "user", "content": "user message"},
]
out = tok.apply_chat_template(
    conversation, chat_template=template, tokenize=True,
    return_assistant_tokens_mask=True, return_dict=True,
)
print(tok.convert_ids_to_tokens(out["input_ids"]))
# ['A', '<', '|', 'user', '|', '>', 'user', 'Ġmessage']
print(out["assistant_masks"])
# main:      [1, 1, 1, 1, 1, 1, 1, 1]  <- whole user turn masked as assistant
# this PR:   [1, 0, 0, 0, 0, 0, 0, 0]
```

Case 2 with `bert-base-uncased` and a generation block rendering `message['content'] + ' '` goes from `[1, 1, 1, 1, 1, 1]` (everything masked) to `[1, 1, 0, 0, 0, 0]`. Full repro for both cases is in #47325.

## Fix

Instead of testing truthiness, scan backwards from `assistant_end_char - 1` towards `assistant_start_char` and take the first char that maps to a token as `end_token`. Only when no char in the span maps to a token (the span was truncated away entirely) fall back to masking to the end of the sequence — preserving the truncation semantics covered by the existing `test_chat_template_return_assistant_tokens_mask_truncated`.

## Tests

Added `test_chat_template_return_assistant_tokens_mask_edge_cases` to `tests/test_tokenization_common.py` with two subcases: an assistant-first span whose last token is index 0, and a generation block ending in a trailing space (with a comment on why byte-level BPE tokenizers make the boundary token ambiguous in the second case).

Running the new test plus the existing truncation test against `main`'s source (new test, pre-fix library):

```
$ pytest tests/models/gpt2/test_tokenization_gpt2.py -k "edge_cases or assistant_tokens_mask_truncated" -q
SUBFAILED[type (openai-community/gpt2)] tests/models/gpt2/test_tokenization_gpt2.py::GPT2TokenizationTest::test_chat_template_return_assistant_tokens_mask_edge_cases
1 failed, 2 passed, 61 deselected
```

On this branch:

```
$ pytest tests/models/gpt2/test_tokenization_gpt2.py -k "edge_cases or assistant_tokens_mask_truncated" -q
2 passed, 61 deselected, 2 subtests passed
```

The truncation test passes before and after, confirming the fallback semantics are unchanged.

## Differentiation from existing PRs

- #34531 (merged) fixed the **start** token being out of bounds under truncation; the falsy **end** token cases fixed here occur without truncation.
- huggingface/tokenizers#1640 fixed a start-token `None` case inside `tokenizers`; it does not touch this end-token truthiness check in `transformers`.
- #44543 (open) fixes all-zero masks on the multimodal **processor** path (`processing_utils.py`); no open PR addresses this tokenizer-path (`tokenization_utils_base.py`) bug.

## Note on AI assistance

Disclosure: this change was developed with AI assistance. I reviewed every changed line, reproduced the bug, and validated the fix and its tests locally, and I stand by the change. Coordination issue: #47325.

## Who can review?

@ArthurZucker @itazap