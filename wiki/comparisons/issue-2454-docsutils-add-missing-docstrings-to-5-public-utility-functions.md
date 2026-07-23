---
title: "Issue #2454: docs(utils): add missing docstrings to 5 public utility functions"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - open-source
---

# Issue #2454: docs(utils): add missing docstrings to 5 public utility functions

> **Source:** gh-huggingfaceoptimum-issue-2454-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/optimum/issues/2454 ingested: 2026-07-14 sha256: e1cce8b187290facb839d9620a83df3ebb862f847d99892f57a8c163fea0cfc9 blog_source: github:huggingface/optimum...
> **Sources:**
>   - gh-huggingfaceoptimum-issue-2454-2026-07-14.md
> **Links:**
- [Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [[Issue #14188: [Quantization] Fix ModelOpt pre-quantized loading]]
- [Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end]
- [Issue #8329: fix: replace list/List with Sequence in function parameter annotations]

## Key Findings

---
source_url: https://github.com/huggingface/optimum/issues/2454
ingested: 2026-07-14
sha256: e1cce8b187290facb839d9620a83df3ebb862f847d99892f57a8c163fea0cfc9
blog_source: github:huggingface/optimum
---
# Issue #2454: docs(utils): add missing docstrings to 5 public utility functions
**State:** open | **Author:** RavSinghChandan | **Created:** 2026-06-30T13:58:22Z
## What does this PR do?
Adds missing docstrings to five public utility functions across two files. Each docstring follows the HuggingFace documentation style.
**`optimum/utils/testing_utils.py` — 4 functions:**
| Function | Added |
|---|---|
| `require_diffusers` | One-line decorator description (consistent with `require_torch_gpu`, `require_ort_rocm`, etc.) |
| `require_timm` | One-line decorator description |
| `require_sentence_transformers` | One-line decorator description |
| `require_datasets` | One-line decorator description |
These four decorators were the only ones in the file without any docstring, making the module inconsistent.
**`optimum/utils/save_utils.py` — 1 function:**
| Function | Added |
|---|---|
| `maybe_load_preprocessors` | Full `Args`/`Returns`/`Example` docstring |
`maybe_save_preprocessors` (in the same file) already had a full docstring; `maybe_load_preprocessors` — which it calls — did not.
## Tests
No logic changed — documentation only.
`black --check` and `ruff check` both pass with no errors.

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [[Issue #14188: [Quantization] Fix ModelOpt pre-quantized loading]]
- [Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end]
- [Issue #8329: fix: replace list/List with Sequence in function parameter annotations]
