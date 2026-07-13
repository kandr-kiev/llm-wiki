---
title: "Issue #47258: [AudioFlamingo3] Fix bfloat16 dtype mismatch in audio encoder positional embedding"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - audio-generation
  - embedding
  - evaluation
  - foundation-model
  - open-source
  - review
  - self-supervised
---
# Issue #47258: [AudioFlamingo3] Fix bfloat16 dtype mismatch in audio encoder positional embedding

> **Source:** gh-huggingfacetransformers-issue-47258-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/issues/47258 ingested: 2026-07-11 sha256: 9d4281bae0f52ae9bf8f372a1708c5763ab8c66364d0163e6097aa1d8445badb blog_source: github:huggingface/t...
> **Sources:**
>   - gh-huggingfacetransformers-issue-47258-2026-07-11.md
> **Links:**
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14168-fix-batching-and-precomputed-embeddings-in-kandinsky-5-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-14169-remove-jaxflax]]
- [[issue-3421-fix-x-lora-adapter-name-mismatch-and-delete_adapter-desync]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/issues/47258
ingested: 2026-07-11
sha256: 9d4281bae0f52ae9bf8f372a1708c5763ab8c66364d0163e6097aa1d8445badb
blog_source: github:huggingface/transformers
---
# Issue #47258: [AudioFlamingo3] Fix bfloat16 dtype mismatch in audio encoder positional embedding
**State:** open | **Author:** snkii | **Created:** 2026-07-11T06:10:43Z
## What does this PR do?
Fixes a `RuntimeError` when loading `AudioFlamingo3ForConditionalGeneration` with `torch_dtype=torch.bfloat16`.
`AudioFlamingo3ForConditionalGeneration` inherits `_keep_in_fp32_modules_strict = ["embed_positions"]` from `VoxtralForConditionalGeneration`, keeping `embed_positions` in float32 even when the model is loaded in bfloat16. In `AudioFlamingo3AudioEncoder.forward()`, the positional embedding addition was missing the dtype cast that `VoxtralEncoder` already applies:
```python
# Before (AudioFlamingo3) — missing cast
hidden_states = inputs_embeds + self.embed_positions.weight
# inputs_embeds: bfloat16, embed_positions.weight: float32
# → hidden_states upcast to float32
# → LayerNorm(float32 input, bfloat16 weight) → RuntimeError: expected scalar type Float but found BFloat16
# After — consistent with VoxtralEncoder.forward()
hidden_states = (inputs_embeds + self.embed_positions.weight).to(inputs_embeds.dtype)
```
### Verification
MMAU-test (9,000 samples), bfloat16 + FlashAttention-2, scored via the official [sonalkum/MMAU-Eval](https://huggingface.co/spaces/sonalkum/MMAU-Eval) space:
| | accuracy |
|---|---|
| bs=5, before fix (dtype mismatch causes audio embedding contamination across samples) | 57.08% |
| bs=5, after fix | **72.40%** |
## Who can review?
@eustlb @vasqu

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14168-fix-batching-and-precomputed-embeddings-in-kandinsky-5-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-14169-remove-jaxflax]]
- [[issue-3421-fix-x-lora-adapter-name-mismatch-and-delete_adapter-desync]]
