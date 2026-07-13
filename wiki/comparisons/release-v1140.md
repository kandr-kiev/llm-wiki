---
title: "Release v1.14.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - analysis
  - backend
  - batch
  - ci-cd
  - cuda
  - data
  - dataset
  - distributed
  - docker
  - embedding
  - foundation-model
  - policy
  - pytorch
  - qlora
  - quantization
  - security
  - use-case
  - workflow
---
# Release v1.14.0

> **Source:** gh-v1140-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/accelerate/releases/tag/v1.14.0 ingested: 2026-07-11 sha256: 1e6b4b534ad120e5015b5d97e036bc8cfc9db7fa67fd68e9841343ec2e86f566 blog_source: github:hugging...
> **Sources:**
>   - gh-v1140-2026-07-11.md
> **Links:**
- [[issue-6360-bump-the-actions-group-with-9-updates]]
- [[release-notes-ollama-vv0312]]
- [[release-v0192]]
- [[issue-6359-truncate-gold-on-policy-prompts-before-generation-keeping-the-prompt-end]]
- [[release-notes-pytorch-vv2130]]

## Key Findings

---
source_url: https://github.com/huggingface/accelerate/releases/tag/v1.14.0
ingested: 2026-07-11
sha256: 1e6b4b534ad120e5015b5d97e036bc8cfc9db7fa67fd68e9841343ec2e86f566
blog_source: github:huggingface/accelerate
---
# Release v1.14.0
## FSDP2 Improvements
This release brings a large batch of FSDP2 fixes and quality-of-life improvements: correct dtype handling on load, sharding of embeddings/norms, QLoRA crash prevention, and a more robust auto-wrap policy.
- Fsdp2 fully_shard embedding and norm by @SunMarc in #4015
- Fix fsdp2 load full state dict dtype mismatch by @SunMarc in #4021
- Fix region compilation fsdpv2 by @SunMarc in #4022
- [FSDP2] Cast model to uniform dtype before fully_shard to fix mixed-dtype AssertionError by @roycho96 in #3985
- [FSDP2] Auto-exclude non-floating frozen Params4bit from fully_shard to prevent QLoRA crash by @roycho96 in #3987
- fix(FSDP2): auto-wrap policy ignoring _no_split_modules fallback by @JohnGiorgi in #3999
- fix: use key-based matching in fsdp2_load_full_state_dict by @roycho96 in #3982
- fix: add missing model_has_params4bit guard to fsdp2_load_full_state_dict call by @roycho96 in #3981
- Fix to-fsdp2: drop REMOVED / NOT_YET_IMPLEMENTED FSDP1 keys instead of leaking them by @lollinng in #4065
- Prevent double-wrapping models in prepare_model() by @joshuaswanson in #3977
## AMD ROCm support
Accelerate now works end-to-end on AMD ROCm devices. Thanks @Abdennacer-Badaoui!
- Make accelerate work end-to-end on AMD ROCm by @Abdennacer-Badaoui in #4025
## Neuron
Further Neuron improvements to reduce recompilation and cover missing device cases.
- Add padded allgather and broadcast for Neuron devices to reduce recompilation by @czkkkkkk in #4000
- fix: add missing neuron device case by @michaelbenayoun in #4042
## Quantization & Offloading
We improved offloading support for quantized models, including Torchao, int8, and tied-weight handling.
- Torchao offload by @SunMarc in #3973
- Fix int8 offload hook detachment statistics restoration by @jiqing-feng in #4044
- Fix keep_in_fp32_modules not working for tied weights in load_and_quantize_model by @jiqing-feng in #4043
- Fix dtype_byte_size for FP8 fnuz / e8m0fnu dtypes by @lollinng in #4063
## Data Loading
- Feat: Support dynamic batch size in BatchSamplerShard with even_batches by @yuxinyuan in #3969
- Fix iterable dataset sharding condition when n_shards == num_processes by @SunMarc in #3958
- Fix implicit padding in split_between_processes when apply_padding=False and num_samples < num_processes by @3manifold in #4052
## Minor fixes
- [DeepSpeed] allow kernels flash-attn in SP by @kashif in #3959
- Fix: Conditionally import torch.distributed.algorithms.join in accelerator.py by @0xDELUXA in #3962
- Fix is_hf_initialized attribute by @SunMarc in #3976
- feat(utils): add max reduction type by @imstevenpmwork in #4027
- fix(state): make MLU backend part of the _prepare_backend elif chain by @Anai-Guo in #4057
- fix notebook launcher cuda init by @SunMarc in 

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-6360-bump-the-actions-group-with-9-updates]]
- [[release-notes-ollama-vv0312]]
- [[release-v0192]]
- [[issue-6359-truncate-gold-on-policy-prompts-before-generation-keeping-the-prompt-end]]
- [[release-notes-pytorch-vv2130]]
