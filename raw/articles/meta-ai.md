---

title: "Meta AI (Facebook)"
type: entity
description: Meta's AI research division behind Llama open-weight models, FAISS, and AI-powered products across Meta's ecosystem
created: 2026-07-06
updated: 2026-07-06
tags: [llm-wiki, company, open-source-llm]
sources: [raw/articles/open-source-llm-landscape-2026.md]
confidence: high
links: [llm-wiki, open-source-llm, openai, anthropic]
---


# Meta AI (Facebook)

## Overview

Meta AI is the artificial intelligence research division of Meta Platforms (formerly Facebook). Founded as part of Meta's original mission to connect the world, Meta AI has become one of the leading forces in open-weight AI model development through the Llama series. Unlike competitors who keep models proprietary, Meta has championed open-weight models, making Llama available for commercial use and driving the open-source AI ecosystem.

## Key Facts

| Field | Details |
|---|---|
| **Founded** | 2013 (as Facebook AI Research), restructured 2024 |
| **Headquarters** | Menlo Park, California, USA |
| **Lead** | Yann LeCun (VP & Chief AI Scientist), Michael Sandel (VP of Llama) |
| **Type** | Division of Meta Platforms Inc. |
| **Key Researchers** | Yann LeCun, Alexander Toshev, Mohammad Norouzi, Oriol Vinyals |
| **Parent Company** | Meta Platforms (NASDAQ: META) |
| **Revenue (Meta 2024)** | ~$135B (annual) |
| **Employees (Meta)** | ~86,000+ |

## Models & Products

### Llama Series (Open-Weight)

- **Llama 4 Maverick** (квітень 2026) — 17B MoE, 128 experts, open-weight флагман
- **Llama 4 Scout** (квітень 2026) — 17B MoE, 16 experts, 10M context window (найбільший серед open-weight)
- **Llama 3.3 70B** (грудень 2024) — Попередній флагман, dense model
- **Llama 3.1 405B** (липень 2024) — largest open-weight at release
- **Llama 3.1 70B/8B** (липень 2024) — mainstream open-weight models
- **Llama 3 8B/70B** (квітень 2024) — попереднє покоління

### Muse Series (2026)

- **Muse Spark** (квітень 2026) — Нова заміна Llama, Meta Superintelligence Labs

### Llama 4 Comparison

| Model | Parameters | Experts | Context | Use Case |
|---|---|---|---|---|
| **Llama 4 Scout** | 17B | 16 | 10M tokens | Ultra-long context, document analysis |
| **Llama 4 Maverick** | 17B | 128 | 128K tokens | Maximum open-weight capability |

### Other Meta AI Products

- **Llama.cpp** — C++ implementation for local LLM inference (community, but Meta supports)
- **FAISS** — Facebook AI Similarity Search library
- **Detectron2** — Object detection and segmentation
- **PyTorch** — Deep learning framework (developed by Meta AI)
- **PyTorch Lightning** — PyTorch wrapper for simpler training
- **Roboflow** — Computer vision platform (acquired)
- **Meta AI Assistant** — Conversational AI across WhatsApp, Instagram, Facebook
- **Llama Guard** — Content safety classification model
- **Code Llama** — Code-specialized Llama variant
- **Llama Guard 3** — Enhanced safety classifier

## Infrastructure

- **Training hardware**: Custom NVIDIA GPU clusters, Meta's own AI Research Super Cluster (RSC)
- **Compute**: Owns significant GPU infrastructure (~350,000+ NVIDIA GPUs)
- **Context window**: Up to 10M tokens (Llama 4 Scout), 128K tokens (Llama 3.3)
- **Fine-tuning**: Supports custom fine-tuning, LoRA, QLoRA
- **Safety**: Llama Guard for content moderation

## Business Model

Meta operates Llama as an open-weight strategy:
- **Open-weight**: Llama models are freely available for commercial and research use
- **API access**: Meta API for Llama models via cloud providers
- **Meta AI Assistant**: Integrated across Meta's social platforms
- **Enterprise**: Custom Llama deployments for businesses
- **AI infrastructure**: Drives Meta's ad technology improvements
- **Competitive strategy**: Open-weight vs closed models (OpenAI, Anthropic)

## Open Source Policy

Meta is the **leading advocate for open-weight AI**:
- **Llama licenses**: Free for commercial use with some restrictions
- **All models open-weight**: Not fully open-source (no training data/code), but weights are public
- **Community ecosystem**: Drives massive open-source community (Ollama, llama.cpp, vLLM)
- **Competes with**: OpenAI (closed), Anthropic (closed), Google (partially open)
- **Philosophy**: "Open-weight models accelerate AI progress and safety through transparency"

## Relationships

- **Google**: Competitor (Gemini vs Llama), also Meta's cloud provider
- **Microsoft**: Competitor (Azure OpenAI vs Meta AI), also Llama deployment partner
- **OpenAI**: Competitor (GPT vs Llama)
- **Amazon**: AWS partners with Meta for Llama deployment
- **Apple**: Uses Llama for on-device AI features
- **Community**: Massive open-source community around Llama ecosystem

## Recent Developments (2024-2026)

1. **Llama 3 launch** (Apr 2024) — 8B/70B/405B models, major capability leap
2. **Llama 3.1** (Jul 2024) — 128K context, 405B model, multilingual
3. **Llama 3.2** (Sep 2024) — Vision models, edge models (1B/3B)
4. **Llama 3.3** (Dec 2024) — 70B model, GPT-4 competitive
5. **Llama 4 Scout + Maverick** (April 2026) — Two 17B MoE models, Scout with 10M context
6. **Meta AI Assistant** — AI across WhatsApp, Instagram, Facebook
7. **Llama Guard 3** — Enhanced safety classification
8. **Code Llama** — Code-specialized model
9. **Muse Spark** (April 2026) — New frontier model line

## Controversies

- **Data scraping** — Llama trained on scraped web content
- **Misuse concerns** — Open-weight models used for harmful purposes
- **Safety vs openness** — debate on open-weight safety implications
- **Labor disputes** — Meta employee activism on AI ethics
- **Competition with open-source** — Meta's open-weight vs other companies' closed models

## See Also

- [[openai]]
- [[anthropic]]
- [[deepmind]]
- [[mistral-ai]]
- [[qwen]]
- [[hugging-face]]
- [[llm-quantization]]
- [[llm-fine-tuning]]
- [[enterprise-ai]]
