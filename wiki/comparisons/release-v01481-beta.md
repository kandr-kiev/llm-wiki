---
title: "Release v0.1.481-beta"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - ci-cd
  - computer-vision
  - cuda
  - data
  - embedding
  - fine-tuning
  - foundation-model
  - gguf
  - hardware
  - image-generation
  - llama
  - lora
  - multimodal
  - nlp
  - offline
  - open-source
  - prompt-tuning
  - quantization
  - rag
  - real-time
  - reinforcement-learning
  - search
  - streaming
  - system-design
  - tool
  - training
  - use-case
---
# Release v0.1.481-beta

> **Source:** gh-v01481-beta-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-12
> **Updated:** 2026-07-12
> **Confidence:** high
> **Description:** --- source_url: https://github.com/unslothai/unsloth/releases/tag/v0.1.481-beta ingested: 2026-07-11 sha256: 902e8fc8b7c11825d234d43a012ab5eb491dd65250ba0bf55efdbe883ee3d0b9 blog_source: github:unslot...
> **Sources:**
>   - gh-v01481-beta-2026-07-11.md
> **Links:**
- [[release-notes-ollama-vv0312]]
- [[release-v180]]
- [[v0230]]
- [[release-notes-vllm-vv0240]]
- [[v0220]]

## Key Findings

---
source_url: https://github.com/unslothai/unsloth/releases/tag/v0.1.481-beta
ingested: 2026-07-11
sha256: 902e8fc8b7c11825d234d43a012ab5eb491dd65250ba0bf55efdbe883ee3d0b9
blog_source: github:unslothai/unsloth
---
# Release v0.1.481-beta
Unsloth Studio can now export to NVFP4, FP8, imatrix GGUFs after training, can act as a llama-swap API system, includes Japanese and Brazilian language support, includes MLX, safetensors tool calling + healing support and much more! Unsloth core makes GRPO 1.3x faster, have HTTP fallback for stalled downloads, better offline mode, makes MoE training 3 to 5x faster, and fixes many bugs! This release series uses `unsloth>=2026.7.2` and tag `v0.1.481-beta`
[DeepSeek-V4-Flash](https://unsloth.ai/docs/models/deepseek-v4) is now supported with Thinking toggles and with all our fixes including improved chat template!
![Deepseek-v4 in unsloth](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FChQx2DGoDLyhf7mp8G2d%252Fdeepseek%2520v4%2520flashhh.png%3Falt%3Dmedia%26token%3Da84f2fbc-8ab0-44cf-a3a8-0bdaaf80a2a7&width=768&dpr=3&quality=100&sign=79c2dcbb&sv=2)
## Update 8th July 2026 `v0.1.481-beta`
1. Fixes Qwen3.5 / Qwen3.6, Gemma-4 finetuning not working well in Studio
2. Adds CPU DiffusionGemma + tool calling support
3. Fixes DeepSeek-V4 GGUFs and other GGUFs not streaming thinking traces
## Smarter OpenAI-Compatible API Serving
Run one local API endpoint across with safer automatic model swapping and better agent-tool recovery.
* API requests can opt into model auto switching, so a request for a different downloaded local GGUF can load and serve that model automatically.
* The model swap path is safe by default: unknown model names keep using the current model and do not trigger surprise downloads.
* /v1/models now returns clean model IDs and the local GGUF catalog, so API clients do not see local .gguf file paths.
* Idle auto-unload can free VRAM after inactivity while still reloading the last model on the next API request.
* API clients can control tool-call healing per request and opt into the extra nudge retry when a model tries to call a tool but returns malformed markup.
## Export Improvements
Exports are more flexible and avoid more unnecessary downloads.
* Unsloth now lets you select multiple export formats at once.
* Unsloth now supports portable FP8/INT8 exports, GGUF LoRA, and source-matched exports.
* `save_pretrained_merged` now supports compressed FP8/FP4 exports.
* The Unsloth export UI now includes imatrix GGUF and compressed export options.
* Exporting multiple checkpoints now avoids more repeated base-model downloads.
* FP8, INT8, and GGUF-LoRA exports now respect `trust_remote_code`.
* GGUF export now handles models with missing quantization settings more reliably.
## RAG and File Chat 
Chat with files should be more useful on real documents.
* RAG attachments c

## Summary

an now use whole-document context. 
* File chat now reads more PDFs and Word documents correctly, including right-to-left text, Indic text, and DOCX tables.
* Local RAG checks are less likely to fail because of proxy settings.
* The embedding model is now customizable, with Hugging Face search and a reorganized settings tab.
## Unsloth Polish and Reliability
Unsloth is smoother and more reliable during everyday use.
* Training and chat progress are less likely to freeze silently during long runs. 
* Compare mode starts more reliably.
* Switching or cancelling models during loading is less likely to get stuck.
* Hub browsing now recovers better from invalid Hugging Face tokens and shows clearer local file paths.
* Hub Discover now shows all models by default, with a cleaner model picker and a fits-on-device filter.
* Project export menus are clearer, with combined project exports and individual chat exports grouped separately.
* Unsloth training runs now show project names.
* Guided tours, reasoning timers, thinking stops, settings, file dialogs, and update screens now feel cleaner and more consistent.
* Japanese and Portuguese (Brazil) are now available in the Unsloth UI.
* Installer and package checks were tightened to catch more unsafe or unexpected dependency changes.
## Installer, Hardware and Platform Fixes
Unsloth installs and runs more reliably across different machines, GPUs, and network setups.
* Installer pins were updated to `unsloth>=2026.6.9`.
* macOS installs no longer require CMake or Homebrew when a prebuilt `llama.cpp` is available.
* Apple Silicon installs now handle paths with spaces more reliably and size GGUF context for unified memory.
* macOS installs work better behind corporate TLS-inspection proxies.
* Linux and macOS path handling is more reliable when folders contain spaces.
* Windows ROCm RAG embedding avoids a `torchao` import crash.
* Windows Unsloth startup handles UTF-8 text more reliably.
* ROCm-on-WSL now supports discrete Radeon RDNA 3/4 GPUs, not just Strix Halo.
* Blackwell `sm_100` and `sm_103` data-center GPUs now use the correct `llama.cpp` prebuilt selection.
* GGUF fit checks now reserve memory for CUDA context and vision/model overhead more accurately.
* Tensor parallelism fixed for vision and `mmproj` GGUF models.
* Existing local `llama.cpp` builds can now be reused with `--with-llama-cpp-dir`.
## Training, Models and Kernels
Training and model loading are more reliable across more model types, GPUs, and fine-tuning setups.
* GRPO training now supports sequence packing by default for old/ref log-probability calculations.
* GRPO now avoids repeating the same shared prompt across grouped completions.
* GRPO logit scaling now works correctly with DDP-wrapped models.
* Full fine-tuning now uses the correct precision on V100 and other GPUs without bf16 support.
* RL trainers no longer reject valid full fine-tuning precision settings.
* Unsloth gradient checkpointing is no longer silently disabled by `Train

## Related Articles

- [[release-notes-ollama-vv0312]]
- [[release-v180]]
- [[v0230]]
- [[release-notes-vllm-vv0240]]
- [[v0220]]
