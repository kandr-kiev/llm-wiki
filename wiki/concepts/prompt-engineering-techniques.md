---
title: "Prompt Engineering Techniques"
type: concept
description: Systematic methods for eliciting desired LLM behavior through carefully crafted inputs
created: 2026-07-06
updated: 2026-07-06
tags: [prompt-engineering, cot, tot, self-consistency, in-context-learning, zero-shot, few-shot]
sources: [raw/articles/advanced-prompt-engineering-2026.md]
confidence: high
links: [advanced-rag-techniques]
---

# Prompt Engineering Techniques

Systematic methods for eliciting desired LLM behavior through carefully crafted inputs, without modifying model parameters.

## Overview

Prompt engineering operates by eliciting desired behaviors solely through inputs. LLMs are highly sensitive to prompt formatting — up to 76 accuracy points across formatting changes in few-shot settings.

## Foundational Techniques

- **Zero-shot** — Direct instructions without examples
- **Few-shot** — In-context learning with examples
- **Chain-of-Thought (CoT)** — Step-by-step reasoning before final answer
- **Self-Consistency** — Multiple CoT rollouts, majority vote

## Advanced Techniques

- **Tree-of-Thought (ToT)** — Parallel reasoning with DFS/BFS/beam search
- **Chain-of-Table** — Structured operations on tables as intermediate steps
- **Meta-Prompting** — LLM composes prompts for another LLM
- **Soft Prompting** — Gradient-based search over floating-point vectors

## Production Management

Prompt engineering maturity model (5 stages):
1. Ad-hoc Experimentation
2. Template Standardization
3. Systematic Evaluation
4. Production Observability
5. Continuous Optimization

## Key References

- [[advanced-rag-techniques]] — RAG as alternative to fine-tuning