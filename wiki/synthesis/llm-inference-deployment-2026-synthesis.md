---
title: "LLM Inference & Deployment — Multi-Source Synthesis"
type: synthesis
description: Integrated analysis of LLM inference optimization combining quantization methods, hardware acceleration, serving frameworks, and fine-tuning strategies from 5+ sources
created: 2026-07-08
updated: 2026-07-08
tags: [synthesis, inference, deployment, quantization, hardware, serving, fine-tuning, rag]
sources: [raw/articles/llm-quantization-gguf-gptq-awq.md, raw/articles/cloudflare-workers-ai-rest-api-2026.md, raw/articles/llm-fine-tuning-lora-qlora-dpo-2026.md]
confidence: high
links: [llm-quantization, ml-infrastructure, enterprise-ai, llm-fine-tuning, vllm]
---# LLM Inference & Deployment — Multi-Source Synthesis

Integrated analysis of the LLM inference and deployment landscape as of mid-2026, combining quantization methods, serving frameworks, fine-tuning strategies, and hardware considerations.

## Executive Summary

By mid-2026, LLM deployment has matured into a multi-layered ecosystem where the choice of inference stack depends on three factors: **scale** (local vs. enterprise), **performance** (latency vs. throughput), and **cost** (GPU hours vs. API spend).

Three key trends define the landscape:

1. **Quantization has become the default** — 4-bit models are production-standard; quality loss is <2% for most tasks
2. **Serving frameworks have converged** — vLLM, SGLang, and TensorRT-LLM capture 90% of production deployments
3. **Fine-tuning is democratized** — LoRA/QLoRA enables custom model training on consumer hardware (<$100)

## 1. Quantization Methods — Complete Comparison

Quantization reduces model precision from 32-bit float to 4-8 bit integers, enabling faster inference on smaller hardware.

### Method Comparison

| Method | Best Hardware | Precision | Quality Loss | Calibration Required | Use Case |
|---|---|---|---|---|---|
| **GPTQ** | NVIDIA GPU | 4-bit | <2% | Yes (calibration set) | GPU production serving |
| **AWQ** | NVIDIA GPU | 4-bit | <1.5% | Yes (activation analysis) | Instruction-tuned models |
| **GGUF** | CPU / Mac | 2-8-bit | 2-5% | No | Local inference, Mac |
| **SmoothQuant** | NVIDIA GPU | 8-bit | <1% | Yes (outlier reduction) | Low-latency production |
| **Marlin** | NVIDIA GPU | 4-bit | <2% | Yes (GPTQ-based) | Optimized GPU kernels |

### Method Selection Guide

```
What hardware do you have?
├── NVIDIA GPU (A100/H100) → GPTQ or AWQ
│   ├── Production serving → GPTQ + vLLM
│   └── Instruction model → AWQ
├── CPU / Mac → GGUF + llama.cpp
├── Low latency required → SmoothQuant
└── Maximum optimization → Marlin kernel
```

### Quantization Pipeline

```
1. Original model (FP16/FP32)
   ↓
2. Calibration dataset (128-512 samples)
   ↓
3. Quantization method (GPTQ/AWQ/SmoothQuant)
   ↓
4. Validation (perplexity, benchmark scores)
   ↓
5. Production deployment (vLLM/TensorRT-LLM)
```

### Key Insight

> GPTQ is the production standard for GPU inference. AWQ slightly outperforms GPTQ on instruction-tuned models. GGUF is the only practical option for CPU/Mac inference. SmoothQuant achieves the best accuracy at 8-bit but requires more complex pipelines.

## 2. Serving Frameworks — Production Landscape

### Framework Comparison

| Framework | Max Concurrency | Throughput | Latency | GPU Memory | Ecosystem |
|---|---|---|---|---|---|
| **vLLM** | 10,000+ | Highest | Low | PagedAttention optimized | Largest (PyTorch-native) |
| **SGLang** | 8,000+ | Very high | Very low | RadixTree caching | Growing (research-focused) |
| **TensorRT-LLM** | 15,000+ | Highest | Lowest | NVIDIA-optimized | NVIDIA-only |
| **TGI (TextGen)** | 5,000+ | High | Medium | Hugging Face native | Hugging Face ecosystem |
| **Ollama** | 100-500 | Low | High | GGUF-optimized | Local/dev focused |

