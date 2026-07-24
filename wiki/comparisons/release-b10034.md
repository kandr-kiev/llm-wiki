---
title: "Release b10034"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - cuda
  - llama
  - open-source
---

# Release b10034

> **Source:** gh-b10034-2026-07-15.md
> **Type:** comparison
> **Created:** 2026-07-16
> **Updated:** 2026-07-16
> **Confidence:** high
> **Description:** --- source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10034 ingested: 2026-07-15 sha256: c60ed153f8acc1c7f8b2f6ec5079c33a639f63d458ff3859122b5729aa55e00f blog_source: github:ggml-org/lla...
> **Sources:**
>   - gh-b10034-2026-07-15.md
> **Links:**
- [[release-b10007]]
- [[release-b10020]]
- [[release-b10015]]
- [[release-b10031]]
- [[Release Notes: Llama.cpp vb9956]]

## Key Findings

---
source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10034
ingested: 2026-07-15
sha256: c60ed153f8acc1c7f8b2f6ec5079c33a639f63d458ff3859122b5729aa55e00f
blog_source: github:ggml-org/llama.cpp
---
# Release b10034
opencl: exclude some moe kernels on Adreno a7x (#25698)
* opencl: exclude Adreno A7x from using Adreno MoE kernels
Some compilers for A7x devices miscompile the repack kernels, corrupting
the weights and causing MoE models to generate garbage output
* opencl: exclude A6x and unknown Adreno from MoE weights repack
**macOS/iOS:**
- [macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-macos-arm64.tar.gz)
- macOS Apple Silicon (arm64, KleidiAI enabled) [DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780)
- [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-macos-x64.tar.gz)
- [iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-xcframework.zip)
**Linux:**
- [Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-ubuntu-x64.tar.gz)
- [Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-ubuntu-arm64.tar.gz)
- [Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-ubuntu-s390x.tar.gz)
- [Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-ubuntu-vulkan-x64.tar.gz)
- [Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-ubuntu-vulkan-arm64.tar.gz)
- [Ubuntu x64 (ROCm 7.2)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-ubuntu-rocm-7.2-x64.tar.gz)
- [Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-ubuntu-openvino-2026.2.1-x64.tar.gz)
- [Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-ubuntu-sycl-fp32-x64.tar.gz)
- [Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-ubuntu-sycl-fp16-x64.tar.gz)
**Android:**
- [Android arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-android-arm64.tar.gz)
**Windows:**
- [Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-win-cpu-x64.zip)
- [Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-win-cpu-arm64.zip)
- [Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-win-opencl-adreno-arm64.zip)
- [Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b10034/llama-b10034-bin-win-cuda-12.4-x64.zip) - [CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b10034/cudart-llama-bin-win-cuda-12

## Summary

See Key Findings for full content.

## Related Articles

- [[release-b10007]]
- [[release-b10020]]
- [[release-b10015]]
- [[release-b10031]]
- [[Release Notes: Llama.cpp vb9956]]
