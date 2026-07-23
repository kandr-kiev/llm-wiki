---
source_url: https://crabtalk.ai/blog/hermes-agent-survey
ingested: 2026-07-21
sha256: d30a41353788d0386cf62fff19efcca3914d9d474d7f81f3a501496e75a4c205
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
