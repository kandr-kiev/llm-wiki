---
source_url: https://crabtalk.ai/blog/hermes-agent-survey
ingested: 2026-07-21
sha256: 93feb9d3f5d92bc89e31271e77e6fbec525d04ed2d7b9e7acacac359de16209b
category: articles
tags: [hermes-agent, nous-research, agent-architecture, open-source, mit-license]
---
# Hermes Agent: what Nous Research built

**Source:** CrabTalk Team · research blog · February 2026

## Overview

In February 2026, Nous Research released Hermes Agent — an open-source (MIT), Python-based agent runtime with persistent memory, autonomous skill creation, and local inference support via Ollama, vLLM, or llama.cpp. It positions itself "between a Claude Code style CLI and an OpenClaw style messaging platform agent." Six thousand GitHub stars in the first month.

## The Model Stack

Hermes Agent runs on Hermes 3 and Hermes 4, a family of fine-tuned open-weight models from Nous Research. The models and the agent runtime are separate projects — Hermes Agent can use any OpenAI-compatible endpoint, but the Hermes models are purpose-built for agentic workloads.

### Hermes 3 (August 2024)

Fine-tuned on Llama 3.1 at three scales: 8B, 70B, and 405B parameters.

**Training:**
- Data: ~390M tokens of synthetically generated responses (not human feedback). 69% output tokens, 31% instruction tokens. Constructed March–August 2024.
- Training: Two-phase — supervised fine-tuning (SFT) followed by direct preference optimization (DPO).
- Packing: 96% sample packing efficiency at 8192-token sequences via Flash Attention 2 with attention masking.
- Format: ChatML (`
