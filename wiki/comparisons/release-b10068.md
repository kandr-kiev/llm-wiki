---
title: "Release b10068"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - cuda
  - foundation-model
  - llama
  - open-source
  - quantization
---

# Release b10068

> **Source:** gh-b10068-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** --- source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10068 ingested: 2026-07-18 sha256: ac8bdce4c583af34232f38720809f3766961d6048a159dac340cde8bd849d23f blog_source: github:ggml-org/lla...
> **Sources:**
>   - gh-b10068-2026-07-18.md
> **Links:**
- [[release-b10007]]
- [[release-b10020]]
- [[release-b10054]]
- [[release-b10064]]
- [[release-b10066]]

## Key Findings

---
source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10068
ingested: 2026-07-18
sha256: ac8bdce4c583af34232f38720809f3766961d6048a159dac340cde8bd849d23f
blog_source: github:ggml-org/llama.cpp
---
# Release b10068
model: rotate injected K/V cache for DFlash (#25823)
* dflash: rotate injected K/V cache when using K/V quantization
* Update src/models/dflash.cpp
Co-authored-by: Georgi Gerganov 
* clearer format
* remove trailing whitespace
---------
Co-authored-by: Georgi Gerganov 
**Website:**
- 
**macOS/iOS:**
- [macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-macos-arm64.tar.gz)
- macOS Apple Silicon (arm64, KleidiAI enabled) [DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780)
- [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-macos-x64.tar.gz)
- [iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-xcframework.zip)
**Linux:**
- [Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-ubuntu-x64.tar.gz)
- [Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-ubuntu-arm64.tar.gz)
- [Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-ubuntu-s390x.tar.gz)
- [Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-ubuntu-vulkan-x64.tar.gz)
- [Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-ubuntu-vulkan-arm64.tar.gz)
- [Ubuntu x64 (ROCm 7.2)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-ubuntu-rocm-7.2-x64.tar.gz)
- [Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-ubuntu-openvino-2026.2.1-x64.tar.gz)
- [Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-ubuntu-sycl-fp32-x64.tar.gz)
- [Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-ubuntu-sycl-fp16-x64.tar.gz)
**Android:**
- [Android arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-android-arm64.tar.gz)
**Windows:**
- [Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-win-cpu-x64.zip)
- [Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-win-cpu-arm64.zip)
- [Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-win-opencl-adreno-arm64.zip)
- [Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b10068/llama-b10068-bin-win-cuda-12.4-x64.zip) - [CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b10068/cudart-llama-bin-win-cuda-12.4-x64.zip)
- [Windows x64 (C

## Summary

See Key Findings for full content.

## Related Articles

- [[release-b10007]]
- [[release-b10020]]
- [[release-b10054]]
- [[release-b10064]]
- [[release-b10066]]
