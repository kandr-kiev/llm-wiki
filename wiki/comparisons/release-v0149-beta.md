---
title: "Release v0.1.49-beta"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - audio-generation
  - backend
  - ci-cd
  - claude
  - design-pattern
  - distributed
  - dpo
  - edge
  - embedding
  - foundation-model
  - gguf
  - gpt
  - llama
  - lora
  - online
  - open-source
  - preprocessing
  - sft
  - stable-diffusion
  - streaming
  - system-design
  - tool
  - training
  - use-case
---

# Release v0.1.49-beta

> **Source:** gh-v0149-beta-2026-07-15.md
> **Type:** comparison
> **Created:** 2026-07-16
> **Updated:** 2026-07-16
> **Confidence:** high
> **Description:** --- source_url: https://github.com/unslothai/unsloth/releases/tag/v0.1.49-beta ingested: 2026-07-15 sha256: a0b4081cc9f7e9a38c8a518905bf67e0bbeec0502ef4c5d622b26bbb7483f350 blog_source: github:unsloth...
> **Sources:**
>   - gh-v0149-beta-2026-07-15.md
> **Links:**
- [[release-v01481-beta]]
- [[release-v0251]]
- [[Release Notes: Ollama vv0.31.2]]
- [[release-500]]
- [[v0.22.1]]

## Key Findings

