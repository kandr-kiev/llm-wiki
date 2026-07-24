---
title: "Hermes Agent Architecture Deep Dive"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - architecture
  - data
  - deep-learning
  - dpo
  - efficiency
  - fine-tuning
  - foundation-model
  - instruction-tuning
  - llama
  - open-source
  - optimization
  - research
  - sft
  - supervised
  - training
  - use-case
---
backlinks:
  - hermes-agent-architecture-deep-dive
---


# Hermes Agent Architecture Deep Dive

> **Source:** hermes-agent-architecture-deep-dive-2026.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://crabtalk.ai/blog/hermes-agent-survey ingested: 2026-07-21 sha256: auto --- # Hermes Agent Architecture Deep Dive ## The Model Stack Hermes Agent runs on Hermes 3 and Hermes 4,...
> **Sources:**
>   - hermes-agent-architecture-deep-dive-2026.md
> **Links:**
- [[nous-research]]
- [[kimi-k3]]
- [[llm-deployment-qa-common-questions]]
- [[databricks]]
- [[atropos]]

## Key Findings

---
source_url: https://crabtalk.ai/blog/hermes-agent-survey
ingested: 2026-07-21
sha256: auto
---
# Hermes Agent Architecture Deep Dive
## The Model Stack
Hermes Agent runs on Hermes 3 and Hermes 4, a family of fine-tuned open-weight models from Nous Research. The models and the agent runtime are separate projects — Hermes Agent can use any OpenAI-compatible endpoint, but the Hermes models are purpose-built for agentic workloads.
### Hermes 3 (August 2024)
Fine-tuned on Llama 3.1 at three scales: 8B, 70B, and 405B parameters.
**Training:**
- Data: ~390M tokens of synthetically generated responses (not human feedback). 69% output tokens, 31% instruction tokens. Constructed March–August 2024.
- Training: Two-phase — supervised fine-tuning (SFT) followed by direct preference optimization (DPO).
- Packing: 96% sample packing efficiency at 8192-token sequences via Flash Attention 2 with attention masking.
- Format: ChatML (`

## Summary

See Key Findings for full content.

## Related Articles

- [[nous-research]]
- [[kimi-k3]]
- [[llm-deployment-qa-common-questions]]
- [[databricks]]
- [[atropos]]
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "hermes-agent-architecture-deep-dive")
```