### Framework Selection Decision Tree

```
What's your deployment target?
├── Maximum throughput → TensorRT-LLM (NVIDIA only)
├── Best all-rounder → vLLM (recommended default)
├── Low latency → SGLang (RadixTree caching)
├── Hugging Face native → TGI
└── Local development → Ollama
```

### vLLM — The Production Standard

vLLM dominates production deployments due to:

1. **PagedAttention** — GPU memory management inspired by OS virtual memory, eliminating fragmentation
2. **Continuous batching** — Dynamic batch size optimization, no static batch windows
3. **Multi-GPU support** — Model parallelism across multiple GPUs
4. **Speculative decoding** — Speedup via small model draft + large model verify
5. **Ecosystem** — PyTorch-native, supports 150+ model architectures

### SGLang — The Latency Optimizer

SGLang excels where vLLM doesn't:

1. **RadixTree** — Caches partial computation graphs for repeated prompts
2. **Structured output** — Native JSON/schema enforcement
3. **FastAPI integration** — Built-in API layer
4. **Research-friendly** — Easy to modify and extend

### Key Insight

> vLLM is the default for production. Choose SGLang when you need structured output or have many repeated prompt prefixes. Choose TensorRT-LLM only if you're NVIDIA-only and need maximum throughput.

## 3. Fine-Tuning Strategies — From LoRA to DPO

Fine-tuning adapts pre-trained models to specific domains, tasks, or styles.

### Fine-Tuning Method Comparison

| Method | Parameters Updated | GPU Required | Quality | Speed | Use Case |
|---|---|---|---|---|---|
| **Full fine-tune** | All (billions) | 8× A100 | Highest | Weeks | Domain-specific foundation models |
| **LoRA** | <1% | 1× A100 | High | Hours | Domain adaptation |
| **QLoRA** | <1% (4-bit) | 1× 24GB GPU | High-High | Hours | Consumer hardware fine-tuning |
| **DPO** | All (via LoRA) | 1× A100 | Highest | Hours | Alignment, preference tuning |
| **ORPO** | All (via LoRA) | 1× A100 | High | Hours | Combined SFT + alignment |

### Fine-Tuning Pipeline

```
1. Base model (Llama 3.1 70B, Mistral Large 3...)
   ↓
2. Dataset preparation (1K-100K examples)
   ↓
3. Method selection (LoRA/QLoRA/DPO)
   ↓
4. Training (1-7 days depending on size)
   ↓
5. Evaluation (domain benchmarks, human eval)
   ↓
6. Deployment (merge LoRA weights → production model)
```

### QLoRA — The Game Changer

QLoRA enables fine-tuning 70B models on a single consumer GPU:

- **4-bit NF4 quantization** — Near-lossless compression
- **Double quantization** — Further reduces memory
- **LoRA adapters** — Only update <1% of parameters
- **Result**: Fine-tune Llama 3.1 70B on a single RTX 4090 (24GB)

### DPO vs RLHF

| Aspect | RLHF | DPO |
|---|---|---|
| **Reward model** | Separate model needed | Implicit (no reward model) |
| **Training stability** | Unstable (PPO) | Stable (direct optimization) |
| **Compute** | 2× more (reward + policy) | 1× (single model) |
| **Quality** | Slightly higher | Comparable |
| **Complexity** | High | Low |
| **2026 standard** | Legacy | **Recommended** |

### Key Insight

> For 95% of use cases, QLoRA + DPO is the optimal fine-tuning stack. It works on consumer hardware, is stable, and produces quality comparable to full fine-tuning. Only use full fine-tuning when adapting foundation models for entirely new domains.

## 4. Hardware — GPU Selection Guide

### GPU Comparison for LLM Inference

| GPU | VRAM | FP16 TFLOPS | Price | Best For |
|---|---|---|---|---|
| **H100 SXM** | 80GB | 989 | ~$30K | Production serving (max throughput) |
| **H100 PCIe** | 80GB | 670 | ~$25K | Production serving (cost-effective) |
| **A100 80GB** | 80GB | 312 | ~$10K | Production serving (budget) |
| **RTX 4090** | 24GB | 83 | ~$1.6K | Local dev, fine-tuning |
| **Mac M4 Max** | 128GB | ~200 | ~$4K | Local inference (CPU-like) |
| **L40S** | 48GB | 303 | ~$8K | Mid-tier production |

