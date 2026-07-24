---
title: "Release b10069"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - cuda
  - llama
  - multi-agent
  - open-source
---

# Release b10069

> **Source:** gh-b10069-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10069 ingested: 2026-07-20 sha256: 29f15db59675f0fb30a3c7984c191f0450c5da933e51996d682e4751e220dd77 blog_source: github:ggml-org/lla...
> **Sources:**
>   - gh-b10069-2026-07-20.md
> **Links:**
- [[release-b10007]]
- [[release-b10068]]
- [[release-b10020]]
- [[release-b10064]]
- [[release-b10054]]

## Key Findings

---
source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10069
ingested: 2026-07-20
sha256: 29f15db59675f0fb30a3c7984c191f0450c5da933e51996d682e4751e220dd77
blog_source: github:ggml-org/llama.cpp
---
# Release b10069
opencl: Support broadcast for Adreno MUL_MAT and honor `view_offs` for Adreno Q8_0 MUL_MAT for llama-server multi-stream (#25910)
* opencl: handle broadcast for adreno gemm/gemv_noshuffle
* opencl: honor view_offs for adreno noshuffle gemm/gemv
* opencl: general GEMM/GEMV support broadcast
* opencl: remove unnecessary tests
* opencl: remove unnecessary comments
---------
Co-authored-by: Li He - 
**Website:**
- 
**macOS/iOS:**
- [macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-macos-arm64.tar.gz)
- macOS Apple Silicon (arm64, KleidiAI enabled) [DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780)
- [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-macos-x64.tar.gz)
- [iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-xcframework.zip)
**Linux:**
- [Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-ubuntu-x64.tar.gz)
- [Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-ubuntu-arm64.tar.gz)
- [Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-ubuntu-s390x.tar.gz)
- [Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-ubuntu-vulkan-x64.tar.gz)
- [Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-ubuntu-vulkan-arm64.tar.gz)
- [Ubuntu x64 (ROCm 7.2)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-ubuntu-rocm-7.2-x64.tar.gz)
- [Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-ubuntu-openvino-2026.2.1-x64.tar.gz)
- [Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-ubuntu-sycl-fp32-x64.tar.gz)
- [Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-ubuntu-sycl-fp16-x64.tar.gz)
**Android:**
- [Android arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-android-arm64.tar.gz)
**Windows:**
- [Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-win-cpu-x64.zip)
- [Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-win-cpu-arm64.zip)
- [Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-win-opencl-adreno-arm64.zip)
- [Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b10069/llama-b10069-bin-win-cuda-12.4-x64.zip) - [CUDA 12

## Summary

See Key Findings for full content.

## Related Articles

- [[release-b10007]]
- [[release-b10068]]
- [[release-b10020]]
- [[release-b10064]]
- [[release-b10054]]
