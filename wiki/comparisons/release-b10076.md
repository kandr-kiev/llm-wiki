---
title: "Release b10076"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - alignment
  - backend
  - claude
  - cuda
  - llama
  - open-source
  - real-time
  - use-case
---
backlinks:
  - release-b10076
---

backlinks:
  - release-b10066
---

backlinks:
  - release-b10064
---


# Release b10076

> **Source:** gh-b10076-2026-07-21.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10076 ingested: 2026-07-21 sha256: e561cdfb6b7a2fdc4ea99632ee016e20b88d600745f07cae21002847c2f7cfce blog_source: github:ggml-org/lla...
> **Sources:**
>   - gh-b10076-2026-07-21.md
> **Links:**
- [[release-b10007]]
- [[release-b10066]]
- [[release-b10020]]
- [[release-b10034]]
- [[release-b10038]]

## Key Findings

---
source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10076
ingested: 2026-07-21
sha256: e561cdfb6b7a2fdc4ea99632ee016e20b88d600745f07cae21002847c2f7cfce
blog_source: github:ggml-org/llama.cpp
---
# Release b10076
CUDA: vectorize same-type get_rows with int4 copy (#25929)
k_get_rows_float did a scalar one-element-per-thread copy and recomputed the
row-invariant work (index load, fast_div_modulo, src/dst row pointers) for
every element. Hoist that out of the per-element loop, and add a vectorized
path (k_get_rows_float_vec) that copies one int4 (16 B) per thread for the
contiguous same-type (no-cast) case.
The vectorized path is gated at compile time (is_same) and at
runtime on 16-byte alignment of the base pointers and all row strides and on
ne00 % VEC == 0. Vectorizing divides the block count by VEC, so a small
single-row gather can drop below the device CU count and regress; an
occupancy gate keeps those on the block-rich scalar path.
On Strix Halo (gfx1151) the DeltaNet recurrent-state gather (ne00=524288)
drops 18.6us -> 13.0us (rocprofv3 HW timestamps), faster than the Vulkan
backend, with no regression on the small conv-state gather; total get_rows
-27%. test-backend-ops GET_ROWS passes (47/47).
Assisted-by: Claude Opus 4.8
**Website:**
- 
**macOS/iOS:**
- [macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-macos-arm64.tar.gz)
- macOS Apple Silicon (arm64, KleidiAI enabled) [DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780)
- [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-macos-x64.tar.gz)
- [iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-xcframework.zip)
**Linux:**
- [Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-ubuntu-x64.tar.gz)
- [Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-ubuntu-arm64.tar.gz)
- [Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-ubuntu-s390x.tar.gz)
- [Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-ubuntu-vulkan-x64.tar.gz)
- [Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-ubuntu-vulkan-arm64.tar.gz)
- [Ubuntu x64 (ROCm 7.2)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-ubuntu-rocm-7.2-x64.tar.gz)
- [Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-ubuntu-openvino-2026.2.1-x64.tar.gz)
- [Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-ubuntu-sycl-fp32-x64.tar.gz)
- [Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b10076/llama-b10076-bin-ubuntu-sycl-fp16-x64.tar.gz)
**Android:**
- [Android arm64 (CPU)](ht

## Summary

See Key Findings for full content.

## Related Articles

- [[release-b10007]]
- [[release-b10066]]
- [[release-b10020]]
- [[release-b10034]]
- [[release-b10038]]
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "release-b10064")
```
