---
title: "Release b10007"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - backend
  - cuda
  - llama
  - open-source
---

# Release b10007

> **Source:** gh-b10007-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10007 ingested: 2026-07-14 sha256: 159b9f839a6befad915e07582cf58879be0354cee53ffef351885483328f6671 blog_source: github:ggml-org/lla...
> **Sources:**
>   - gh-b10007-2026-07-14.md
> **Links:**
- [[Release Notes: Llama.cpp vb9956]]
- [[pytorch-2110-release]]
- [[pytorch-2121-release-bug-fix-release]]
- [[Release Notes: Ollama vv0.31.2]]
- [[release-v1143]]

## Key Findings

---
source_url: https://github.com/ggml-org/llama.cpp/releases/tag/b10007
ingested: 2026-07-14
sha256: 159b9f839a6befad915e07582cf58879be0354cee53ffef351885483328f6671
blog_source: github:ggml-org/llama.cpp
---
# Release b10007
opencl: fix a dp4a bug for devices where cl_khr_integer_dot_product is unavailable (#25639)
* opencl: do not fail backend init on devices without cl_khr_integer_dot_product
* opencl: do not call dp4 kernels when dp is unavailable
---------
Co-authored-by: Li He - 
**macOS/iOS:**
- [macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-macos-arm64.tar.gz)
- macOS Apple Silicon (arm64, KleidiAI enabled) [DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780)
- [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-macos-x64.tar.gz)
- [iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-xcframework.zip)
**Linux:**
- [Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-ubuntu-x64.tar.gz)
- [Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-ubuntu-arm64.tar.gz)
- [Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-ubuntu-s390x.tar.gz)
- [Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-ubuntu-vulkan-x64.tar.gz)
- [Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-ubuntu-vulkan-arm64.tar.gz)
- [Ubuntu x64 (ROCm 7.2)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-ubuntu-rocm-7.2-x64.tar.gz)
- [Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-ubuntu-openvino-2026.2.1-x64.tar.gz)
- [Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-ubuntu-sycl-fp32-x64.tar.gz)
- [Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-ubuntu-sycl-fp16-x64.tar.gz)
**Android:**
- [Android arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-android-arm64.tar.gz)
**Windows:**
- [Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-win-cpu-x64.zip)
- [Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-win-cpu-arm64.zip)
- [Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-win-opencl-adreno-arm64.zip)
- [Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b10007/llama-b10007-bin-win-cuda-12.4-x64.zip) - [CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b10007/cudart-llama-bin-win-cuda-12.4-x64.zip)
- [Windows x64 (CUDA 13)](https://gith

## Summary

See Key Findings for full content.

## Related Articles

- [[Release Notes: Llama.cpp vb9956]]
- [[pytorch-2110-release]]
- [[pytorch-2121-release-bug-fix-release]]
- [[Release Notes: Ollama vv0.31.2]]
- [[release-v1143]]
