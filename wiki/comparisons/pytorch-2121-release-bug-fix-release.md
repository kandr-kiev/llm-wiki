---
title: "PyTorch 2.12.1 Release, bug fix release"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - pytorch
---
# PyTorch 2.12.1 Release, bug fix release

> **Source:** pytorch-2121-release-bug-fix-release-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/pytorch/pytorch/releases/tag/v2.12.1 ingested: 2026-07-10 sha256: 24e097764f767f873a45d90982370d8df6b2abc15dbe848e84938515d1c9e6c5 blog_source: github --- # PyTorch...
> **Sources:**
>   - pytorch-2121-release-bug-fix-release-2026-07-10.md
> **Links:**
- [[release-notes-ollama-vv0312]]
- [[patch-release-v5104]]
- [[patch-release-v5121]]
- [[release-notes-llamacpp-vb9956]]
- [[release-v1140]]

## Key Findings

---
source_url: https://github.com/pytorch/pytorch/releases/tag/v2.12.1
ingested: 2026-07-10
sha256: 24e097764f767f873a45d90982370d8df6b2abc15dbe848e84938515d1c9e6c5
blog_source: github
---
# PyTorch 2.12.1 Release, bug fix release
## Release Notes
This release is meant to fix the following regressions and silent correctness issues:
## Regression fixes
- Fix nondeterministic outputs in test_batch_invariance with FLASH_ATTN on NVIDIA B200 GPUs ([#181248](https://github.com/pytorch/pytorch/issues/181248)), fixed by updating Triton to 3.7.1 ([#186814](https://github.com/pytorch/pytorch/pull/186814))
- Fix illegal memory access in the Triton convolution2d_bwd_weight kernel on B100/B200 (sm100) GPUs ([#187081](https://github.com/pytorch/pytorch/issues/187081)), fixed by updating Triton to 3.7.1 ([#186814](https://github.com/pytorch/pytorch/pull/186814))
- Fix fill_ on byte-dtype views with misaligned storage offset ([#186821](https://github.com/pytorch/pytorch/pull/186821))
## Releng / Build
- Drop CPython 3.13t from the binary build matrix ([#182951](https://github.com/pytorch/pytorch/pull/182951))
## Download
https://github.com/pytorch/pytorch/releases/tag/v2.12.1

## Summary

See Key Findings for full content.

## Related Articles

- [[release-notes-ollama-vv0312]]
- [[patch-release-v5104]]
- [[patch-release-v5121]]
- [[release-notes-llamacpp-vb9956]]
- [[release-v1140]]
