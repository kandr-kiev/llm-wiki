---
title: "Issue #47326: Fix assistant tokens mask when a generation span ends at token index 0 or on stripped whitespace"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - ci-cd
  - library
  - multimodal
  - open-source
  - real-time
  - review
  - rlhf
  - sft
  - system-design
  - use-case
  - zero-shot
---

# Issue #47326: Fix assistant tokens mask when a generation span ends at token index 0 or on stripped whitespace

> **Source:** gh-huggingfacetransformers-issue-47326-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/issues/47326 ingested: 2026-07-14 sha256: f118ff36a494787eca5f86a78d622e2f0bc40a04fd871f4aab32ff982fbd4e11 blog_source: github:huggingface/t...
> **Sources:**
>   - gh-huggingfacetransformers-issue-47326-2026-07-14.md
> **Links:**
- [[Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer]]
- [[Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]]
- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]
- [[Issue #47323: Fix deepgemm on multiple devices]]
- [[Issue #14167: FlashPack support for transformers pipeline components]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/issues/47326
ingested: 2026-07-14
sha256: f118ff36a494787eca5f86a78d622e2f0bc40a04fd871f4aab32ff982fbd4e11
blog_source: github:huggingface/transformers
---
# Issue #47326: Fix assistant tokens mask when a generation span ends at token index 0 or on stripped whitespace
**State:** open | **Author:** sohumt123 | **Created:** 2026-07-14T16:43:33Z
[![CI](https://transformers-ci.lor-e.huggingface.cool/badge/pr?pr=47326)](https://transformers-ci.lor-e.huggingface.cool/d/pytest-observability-by-pr/pytest-observability-branch?var-pr=47326)
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
"{% else %}{{ '' + message['content'] }}{% endif %}"
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
# ['A', '', 'user', 'Ġmessage']
print(out["assistant_masks"])
# main: [1, 1, 1, 1, 1, 1, 1, 1] <- whole user turn masked as assistant
# this PR: [1, 0, 0, 0, 0, 0, 0, 0]
```
Case 2 with `bert-base-uncased` and a generation block rendering `message['content'] + ' '` goes from `[1, 1, 1, 1, 1, 1]` (everything masked) to `[1, 1, 0, 0, 0, 0]`. Full 

## Summary

See Key Findings for full content.

## Related Articles

- [[Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer]]
- [[Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]]
- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]
- [[Issue #47323: Fix deepgemm on multiple devices]]
- [[Issue #14167: FlashPack support for transformers pipeline components]]
