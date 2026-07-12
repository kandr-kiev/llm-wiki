---
title: "LLM Evaluation"
type: concept
description: Systematic evaluation of LLMs across multiple dimensions: accuracy, safety, fairness, robustness, calibration, efficiency, and alignment
created: 2026-07-06
updated: 2026-07-06
tags: [llm-benchmarks, evaluation, helk, mmlu, mt-bench, truthfulqa, safety, robustness]
sources: [raw/articles/llm-evaluation-benchmarks-2026.md]
confidence: high
links: [llm-fine-tuning, open-source-llm-models]
---# LLM Evaluation

Systematic evaluation of LLMs across multiple dimensions: accuracy, safety, fairness, robustness, calibration, efficiency, and alignment.

## Seven Evaluation Dimensions

1. **Accuracy & Knowledge** — factual correctness, domain knowledge
2. **Safety & Harm Prevention** — refusal of harmful requests
3. **Fairness & Bias** — demographic parity, representation
4. **Robustness** — consistency across prompt variations
5. **Calibration & Uncertainty** — confidence calibration
6. **Efficiency** — latency, throughput, cost per token
7. **Alignment & Helpfulness** — instruction following, user satisfaction

## Major Benchmarks

| Benchmark | Focus |
|---|---|
| HELM | Holistic evaluation (Stanford CRFM) |
| MMLU | 57-subject knowledge test |
| MT-Bench | Multi-turn dialogue (LMSYS) |
| TruthfulQA | Hallucination measurement |
| BIG-Bench | Safety, fairness, reliability |
| HumanEval / MBPP | Code generation |
| SWE-Bench Pro | Real-world software engineering |

## Evaluation Methodology (2026)

1. Frozen domain-specific golden set (deterministic metrics)
2. Public capability benchmarks (detect regression)
3. LLM-as-judge (open-ended outputs)
4. Live shadow trace evaluation (production behavior)

## Key References

- [[llm-fine-tuning]] — Evaluate fine-tuned models
- [[concepts/open-source-llm-models]] — Model benchmark comparisons