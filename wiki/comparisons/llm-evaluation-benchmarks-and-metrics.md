---
title: "LLM Evaluation Benchmarks and Metrics"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - academic
  - ai
  - alignment
  - benchmark
  - cost
  - dpo
  - efficiency
  - evaluation
  - fine-tuning
  - foundation-model
  - instruction-tuning
  - llm
  - lora
  - multi-agent
  - multimodal
  - nlp
  - open-source
  - privacy
  - prompt-engineering
  - prompt-tuning
  - qlora
  - rag
  - real-time
  - retrieval
  - software
  - standards
  - tool
---
# LLM Evaluation Benchmarks and Metrics

> **Source:** llm-evaluation-benchmarks-2026.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://responsibleailabs.ai/knowledge-hub/articles/llm-evaluation-benchmarks-2025 ingested: 2026-07-06 sha256: 8f5936ca3c7af19cc3975855e245d494466b5a866972ca8b67066e2717a89a85 --- # L...
> **Sources:**
>   - llm-evaluation-benchmarks-2026.md
> **Links:**
- [[llm-evaluation-benchmarks-2026]]
- [[llm-evaluation]]
- [[how-to-evaluate-llm-models]]
- [[llm-landscape-2026-synthesis]]
- [[advanced-prompt-engineering-techniques]]

## Key Findings

---
source_url: https://responsibleailabs.ai/knowledge-hub/articles/llm-evaluation-benchmarks-2025
ingested: 2026-07-06
sha256: 8f5936ca3c7af19cc3975855e245d494466b5a866972ca8b67066e2717a89a85
---
# LLM Evaluation Benchmarks and Metrics 2026
Sources:
- https://responsibleailabs.ai/knowledge-hub/articles/llm-evaluation-benchmarks-2025
- https://alopatenko.github.io/LLMEvaluation
- https://www.confident-ai.com/blog/llm-benchmarks-mmlu-hellaswag-and-beyond
- https://galileo.ai/blog/llm-benchmarks-categories
Date ingested: 2026-07-06
## Overview
LLM benchmarking is the systematic process of evaluating models against standardized frameworks. Unlike traditional ML evals (clear ground truth), LLM benchmarking must handle non-deterministic, diverse outputs.
## Seven Dimensions of LLM Evaluation
1. **Accuracy & Knowledge** — factual correctness, domain knowledge
2. **Safety & Harm Prevention** — refusal of harmful requests
3. **Fairness & Bias** — demographic parity, representation
4. **Robustness** — consistency across prompt variations
5. **Calibration & Uncertainty** — confidence calibration
6. **Efficiency** — latency, throughput, cost per token
7. **Alignment & Helpfulness** — instruction following, user satisfaction
## Major Academic Benchmarks
### HELM (Holistic Evaluation of Language Models)
- Stanford CRFM
- Most comprehensive academic benchmark
- Multiple scenario types and scoring dimensions
- URL: https://crfm.stanford.edu/helm/
### MMLU (Massive Multitask Language Understanding)
- 57 subjects, STEM + humanities + social sciences
- 15,908 multiple-choice questions
- Many models now exceed 90% → spurred MMLU-Pro development
### MT-Bench (LMSYS)
- Fine-grained multi-turn dialogue evaluation
- MT-Bench-101: finer granularity (arXiv:2402.14762)
### TruthfulQA
- 817 questions where humans commonly give wrong answers
- Measures hallucination tendency directly
- Surprisingly low truthfulness in SOTA models
### BIG-Bench
- Covers safety, fairness, reliability
- BIG-Bench Hard subset for difficult tasks
### HellaSwag
- Commonsense reasoning and completion
## Code Generation Benchmarks
| Benchmark | Description | Metric |
|---|---|---|
| HumanEval | 164 hand-crafted Python problems | Pass@k |
| MBPP | 1,000 crowd-sourced Python problems | Pass@k |
| SWE-Bench Pro | Real-world software engineering tasks | % solved |
As of April 2026, GLM-5.1 leads SWE-Bench Pro at 58.4%.
## Reasoning Benchmarks
| Benchmark | Focus |
|---|---|
| GSM8K | Grade-school math |
| MATH | Complex math problems |
| JustLogic | Deductive reasoning (arXiv:2501.14851) |
## Multimodal Benchmarks
| Benchmark | Focus |
|---|---|
| MMT-Bench | Multimodal multitask AGI (arXiv:2404.16006) |
| MM-SafetyBench | Multimodal safety evaluation |
## Safety-Specific Benchmarks
| Benchmark | Dimensions |
|---|---|
| HEx-PHI | Harmful examples, prohibited instructions |
| RAIL-HH-10K | All 5 responsible AI dimensions (safety, fairness, reliability, privacy, transparency) |
## Evaluation Methodology

## Summary

See Key Findings for full content.

## Related Articles

- [[llm-evaluation-benchmarks-2026]]
- [[llm-evaluation]]
- [[how-to-evaluate-llm-models]]
- [[llm-landscape-2026-synthesis]]
- [[advanced-prompt-engineering-techniques]]