---
source_url: https://github.com/unslothai/unsloth/releases/tag/v0.1.49-beta
ingested: 2026-07-15
sha256: a0b4081cc9f7e9a38c8a518905bf67e0bbeec0502ef4c5d622b26bbb7483f350
blog_source: github:unslothai/unsloth
---
# Release v0.1.49-beta
Unsloth Studio now supports [Inkling](https://unsloth.ai/docs/models/inkling), a new 975B parameter (41B active) open model with up to a 1M context window. Licensed under Apache 2.0, Inkling accepts text, images, and audio and generates text. Unsloth Studio natively supports it!
# Updating Unsloth
To update Unsloth or install a fresh Unsloth Unsloth, use the commands below:
**macOS, Linux, WSL:**
```
curl -fsSL https://unsloth.ai/install.sh | sh
```
**Windows:**
```
irm https://unsloth.ai/install.ps1 | iex
```
## What's Changed
* Bump install.sh / install.ps1 pin to unsloth>=2026.7.1 by @danielhanchen in https://github.com/unslothai/unsloth/pull/6943
* Sort chat recents by last activity by @NilayYadav in https://github.com/unslothai/unsloth/pull/6844
* Studio: render \[ \] and \( \) LaTeX delimiters in chat by @oobabooga in https://github.com/unslothai/unsloth/pull/6914
* fix: match qwen3-thinking double-newline in train_on_responses_only response pattern by @InfoSage05 in https://github.com/unslothai/unsloth/pull/6926
* Studio: stream reasoning tokens in the tool-loop generator (fixes DeepSeek thinking not streaming with a pill on) by @oobabooga in https://github.com/unslothai/unsloth/pull/6947
* Create ossf.yml by @danielhanchen in https://github.com/unslothai/unsloth/pull/6952
* Speed up Studio startup path by @wasimysaid in https://github.com/unslothai/unsloth/pull/6899
* Polish assistant message actions menu by @shimmyshimmer in https://github.com/unslothai/unsloth/pull/6962
* Move New badge to System settings tab by @shimmyshimmer in https://github.com/unslothai/unsloth/pull/6963
* Fix opencode Unsloth provider selection by @Imagineer99 in https://github.com/unslothai/unsloth/pull/6906
* Fix Hermes install hint on Windows by @Imagineer99 in https://github.com/unslothai/unsloth/pull/6903
* Studio: heal DiffusionGemma tool calls into structured tool_calls by @oobabooga in https://github.com/unslothai/unsloth/pull/6851
* Fix case-variant model matching and GGUF cache reuse in unsloth start by @Imagineer99 in https://github.com/unslothai/unsloth/pull/6900
* Studio: show Hugging Face address on hover for Hub and online model rows (#6382) by @danielhanchen in https://github.com/unslothai/unsloth/pull/6928
* Studio: fix currency and indentation edge cases in LaTeX rendering by @danielhanchen in https://github.com/unslothai/unsloth/pull/6957
* Add MLX backend support for CLI unsloth train by @Lyxot in https://github.com/unslothai/unsloth/pull/6709
* feat(cli): support MLX distributed inference by @Lyxot in https://github.com/unslothai/unsloth/pull/6845
* Route MLX trainer callbacks through UnslothTrainer by @Lyxot in https://github.com/unslothai/unsloth/pull/6929
* (GRPO) Fix PEFT replacement for TRL >= 1.7.0, add 

## Summary

missing compute_aux_loss for TRL >= 1.7.0 by @marcandrelarochelle in https://github.com/unslothai/unsloth/pull/6904
* version-compat CI: fake CPU training runs for SFT/GRPO/DPO by @danielhanchen in https://github.com/unslothai/unsloth/pull/6965
* Fix OpenClaw start default to local TUI by @Imagineer99 in https://github.com/unslothai/unsloth/pull/6937
* feat: detect installed coding agent CLIs in Studio settings by @ErenAta16 in https://github.com/unslothai/unsloth/pull/6909
* Studio: don't pin transformers before the training worker activates the 5.x sidecar by @danielhanchen in https://github.com/unslothai/unsloth/pull/6968
* Studio: source CPU llama.cpp prebuilts from unslothai/llama.cpp by @oobabooga in https://github.com/unslothai/unsloth/pull/6311
* fix(studio/hub): apply repo_id length limit per segment, not whole string (#6946) by @Anai-Guo in https://github.com/unslothai/unsloth/pull/6953
* MoE LoRA: auto-target per-expert Linear experts (gpt-oss 4bit) instead of leaving them frozen by @danielhanchen in https://github.com/unslothai/unsloth/pull/6936
* Studio: fix flash-attn and torchao install on Blackwell (sm_100+) GPUs (Closes #6961) by @ThomasEricB in https://github.com/unslothai/unsloth/pull/6970
* Fix Backend CI: add has_blackwell_gpu to the mlx worker test stub by @danielhanchen in https://github.com/unslothai/unsloth/pull/6980
* Studio: allow CPU-only DiffusionGemma by granting the diffusion runner the CPU device by @danielhanchen in https://github.com/unslothai/unsloth/pull/6979
* Bump install.sh / install.ps1 pin to unsloth>=2026.7.2 by @danielhanchen in https://github.com/unslothai/unsloth/pull/6981
* Studio: render thinking blocks for safetensors inference with prefilled templates by @shimmyshimmer in https://github.com/unslothai/unsloth/pull/6816
* Remove API menu new badge by @shimmyshimmer in https://github.com/unslothai/unsloth/pull/6983
* Fix BAD_MAPPINGS not redirecting the -unsloth-bnb-4bit dynamic quants by @vineethsaivs in https://github.com/unslothai/unsloth/pull/6949
* Fix duplicate gemma-2b-bnb-4bit key routing the base model to the instruct model by @vineethsaivs in https://github.com/unslothai/unsloth/pull/6891
* Fix to_sharegpt optional block rendering "None" for missing extra columns by @vineethsaivs in https://github.com/unslothai/unsloth/pull/6827
* Guard FP8 Triton launches with tensor device context by @ramisworld in https://github.com/unslothai/unsloth/pull/6888
* Fix per-block ID collisions and add block cleanup for unstructured uploads by @NilayYadav in https://github.com/unslothai/unsloth/pull/6944
* Stabilize floating monitor drag by @shimmyshimmer in https://github.com/unslothai/unsloth/pull/6984
* Retry the Studio UI shutdown re-login on transient goto timeout by @danielhanchen in https://github.com/unslothai/unsloth/pull/7027
* Fix FastSentenceTransformer Qwen embedding preprocessing by @Etherll in https://github.com/unslothai/unsloth/pull/6939
* unsloth start: warn before running an agent's remote i

## Related Articles

- [[release-v01481-beta]]
- [[release-v0251]]
- [[Release Notes: Ollama vv0.31.2]]
- [[release-500]]
- [[v0.22.1]]
