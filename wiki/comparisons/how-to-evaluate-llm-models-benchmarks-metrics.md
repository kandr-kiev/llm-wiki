---
title: "How to Evaluate LLM Models — Benchmarks & Metrics"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - academic
  - ai
  - alignment
  - analysis
  - api
  - async
  - benchmark
  - claude
  - comparison
  - cost
  - dpo
  - efficiency
  - evaluation
  - fine-tuning
  - foundation-model
  - framework
  - gpt
  - gpu
  - instruction-tuning
  - llama
  - llm
  - lora
  - multi-agent
  - nlp
  - open-source
  - pipeline
  - playbook
  - prompt-tuning
  - qlora
  - real-time
  - self-supervised
  - standards
  - system-design
  - use-case
---
# How to Evaluate LLM Models — Benchmarks & Metrics

> **Source:** how-to-evaluate-llm-models.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- type: playbook title: "How to Evaluate LLM Models — Benchmarks & Metrics" description: Actionable runbook for evaluating LLM models using academic benchmarks, custom tests, and production metrics...
> **Sources:**
>   - how-to-evaluate-llm-models.md
> **Links:**
- [[how-to-evaluate-llm-models]]
- [[llm-evaluation]]
- [[llm-evaluation-benchmarks-2026]]
- [[how-to-fine-tune-llm]]
- [[how-to-engineer-prompts]]

## Key Findings