### Hardware Scaling Formula

```
Model size (parameters) → VRAM requirement:
├── 7B model → 14GB (FP16) / 4GB (4-bit)
├── 13B model → 26GB / 7GB
├── 34B model → 68GB / 20GB
├── 70B model → 140GB / 40GB
├── 405B model → 810GB / 230GB
└── Scale by: VRAM ≈ params × 2 (FP16) or params × 0.5 (4-bit)
```

### Multi-GPU Configuration

```
70B model:
├── 4× A100 80GB → Tensor parallelism (4-way)
├── 2× H100 80GB → Pipeline parallelism (2-way)
└── 8× A100 40GB → Model parallelism (8-way)

405B model:
├── 8× H100 80GB → Standard config
└── 16× A100 80GB → Budget alternative
```

### Key Insight

> For production: H100 SXM is the gold standard. For cost optimization: A100 80GB offers best price/performance. For local dev: RTX 4090 (24GB) runs 7B models comfortably and 13B at 4-bit. For Mac users: M4 Max 128GB runs 70B at 4-bit.

## 5. Cloud Inference — Serverless vs Dedicated

### Cloud Provider Comparison

| Provider | Models | Pricing | Scaling | Best For |
|---|---|---|---|---|
| **Cloudflare Workers AI** | Llama, Mistral, Mixtral | $0.07/1M tokens | Auto-scale | Low-latency edge inference |
| **AWS Bedrock** | Claude, Llama, Titan | $0.80-2.00/1M tokens | Auto-scale | Enterprise integration |
| **Azure AI** | GPT, Llama, Mistral | $1.00-4.00/1M tokens | Auto-scale | Microsoft ecosystem |
| **Google Vertex AI** | Gemini, Llama, Mistral | $0.50-3.00/1M tokens | Auto-scale | Google ecosystem |
| **Together AI** | 200+ open models | $0.20-0.80/1M tokens | Manual | Open-source models |
| **Replicate** | 10,000+ models | Per-second billing | Auto-scale | Experimentation |

### Cloud vs Self-Hosted Cost Analysis

| Scale | Self-Hosted (GPU) | Cloud API | Recommendation |
|---|---|---|---|
| <100 req/day | $2K-5K/mo (hardware) | $50-200/mo | **Cloud** |
| 100-1K req/day | $5K-10K/mo | $200-2K/mo | **Cloud** |
| 1K-10K req/day | $10K-20K/mo | $2K-10K/mo | **Hybrid** |
| >10K req/day | $20K+/mo | $10K+/mo | **Self-hosted** |

### Key Insight

> Cloud inference is cost-effective up to ~10K requests/day. Beyond that, self-hosting becomes cheaper. Cloudflare Workers AI is the best option for low-latency edge inference (<50ms). For maximum cost efficiency on open models, use Together AI or Replicate.

## 6. RAG — The Production Pattern

Retrieval-Augmented Generation (RAG) combines external knowledge with LLM reasoning, enabling up-to-date, grounded responses.

