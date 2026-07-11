---
title: "Open Source LLM Models"
type: concept
description: Overview of the major open-weight LLM families available for local deployment and fine-tuning
created: 2026-07-06
updated: 2026-07-06
tags: [open-source-llm, llama, mistral, qwen, gemma, glm, deepseek, benchmark]
sources: [raw/articles/open-source-llm-landscape-2026.md]
confidence: high
links: [llm-quantization, local-llm-hardware]
---

# Open Source LLM Models

Overview of the major open-weight LLM families available for local deployment and fine-tuning.

## Overview

As of 2026, six labs ship competitive open-weight models rivaling or surpassing closed alternatives on practical workloads.

## Major Families

### Llama (Meta)
- Sizes: 8B, 70B
- Context: 8K baseline, community extended to 100K+
- Best for: General reasoning, ecosystem breadth, community support
- License: Custom Meta (commercial OK, no competing LLMs)

### Mistral (Mistral AI)
- Sizes: 7B, Small 12B, Medium 35B, Large 72B
- Context: 32K native
- Best for: Performance-per-compute, inference speed, efficiency
- License: Unrestricted commercial

### Qwen (Alibaba)
- Sizes: 7B, 14B, 32B, 72B, 397B
- Context: Up to 200K tokens
- Best for: Multilingual (Chinese/Asian), long documents
- License: Creative Commons

### Other Notable Models
- **GLM-5.1** (Zhipu AI) — SWE-Bench Pro leader at 58.4%
- **Gemma 4** (Google) — Google ecosystem integration
- **DeepSeek V4** — Reasoning tasks rival GPT-5

## Deployment

All three support identical deployment patterns (vLLM, Ray Serve, Together.AI API). Quantization (GGUF, 4-bit) enables consumer hardware deployment.

## Key References

- [[llm-quantization]] — Quantization methods
- [[local-llm-hardware]] — Hardware requirements