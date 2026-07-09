---
title: "LLM Fine-Tuning"
type: concept
description: Parameter-efficient and full fine-tuning methods for adapting pre-trained LLMs
created: 2026-07-06
updated: 2026-07-06
tags: [fine-tuning, lora, qlora, dpo, peft, sft, rlhf]
sources: [raw/articles/llm-fine-tuning-lora-qlora-dpo-2026.md]
confidence: high
links: [llm-quantization, advanced-rag-techniques, open-source-llm-models]
---

# LLM Fine-Tuning

Parameter-efficient and full fine-tuning methods for adapting pre-trained LLMs to specific domains and tasks.

## Overview

Fine-tuning adapts a pre-trained LLM to specific needs by continuing training on domain-specific data. In 2026, the standard stack is **PEFT (parameter-efficient fine-tuning)** rather than full parameter updates.

## Methods

### PEFT Methods

- **LoRA** — Low-rank adaptation. Injects trainable A×B matrices into attention/MLP weights. 0.1–1% of base params. Default PEFT in 2026.
- **QLoRA** — LoRA on 4-bit NF4 quantized base. Enables 65B-class fine-tuning on single 48GB GPU.
- **BitFit** — Bias-only updates. Smallest footprint, lower ceiling.
- **Adapters / IA³ / Prefix-Tuning** — Alternative PEFT approaches.

### Supervision Regimes

- **SFT** — Supervised fine-tuning on instruction-response pairs
- **DPO** — Direct preference optimization. Replaced RLHF for most teams (2026 default)
- **RLHF** — Reinforcement learning from human feedback. Frontier labs still use for final alignment

## When to Fine-Tune

1. Prompt optimization cannot close measured quality gap
2. Need lower per-request cost than frontier API
3. Need smaller model footprint for latency/on-prem reasons
4. Need domain-specific behavior not achievable via RAG

## Key References

- [[llm-fine-tuning]] — Detailed techniques guide
- [[llm-quantization]] — Quantization for deployment
- [[advanced-rag-techniques]] — RAG as alternative to fine-tuning
- [[open-source-llm-models]] — Base model selection