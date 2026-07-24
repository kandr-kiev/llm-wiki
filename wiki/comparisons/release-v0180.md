---
title: "Release v0.18.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - ci-cd
  - cloud
  - computer-vision
  - dataset
  - docker
  - dpo
  - fine-tuning
  - foundation-model
  - framework
  - gpu
  - image-generation
  - library
  - lora
  - multi-agent
  - multimodal
  - nlp
  - optimization
  - performance
  - qlora
  - sft
  - streaming
  - training
  - transfer-learning
---

# Release v0.18.0

> **Source:** gh-v0180-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://github.com/axolotl-ai-cloud/axolotl/releases/tag/v0.18.0 ingested: 2026-07-17 sha256: cce75bfb1855a3034a2b968581483bc76941677e67ea43bdf981a0c1c9a6ebd0 blog_source: github:axolo...
> **Sources:**
>   - gh-v0180-2026-07-17.md
> **Links:**
- [[release-v0170]]
- [[release-v0251]]
- [[v0.23.0]]
- [[v0.22.1]]
- [[v0.24.0]]

## Key Findings

---
source_url: https://github.com/axolotl-ai-cloud/axolotl/releases/tag/v0.18.0
ingested: 2026-07-17
sha256: cce75bfb1855a3034a2b968581483bc76941677e67ea43bdf981a0c1c9a6ebd0
blog_source: github:axolotl-ai-cloud/axolotl
---
# Release v0.18.0
# Axolotl v0.18.0 Release Notes
We've been hard at work doing low level improvements in the kernels. Over 90 commits since v0.17.0 (June 3, 2026), themed around fine-tuning very large sparse-MoE models cheaply: 4-bit expert LoRA/QLoRA (NVFP4, MXFP4, bnb) that runs fast and stays memory-flat at long context on Blackwell and Hopper, plus a supply-chain hardening pass on CI.
---
## Highlights
### **NVFP4 MoE-LoRA: ScatterMoE and SonicMoE**
4-bit NVFP4 expert LoRA now runs fast on both MoE kernel backends.
#### ScatterMoE
ScatterMoE gains fused NVFP4 (Marlin/DeepGEMM) and bnb-4bit expert paths for Gemma 4 (128 experts) and DeepSeek-V4. Active VRAM stays nearly flat from 4k to 32k context: NVFP4 is fastest at short sequences, bnb uses the least memory.
![scattermoe_nvfp4_gemma4](https://github.com/user-attachments/assets/156eea6e-2e3b-4db0-862e-3dcab771fa57)
Configs: `examples/gemma4/26b-a4b-moe-nvfp4-lora.yaml` (ScatterMoE)
- Contributed by @winglian in #3747
#### SonicMoE
SonicMoE adds native FP4-activation MoE-LoRA (W4A4: 4-bit weights and activations) through the quack/CUTLASS kernels. On B200 it beats the Marlin W4A16 (16-bit-activation) path at every sequence length at matched quality, validated on the Qwen3-30B-A3B and Qwen3-Next-80B-A3B NVFP4 checkpoints.
It also runs on consumer Blackwell (RTX 50xx / sm120) via the quack 0.6 migration (#3830), and the new `nvfp4_merge_aware` mode keeps the adapter bitwise-consistent when merged back into the NVFP4 base (#3822).
![sweep_fp4_scale](https://github.com/user-attachments/assets/3fe48923-7419-49fb-b56a-5d145c7f487f)
![sweep_fp4_stageD-2](https://github.com/user-attachments/assets/ca1ea76c-12b0-4d4a-8e3e-09aeb5d46503)
Configs: `examples/qwen3/30b-a3b-nvfp4-lora.yaml` (SonicMoE).
- Contributed by @NanoCode012 in #3780, #3822, and #3830.
### **GLM-5.2 (DSA) Fine-tuning with 2D Expert Parallelism**
Fine-tune GLM-5.2 (`glm_moe_dsa`) from its NVFP4 checkpoint on multi-GPU FSDP2. It follows the DeepSeek-V3.2 sparse-MLA lineage: 256 routed experts with Lightning-Indexer token selection. DeepEP expert parallelism now composes in 2D (`EP × cp`), and dedicated DSA attention kernels (`use_glm_dsa_kernels`) with rank0 + broadcast loading keep the ~250 GB 4-bit experts from OOMing on load. Config: `examples/glm_moe_dsa/glm-5.2-nvfp4-lora.yaml` (requires `deep_ep`).
- Contributed by @winglian in #3759, with post-merge fixes in #3781 (@NanoCode012) and #3832.
### **Hidden-States Activation Offloading for Long-Context Full-Parameter Training**
New `activation_offloading: hidden_states` offloads only the per-layer checkpoint input to CPU and recomputes the rest, so PCIe stays within budget where the offload-everything mode saturates it. On Qwen3-8B full-param it reaches 128k cont

## Summary

ext where plain gradient checkpointing OOMs, and the memory advantage widens with sequence length (1.23x less at 64k, tied throughput) with bit-exact gradients.
- Contributed by @winglian in #3733 and #3776.
### **Multi-Turn Inference Chat Interface**
`axolotl inference config.yaml --chat` starts an interactive multi-turn chat with streaming token output, runtime-adjustable generation parameters, and streaming reasoning blocks for thinking models.
![inference-chat](https://github.com/user-attachments/assets/c444fa99-578e-444f-8fed-8a6d4d68abfd)
- Contributed by @NanoCode012 in #3723.
---
## Performance & Kernel Optimizations
- **Blackwell (sm120) MoE-LoRA** (#3714 by @winglian): makes the vendored ScatterMoE Triton path the working MoE+LoRA story on sm120 where the SonicMoE CUTLASS kernel can't compile. EP sentinel-skip drops masked remote rows (2 to 10x fwd+bwd at ep 2 to 8), gpt_oss layout support (9.5 to 48x vs eager), fused MXFP4 with no dequant (1.7 to 3.7x, 16 to 24x less transient memory), and a SonicMoE-to-ScatterMoE fallback on sm120.
- **Grouped-Gram dA/dB for large-E MoEs** (#3712 by @winglian): recompute-free grouped-Gram LoRA weight grads plus a sync-free `dX_lora` path, up to 2.2x fwd+bwd on Qwen3-MoE / DeepSeek (E>=128), bit-identical to the split kernel.
- **LoRA kernel memory** (#3704 by @winglian): removes an intermediate materialization in the LoRA kernel op.
- **Faster multimodal assistant-only masking** (#3672 by @thad0ctor): vectorized role-boundary scanner (byte-identical to the reference) plus a fused `process_labels`, ~1.3 to 1.5x on Gemma 3/4 and Qwen 2 under DataLoader-worker conditions.
- **torch.compile coverage for 4-bit dequant** (#3677 by @thad0ctor): registers the NF4 dequant fast path as a Dynamo-opaque `torch.library.custom_op`, removing the ctypes trace failure and `get_ptr` recompile thrash on `torch_compile: true` QLoRA. Eager path is byte-identical.
- **Custom torch ops for in-repo kernels** (#3788 by @winglian): registers ~25 `axolotl::` custom ops (attention, SwiGLU/GeGLU, RMSNorm, dsv4/glm_dsa) so kernels compile without graph breaks; a follow-up (#3789) hoists multidoc routing out of the d512 attention path to clear the last graph breaks under `torch.compile`.
- **Fused LoRA for GatedDeltaNet** (#3732 by @thad0ctor): route Qwen3.5 GatedDeltaNet linear-attention LoRA projections through the fused kernel under `lora_qkv_kernel` / `lora_o_kernel`, avoiding a bf16/fp32 activation round-trip.
---
## New Features
- **Multi-adapter MoE LoRA** (#3719 by @winglian): multi-LoRA (multi-tenant) support for the ScatterMoE and SonicMoE kernels with optimized routing and gradient computation.
- **Selective activation checkpointing** (#3786 by @winglian): `selective_checkpointing` saves attention outputs (SDPA/flash-attn) instead of recomputing them, fully eager, with optional CPU offload of the saved tensors.
- **Per-module LoRA rank/alpha** (#3673 by @thad0ctor): `lora_rank_pattern` / `lora_alpha_pattern` set per-modu

## Related Articles

- [[release-v0170]]
- [[release-v0251]]
- [[v0.23.0]]
- [[v0.22.1]]
- [[v0.24.0]]
