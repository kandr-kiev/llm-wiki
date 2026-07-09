---
source_url: https://cast.ai/blog/demystifying-quantizations-llms
ingested: 2026-07-06
sha256: 287809ead8a426f430e1668261efb72522a0910ef3d38e8db9790b9ef332ddb6
---
# LLM Quantization Methods: GPTQ, AWQ, GGUF, SmoothQuant
By Igor Šušić, Cast AI.

## What is Quantization
Quantization is the process of constraining an input from a continuous or large set of values to a discrete set. For LLMs, this means reducing weight precision (e.g., from 32-bit float to 4-bit or 8-bit integer).

## Why It Matters
LLMs are huge and need massive GPU memory. Quantization reduces model size and speeds up inference while keeping accuracy acceptable. Key factors: throughput, memory footprint, accuracy, cost.

## Methods

### GPTQ (Generative Pre-trained Quantized)
- Post-training quantization method
- Works by quantizing weights layer-by-layer using second-order derivatives (Hessian)
- Optimizes quantization error on a calibration set
- Best for: GPU inference, NVIDIA GPUs, production serving
- Supported by: vLLM, SGLang, Triton
- Trade-off: Good accuracy at 4-bit, requires calibration data

### AWQ (Activation-Aware Weight Quantization)
- Protects salient weights by observing activations
- Excellent quantization performance, especially for instruction-tuned LMs
- Activation-aware: identifies which weights matter most based on activation patterns
- Best for: Instruction-tuned models, mixed precision
- Trade-off: Better than GPTQ for instruction models, but requires activation analysis

### GGUF (GGML Format Successor)
- File format for storing quantized models
- Designed for CPU and Apple M-series devices
- Supports layer offloading (some layers to GPU, rest to CPU)
- Best for: Local inference, Mac users, CPU-heavy setups
- Supported by: llama.cpp, Ollama, LM Studio
- Trade-off: Most flexible format, but pure inference is least efficient (loads entire model)

### SmoothQuant
- Reduces outlier magnitudes before quantization
- Moves quantization difficulty from activations to weights
- Enables per-token quantization of activations
- Trade-off: Better accuracy at low bit-widths

### Other Methods
- Marlin: Optimized kernel for GPTQ models
- BitBLAS: Tensor-level quantization optimization
- BitsandBytes: Python library for quantization (4-bit/8-bit NF4)

## Key Concepts
- Symmetric vs Asymmetric quantization (zero point fixed at 0 vs shifted)
- Per-token vs per-channel quantization
- 32-bit float (FP32) → 16-bit float (FP16) → 8-bit int (INT8) → 4-bit int (INT4)
- Sharding: splitting model across multiple GPUs before quantization
