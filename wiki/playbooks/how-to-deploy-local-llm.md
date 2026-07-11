---
title: "How to Deploy a Local LLM — Step-by-Step"
type: playbook
description: Actionable runbook for deploying quantized LLMs locally on consumer or server hardware
created: 2026-07-06
updated: 2026-07-06
tags: [playbook, local-llm-hardware, reference, automation, llama]
sources: [raw/articles/llm-quantization-gguf-gptq-awq.md, raw/articles/open-source-llm-landscape-2026.md]
confidence: high
links: [llm-quantization, local-llm-hardware, open-source-llm-models]
---

# How to Deploy a Local LLM — Step-by-Step

Actionable runbook for deploying quantized LLMs locally on consumer or server hardware.

## Prerequisites

- GPU with ≥8 GB VRAM (consumer) or ≥40 GB (server)
- Linux or WSL2 recommended
- Python 3.10+ or Docker

## Phase 1: Hardware Assessment

### Step 1.1 — Check your GPU

```bash
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv
```

### Step 1.2 — Match model to VRAM

| Model Size | 4-bit (GGUF) | 8-bit | FP16 | Min VRAM |
|---|---|---|---|---|
| 7B | ~4 GB | ~8 GB | ~14 GB | 8 GB |
| 8B | ~5 GB | ~10 GB | ~16 GB | 10 GB |
| 14B | ~8 GB | ~16 GB | ~28 GB | 16 GB |
| 35B | ~20 GB | ~40 GB | ~70 GB | 24 GB |
| 70B | ~40 GB | ~80 GB | ~140 GB | 80 GB |
| 397B | N/A | N/A | N/A | Multi-GPU |

### Step 1.3 — Choose deployment target

| Use Case | Recommended Setup | Est. Cost |
|---|---|---|
| Personal assistant | RTX 4090 (24 GB) | ~$1,600 |
| Small team | 2x RTX 4090 (48 GB) | ~$3,200 |
| Production | A100 80 GB (cloud) | $2.70/hr |
| Edge/mobile | Qualcomm/NPU | Varies |

## Phase 2: Model Selection & Download

### Step 2.1 — Pick your model

```
Llama 3.1 8B Instruct  — best general-purpose, largest ecosystem
Mistral 7B Instruct    — fastest inference, unrestricted license
Qwen 2.5 14B           — multilingual, strong coding/math
```

### Step 2.2 — Download from Hugging Face

```bash
# Using huggingface-cli
pip install huggingface_hub
huggingface-cli download meta-llama/Meta-Llama-3.1-8B-Instruct \
  --local-dir ./llama-3.1-8b \
  --token $HF_TOKEN
```

Or download GGUF directly (for llama.cpp):

```bash
# From TheBloke's organized GGUF repo
huggingface-cli download TheBloke/Llama-3.1-8B-Instruct-GGUF \
  llama-3.1-8b-instruct.Q4_K_M.gguf \
  --local-dir ./models
```

## Phase 3: Deployment Option A — Ollama (Easiest)

### Step 3.1 — Install Ollama

```bash
# Linux/macOS
curl -fsSL https://ollama.com/install.sh | sh

# Windows — download from https://ollama.com
```

### Step 3.2 — Pull and run

```bash
# Pull model (auto-quantizes to 4-bit)
ollama pull llama3.1:8b

# Run interactive chat
ollama run llama3.1:8b

# Serve as API
ollama serve  # listens on localhost:11434
```

### Step 3.3 — API usage

```python
import requests

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3.1:8b",
    "prompt": "Explain quantum computing",
    "stream": False
})
print(response.json()["response"])
```

### Step 3.4 — Create a Modelfile (customization)

```dockerfile
FROM llama3.1:8b
SYSTEM "You are a helpful technical assistant."
PARAMETER temperature 0.7
PARAMETER num_ctx 8192
```

```bash
ollama create my-assistant -f Modelfile
ollama run my-assistant
```

## Phase 4: Deployment Option B — llama.cpp (Maximum Control)

