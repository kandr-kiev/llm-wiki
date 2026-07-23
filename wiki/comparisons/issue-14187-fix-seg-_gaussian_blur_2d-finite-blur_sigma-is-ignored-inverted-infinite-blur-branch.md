---
title: "Issue #14187: Fix SEG `_gaussian_blur_2d`: finite `blur_sigma` is ignored (inverted infinite-blur branch)"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - image-generation
  - open-source
  - pipeline
  - real-time
  - self-supervised
  - standards
  - use-case
---

# Issue #14187: Fix SEG `_gaussian_blur_2d`: finite `blur_sigma` is ignored (inverted infinite-blur branch)

> **Source:** gh-huggingfacediffusers-issue-14187-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/diffusers/issues/14187 ingested: 2026-07-14 sha256: 3eee375a8478857841464c9fa2e990e0bc8c0b7bf334c46cdec03a85437c1609 blog_source: github:huggingface/diff...
> **Sources:**
>   - gh-huggingfacediffusers-issue-14187-2026-07-14.md
> **Links:**
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [Issue #2848: Implement multi-domain intake architecture and related specs]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #14169: Remove JAX/Flax]

## Key Findings

---
source_url: https://github.com/huggingface/diffusers/issues/14187
ingested: 2026-07-14
sha256: 3eee375a8478857841464c9fa2e990e0bc8c0b7bf334c46cdec03a85437c1609
blog_source: github:huggingface/diffusers
---
# Issue #14187: Fix SEG `_gaussian_blur_2d`: finite `blur_sigma` is ignored (inverted infinite-blur branch)
**State:** open | **Author:** XIONGPEILIN | **Created:** 2026-07-14T13:08:30Z
## What does this PR do?
Fixes a branch inversion in `SmoothedEnergyGuidanceHook` / `_gaussian_blur_2d`
(`src/diffusers/hooks/smoothed_energy_guidance_utils.py`) where the **finite-sigma** and
**infinite-blur** code paths are swapped. As a result any *finite* `blur_sigma` is silently
discarded and replaced by a uniform (spatial-mean) query, so sweeping finite sigma has no effect.
### The bug
```python
is_inf = sigma > sigma_threshold_inf
...
if is_inf: # sigma "infinite"
... 2D Gaussian conv ... # threshold` should give the spatial mean, and a finite sigma should be an actual
Gaussian blur.
2. **The original SEG-SDXL implementation** this function is "Copied/Modified from"
([pipeline_seg.py#L171-L175](https://github.com/SusungHong/SEG-SDXL/blob/cf8256d640d5373541cfea3b3b6caf93272cf986/pipeline_seg.py#L171-L175)):
```python
if not self.inf_blur: # finite sigma
query_ptb = gaussian_blur_2d(query_ptb, kernel_size, self.blur_sigma)
else: # infinite
query_ptb[:] = query_ptb.mean(dim=(-2, -1), keepdim=True)
```
Because the default `seg_blur_sigma=9999999.0` always takes the (huge-sigma ≈ uniform) conv branch,
the bug is masked for default usage and only surfaces when a finite sigma is requested.
### Reproduction
```python
import math, torch
from diffusers.hooks.smoothed_energy_guidance_utils import _gaussian_blur_2d
q = torch.randn(2, 1024, 8) # 1024 = 32x32 image-token grid
def run(sig):
ks = math.ceil(6 * sig) + 1 - math.ceil(6 * sig) % 2
return _gaussian_blur_2d(q.clone(), ks, sig, 9999.9)
print(torch.equal(run(4.0), run(16.0))) # main: True -> finite sigma has no effect
```
On `main`, different finite sigmas are byte-identical (`max|sig4 - sig32| = 0.0`). With this PR they
differ (larger sigma smooths more), while `sigma > threshold` returns the exact spatial mean.
### Fix
Swap the two branches: `is_inf` → spatial mean (exact uniform queries); finite sigma → the real 2D
Gaussian blur of standard deviation `sigma`.
### Note on behavior change
For the default (`sigma > threshold`) the output changes from a huge-kernel Gaussian conv (an
*approximate* uniform) to the *exact* spatial mean — matching the documented "uniform queries".
Finite `blur_sigma` values now actually control the blur amount. SEG is marked experimental in the
code, so this may affect users who relied on the (buggy) finite-sigma-as-uniform behavior.
## Before submitting
- [x] Read the [contributor guideline](https://github.com/huggingface/diffusers/blob/main/CONTRIBUTING.md).
- [x] `ruff check` / `ruff format` pass on the changed file.
- [ ] Happy to add a small regression test (finite sigmas di

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [Issue #2848: Implement multi-domain intake architecture and related specs]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #14169: Remove JAX/Flax]
