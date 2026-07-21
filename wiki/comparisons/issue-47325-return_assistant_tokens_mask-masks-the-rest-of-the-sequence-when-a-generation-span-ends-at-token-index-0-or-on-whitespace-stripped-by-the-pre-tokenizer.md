---
title: "Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - multimodal
  - open-source
  - rlhf
  - sft
  - system-design
  - use-case
  - zero-shot
---

# Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer

> **Source:** gh-huggingfacetransformers-issue-47325-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/issues/47325 ingested: 2026-07-14 sha256: 616b11979ef26e0915e017f8a9de58923bca6e2969ba47467fd3e45448510d02 blog_source: github:huggingface/t...
> **Sources:**
>   - gh-huggingfacetransformers-issue-47325-2026-07-14.md
> **Links:**
- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]
- [[Issue #14167: FlashPack support for transformers pipeline components]]
- [[Issue #8330: Dataset Studio and Viewer down]]
- [[Issue #3419: FIX Bug in forgetting metric in MetaMathQA]]
- [[Issue #3425: FIX Accept layers_to_transform=0 together with layers_pattern]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/issues/47325
ingested: 2026-07-14
sha256: 616b11979ef26e0915e017f8a9de58923bca6e2969ba47467fd3e45448510d02
blog_source: github:huggingface/transformers
---
# Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer
**State:** open | **Author:** sohumt123 | **Created:** 2026-07-14T16:42:44Z
### System Info
- `transformers` main (`fc7cf96`), `tokenizers` 0.22.2, Python 3.11 (macOS). The affected code path is unchanged on `main`, so this reproduces on recent releases as well.
### Reproduction
```python
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("gpt2")
# The assistant turn is the first content in the sequence, so the last token of
# its {% generation %} span is token index 0.
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
conversation,
chat_template=template,
tokenize=True,
return_assistant_tokens_mask=True,
return_dict=True,
)
print(tok.convert_ids_to_tokens(out["input_ids"]))
print(out["assistant_masks"])
```
Actual output on `main`:
```
['A', '', 'user', 'Ġmessage']
[1, 1, 1, 1, 1, 1, 1, 1]
```
The whole user turn is masked as assistant tokens.
### Expected behavior
Only the assistant span should be masked:
```
[1, 0, 0, 0, 0, 0, 0, 0]
```
### Root cause
In `PreTrainedTokenizerBase.apply_chat_template` (`src/transformers/tokenization_utils_base.py`), the end of each `{% generation %}` span is computed as:
```python
end_token = out.char_to_token(i, assistant_end_char - 1)
...
for token_id in range(start_token, end_token + 1 if end_token else len(input_ids[i])):
```
The ternary tests the **truthiness** of `end_token`, but `end_token` is legitimately falsy in two non-truncation cases:
1. `end_token == 0` — the span's last char maps to token index 0 (the assistant turn is the first content in the sequence), as in the gpt2 repro above. `0` is a valid token index.
2. `end_token is None` — `char_to_token` returns `None` because the span's last char has no aligned token, e.g. a trailing space inside `{% generation %}` that the pre-tokenizer strips. With `bert-base-uncased` (WordPiece) and a template whose generation block renders `message['content'] + ' '`:
```
tokens: ['hello', 'world', 'follow', '##up', 'question', 'here']
mask: [1, 1, 1, 1, 1, 1] # expected: [1, 1, 0, 0, 0, 0]
```
In both cases the loop silently falls through to `len(input_ids[i])` and masks every remaining token, labelling subsequent user/system turns as assistant tokens. Since `assistant_masks` is typically used to build SFT/RLHF loss masks, this silently trains on user/syste

## Summary

See Key Findings for full content.

## Related Articles

- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]
- [[Issue #14167: FlashPack support for transformers pipeline components]]
- [[Issue #8330: Dataset Studio and Viewer down]]
- [[Issue #3419: FIX Bug in forgetting metric in MetaMathQA]]
- [[Issue #3425: FIX Accept layers_to_transform=0 together with layers_pattern]]
