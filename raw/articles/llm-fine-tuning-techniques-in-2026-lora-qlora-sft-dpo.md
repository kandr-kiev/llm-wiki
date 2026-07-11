---
title: "LLM Fine-Tuning Techniques in 2026: LoRA, QLoRA, SFT, DPO"
type: comparison
tags: [comparison, dpo, fine-tuning, lora, qlora, sft]
description: Comparison page for LLM Fine-Tuning Techniques in 2026: LoRA, QLoRA, SFT, DPO

sources: []
links: []
description: Comparison page for LLM Fine-Tuning Techniques in 2026: LoRA, QLoRA, SFT, DPO

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
contested: false

---
# LLM Fine-Tuning Techniques in 2026: LoRA, QLoRA, SFT, DPO

> **Source:** llm-fine-tuning-lora-qlora-dpo-2026.md
> **Type:** comparison
> **Created:** 2026-07-08

## Key Findings

---
source_url: https://futureagi.com/blog/llm-fine-tuning-techniques-i-ii
ingested: 2026-07-06
sha256: a6666d6e7e48fa4be0a97c7af36140e187fc7da5c17a6c11e36bbf70efa1b318
---
# LLM Fine-Tuning Techniques in 2026: LoRA, QLoRA, SFT, DPO
Source: https://futureagi.com/blog/llm-fine-tuning-techniques-i-ii
Published: 2026
Author: Rishav Hada (Future AGI)
Date ingested: 2026-07-06
## Overview
Fine-tuning in 2026 is a stack of decisions: pick a base model, pick parameter scope (feature-based, head-only, full, PEFT), pick supervision regime (SFT, DPO, RLHF), and pick evaluation methodology.
## Key Methods
### PEFT (Parameter-Efficient Fine-Tuning)
| Method | Trainable Params | Best For | Cost |
|---|---|---|---|
| Feature-based | 0 (base frozen) + small head | Classification baselines | Lowest |
| Head-only | Classifier head only | Encoder LLM classification | Low |
| Full fine-tuning | 100% | Highest quality, narrow domain | Highest |
| LoRA | ~0.1–1% | Default PEFT in 2026 | Low |
| QLoRA | ~0.1–1% on 4-bit base | Big models on single GPU | Lowest |
| BitFit | Bias only | Tiny budget, ablation | Very low |
| Adapters / IA³ / Prefix | Small inserted modules | PEFT alternatives | Low |
### Supervision Regimes
- **SFT (Supervised Fine-Tuning):** Instruction-response pairs. Base learns to follow commands.
- **DPO (Direct Preference Optimization):** Trains on (prompt, preferred, rejected) triples using Bradley-Terry classification loss. No reward model, no PPO loop. Replaced RLHF for most teams.
- **RLHF (Reinforcement Learning from Human Feedback):** Reward model + PPO. Frontier labs still use for final alignment.
- **Variants:** IPO, KTO, ORPO.
### Three Forces Reshaping 2026 Fine-Tuning
1. **DPO is the new default** for preference tuning (Rafailov et al., 2023, arXiv:2305.18290).
2. **QLoRA makes big-model adaptation accessible** — 4-bit NF4 quantization, paged optimizers, double quantization (Dettmers et al., 2023, arXiv:2305.14314). Single 48GB GPU can fine-tune 65B-class base.
3. **Prompting and retrieval close more of the gap** — DSPy, GEPA, ProTeGi, long-context windows, structured tool use. Fine-tune when prompting cannot close the gap.
### Practical Guidance
- **Data:** Quality over volume. 5k well-curated SFT > 50k noisy. Deduplicate and check contamination. Mix 5–20% base data to reduce catastrophic forgetting.
- **Hyperparameters:** LR 1e-5–5e-4 for LoRA; 1e-6–5e-5 for full SFT. LoRA rank r, alpha, target modules (q_proj, k_proj, v_proj, o_proj).
- **Evaluation:** Frozen domain-specific golden set + public benchmarks (MMLU, IFEval, GSM8K, HumanEval, MT-Bench) + LLM-as-judge + live shadow trace.
### Decision Tree
- Classification baseline → Feature-based or head-only
- Teach small base to follow prompts → SFT + LoRA (QLoRA if large base)
- SFT correct but not aligned → Add DPO on top of LoRA
- Maximum quality, narrow domain → Full SFT, then DPO
- Exhausting prompting and retrieval → Fine-tune
- Otherwise → Prompt-optimize and instrument first
## Ke

## Summary

See Key Findings for full content.

## Related Articles

- 
- 
- 
- [[llm-fine-tuning]]
- 
