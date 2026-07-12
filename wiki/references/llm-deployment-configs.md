---
title: "LLM Deployment Configurations — Reference"
type: reference
description: Ready-to-use configuration templates for deploying LLMs with Ollama, llama.cpp, and vLLM
created: 2026-07-06
updated: 2026-07-06
tags: [reference, local-llm-hardware, automation, deployment, configuration]
sources: [raw/articles/open-source-llm-landscape-2026.md]
confidence: high
links: [local-llm-hardware, how-to-deploy-local-llm, llm-quantization]
---# LLM Deployment Configurations — Reference

Ready-to-use configuration templates for deploying LLMs with Ollama, llama.cpp, and vLLM.

## Ollama Configurations

### Minimal Modelfile (8B model)
```
FROM llama3.1:8b
SYSTEM "You are a helpful technical assistant. Be concise and accurate."
PARAMETER temperature 0.7
PARAMETER num_ctx 8192
PARAMETER num_gpu_layers 35
```

### High-Quality Modelfile (70B model)
```
FROM llama3.1:70b
SYSTEM "You are an expert technical assistant. Provide detailed, accurate responses with code examples when relevant."
PARAMETER temperature 0.3
PARAMETER num_ctx 131072
PARAMETER num_gpu_layers -1
PARAMETER top_p 0.9
PARAMETER repeat_penalty 1.1
```

### Fine-tuned Modelfile
```
FROM llama3.1:8b
ADAPTER ./my-finetune.safetensors
SYSTEM "You are a medical assistant. Always cite your sources."
PARAMETER temperature 0.2
PARAMETER num_ctx 4096
```

## llama.cpp Configurations

### CLI invocation (8B, 4-bit)
```bash
./build/bin/llama-cli \
  -m ./models/llama-3.1-8b-instruct.Q4_K_M.gguf \
  -p "You are a helpful assistant. Question: " \
  -n 512 \
  --temp 0.7 \
  --ctx-size 8192 \
  --threads 8 \
  --gpu-layers 35
```

### Server mode (70B, multi-GPU)
```bash
./build/bin/llama-server \
  -m ./models/llama-3.1-70b-instruct.Q4_K_M.gguf \
  -c 131072 \
  --host 0.0.0.0 \
  --port 8080 \
  --threads 16 \
  --gpu-layers 99 \
  --log-disable
```

### Batch inference
```bash
./build/bin/llama-bench \
  -m ./models/llama-3.1-8b-instruct.Q4_K_M.gguf \
  -n 128 \
  -b 1 \
  -t 8 \
  -ngl 35 \
  -d 8192
```

## vLLM Configurations

### Docker Compose (single GPU)
```yaml
version: '3.8'
services:
  llm-server:
    image: vllm/vllm-openai:latest
    container_name: llm-server
    runtime: nvidia
    ports:
      - "8000:8000"
    environment:
      - HUGGING_FACE_HUB_TOKEN=${HF_TOKEN}
    volumes:
      - ./models:/models
    command: >
      meta-llama/Meta-Llama-3.1-8B-Instruct
      --host 0.0.0.0
      --port 8000
      --max-model-len 8192
      --gpu-memory-utilization 0.9
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

### Multi-GPU configuration
```yaml
version: '3.8'
services:
  llm-server:
    image: vllm/vllm-openai:latest
    container_name: llm-server-70b
    runtime: nvidia
    ports:
      - "8000:8000"
    environment:
      - HUGGING_FACE_HUB_TOKEN=${HF_TOKEN}
    command: >
      meta-llama/Meta-Llama-3.1-70B-Instruct
      --host 0.0.0.0
      --port 8000
      --tensor-parallel-size 4
      --max-model-len 16384
      --gpu-memory-utilization 0.95
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 4
              capabilities: [gpu]
```

## Environment Variables

### HuggingFace
```bash
export HF_TOKEN="hf_your_token_here"
export HF_HOME="/path/to/cache"
```

### vLLM
```bash
export VLLM_WORKER_MULTIPROC_METHOD="spawn"
export VLLM_LOGGING_LEVEL="INFO"
export VLLM_TARGET_DEVICE="cuda"
```

### llama.cpp
```bash
export LLAMA_NO_MMAP=true
export LLAMA_MULTITHREAD_MMAP=true
export LLAMA_LOG_LEVEL=3
```

### Ollama
```bash
export OLLAMA_HOST="0.0.0.0:11434"
export OLLAMA_MODELS="/path/to/models"
export OLLAMA_KEEP_ALIVE="24h"
export OLLAMA_NUM_PARALLEL=4
```

## Quick Reference: Parameter Tuning

| Parameter | Low Value | Medium | High | Effect |
|---|---|---|---|---|
| `temperature` | 0.1 | 0.7 | 1.0 | Creativity vs determinism |
| `top_p` | 0.5 | 0.9 | 1.0 | Nucleus sampling threshold |
| `num_ctx` | 2048 | 8192 | 131072 | Context window size |
| `num_gpu_layers` | 0 | 30 | -1 | Layers on GPU (0=CPU, -1=all) |
| `threads` | 2 | 8 | 32 | CPU threads for inference |
| `repeat_penalty` | 1.0 | 1.1 | 1.5 | Repetition suppression |
| `max_tokens` | 128 | 512 | 4096 | Max output length |

## Key References

- `[[concepts/local-llm-hardware]]` — Hardware requirements
- `[[playbooks/how-to-deploy-local-llm]]` — Deployment runbook
- `[[llm-quantization]]` — Quantization methods
