---
title: "Release v0.1.50-beta"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - ci-cd
  - cuda
  - data
  - dataset
  - fine-tuning
  - foundation-model
  - gguf
  - gpu
  - guide
  - hardware
  - llama
  - llm
  - lora
  - multimodal
  - nlp
  - open-source
  - parallel
  - rag
  - real-time
  - reinforcement-learning
  - search
  - standards
  - system-design
  - tool
  - training
  - use-case
  - web
---

# Release v0.1.50-beta

> **Source:** gh-v0150-beta-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://github.com/unslothai/unsloth/releases/tag/v0.1.50-beta ingested: 2026-07-20 sha256: f79916dc5e2380e22cb1e437abc0cc969c46adcd5ade2dd20cab43aeabd1c170 blog_source: github:unsloth...
> **Sources:**
>   - gh-v0150-beta-2026-07-20.md
> **Links:**
- [[Release v0.1.481-beta]]
- [[Release v0.1.49-beta]]
- [[Release 5.0.0]]
- [[Release v0.25.1]]
- [[Release Notes: Ollama vv0.31.2]]

## Key Findings

---
source_url: https://github.com/unslothai/unsloth/releases/tag/v0.1.50-beta
ingested: 2026-07-20
sha256: f79916dc5e2380e22cb1e437abc0cc969c46adcd5ade2dd20cab43aeabd1c170
blog_source: github:unslothai/unsloth
---
# Release v0.1.50-beta
Hey everyone! This release brings local LLM training and inference to AMD GPUs across Windows, WSL and Linux. [Read our AMD Blog + Guide](https://unsloth.ai/docs/basics/amd)
Starting today, our AMD collaboration, custom Triton kernels, and math algorithms enables you to train and run 500+ models across AMD's Radeon, Instinct, Ryzen and data center GPUs, up to 2× faster with 70% less VRAM and no accuracy loss. Optimized ROCm builds also support GGUF & Safetensors inference.
![AMD in Unsloth](https://github.com/user-attachments/assets/bb8bc525-9fb8-405d-98f5-6c9c07128085)
## Train LLMs Locally on AMD
- Train, run RL, chat with and deploy models locally on AMD GPUs.
- More reliable AMD GPU detection and installation across Windows, WSL and Linux.
- Improved ROCm compatibility for AMD MI300X and MI325X GPUs.
- Remote access Unsloth via `unsloth studio --secure` through free HTTPS via Cloudflare
## Run Larger Models on Your Hardware
- Use automatic GPU placement or choose exactly which GPUs and model layers to use.
- Move MoE expert layers into system memory to help larger models fit.
- Split models across multiple GPUs or use Tensor Parallelism.
- Save hardware settings separately for each model and quant.
## Faster Chat Restarts and More Reliable Downloads
- Resume long chats without rebuilding the full conversation after an idle model frees its VRAM.
- Stalled Hugging Face XET downloads automatically retry over standard HTTP.
- Existing GGUF files are reused instead of being downloaded again whenever a model loads.
## Better Search, Tools and Agents
- Web search can now read PDF papers, manuals and other PDF results.
- Parallel tool calls, reasoning output and tool retries work more reliably.
- A new opt-in MCP endpoint lets compatible AI clients inspect models and training history, start or stop training, load checkpoints, validate recipes and export GGUFs.
- Enable it with `UNSLOTH_STUDIO_ENABLE_MCP=1` and set the required bearer token with `UNSLOTH_STUDIO_MCP_TOKEN`.
## Training and Export Fixes
- Text-only training with multimodal models no longer truncates long examples before packing.
- Fine-tuned Qwen3.5 and Qwen3.6 MTP models now export correctly to GGUF.
- Fixed a Windows permission error that could stop GGUF exports during the final write step.
## In Case You Missed It
Our previous Studio release added Dynamic NVFP4 models, deeper personalization, seven new display languages, safer agents and Vulkan GPU acceleration.
### Dynamic NVFP4
Unsloth Dynamic NVFP4 keeps accuracy-sensitive layers in FP8 or BF16 while running the rest in W4A4. On NVIDIA Blackwell GPUs, this enables up to 2.5x faster inference, while calibrated FP8 KV caches provide up to 2x longer context.
Read the [Dynamic NVFP4 guide](https://uns

## Summary

loth.ai/docs/basics/nvfp4) and explore our expanded [NVFP4 collection](https://huggingface.co/collections/unsloth/nvfp4), including Qwen3.6, Qwen3.5, Inkling, GLM-4.7 Flash and Gemma 4.
### Personalize Your Studio
Choose between Standard, Classic and Minimal color palettes, each with light and dark modes. You can also customize colors, import fonts and adjust font size, contrast, reduced motion and more.
Studio also includes a Voice settings tab for dictation, custom dictionary settings and read-aloud.
### New Languages
Unsloth Studio is now available in French, German, Spanish, Hindi, Arabic, Russian and Korean, alongside Chinese (Simplified), Japanese and Portuguese (Brazil). Browser-language auto-detection is now the default.
### Safer Agents
A four-level tool-call permission selector-**Ask**, **Approve for me**, **Off** and **Full access**-provides finer control over agents. Agent workspace isolation and safer installer checks also reduce the risk of unintended changes.
## Updating Unsloth
To update Unsloth or install a fresh Unsloth, use the commands below:
**macOS, Linux, WSL:**
```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```
**Windows:**
```powershell
irm https://unsloth.ai/install.ps1 | iex
```
## What's Changed in Unsloth
* Bump install.sh / install.ps1 pin to unsloth>=2026.7.3 by @danielhanchen in https://github.com/unslothai/unsloth/pull/7155
* fix(dataprep): smart_chunk_text single-chunk path leaks internal tensor type when eos_token_id is None by @chuenchen309 in https://github.com/unslothai/unsloth/pull/7151
* Fix Settings layout overflow by @shimmyshimmer in https://github.com/unslothai/unsloth/pull/7167
* Keep nested dropdown menus on screen by @shimmyshimmer in https://github.com/unslothai/unsloth/pull/7168
* Fix DeepSeek reasoning test shim by @shimmyshimmer in https://github.com/unslothai/unsloth/pull/7169
* Harden desktop release token permissions by @wasimysaid in https://github.com/unslothai/unsloth/pull/7172
* Studio: clickable sidebar settings cog, long name truncation, Canvas menu opt-in by @shimmyshimmer in https://github.com/unslothai/unsloth/pull/7171
* CI: opt tool-calling smoke tests out of the chat tool approval gate by @danielhanchen in https://github.com/unslothai/unsloth/pull/7162
* Fix Inkling reasoning-effort coercion for duck-typed engine stand-ins by @danielhanchen in https://github.com/unslothai/unsloth/pull/7158
* fix config cards clipping content at narrow window widths by @NilayYadav in https://github.com/unslothai/unsloth/pull/7146
* Studio: use one shared Hugging Face token across Settings and training by @NilayYadav in https://github.com/unslothai/unsloth/pull/7152
* Studio: don't drop parallel tool calls after an internal no-op by @oobabooga in https://github.com/unslothai/unsloth/pull/7157
* Studio: extract text from PDF web results by @oobabooga in https://github.com/unslothai/unsloth/pull/7154
* don't kill live llama-servers when a new Studio instance starts by @NilayYadav in https://gith

## Related Articles

- [[Release v0.1.481-beta]]
- [[Release v0.1.49-beta]]
- [[Release 5.0.0]]
- [[Release v0.25.1]]
- [[Release Notes: Ollama vv0.31.2]]
