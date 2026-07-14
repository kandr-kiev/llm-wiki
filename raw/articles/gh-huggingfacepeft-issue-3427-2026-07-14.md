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