---
type: entity
title: Ask in the Dark — Uncertainty-Gated LLM Assistance Under Partial Observability
description: Research on uncertainty-aware LLM assistance where the model gates its help based on confidence, asking for clarification when observability is partial.
created: 2026-07-07
updated: 2026-07-07
tags: [uncertainty, partial-observability, llm-assistance, clarification, trust]
sources: [raw/articles/ask-in-the-dark-uncertainty-gated-llm-assistance-under-partial-observability-2026-07-07.md]
confidence: high
contested: false
links: [controllable-neural-text-generation, oyster-ii-reinforcement-learning-for-constructive-safety-alignment-in-large-language-models]
---# Ask in the Dark — Uncertainty-Gated LLM Assistance

## Overview

"Ask in the Dark" is a research framework for uncertainty-aware LLM assistance. The model assesses its own confidence in answering and gates its response — providing help when confident, or asking for clarification when operating under partial observability.

## Core Problem

In real-world scenarios, users often provide incomplete or ambiguous information. Standard LLMs either:
1. Hallucinate answers despite low confidence
2. Provide vague, unhelpful responses

This work introduces **uncertainty gating** — the model explicitly signals when it needs more information.

## Key Contributions

### Uncertainty Estimation
- Calibrated confidence scores for LLM responses
- Methods for detecting partial observability in user queries
- Distinguishing between "I don't know" and "I need more info"

### Clarification-Seeking Behavior
- Model learns to ask targeted follow-up questions
- Reduces unnecessary clarification while avoiding hallucination
- Balances helpfulness with epistemic humility

### Human-Agent Collaboration
- Framework for iterative information gathering
- User studies show improved trust and satisfaction
- Reduced frustration from incorrect answers

## Technical Approach

1. **Confidence calibration** — Temperature scaling + conformal prediction
2. **Partial observability detection** — KL-divergence between observed and expected information
3. **Clarification policy** — RL-trained policy for question selection
4. **Response gating** — Threshold-based routing to answer vs. clarification

## Related Pages

- [[concepts/controllable-neural-text-generation]] — Controlled generation for reliable outputs
- [[oyster-ii-reinforcement-learning-for-constructive-safety-alignment-in-large-language-models]] — RL-based alignment
