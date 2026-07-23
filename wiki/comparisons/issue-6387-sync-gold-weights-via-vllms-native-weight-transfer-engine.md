---
title: "Issue #6387: Sync GOLD weights via vLLM's native weight transfer engine"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - api
  - async
  - backend
  - distributed
  - foundation-model
  - llm
  - open-source
  - policy
  - real-time
  - training
  - transfer-learning
  - use-case
  - zero-shot
---

# Issue #6387: Sync GOLD weights via vLLM's native weight transfer engine

> **Source:** gh-huggingfacetrl-issue-6387-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/trl/issues/6387 ingested: 2026-07-14 sha256: d087918b2b4e6756a3c9cb85795eb9b33664ac1dcb980ee1c97560f36ea82a87 blog_source: github:huggingface/trl --- # I...
> **Sources:**
>   - gh-huggingfacetrl-issue-6387-2026-07-14.md
> **Links:**
- [Issue #6385: AsyncGRPO fork-independent epoch counting]
- [[Release v1.8.0]]
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end]
- [Issue #6384: Fix SDPO/SDFT use_liger_kernel under DeepSpeed ZeRO-3 during evaluation]

## Key Findings

---
source_url: https://github.com/huggingface/trl/issues/6387
ingested: 2026-07-14
sha256: d087918b2b4e6756a3c9cb85795eb9b33664ac1dcb980ee1c97560f36ea82a87
blog_source: github:huggingface/trl
---
# Issue #6387: Sync GOLD weights via vLLM's native weight transfer engine
**State:** open | **Author:** kashif | **Created:** 2026-07-14T10:18:09Z
In vLLM server mode, GOLDTrainer now pushes updated student weights through vLLM's native weight transfer engine (https://docs.vllm.ai/en/stable/training/weight_transfer/) with packed=True, the same mechanism AsyncGRPOTrainer already uses. The engine packs tensors into 1 GB double-buffered NCCL broadcasts internally, so per-tensor round trips and manual bucketing disappear.
- trl vllm-serve exposes the four native engine endpoints (init_weight_transfer_engine, start_weight_update, update_weights, finish_weight_update), delegating to the sync LLM API
- GOLDTrainer streams params one at a time (full_tensor() per param for FSDP2), falling back to VLLMGeneration.sync_weights() for PEFT, ZeRO-3 and colocate mode
- WeightTransferClient moves from trl/experimental/async_grpo/ to trl/generation/ so gold does not import the async GRPO package; async GRPO import updated
Extracted from #6126 since X-Token training is off-policy and never syncs weights.
---
> [!NOTE]
> **Medium Risk**
> Changes the on-policy vLLM weight-sync path (NCCL rendezvous and distributed collectives); mis-sync would break generation during GOLD training, though PEFT/ZeRO-3 and colocate modes keep the prior path.
> 
> **Overview**
> **GOLDTrainer** in vLLM **server** mode can now push updated student weights through vLLM’s native weight transfer engine (`packed=True` NCCL broadcasts), matching what **AsyncGRPOTrainer** already uses, instead of always going through `VLLMGeneration.sync_weights()`.
> 
> When vLLM ≥ 0.22, server mode, and the student is neither PEFT nor DeepSpeed ZeRO-3, the trainer builds a shared **`WeightTransferClient`**, streams parameters one-by-one (with **`DTensor.full_tensor()`** on FSDP2 so ranks stay in collectives without materializing the full model), and resets the vLLM prefix cache after sync. PEFT, ZeRO-3, and non-server paths still use the existing merge/gather **`sync_weights`** path.
> 
> **`WeightTransferClient`** lives under **`trl/generation/`** (imports fixed); async GRPO only updates its import. **`trl vllm-serve`** wires **`WeightTransferConfig(backend="nccl")`** into worker **`LLM`** construction and adds HTTP routes that delegate **`init_weight_transfer_engine`**, **`start_weight_update`**, **`update_weights`**, and **`finish_weight_update`** to workers; **`start_weight_update`** no longer sends a JSON body.
> 
> Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 793799dec2b01ebc0d21d21111dbdcfd74bbc94b. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #6385: AsyncGRPO fork-independent epoch counting]
- [[Release v1.8.0]]
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end]
- [Issue #6384: Fix SDPO/SDFT use_liger_kernel under DeepSpeed ZeRO-3 during evaluation]
