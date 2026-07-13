---
title: "Release Notes: vLLM vv0.24.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - async
  - audio-generation
  - backend
  - computer-vision
  - cuda
  - distributed
  - embedding
  - fine-tuning
  - foundation-model
  - frontend
  - gpt
  - gpu
  - hardware
  - image-generation
  - integration
  - library
  - llm
  - lora
  - multi-agent
  - multimodal
  - nlp
  - offline
  - online
  - open-source
  - optimization
  - parallel
  - performance
  - pipeline
  - policy
  - preprocessing
  - prompt-tuning
  - quantization
  - retrieval
  - search
  - self-supervised
  - stable-diffusion
  - streaming
  - tool
  - transfer-learning
  - video-generation
  - zero-shot
---
# Release Notes: vLLM vv0.24.0

> **Source:** gh-vllm-release-v0.24.0-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/unknown/unknown ingested: 2026-07-11 sha256: 251aa5f88e7be35cc5f38e591223d94ad71241d2587c7e4d69c7398b38a99474 blog_source: github:unknown --- # Release Notes: vLLM v...
> **Sources:**
>   - gh-vllm-release-v0.24.0-2026-07-10.md
> **Links:**
- [[release-notes-ollama-vv0312]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-notes-pytorch-vv2130]]
- [[release-v0390]]
- [[release-v1140]]

## Key Findings

