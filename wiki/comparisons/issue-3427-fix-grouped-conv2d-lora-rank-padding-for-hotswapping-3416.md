---
title: "Issue #3427: FIX grouped Conv2d LoRA rank padding for hotswapping (#3416)"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - foundation-model
  - lora
  - open-source
---

# Issue #3427: FIX grouped Conv2d LoRA rank padding for hotswapping (#3416)

> **Source:** gh-huggingfacepeft-issue-3427-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/peft/issues/3427 ingested: 2026-07-14 sha256: 5ed88525629c3ec6d63b431d34797704b326438f3511845a4bd1808761047e11 blog_source: github:huggingface/peft --- #...
> **Sources:**
>   - gh-huggingfacepeft-issue-3427-2026-07-14.md
> **Links:**
- [Issue #3420: Fix hotswapping for LoRA adapters targeting grouped Conv2d]
- [Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters]
- [Issue #47256: [serge] integration failure triage -](https://github.com/pytorch/pytorch/issues/47256)
- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]
- [Issue #8329: fix: replace list/List with Sequence in function parameter annotations]

## Key Findings

---
source_url: https://github.com/huggingface/peft/issues/3427
ingested: 2026-07-14
sha256: 5ed88525629c3ec6d63b431d34797704b326438f3511845a4bd1808761047e11
blog_source: github:huggingface/peft
---
# Issue #3427: FIX grouped Conv2d LoRA rank padding for hotswapping (#3416)
**State:** open | **Author:** eSVeeF | **Created:** 2026-07-13T19:18:05Z
Resolves #3416
### Description
The reported bug is this: `prepare_model_for_compiled_hotswap` failed when used with LoRA adapters targeting grouped `Conv2d` layers and a larger target rank.
For grouped convolutions, the second dimension of the LoRA B weight is stored per group rather than as the global LoRA rank. For example, with `groups=2` and rank 2, the stored LoRA B shape contains `rank // groups == 1` input channel per group. The hotswap padding code interpreted this dimension as the global rank, which produced an invalid padded layer shape and raised the generic "Something went wrong when trying to pad the LoRA weights" error.
Fixing the shape calculation exposed another issue: LoRA A channels must be copied per group rather than as a single prefix.
### Changes
- Account for the per-group LoRA B dimension when calculating the effective rank
- Allocate grouped LoRA B layers with `target_rank // groups` input channels per group
- Validate that the target rank is divisible by the convolution group count
- Preserve the group-local channel layout of LoRA A when padding
- Preserve the same layout when hotswapping a smaller grouped adapter into a padded model
- Keep the existing grouped-convolution behavior and merge limitation unchanged
### Tests
Added grouped Conv2d regression coverage based on existing tests
Validation:
- `TestHotSwapping`: 35 passed

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #3420: Fix hotswapping for LoRA adapters targeting grouped Conv2d]
- [Issue #3422: FIX TinyLoRA weight_tying [Issue #47256: [serge] integration failure triage -](https://github.com/pytorch/pytorch/issues/47256) #47256: [serge] integration failure triage -]]
- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]
- [Issue #8329: fix: replace list/List with Sequence in function parameter annotations]
