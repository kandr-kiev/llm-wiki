---

title: "Anthropic"
type: entity
description: American AI safety-focused company behind Claude models, emphasizing constitutional AI and responsible AI development
created: 2026-07-06
updated: 2026-07-06
tags: [llm-wiki, company, model]
sources: [raw/articles/open-source-llm-landscape-2026.md]
confidence: high
links: [llm-wiki, openai, deepmind, mistral]

---


# Anthropic

## Overview

Anthropic is an American AI safety and research company founded in December 2021 by former OpenAI researchers Dario Amodei, Daniela Amodei, Arcas, and others. The company's mission is to create reliable, interpretable, and steerable AI systems that are safe and beneficial. Anthropic is known for its Constitutional AI approach and the Claude family of large language models.

## Key Facts

| Field | Details |
|
|---|
| **Founded** | December 2021 |
| **Headquarters** | San Francisco, California, USA |
| **CEO** | Dario Amodei |
| **Co-founder** | Daniela Amodei (VP of Research), Tom Brown, John Schulman |
| **Type** | Public Benefit Corporation (B-Corp) |
| **Key Investors** | Google ($6B+), Amazon, OpenAI (former), Scale AI |
| **Revenue (2024)** | ~$1.5B (annualized run rate) |
| **Employees** | ~1,000+ |

## Models & Products

### Claude Series (2026 Lineup)
- **Claude Fable 5** (червень 2026) — Новий флагман, найкраща у benchmarks
- **Claude Opus 4.8** (2026) — Найсильніший reasoning, $5/$25 per 1M tokens
- **Claude Sonnet 5** (квітень 2026) — Agentic Sonnet, балансований
- **Claude Haiku 4.5** (2026) — Найшвидший, $0.25/$1.25 per 1M tokens
- **Claude 3.5 Sonnet** (жовтень 2024) — coding breakthrough, surpassed Opus
- **Claude 3 Opus** (березень 2024) — Попередній флагман reasoning

### Claude Opus vs Sonnet vs Haiku

| Model | Speed | Cost | Capability | Use Case |
|---|---|---|---|---|
| **Haiku** | Fastest | Lowest | Good for simple tasks | Quick Q&A, classification |
| **Sonnet** | Medium | Medium | Balanced | General purpose, coding |
| **Opus** | Slowest | Highest | Best reasoning | Complex reasoning, research |

### Other Products
- **Claude** — conversational AI interface (web and mobile apps)
- **Claude API** — REST API for model access
- **Claude Computer Use** — AI that can operate a computer desktop
- **Claude Code** — AI coding assistant (CLI tool)
- **Artifacts** — Claude's ability to render HTML, code, diagrams
- **Claude for Enterprise** — enterprise deployment with data privacy
- **Claude Research Preview** — access to experimental models

## Constitutional AI

Anthropic's signature approach to AI safety:

1. **Constitutional Principles** — predefined rules that guide model behavior
2. **Self-Critique** — model critiques its own responses against the constitution
3. **RL from AI Feedback (RLAIF)** — uses model-generated feedback for training
4. **Red Teaming** — systematic testing for harmful behaviors
5. **Interpretability Research** — understanding model internals for safety

Key papers:
- ["Constitutional AI: Harmlessness from AI Feedback"](https://arxiv.org/abs/2212.08073) (Dec 2022)
- ["Training language models to follow instructions with human feedback"](https://arxiv.org/abs/2203.02155) (Mar 2022) — original InstructGPT/RLHF

## Infrastructure

- **Training hardware**: Custom NVIDIA H100 clusters
- **Compute partnerships**: Google Cloud (multi-billion dollar deal), AWS
- **Context window**: Up to 200K tokens (Claude 3.5/4)
- **Fine-tuning**: Supports custom fine-tuning via API (Anthropic Fine-Tuning API)
- **Safety**: Constitutional AI, Claude's built-in safety layers

## Business Model

Anthropic operates a revenue-focused model:
- Revenue from API usage, Claude subscriptions, enterprise contracts
- Google partnership provides compute and investment ($6B+ committed)
- Amazon partnership for AWS integration
- Claude subscriptions for individual users ($20/month)
- Enterprise tier offers data privacy, dedicated infrastructure

## Open Source Policy

Anthropic is **partially open**:
- **Open weights**: Claude models are NOT open-source (API only)
- **Transparency reports**: Publishes detailed safety evaluations
- **Research papers**: All research published openly
- **Safety research**: Open-sourced constitutional AI methodology
- **Claude Code**: Released as open-source CLI tool (2025)
- **Competes with**: Llama (Meta), Mistral, Qwen (open-weight)

## Relationships

- **Google**: Major investor ($6B+), cloud provider, co-developer
- **Amazon**: Cloud partnership, AWS integration
- **OpenAI**: Former colleagues (founded by ex-OpenAI researchers)
- **Microsoft**: Competitor (competing with GPT)
- **Meta**: Competitor (competing with Llama)
- **Apple**: Claude integration in iOS/macOS (2024)

## Recent Developments (2024-2026)

1. **Claude 3 launch** (Mar 2024) — multimodal models (Haiku, Sonnet, Opus)
2. **Claude 3.5 Sonnet** (Oct 2024) — coding breakthrough, surpassed Opus
3. **Claude Computer Use** (Dec 2024) — AI that can operate desktop
4. **Claude 3.7 Sonnet** (Feb 2025) — hybrid reasoning with extended thinking
5. **Claude 4** (2025) — next-generation multimodal models
6. **Claude Code** (2025) — open-source AI coding assistant
7. **Claude for Enterprise** — enterprise deployment with data privacy guarantees
8. **Anthropic Fine-Tuning API** — custom model training via API

## Controversies

- **Google partnership** — concerns about AI safety and Google's influence
- **Safety vs capability debate** — critics argue safety focus slows progress
- **Data scraping** — training on copyrighted content
- **Labor concerns** — employee activism on AI safety
- **Competition with open-source** — closed models vs open-weight debate

## See Also
- [[openai]]
- [[meta-ai]]
- [[deepmind]]
- [[mistral-ai]]
- [[qwen]]
- [[hugging-face]]
- [[llm-quantization]]
- [[llm-fine-tuning]]
- [[enterprise-ai]]