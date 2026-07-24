---
title: "Issue #123252: [PjRt-IFRT] Use HighwayHash for array hashing"
type: concept
tags:
  - llm-wiki
  - knowledge-base
    - open-source
  - tensorflow
  - use-case
confidence: medium
created: 2026-07-23
description: Auto-filled by Wiki Doctor
links: []
sources: []
updated: 2026-07-23
---

# Issue #123252: [PjRt-IFRT] Use HighwayHash for array hashing

> **Source:** gh-tensorflowtensorflow-issue-123252-2026-07-14.md
> **Type:** concept
> **Created:** 2026-07-22
> **Updated:** 2026-07-22
> **Confidence:** high
> **Description:** --- source_url: https://github.com/tensorflow/tensorflow/issues/123252 ingested: 2026-07-14 sha256: 2482efe9887cdf3d028d9b5bccf01887e6e6ecc8cd7c92f5740c247924afe97c blog_source: github:tensorflow/tens...
> **Sources:**
>   - gh-tensorflowtensorflow-issue-123252-2026-07-14.md
> **Links:**
- [Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer]
- [Issue #3425: FIX Accept layers_to_transform=0 together with layers_pattern]
- [Issue #3427: FIX grouped Conv2d LoRA rank padding for hotswapping (#3416)]
- [Issue #123251: PR #44403: [XLA:CPU] onednn_threadpool: cap num_workers at n in parallel_for](https://github.com/pytorch/pytorch/issues/123251)
- [Issue #14187: Fix SEG `_gaussian_blur_2d`: finite `blur_sigma` is ignored (inverted infinite-blur branch)]

## Key Findings

---
source_url: https://github.com/tensorflow/tensorflow/issues/123252
ingested: 2026-07-14
sha256: 2482efe9887cdf3d028d9b5bccf01887e6e6ecc8cd7c92f5740c247924afe97c
blog_source: github:tensorflow/tensorflow
---
# Issue #123252: [PjRt-IFRT] Use HighwayHash for array hashing
**State:** open | **Author:** copybara-service[bot] | **Created:** 2026-07-14T20:24:41Z
[PjRt-IFRT] Use HighwayHash for array hashing
This change replaces `tsl::Fingerprint64` with `HighwayHash` for IFRT array hashing.
`HighwayHash` is roughly 25.2% faster in a simple microbenchmark.

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer]
- [Issue #3425: FIX Accept layers_to_transform=0 together with layers_pattern]
- [Issue #3427: FIX grouped Conv[Issue #123251: PR #44403: [XLA:CPU] onednn_threadpool: cap num_workers at n in parallel_for](https://github.com/pytorch/pytorch/issues/123251)readpool: cap num_workers at n in parallel_for]]
- [Issue #14187: Fix SEG `_gaussian_blur_2d`: finite `blur_sigma` is ignored (inverted infinite-blur branch)]