---
source_url: https://github.com/unknown/unknown
ingested: 2026-07-11
sha256: 251aa5f88e7be35cc5f38e591223d94ad71241d2587c7e4d69c7398b38a99474
blog_source: github:unknown
---
# Release Notes: vLLM vv0.24.0
**Source:** https://github.com/vllm-project/vllm/releases/tag/v0.24.0
**Published:** 2026-07-10 19:55 UTC
**Type:** Release notes / changelog
---
## What's New
# vLLM v0.24.0 Release Notes
## Highlights
This release features 571 commits from 256 contributors (77 new)!
* **MiniMax-M3**: Added support for the new **MiniMax-M3** model (#45381), with a fast follow-on of BF16/FP8 indexer via MSA (#45892), MXFP4 support (#45896), FP8 sparse GQA (#45744), and extensive AMD/ROCm tuning — mxfp8 MoE/linear on gfx950 (#45725), fp8_per_channel for bf16 weights on MI300X (#45854), FP8 KV-cache fix (#45720), and packed-modules mapping (#45794). A MiniMax-M2 perf regression was also fixed (#45935).
* **DeepSeek-V4 keeps maturing**: Following its debut, DeepSeek-V4 received another large optimization pass — a FlashInfer sparse index cache (2–4% TTFT) (#45863), prefill chunk-planning optimization (4% E2E throughput) (#45061), a cluster-cooperative topK kernel for low-latency (#43008), contiguous per-block KV allocations (#44577), TEP=16 for the block-FP8 shared expert (#46001), and native DSA indexer decode for `next_n > 2` on SM100 (#45322). It is now enabled on **SM120** alongside GLM-5.1 (#43477), with XPU (#44144, #44517, #45240) and ROCm (#44899, #45103, #45681) attention/MoE paths added.
* **Model Runner V2 (MRv2) continues to expand**: MRv2 now **supports quantized models by default** (#44446), enables **GraniteMoE by default** (#45461), and gained migration of Qwen + DeepSeek-V2 MoE models (#42667), DFlash speculative decoding (#44586), and more accurate FP32 Gumbel sampling (#45996).
* **Streaming Parser Engine**: A new streaming parser engine unifies tool-call/reasoning parsing across models, with parsers for Qwen3 (#45413), MiniMax-M2 (#45701), GLM-4.7/5.1/5.2 (#45915), and Nemotron V3 (#45755).
* **Diffusion LLMs**: Added **DiffusionGemma** (#45163), including a CPU path (#45690) and structured-output guardrails for diffusion decoders (#45468).
* **WideEP / DeepEP v2**: Integrated **DeepEP v2** for expert parallelism (#41183), with follow-on robustness fixes (#46404, #46432).
* **Rust frontend matures further**: Added API-key authentication (#44321), CORS (#45753), `/tokenize` + `/detokenize` (#44222), `/pause` `/resume` `/is_paused` (#44499), `/abort_requests` (#44382), `/get_world_size` (#44801), `thinking_token_budget` (#46137), a Python bridge for Rust tool parsers (#44624), and many new parsers and validation paths.
* **Device selection change**: vLLM no longer sets `CUDA_VISIBLE_DEVICES` internally; a new `device_ids` argument is provided instead (#45026). On ROCm, a deprecation window for `CUDA_VISIBLE_DEVICES` has begun (#46636).
### Model Support
* **New models**: MiniMax-M3 (#45381), DiffusionGemma (#45163) + Gemma Diffusion on CPU (#456

## Summary

90), Hierarchical Reasoning Model — Text / HrmTextForCausalLM (#43098), OpenMOSS (#44124).
* **Gemma 4**: Unified FlashAttention (FA4) across all layers + `mm_prefix` support (#42175); many parser/serving fixes — forced-JSON skip for required/named tool choice (#45795), parsing with thinking disabled (#45832), streaming reasoning-state init (#45852), reasoning rendering on assistant turns (#45867), offline-parser truncation/token-leak fix (#45553); legacy Gemma4 parsers replaced with an engine-based implementation (#45588).
* **DeepSeek-V4**: OOM fix (#44914), MTP projection prefixing (#44821), supported KV-cache dtypes (#44892).
* **Qwen / multimodal**: Qwen3-VL video loader (#44412), Qwen2-VL/Qwen2.5-VL processor-mapped video loader (#45555), Qwen3-VL multi-video processing optimization (#46026) and multi-video crash fix (#46305), Qwen3-Omni VIT cu_seqlens device fix (#44264), fused qk-rmsnorm-rope-gate for Qwen3.5 (#44176), Qwen3.5 EP weight-loading fix (#45002).
* **ViT full CUDA graph**: GLM-4.1V (#40576), DeepSeek-OCR dual-path (#43586), Kimi-VL (#41992), mllama4 (#40660), Lfm2VL encoder (#44930).
* **Other model fixes**: Llama4 weight loading (#45047) and streamed loading to avoid host-OOM (#44645), MiMo v2.x QKV TP sharding + FP4 (#45200), ColQwen3.5 retrieval correctness (#46108), EXAONE-4.5 vision encoder (#45073), MiDashengLM TP>1 audio-encoder crash (#44408), MiniCPM-o/V device-placement and image-size fixes (#43844, #42332, #44980, #45244), Cohere2 MoE weight loading + parser (#44747, #44907), Nemotron V3 reasoning-as-content (#39091), ColBERT AutoWeightsLoader + query/document embedding io processor (#44999, #45210).
* **Kernels**: GLM-5 TRT-LLM ragged MLA prefill dimensions (#43525), GLM-5 router GEMM (#46385).
### Engine Core
* **Model Runner V2**: Quantized models by default (#44446), GraniteMoE default (#45461), Qwen/DSv2 MoE migration (#42667), DFlash (#44586), simplified async output handling (#45442), attention-group split on `num_heads_q` (#45564), LoRA warmup fix (#35536), more accurate FP32 Gumbel sampling (#45996), `min_tokens` off-by-one fix in the V2 GPU sampler (#46243), plus assorted model/config compatibility fixes (#45868).
* **Speculative decoding**: Dynamic SD (#32374); DFlash with FlashInfer (#43081), mixed KV page sizes (#45181), and Qwen3Next targets (#45319); EAGLE3 support for Qwen3 (#43132); reduced TP communication for large-vocab drafts (#39419); race fix in async accepted counts (#45100); EAGLE multimodal encoder cache fixes (#46315).
* **KV cache & scheduler**: KV-cache watermark to reduce preemptions (#44594), two-phase allocation for cross-group prefix-cache hits (#44409), Marconi-style admission policy for hybrid cache (#37898), prefix-cache retention for Mamba/linear attention (#45845), DS Mamba tail-copy for MTP align mode (#45473), reduced scheduler copy overhead (#45840).
* **Attention**: Re-enabled cross-layer KV cache layout for MLA via stride-aware kernels (#45111), MLA prefill FA4 fp8 output (

## Related Articles

- [[release-notes-ollama-vv0312]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-notes-pytorch-vv2130]]
- [[release-v0390]]
- [[release-v1140]]
