---
title: "Release v0.17.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - backend
  - cloud
  - computer-vision
  - cuda
  - data
  - distributed
  - docker
  - dpo
  - evaluation
  - fine-tuning
  - foundation-model
  - framework
  - gpu
  - guide
  - hardware
  - image-generation
  - integration
  - library
  - llama
  - lora
  - mistral
  - multi-agent
  - multimodal
  - parallel
  - performance
  - policy
  - pytorch
  - qlora
  - quantization
  - reinforcement-learning
  - security
  - sft
  - standards
  - system-design
  - training
  - use-case
---

# Release v0.17.0

> **Source:** gh-v0170-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/axolotl-ai-cloud/axolotl/releases/tag/v0.17.0 ingested: 2026-07-14 sha256: 72951ac1ff98fcaaee946e2665e929f27d4d27c5c1911a5f7864fd2697c1f820 blog_source: github:axolo...
> **Sources:**
>   - gh-v0170-2026-07-14.md
> **Links:**
- [[v0.22.1]]
- [[v0.23.0]]
- [[v0.24.0]]
- [[Release v0.1.481-beta]]
- [[Release 5.0.0]]

## Key Findings

---
source_url: https://github.com/axolotl-ai-cloud/axolotl/releases/tag/v0.17.0
ingested: 2026-07-14
sha256: 72951ac1ff98fcaaee946e2665e929f27d4d27c5c1911a5f7864fd2697c1f820
blog_source: github:axolotl-ai-cloud/axolotl
---
# Release v0.17.0
# Axolotl v0.17.0 Release Notes
Another packed release. ~84 commits since v0.16.1 last month, bringing Expert Parallelism for MoE training, BitNet 1.58-bit fine-tuning, remote training via Tinker, context parallelism for hybrid SSM models, MXFP4 ScatterMoE-LoRA, fused RMSNorm+RoPE kernels for the Qwen3 family, a systemic fix for multimodal loss masking, a `uv`-first install path, and a long tail of stability/perf work on FSDP2, Gemma 4, and DPO.
---
## Highlights
### **Expert Parallelism (EP) via DeepEP**
Distributed MoE training across ranks via DeepSeek's [DeepEP](https://github.com/deepseek-ai/DeepEP) all-to-all kernels, verified on 2×A100, 4×A100, 8×H100, and EP + FSDP composition. Hopper low-latency kernels and TP/CP composition are follow-ups. See the [Expert Parallelism docs](https://docs.axolotl.ai/docs/nd_parallelism.html) and [DeepEP integration guide](https://docs.axolotl.ai/docs/custom_integrations.html#expert-parallelism-integration).
![qwen30b_h100_chart](https://github.com/user-attachments/assets/cd9b5f55-9ca1-4186-aee5-c4966bab6da4)
![sweep_speedup](https://github.com/user-attachments/assets/59a2cc89-195e-4ddf-a1ba-97b139965184)
- Contributed by @NanoCode012 in #3632.
### **Train on Remote Compute via Tinker-compatible APIs**
Run training against a Tinker / Hatchery API endpoint instead of local hardware, with example SFT and GRPO configs plus a math reward function for RL workflows.
- Contributed by @winglian in #3614.
### **BitNet 1.58-bit Fine-tuning**
Full fine-tuning support for BitNet via the [`onebitllms`](https://github.com/tiiuae/onebitllms) library, with config-validation guards against incompatible LoRA setups and a setup guide for post-training conversion.
- Contributed by @younesbelkada in #3634 and #3636.
### **Q-GaLore Optimizer**
New memory-efficient optimizer `q_galore_adamw8bit` based on [Q-GaLore](https://arxiv.org/pdf/2407.08296). Requires FSDP2, full fine-tuning, and bf16. Not compatible with adapters.
- Contributed by @ved1beta in #3654.
### **MoRA / ReMoRA Integration**
Optional [MoRA](https://arxiv.org/abs/2405.12130) (Mixture-of-Rank-Adapters) support with ReMoRA restart scheduling, registered through a new plugin-based adapter system so future custom adapters can slot in the same way. A companion ReLoRA cleanup fixes the optimizer reset scope, adds a configurable `relora_prune_method`, and renames `relora_steps` → `jagged_restart_steps` (**breaking**, see Deprecations).
- Contributed by @winglian in #3647 and #3646.
### **Multimodal Assistant-only Loss Masking**
Fixes a long-standing bug where `train_on_inputs` / `roles_to_train` / `train_on_eos` were silently ignored in the multimodal collator: every model except Gemma 3n was training on the full sequence regardless 

## Summary

of config. New per-template strategies for Gemma 4, Llama 3.2 Vision, Llama 4, Pixtral, and Mistral V7 Tekken, plus an opt-in `cfg.role_boundaries` override for unverified templates.
> **Heads up:** if you were training multimodal models on assistant-only data, your loss values will change after upgrading. This is expected.
- Contributed by @thad0ctor in #3625.
### **DPO Loss Types & SimPO LoRA fix**
New `dpo_loss_type` (list) and `dpo_loss_weights` config knobs expose the full TRL ≥ 0.29 loss menu and let users mix multiple DPO losses with custom weightings, restoring losses like RPO that broke after the TRL 0.29 refactor. Separately, `rl: simpo` + LoRA no longer raises `ValueError: You passed a PeftModel instance together with a peft_config`.
> **Deprecation:** `rl: ipo` is deprecated. Use `rl: dpo` with `dpo_loss_type: ["ipo"]` instead.
- Contributed by @BrownianNotion in #3566 and @ved1beta in #3665.
### **Context Parallelism for Hybrid SSM Models**
Context parallel support for hybrid attention + Mamba2 SSM models (**Nemotron-H, Falcon-H1, Bamba, Granite MoE Hybrid, and Zamba2**), plus `seq_idx` threading so SSM state resets correctly at packed-sequence boundaries. Uses an exact additive correction (exploiting SSM linearity) with one P2P round per layer, not the O(world_size) of ring attention.
- Contributed by @ved1beta in #3572.
### **uv-first installs and Docker images**
`uv` is now the recommended package manager. New `-uv` Docker image variants ship with a generated lockfile and a migration guide from pip; minimum PyTorch is bumped to 2.9.1.
- Contributed by @NanoCode012 in #3545.
### **Gemma 4 Hybrid Attention + Fused RMSNorm/RoPE Kernels**
Mixed FA + SDPA dispatch for Gemma 4 (FA2 on standard layers, SDPA where head_dim=512 OOMs FA2), plus a fused RMSNorm+RoPE Triton kernel. Enable via `gemma4_hybrid_attn_impl: true`. A VRAM leak in this path under activation checkpointing was also fixed.
- Contributed by @winglian in #3598 and @thad0ctor in #3611.
### **Fused RMSNorm+RoPE Kernels for Qwen3 / Qwen3.X**
Generalizes the Gemma 4 fused RMSNorm+RoPE Triton kernel to the Qwen3 family (Qwen3, Qwen3-MoE, Qwen3.5, Qwen3.6, Qwen3-VL) behind a new opt-in `cfg.fused_attn_kernel`, and auto-enables Liger's fused (m-)rope for the Qwen-VL models.
- Contributed by @thad0ctor in #3680.
### **ScatterMoE-LoRA: MXFP4 Weights and Tiled-MLP for Long Context**
Adds MXFP4-quantized expert weights to ScatterMoE-LoRA for memory-efficient MoE adapter training, plus a tiled-MLP path (FSDP2 reshard fix, grad-accumulator dtype fix, and a shard-count heuristic worth 3.2× at long context). An INT64 indices fix in the `scatter2scatter` Triton family resolves silent cuBLAS failures when routed-token offsets cross the 2³¹ boundary.
- Contributed by @winglian in #3663 (MXFP4), #3666 (tiled-MLP), and #3667 (INT64 indices).
---
## Performance & Kernel Optimizations
- **Pre-cache eot token ids** (#3594 by @winglian): avoids recomputing on every iteration.
- **DPO collation p

## Related Articles

- [[v0.22.1]]
- [[v0.23.0]]
- [[v0.24.0]]
- [[Release v0.1.481-beta]]
- [[Release 5.0.0]]
