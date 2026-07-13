---
title: "How to Fine-Tune an LLM — Step-by-Step"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - alignment
  - batch
  - best-practice
  - comparison
  - data
  - dataset
  - deployment
  - dpo
  - evaluation
  - few-shot
  - fine-tuning
  - foundation-model
  - gpu
  - hardware
  - instruction-tuning
  - llama
  - llm
  - lora
  - mistral
  - open-source
  - playbook
  - prompt-tuning
  - qlora
  - quantization
  - rlhf
  - sft
  - training
  - use-case
---
# How to Fine-Tune an LLM — Step-by-Step

> **Source:** how-to-fine-tune-llm.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- title: "How to Fine-Tune an LLM — Step-by-Step" type: playbook description: Actionable runbook for parameter-efficient fine-tuning (LoRA/QLoRA) and alignment (DPO) of open-source LLMs created: 202...
> **Sources:**
>   - how-to-fine-tune-llm.md
> **Links:**
- [[how-to-fine-tune-llm]]
- [[how-to-deploy-local-llm]]
- [[llm-deployment-qa]]
- [[how-to-evaluate-llm-models]]
- [[llm-fine-tuning]]

## Key Findings


# How to Fine-Tune an LLM — Step-by-Step
Actionable runbook for parameter-efficient fine-tuning and alignment of open-source LLMs.
## Prerequisites
- GPU with ≥24 GB VRAM (RTX 4090, A10) or ≥80 GB (A100/H100 for 70B)
- Python 3.10+, `transformers`, `peft`, `accelerate`, `bitsandbytes`
- Dataset in Alpaca/ShareGPT format (JSONL)
## Phase 1: Data Preparation
### Step 1.1 — Format your dataset
Convert to Alpaca-style JSONL:
```json
{"instruction": "Explain quantum computing.", "input": "", "output": "Quantum computing uses qubits..."}
```
### Step 1.2 — Split and validate
```bash
# 80/20 train/val split
python -c "
import json, random
data = [json.loads(l) for l in open('dataset.jsonl')]
random.shuffle(data)
train, val = data[:int(len(data)*0.8)], data[int(len(data)*0.8):]
json.dump(train, open('train.json','w'), indent=2)
json.dump(val, open('val.json','w'), indent=2)
"
```
### Step 1.3 — Quality checks
- Verify instruction/output pairs are non-empty
- Check for data leakage (test examples in train)
- Ensure consistent formatting across all entries
- Target: 500–5000 examples for LoRA, 10K+ for SFT
## Phase 2: Base Model Selection
### Step 2.1 — Choose your base
| Use Case | Recommended Model | Size |
|---|---|---|
| Quick prototyping | Mistral 7B | 7B |
| Best quality/size | Llama 3.1 8B | 8B |
| Complex reasoning | Llama 3.1 70B | 70B |
| Multilingual | Qwen 2.5 14B | 14B |
### Step 2.2 — Load with quantization (QLoRA)
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
bnb_config = BitsAndBytesConfig(
load_in_4bit=True,
bnb_4bit_quant_type="nf4",
bnb_4bit_compute_dtype="float16",
bnb_4bit_use_double_quant=True,
)
model = AutoModelForCausalLM.from_pretrained(
"meta-llama/Meta-Llama-3.1-8B-Instruct",
quantization_config=bnb_config,
device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")
```
## Phase 3: LoRA Configuration
### Step 3.1 — Configure LoRA
```python
from peft import LoraConfig, get_peft_model
lora_config = LoraConfig(
r=16, # Rank — higher = more capacity, more VRAM
lora_alpha=32, # Scaling factor (2× rank)
lora_dropout=0.1, # Regularization
target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
task_type="CAUSAL_LM",
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters() # Should show ~0.1–1% trainable params
```
### Step 3.2 — Training arguments
```python
from transformers import TrainingArguments
training_args = TrainingArguments(
output_dir="./lora-output",


## Summary

See Key Findings for full content.

## Related Articles

- [[how-to-fine-tune-llm]]
- [[how-to-deploy-local-llm]]
- [[llm-deployment-qa]]
- [[how-to-evaluate-llm-models]]
- [[llm-fine-tuning]]
