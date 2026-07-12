---

title: "OpenAI"
type: entity
description: American AI research laboratory and company behind GPT-4, GPT-5, o-series models, and ChatGPT
created: 2026-07-06
updated: 2026-07-06
tags: [open-source-llm, llm-wiki, company, model]
sources: [raw/articles/open-source-llm-landscape-2026.md]
confidence: high
links: [open-source-llm, llama, mistral, qwen, gpt, chatgpt, deepmind]

---# OpenAI

## Overview

OpenAI is an American artificial intelligence research organization and commercial company founded in December 2015 by Sam Altman, Greg Brockman, Ilya Sutskever, Wojciech Zaremba, and John Schulman. Its mission is to ensure that artificial general intelligence (AGI) benefits all of humanity. OpenAI has developed some of the most influential large language models including GPT-4, GPT-5, and the o-series reasoning models.

## Key Facts

| Field | Details |
|
|---|
| **Founded** | December 2015 |
| **Headquarters** | San Francisco, California, USA |
| **CEO** | Sam Altman (interim, then returned in Nov 2023) |
| **Type** | Capped-profit (formerly non-profit, now for-profit with profit cap) |
| **Key Investors** | Microsoft ($13B+ invested), NVIDIA, NVIDIA, Google |
| **Revenue (2024)** | ~$7.8B (annualized run rate) |
| **Employees** | ~10,000+ |

## Models & Products

### GPT Series (Closed-Source API)
- **GPT-5.5** (квітень 2026) — Флагманська модель, найкраща у benchmarks
- **GPT-5.4** (березень 2026) — Попередній флагман
- **GPT-5.1** (листопад 2025) — Виведена з експлуатації (березень 2026)
- **GPT-4o** (травень 2024) — Multimodal (text, image, audio), швидка API модель
- **GPT-4** (березень 2023) — Multimodal, ~1.8T parameters (estimated)

### o-Series (Reasoning Models)
- **o1** (вересень 2023) — Перша reasoning модель, математика, наука
- **o3** (2025) — Покращений reasoning, coding, SWE-Pro benchmarks
- **o4-mini** (2025) — Ефективний reasoning для малих задач

### Other Products
- **ChatGPT** — conversational AI interface (100M+ weekly active users)
- **DALL-E** — text-to-image generation models
- **Sora** — text-to-video generation model
- **GPT-4o Realtime** — real-time voice interaction
- **ChatGPT Enterprise** — enterprise-grade deployment
- **OpenAI API** — REST API for model access
- **OpenAI Platform** — developer platform for custom GPTs

## Infrastructure

- **Training hardware**: Custom NVIDIA H100 clusters, estimated 100,000+ GPUs
- **Compute partnerships**: Microsoft Azure (multi-billion dollar deal)
- **Context window**: Up to 200K tokens (GPT-4o)
- **Fine-tuning**: Supports custom fine-tuning via API
- **Safety**: Constitutional AI, RLHF, red-teaming

## Business Model

OpenAI operates a capped-profit structure:
- Revenue from API usage, ChatGPT subscriptions, enterprise contracts
- Microsoft partnership provides compute infrastructure in exchange for equity stake
- OpenAI Platform allows third-party developers to build on top of models
- Enterprise tier offers data privacy, dedicated infrastructure, custom models

## Open Source Policy

OpenAI has historically been **closed-source**, releasing models only via API. However:
- Released **Whisper** (speech recognition) as open-source in 2023
- Released **CLIP** (vision-language) as open-source in 2021
- Released **Evoformer** components for AlphaFold collaboration
- GPT models remain proprietary with API access only
- Competes with open-weight models like Llama, Mistral, Qwen

## Relationships

- **Microsoft**: Major investor ($13B+), Azure cloud provider, co-developer of Copilot
- **NVIDIA**: GPU supplier, co-developer of inference optimizations
- **Apple**: ChatGPT integration in iOS (2024)
- **Google**: Competitor (competing with Gemini)
- **Meta**: Competitor (competing with Llama)
- **Anthropic**: Competitor (competing with Claude)

## Recent Developments (2024-2026)

1. **GPT-4o launch** (May 2024) — multimodal model with real-time voice
2. **o1 reasoning model** (Sep 2024) — chain-of-thought training approach
3. **ChatGPT surpasses 200M weekly active users** (2024)
4. **GPT-5 development** (2025-2026) — next-gen reasoning capabilities
5. **o3 models** — competitive AI programming and math performance
6. **OpenAI Operator** — autonomous web browsing agent (2024)
7. **Custom GPT Store** — third-party AI assistant marketplace
8. **GPT-4o Realtime** — sub-500ms voice interaction latency

## Controversies

- **Sam Altman ousting and return** (Oct 2023) — board fired him, returned days later
- **Safety concerns** — debates about AGI risk and deployment pace
- **Data scraping** — training on copyrighted content without consent
- **Competition with open-source** — critics argue closed models slow progress
- **Labor disputes** — employee protests over government AI contracts

## See Also
- [[entities/anthropic]]
- [[comparisons/ai]]
- [[entities/deepmind]]
- [[comparisons/ai]]
- [[entities/qwen]]
- [[hugging-face]]
- [[llm-quantization]]
- [[llm-fine-tuning]]
- [[comparisons/ai]]