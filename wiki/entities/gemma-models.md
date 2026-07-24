---
title: Gemma Models
type: entity
tags: [gemma, gemma4, google, multimodal, local-llm]
sources: [raw/articles/lukesdevlab-youtube-model-configs.ini]
confidence: high
links: [llama-cpp, qwen-models, diffusion-models]
created: 2026-07-24
updated: 2026-07-24
description: Auto-filled by Wiki Doctor
---

# Gemma Models

> **Опис:** Сімейство моделей Gemma від Google для локального інференсу

## Визначення

Gemma — це сімейство open-weight LLM від Google. Включає text-only та multimodal (mmproj) моделі, з підтримкою quantization та coding-спеціалізації.

## Ключові моделі

| Модель | Розмір | Quantization | VRAM | Примітки |
|---|---|---|---|---|
| **Gemma4-12B** | 12B | IQ4_NL | ~7GB | Base model |
| **Gemma4-12B Q8** | 12B | Q8_K_XL | ~13GB | Higher quality |
| **Gemma4-12B QAT** | 12B | Q4_K_XL | ~7GB | Quantization-aware trained |
| **Gemma4-12B BF16** | 12B | BF16 | ~24GB | Exceeds 16GB VRAM |
| **Gemma4-12B Coder** | 12B | Q4_K_M | ~7GB | Coding specialized |
| **Gemma4-26B** | 26B | IQ4_NL | ~15GB | Large model |
| **Gemma4-26B QAT** | 26B | Q4_0 | ~14GB | +1.3GB mmproj |
| **Gemma4-26B Coder** | 26B | IQ4_NL | ~15GB | Coding specialized |
| **DiffusionGemma-26B** | 26B | Q4_K_M | ~16GB | Diffusion model |

## Multimodal (mmproj)

Більшість моделей підтримують multimodal inference через mmproj:

```ini
mmproj = {llama-root}/models/gemma-4-12b-mmproj/mmproj-BF16.gguf
```

Для MTP моделей:

```ini
mmproj = {llama-root}/models/qwen3.6-27b-mmproj/mmproj-BF16.gguf
```

## Quantization Methods

| Method | Якість | Розмір | Використання |
|---|---|---|---|
| **IQ4_NL** | Good | ~7GB | Default for 12B |
| **Q8_K_XL** | Excellent | ~13GB | High quality |
| **Q4_K_M** | Good | ~7GB | Balanced |
| **Q4_K_XL** | Very Good | ~14GB | Large models |
| **Q2_0** | Low | ~7GB | Ternary Bonsai |

## Зв'язки

- [[llama-cpp]] — Inference engine
- [[qwen-models]] — Alternative model family
- [[diffusion-models]] — DiffusionGemma

## Джерела

- [model-configs.ini](raw/articles/lukesdevlab-youtube-model-configs.ini)