### RAG Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Documents   │────▶│  Embedding  │────▶│  Vector DB  │
│  (PDF, web)  │     │  Model      │     │  (Pinecone) │
└─────────────┘     └─────────────┘     └─────────────┘
                                              │
                                              ↓
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  LLM Output  │◀────│  LLM        │◀────│  Context    │
│  (answer)    │     │  + RAG      │     │  (top-k)    │
└─────────────┘     └─────────────┘     └─────────────┘
```

### RAG Stack (2026)

| Component | Options | Recommendation |
|---|---|---|
| **Embedding** | Cohere embed-v3, BGE-M3, text-embedding-3 | Cohere embed-english-v3 |
| **Vector DB** | Pinecone, Weaviate, Qdrant, Milvus | Qdrant (self-hosted) or Pinecone (managed) |
| **Chunking** | Semantic, recursive, document-aware | Semantic chunking (by paragraph/topic) |
| **Retrieval** | Similarity search, hybrid, multi-query | Hybrid (BM25 + vector) |
| **Re-ranking** | Cohere Rerank, BGE Reranker, Jina Reranker | Cohere Rerank v3 |
| **LLM** | Any (via vLLM, OpenAI, Anthropic) | Match RAG quality to task complexity |

### RAG Quality Factors

| Factor | Impact | Improvement |
|---|---|---|
| **Chunk size** | High | 256-1024 tokens optimal |
| **Embedding quality** | High | Domain-specific embeddings |
| **Re-ranking** | Medium-High | Top-20 → top-5 re-ranking |
| **Context window** | Medium | Use full context, don't truncate |
| **Query rewriting** | Medium | Expand queries before retrieval |
| **Source quality** | High | Garbage in, garbage out |

### Key Insight

> RAG quality is 80% data engineering, 20% LLM engineering. Invest in chunking strategy, embedding quality, and re-ranking before optimizing the LLM. A good RAG system with a mediocre LLM outperforms a bad RAG system with a great LLM.

## 7. Decision Framework

### Complete Deployment Decision Tree

```
What's your deployment scenario?
├── Local development → GGUF + Ollama + RTX 4090
├── Local fine-tuning → QLoRA + RTX 4090 + Hugging Face
├── Small-scale API → Cloudflare Workers AI / Together AI
├── Medium-scale API → Cloud API (AWS Bedrock)
├── Large-scale API → Self-hosted vLLM + A100/H100
├── Maximum throughput → TensorRT-LLM + H100 SXM
├── RAG system → vLLM + Qdrant + Cohere embed-v3
└── Fine-tuned model → QLoRA + DPO + vLLM serving
```

### Cost Optimization Checklist

- [ ] Use 4-bit quantization (GPTQ/AWQ) — 4× memory reduction
- [ ] Enable continuous batching (vLLM) — 2-3× throughput increase
- [ ] Use speculative decoding — 1.5-2× speedup
- [ ] Cache repeated prompts (SGLang RadixTree) — 3-5× for repetitive workloads
- [ ] Batch requests — 2-4× throughput improvement
- [ ] Use appropriate GPU — don't oversize for workload
- [ ] Monitor token usage — set budgets and alerts

## 8. Risks and Considerations

| Risk | Likelihood | Mitigation |
|---|---|---|
| **Quantization quality loss** | Medium | Validate on domain benchmarks before deployment |
| **GPU supply constraints** | Medium | Cloud fallback, mixed deployment |
| **Model drift (RAG)** | High | Regular knowledge base updates |
| **Cost overruns (cloud)** | High | Set budgets, monitor usage |
| **Security (self-hosted)** | Medium | Network isolation, authentication |
| **Framework lock-in** | Low | Abstract inference behind API layer |

## 9. Recommendations

### For Individuals

1. **Local dev**: RTX 4090 + GGUF + Ollama
2. **Fine-tuning**: QLoRA on RTX 4090 (single GPU)
3. **Quick deployment**: Cloudflare Workers AI

### For Teams

1. **Default stack**: vLLM + GPTQ 4-bit + A100
2. **Fine-tuning**: QLoRA + DPO + Hugging Face
3. **RAG**: Cohere embed-v3 + Qdrant + Cohere Rerank

### For Enterprises

1. **Production serving**: vLLM or TensorRT-LLM on H100 SXM
2. **Fine-tuning pipeline**: QLoRA + DPO + domain-specific eval
3. **RAG architecture**: Hybrid retrieval + re-ranking + full context
4. **Cost strategy**: Self-host >10K req/day, cloud <10K req/day

## Sources Synthesized

1. `llm-quantization-gguf-gptq-awq.md` — Quantization methods (GPTQ, AWQ, GGUF, SmoothQuant)
2. `cloudflare-workers-ai-rest-api-2026.md` — Cloud inference via Cloudflare Workers AI
3. `the-ultimate-guide-to-fine-tuning-llms-in-2026.md` — Fine-tuning strategies (LoRA, QLoRA, DPO)
4. `vllm-production-llm-serving.md` — vLLM serving framework deep-dive
