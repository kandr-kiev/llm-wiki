---
type: concept
title: LLM Quantization
description: Techniques for reducing LLM weight precision (FP32→FP16→INT8→INT4) to enable local inference on consumer hardware.
created: 2026-07-06
updated: 2026-07-06
tags: [local-llm-hardware, architecture, comparison]
sources: [raw/articles/llm-quantization-gguf-gptq-awq.md]
confidence: high
contested: false
links: [local-llm-hardware, rtx-5070-ti]
---# LLM Quantization Methods: GPTQ, AWQ, GGUF, SmoothQuant

Quantization is the process of constraining model weights from continuous high-precision values to discrete low-precision representations. For LLMs, this is the primary method for running models on consumer hardware.

## Precision Progression

| Precision | Bits | Typical Use |
|---|---|---|
| FP32 | 32 | Training, baseline inference |
| FP16 | 16 | Standard inference |
| INT8 | 8 | Production serving |
| INT4 | 4 | Local/consumer inference |

## Major Methods

### GPTQ (Generative Pre-trained Quantized)
Post-training quantization using second-order derivatives (Hessian). Layer-by-layer optimization on calibration data. Best for GPU inference on NVIDIA hardware. Supported by vLLM, SGLang, Triton.

### AWQ (Activation-Aware Weight Quantization)
Protects salient weights by observing activation patterns. Better than GPTQ for instruction-tuned models. Requires activation analysis during quantization.

### GGUF (GGML Format Successor)
File format (not a method) for storing quantized models. Designed for CPU and Apple M-series. Supports layer offloading (partial GPU, rest CPU). Supported by llama.cpp, Ollama, LM Studio.

### SmoothQuant
Reduces outlier magnitudes before quantization. Moves quantization difficulty from activations to weights. Enables per-token quantization of activations for better low-bit accuracy.

## Key Concepts

- **Symmetric vs Asymmetric:** Whether zero point is fixed at 0 or shifted
- **Per-token vs Per-channel:** Granularity of quantization parameters
- **Sharding:** Splitting model across multiple GPUs before quantization

## Hardware Implications

Quantization directly determines what hardware can run a given model. For example, a 7B model at INT4 requires ~4GB VRAM, while the same model at FP16 requires ~14GB. This makes quantization critical for [[concepts/local-llm-hardware]] planning.

## Related Pages

- [[concepts/local-llm-hardware]] — Hardware requirements for local LLM inference
- [[rtx-5070-ti]] — NVIDIA RTX 5070 Ti GPU specs and AI performance
- [[concepts/karpathy-llm-wiki-2026]] — LLM Wiki pattern for local knowledge management
