---
title: "Release v0.25.1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - foundation-model
  - quantization
  - real-time
  - system-design
  - use-case
---

# Release v0.25.1

> **Source:** gh-v0251-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/vllm-project/vllm/releases/tag/v0.25.1 ingested: 2026-07-14 sha256: 60e5cc419ff50799c0b43f69d97a484fd1efffd9a2045133020c36b0636a78fd blog_source: github:vllm-project...
> **Sources:**
>   - gh-v0251-2026-07-14.md
> **Links:**
- [[v0.22.1]]
- [[v0.22.0]]
- [[release-500]]
- [[Release Notes: Ollama vv0.31.2]]
- [[release-v0231]]

## Key Findings

---
source_url: https://github.com/vllm-project/vllm/releases/tag/v0.25.1
ingested: 2026-07-14
sha256: 60e5cc419ff50799c0b43f69d97a484fd1efffd9a2045133020c36b0636a78fd
blog_source: github:vllm-project/vllm
---
# Release v0.25.1
# vLLM v0.25.1
## Highlights
This release features 2 commits from 2 contributors (1 new)!
v0.25.1 is a patch release containing two targeted bug fixes on top of v0.25.0.
### Bug Fixes
* **Avoid blocking model launching when no system FFmpeg is available for TorchCodec** (#47888). Previously `import torchcodec` raised a `RuntimeError` at import time when system FFmpeg was missing, which blocked startup (e.g. `vllm serve Qwen/Qwen3-VL-2B-Instruct`) even when TorchCodec was not in use. The error is now deferred to runtime so it only surfaces if TorchCodec is actually needed.
* **Guard mixed-dtype allreduce RMSNorm quant fusions** (#48330). The fused FlashInfer allreduce + RMSNorm + static-quantization patterns could match graphs where the activation and RMSNorm weight dtypes differ (e.g. a BF16 residual stream with an FP32 Gemma/Qwen-style RMSNorm weight in NVFP4 models), corrupting the hidden state and producing garbage output such as repeated `!!!!!` tokens. A dtype-match guard now routes incompatible mixed-dtype graphs to the safe path, while same-dtype models retain the full allreduce + RMSNorm + quant fusion.
## Contributors
@Isotr0py, @hugo-cen
## New Contributors
* @hugo-cen made their first contribution in https://github.com/vllm-project/vllm/pull/48330

## Summary

See Key Findings for full content.

## Related Articles

- [[v0.22.1]]
- [[v0.22.0]]
- [[release-500]]
- [[Release Notes: Ollama vv0.31.2]]
- [[release-v0231]]
