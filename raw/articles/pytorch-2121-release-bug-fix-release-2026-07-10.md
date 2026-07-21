---

source_url: https://github.com/pytorch/pytorch/releases/tag/v2.12.1
ingested: 2026-07-10
sha256: f57ba8ab9c12a2b8fa7aba518f5e362b72f23ff62aa7264643966730ff597866
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