# How to Evaluate LLM Models — Benchmarks & Metrics
Actionable runbook for evaluating LLM models using standardized benchmarks, custom tests, and production metrics.
## Prerequisites
- Python 3.10+
- Access to models to evaluate (API or local via vLLM/Ollama)
- Benchmark datasets (downloaded or API-accessible)
## Phase 1: Evaluation Framework Setup
### Step 1.1 — Install evaluation tools
```bash
pip install lm-eval transformers accelerate vllm wandb
```
### Step 1.2 — Define evaluation dimensions
From the 2026 standard, evaluate across 7 dimensions:
| Dimension | What it measures | Key metrics |
|---|---|---|
| **Accuracy & Knowledge** | Factual correctness | MMLU, TruthfulQA |
| **Safety & Harm Prevention** | Refusal of harmful requests | HEx-PHI, RAIL-HH-10K |
| **Fairness & Bias** | Demographic parity | RAIL-HH-10K |
| **Robustness** | Consistency across prompts | Prompt variation tests |
| **Calibration & Uncertainty** | Confidence calibration | ECE, Brier score |
| **Efficiency** | Latency, throughput, cost | Tokens/sec, $/1M tokens |
| **Alignment & Helpfulness** | Instruction following | IFEval, user satisfaction |
## Phase 2: Run Academic Benchmarks
### Step 2.1 — MMLU (Massive Multitask Language Understanding)
```python
from lm_eval import simple_evaluate
# Run MMLU benchmark
results = simple_evaluate(
model="hf",
model_args="pretrained=meta-llama/Llama-3.1-8B-Instruct",
tasks=["mmlu"],
batch_size=8
)
print(results["results"]["mmlu"])
# Expected: ~68% for Llama 3.1 8B, ~90%+ for top models
```
### Step 2.2 — MT-Bench (Multi-turn dialogue)
```python
# Using lm-eval framework
results = simple_evaluate(
model="hf",
model_args="pretrained=meta-llama/Llama-3.1-8B-Instruct",
tasks=["mt_bench", "mt_bench_hard"],
batch_size=1
)
print(results["results"]["mt_bench"])
# Expected: ~7.5/10 for strong models
```
### Step 2.3 — TruthfulQA (Hallucination detection)
```python
results = simple_evaluate(
model="hf",
model_args="pretrained=meta-llama/Llama-3.1-8B-Instruct",
tasks=["truthfulqa"],
batch_size=1
)
print(results["results"]["truthfulqa"])
# Measures: how often model gives WRONG answers that humans commonly give
```
### Step 2.4 — Code Generation Benchmarks
```python
# HumanEval (Python code generation)
results = simple_evaluate(
model="hf",
model_args="pretrained=meta-llama/Llama-3.1-8B-Instruct",
tasks=["humaneval", "mbpp"],
batch_size=1
)
print(results["results"]["humaneval"])
# Pass@1: Expected ~35% for 8B, ~70%+ for 70B+
```
### Step 2.5 — Reasoning Benchmarks
```python
re

## Summary

sults = simple_evaluate(
model="hf",
model_args="pretrained=meta-llama/Llama-3.1-8B-Instruct",
tasks=["gsm8k", "math"],
batch_size=1
)
print(results["results"]["gsm8k"])
# Grade-school math: Expected ~55% for 8B
```
## Phase 3: Custom Evaluation
### Step 3.1 — Domain-specific golden set
```python
# Create your own evaluation set
import json
evaluation_data = [
{
"question": "What is the capital of France?",
"answer": "Paris",
"category": "general_knowledge"
},
{
"question": "Write a Python function to calculate Fibonacci numbers",
"answer": "def fib(n): return n if n 0.9 consistency for robust models
```
## Phase 4: Production Metrics
### Step 4.1 — Latency & throughput
```python
import time
import asyncio
async def benchmark_latency(model_url, prompts, num_requests=100):
"""Measure latency and throughput."""
latencies = []
async with aiohttp.ClientSession() as session:
for _ in range(num_requests):
start = time.time()
async with session.post(model_url, json={"prompt": "test"}) as resp:
await resp.text()
latencies.append(time.time() - start)
print(f"Mean latency: {sum(latencies)/len(latencies):.3f}s")
print(f"P50 latency: {sorted(latencies)[len(latencies)//2]:.3f}s")
print(f"P99 latency: {sorted(latencies)[int(len(latencies)*0.99)]:.3f}s")
print(f"Throughput: {num_requests / sum(latencies):.1f} req/s")
```
### Step 4.2 — Cost analysis
```python
def calculate_cost(model, tokens_used, price_per_million):
"""Calculate cost for tokens used."""
return (tokens_used / 1_000_000) * price_per_million
# Example: Llama 3.1 8B via vLLM (self-hosted)
# Cost: ~$0.001 per 1M tokens (GPU cost only)
# vs GPT-4o: $10 per 1M input tokens
print("Cost comparison (per 1M tokens):")
print(f" Llama 3.1 8B (self-hosted): $0.001")
print(f" GPT-4o: $10.00")
print(f" Claude Sonnet: $3.00")
```
## Phase 5: Full Evaluation Pipeline
### Step 5.1 — Complete evaluation script
```python
from lm_eval import simple_evaluate
import json
def run_full_evaluation(model_name, output_file="eval_results.json"):
"""Run comprehensive evaluation."""
# Academic benchmarks
results = simple_evaluate(
model="hf",
model_args=f"pretrained={model_name}",
tasks=[
"mmlu", # General knowledge
"mt_bench", # Dialogue quality
"truthfulqa", # Hallucination
"humaneval", # Code generation
"gsm8k", # Reasoning
"hellaswag", # Commonsense
],
batch_size=8
)
# Save results
with open(output_file, "w") as f:
json.dump(results, f, indent=2)
# Summary
print(f"=== {model_name} Evaluation ===")
for task, metrics in results["results"].items():
print(f" {task}: {metrics}")
return results
```
### Step 5.2 — Shadow trace evaluation
```python
# Capture real user requests in staging
def shadow_trace_eval(model_url, staging_requests):
"""Evaluate model on live user requests without exposing results."""
results = []
for req in staging_requests:
response = requests.post(model_url, json=req).json()
results.append({
"request": req,
"model_output": response["output"],
"expected": req.get("expected_output"),
"latency": response.ge

## Related Articles

- [[how-to-evaluate-llm-models]]
- [[llm-evaluation]]
- [[llm-evaluation-benchmarks-2026]]
- [[how-to-fine-tune-llm]]
- [[how-to-engineer-prompts]]
