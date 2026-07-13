---
title: "How to Deploy with vLLM — Production LLM Serving"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - application
  - architecture
  - awq
  - comparison
  - compliance
  - container
  - cuda
  - deep-learning
  - deployment
  - docker
  - dpo
  - fine-tuning
  - foundation-model
  - gptq
  - gpu
  - image-generation
  - kubernetes
  - llama
  - llm
  - lora
  - multi-agent
  - open-source
  - parallel
  - playbook
  - prompt-tuning
  - qlora
  - quantization
  - rag
  - self-supervised
  - system-design
  - use-case
  - vllm
---
# How to Deploy with vLLM — Production LLM Serving

> **Source:** how-to-deploy-with-vllm.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- type: playbook title: "How to Deploy with vLLM — Production LLM Serving" description: Actionable runbook for deploying vLLM: single-GPU, multi-GPU, Docker Compose, Kubernetes, monitoring, and prod...
> **Sources:**
>   - how-to-deploy-with-vllm.md
> **Links:**
- [[how-to-deploy-with-vllm]]
- [[how-to-deploy-local-llm]]
- [[llm-deployment-qa]]
- [[how-to-use-cloudflare-workers-ai]]
- [[how-to-fine-tune-llm]]

## Key Findings


# How to Deploy with vLLM — Production LLM Serving
Actionable runbook for deploying vLLM as a production inference engine. Covers single-GPU, multi-GPU, Docker, Kubernetes, and monitoring.
## Prerequisites
- NVIDIA GPU (A100, H100, L4, or RTX 4090 recommended)
- NVIDIA Driver ≥ 525, CUDA ≥ 12.1
- NVIDIA Container Toolkit ≥ 1.14
- Docker Engine ≥ 23.0 (or Kubernetes ≥ 1.27 for production)
- Hugging Face account with accepted model licenses
## Phase 1: Understand vLLM Architecture
### Step 1.1 — Why vLLM?
vLLM achieves **14–24× higher throughput** than naive Transformers serving through three key innovations:
| Innovation | What it does | Impact |
|---|---|---|
| **PagedAttention** | Memory paging for KV caches | 4× less memory waste |
| **Continuous Batching** | Add new requests as old ones finish | Max GPU utilization |
| **Optimized CUDA Kernels** | Custom GPU operations | 2–4× faster than Ollama |
### Step 1.2 — When to Use vLLM
```
Need production API serving?
├── YES → vLLM
└── NO
Single user / development? → Ollama or llama.cpp
Enterprise compliance? → vLLM (self-hosted)
Kubernetes scale? → vLLM + KEDA
```
### Step 1.3 — Key Parameters
| Parameter | Purpose | Typical Value |
|---|---|---|
| `--model` | HuggingFace model ID | `meta-llama/Llama-3.1-8B-Instruct` |
| `--gpu-memory-utilization` | % of GPU VRAM for KV cache | `0.90` |
| `--max-model-len` | Max sequence length | `8192` (match your use case) |
| `--tensor-parallel-size` | GPUs for model sharding | `2`, `4`, `8` |
| `--quantization` | Quantization method | `awq`, `gptq` |
| `--enable-prefix-caching` | Cache shared prompt prefixes | On for chatbots |
| `--dtype` | Precision | `float16`, `auto` |
## Phase 2: Quick Start (Single GPU)
### Step 2.1 — Install vLLM
```bash
# Virtual environment (recommended)
python3 -m venv vllm-env
source vllm-env/bin/activate
# Install vLLM
pip install vllm
# Verify
python -c "import vllm; print(vllm.__version__)"
```
### Step 2.2 — Run Your First Model
```bash
python -m vllm.entrypoints.openai.api_server \
--model meta-llama/Llama-3.1-8B-Instruct \
--port 8000
```
Expected output:
```
INFO: Started server process [12345]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000
```
### Step 2.3 — Test with curl
```bash
curl http://localhost:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
"model": "meta-llama/Llama-3.1-8B-Instruct",
"prompt": "Explain vLLM in one sentence",
"max_tokens": 100,
"te

## Summary

mperature": 0.7
}'
```
### Step 2.4 — Test with OpenAI Python Client
```python
from openai import OpenAI
client = OpenAI(
base_url="http://localhost:8000/v1",
api_key="not-needed"
)
response = client.chat.completions.create(
model="meta-llama/Llama-3.1-8B-Instruct",
messages=[
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "What is PagedAttention?"}
],
max_tokens=200
)
print(response.choices[0].message.content)
```
## Phase 3: Docker Deployment
### Step 3.1 — Single-GPU Docker
```bash
docker run -d \
--name vllm-server \
--gpus '"device=0"' \
--shm-size=4g \
-p 8000:8000 \
-v ~/.cache/huggingface:/root/.cache/huggingface \
--env-file .env \
vllm/vllm-openai:v0.8.3 \
--model hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4 \
--served-model-name llama-3.1-8b \
--max-model-len 8192 \
--quantization awq \
--dtype auto \
--gpu-memory-utilization 0.90 \
--enable-prefix-caching \
--port 8000
```
### Step 3.2 — .env file
```bash
HUGGING_FACE_HUB_TOKEN=hf_your_token_here
VLLM_API_KEY=your_secure_api_key
```
```bash
chmod 600 .env
```
### Step 3.3 — Multi-GPU with Tensor Parallelism
```bash
docker run -d \
--name vllm-server-tp4 \
--gpus '"device=0,1,2,3"' \
--shm-size=16g \
--ipc=host \
-p 8000:8000 \
-v ~/.cache/huggingface:/root/.cache/huggingface \
--env-file .env \
-e NCCL_DEBUG=WARN \
vllm/vllm-openai:v0.8.3 \
--model meta-llama/Llama-3.1-70B-Instruct \
--served-model-name llama-3.1-70b \
--tensor-parallel-size 4 \
--max-model-len 16384 \
--dtype auto \
--gpu-memory-utilization 0.90 \
--enable-prefix-caching \
--port 8000
```
## Phase 4: Production Docker Compose
### Step 4.1 — docker-compose.yml
```yaml
version: '3.8'
services:
vllm:
image: vllm/vllm-openai:v0.8.3
container_name: vllm-server
restart: unless-stopped
deploy:
resources:
reservations:
devices:
- driver: nvidia
count: all
capabilities: [gpu]
shm_size: "16g"
ipc: host
volumes:
- model-cache:/root/.cache/huggingface
env_file:
- .env
command: >
--model hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4
--served-model-name llama-3.1-8b
--max-model-len 8192
--quantization awq
--dtype auto
--gpu-memory-utilization 0.90
--enable-prefix-caching
--enable-metrics
--port 8000
healthcheck:
test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
interval: 30s
timeout: 10s
retries: 3
start_period: 120s
ports:
- "8000:8000"
volumes:
model-cache:
driver: local
```
### Step 4.2 — Start the stack
```bash
docker compose up -d
docker compose ps # Verify running
curl http://localhost:8000/health # Health check
```
## Phase 5: Kubernetes Deployment
### Step 5.1 — Prerequisites
```bash
# Install NVIDIA GPU Operator
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/gpu-operator/v1.11.0/manifests/ops/crds/crd-node-feature-discovery.yaml
helm install gpu-operator nvidia/gpu-operator --namespace gpu-operator
# Create namespace
kubectl create namespace llm-serving
```
### Step 5.2 — Create Secrets
```bash
kubectl create secret generic hf-secret \
--from-lite

## Related Articles

- [[how-to-deploy-with-vllm]]
- [[how-to-deploy-local-llm]]
- [[llm-deployment-qa]]
- [[how-to-use-cloudflare-workers-ai]]
- [[how-to-fine-tune-llm]]