### Step 4.1 — Install llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
cmake -B build
cmake --build build --config Release -j $(nproc)
```

### Step 4.2 — Run GGUF model

```bash
./build/bin/llama-cli \
  -m ./models/llama-3.1-8b-instruct.Q4_K_M.gguf \
  -p "Explain quantum computing:" \
  -n 512 \
  --temp 0.7 \
  -t 8  # CPU threads
```

### Step 4.3 — Serve as HTTP server

```bash
./build/bin/llama-server \
  -m ./models/llama-3.1-8b-instruct.Q4_K_M.gguf \
  -c 8192 \
  --host 0.0.0.0 \
  --port 8080
```

### Step 4.4 — API-compatible endpoint

```python
import requests

response = requests.post("http://localhost:8080/completion", json={
    "prompt": "Explain quantum computing",
    "n_predict": 512,
    "temperature": 0.7
})
print(response.json()["content"])
```

## Phase 5: Deployment Option C — vLLM (Production)

### Step 5.1 — Install vLLM

```bash
pip install vllm
```

### Step 5.2 — Launch server

```bash
vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct \
  --port 8000 \
  --tensor-parallel-size 1 \
  --max-model-len 8192
```

### Step 5.3 — OpenAI-compatible API

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    max_tokens=512,
    temperature=0.7,
)
print(response.choices[0].message.content)
```

### Step 5.4 — Multi-GPU deployment

```bash
vllm serve meta-llama/Meta-Llama-3.1-70B-Instruct \
  --port 8000 \
  --tensor-parallel-size 4 \
  --max-model-len 16384
```

## Phase 6: Performance Tuning

### Step 6.1 — Benchmark

```python
# vLLM benchmark
python -m vllm.entrypoints.api_server \
  --model meta-llama/Meta-Llama-3.1-8B-Instruct \
  --port 8000 \
  --enforce-eager  # faster first request

# Measure tokens/sec
time curl -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"...","prompt":"Hello","max_tokens":1024}'
```

### Step 6.2 — Optimize parameters

| Parameter | Default | Tuning |
|---|---|---|
| `num_ctx` | 2048 | Increase to 8192–131072 for long context |
| `gpu_memory_utilization` | 0.9 | Increase to 0.95 for max throughput |
| `max_num_seqs` | 256 | Increase for higher concurrency |
| `quantization` | None | Use `awq` or `gguf` for VRAM efficiency |
| `tensor_parallel_size` | 1 | Set to GPU count for multi-GPU |

### Step 6.3 — Monitoring

```bash
# GPU utilization
nvidia-smi -l 1

# vLLM metrics (Prometheus)
# Access at http://localhost:8000/metrics
```

## Phase 7: Security & Production Hardening

### Step 7.1 — Authentication

```bash
# vLLM with auth
vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct \
  --port 8000 \
  --api-key YOUR_SECRET_KEY
```

### Step 7.2 — Rate limiting

```python
# Using nginx reverse proxy
# /etc/nginx/nginx.conf
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

location /v1/ {
    limit_req zone=api burst=20;
    proxy_pass http://localhost:8000;
}
```

### Step 7.3 — Containerization

```dockerfile
FROM python:3.11-slim
RUN pip install vllm
COPY . /app
WORKDIR /app
CMD ["vllm", "serve", "meta-llama/Meta-Llama-3.1-8B-Instruct", "--port", "8000"]
```

```bash
docker build -t local-llm .
docker run -p 8000:8000 --gpus all local-llm
```

## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| OOM during load | Model too large for VRAM | Use 4-bit quantization (GGUF) |
| Slow inference | CPU fallback, no GPU | Verify `cuda` device, check drivers |
| Context window errors | `num_ctx` exceeded | Increase `--max-model-len` |
| API connection refused | Server not started | Check `vllm serve` or `ollama serve` |
| Poor generation quality | Wrong quantization | Try Q5_K_S or Q6_K instead of Q4 |
| CUDA errors | Driver mismatch | `nvidia-smi` vs `nvcc --version` |

## Key References

- `[[llm-quantization]]` — GGUF, GPTQ, AWQ methods
- `[[local-llm-hardware]]` — Hardware requirements
- `[[open-source-llm-models]]` — Available model families
