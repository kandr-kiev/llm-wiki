---
title: "Issue #2450: Fix #2407: Fix get_wikitext2 tokenization bug causing sequence length warning"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - ci-cd
  - foundation-model
  - open-source
  - review
---

# Issue #2450: Fix #2407: Fix get_wikitext2 tokenization bug causing sequence length warning

> **Source:** gh-huggingfaceoptimum-issue-2450-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/optimum/issues/2450 ingested: 2026-07-14 sha256: 626a53850e7c8be2069cf889ba3ffe29119f9f7021a823f81c18dc114524c875 blog_source: github:huggingface/optimum...
> **Sources:**
>   - gh-huggingfaceoptimum-issue-2450-2026-07-14.md
> **Links:**
- [Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]
- [Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse]
- [Issue #3419: FIX Bug in forgetting metric in MetaMathQA]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [Issue #14188: [Quantization] Fix ModelOpt pre-quantized loading](https://github.com/pytorch/pytorch/issues/14188)

## Key Findings

---
source_url: https://github.com/huggingface/optimum/issues/2450
ingested: 2026-07-14
sha256: 626a53850e7c8be2069cf889ba3ffe29119f9f7021a823f81c18dc114524c875
blog_source: github:huggingface/optimum
---
# Issue #2450: Fix #2407: Fix get_wikitext2 tokenization bug causing sequence length warning
**State:** open | **Author:** nandanadileep | **Created:** 2026-06-12T09:08:12Z
Fixes #2407
Changed `get_wikitext2` from concatenating 1000 entries into a single string and tokenizing all at once (producing 73K+ token sequences that exceed the model's max length), to per-sample tokenization with a retry loop matching `get_c4`/`get_c4_new`.
Local test infra unavailable in CI sandbox.
---
This change was prepared with AI assistance under human direction and review.

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]
- [Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse]
- [Issue #3419: FIX Bug in forgetting metric in MetaMathQA]
- [Issue #83[Issue #14188: [Quantization] Fix ModelOpt pre-quantized loading](https://github.com/pytorch/pytorch/issues/14188)ntization] Fix ModelOpt pre-quantized loading]]
