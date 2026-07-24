---
title: "Release v0.39.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - alignment
  - api
  - architecture
  - backend
  - few-shot
  - foundation-model
  - framework
  - image-generation
  - instruction-tuning
  - integration
  - library
  - llm
  - lora
  - multimodal
  - nlp
  - parallel
  - pipeline
  - prompt-tuning
  - quantization
  - stable-diffusion
  - transfer-learning
  - transformers
  - video-generation
---
# Release v0.39.0

> **Source:** gh-v0390-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/diffusers/releases/tag/v0.39.0 ingested: 2026-07-11 sha256: 900cea2ac13565acefcd6520dcc2a6dd7e93ffc4a469adbe5d7737d4237f32e7 blog_source: github:huggingf...
> **Sources:**
>   - gh-v0390-2026-07-11.md
> **Links:**
- [[release-notes-ollama-vv0312]]
- [[issue-2848-implement-multi-domain-intake-architecture-and-related-specs]]
- [Issue #47256: [serge] integration failure triage -](https://github.com/pytorch/pytorch/issues/47256)
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14168-fix-batching-and-precomputed-embeddings-in-kandinsky-5-pipelines]]

## Key Findings

---
source_url: https://github.com/huggingface/diffusers/releases/tag/v0.39.0
ingested: 2026-07-11
sha256: 900cea2ac13565acefcd6520dcc2a6dd7e93ffc4a469adbe5d7737d4237f32e7
blog_source: github:huggingface/diffusers
---
# Release v0.39.0
## New Pipelines
### Cosmos 3
[**Cosmos 3**](https://huggingface.co/docs/diffusers/main/api/pipelines/cosmos3) is NVIDIA's unified world foundation model (WFM) for Physical AI — a single omni-model built on a Mixture-of-Transformers (MoT) architecture that combines world generation, physical reasoning, and action generation, replacing the separate Predict, Reason, and Transfer models from earlier Cosmos releases. A single `Cosmos3OmniTransformer` runs a Qwen-style language model in parallel with a diffusion generation pathway, joined by a 3D multimodal RoPE. This release also lands video-to-video and action-conditioned generation, and a sound encoder.
- PR: [https://github.com/huggingface/diffusers/pull/13818](https://github.com/huggingface/diffusers/pull/13818)
- Docs: [https://huggingface.co/docs/diffusers/main/api/pipelines/cosmos3](https://huggingface.co/docs/diffusers/main/api/pipelines/cosmos3)
Thanks to @atharvajoshi10, @yzhautouskay, and @MaciejBalaNV for the contributions.
### Ideogram 4
[**Ideogram 4**](https://huggingface.co/docs/diffusers/main/api/pipelines/ideogram4) is a flow-matching text-to-image model that uses a multimodal text encoder and an asymmetric classifier-free guidance scheme: a dedicated `unconditional_transformer` produces the negative branch with zeroed text features, while the main `transformer` consumes the full packed text + image sequence. The pipeline ships with structured prompt upsampling and LoRA loading support.
- PR: [https://github.com/huggingface/diffusers/pull/13859](https://github.com/huggingface/diffusers/pull/13859)
- Docs: [https://huggingface.co/docs/diffusers/main/api/pipelines/ideogram4](https://huggingface.co/docs/diffusers/main/api/pipelines/ideogram4)
Thanks to @JinLiIdeogram for the contribution.
### Krea 2
[**Krea 2 (K2)**](https://huggingface.co/docs/diffusers/main/api/pipelines/krea2) is a flow-matching text-to-image model built around a single-stream MMDiT with grouped-query attention. A Qwen3-VL text encoder provides the conditioning — hidden states from twelve decoder layers are tapped per token and fused inside the transformer by a small text-fusion stage — and images are decoded with the Qwen-Image VAE. Both the base (midtrain) and TDM (distilled, few-step) checkpoints are supported, alongside a LoRA DreamBooth trainer.
- PR: [https://github.com/huggingface/diffusers/pull/14045](https://github.com/huggingface/diffusers/pull/14045)
- Docs: [https://huggingface.co/docs/diffusers/main/api/pipelines/krea2](https://huggingface.co/docs/diffusers/main/api/pipelines/krea2)
Thanks to @EleaZhong and @Abhinay1997 for the contribution.
### DreamLite
[**DreamLite**](https://huggingface.co/docs/diffusers/main/api/pipelines/dreamlite) is a text-to-image and image-editi

## Summary

ng model from ByteDance. It pairs a custom 2D U-Net (`DreamLiteUNetModel`) with the `Qwen3-VL` multimodal encoder as its prompt / image-instruction encoder, and uses an `AutoencoderTiny` (TAESD-style) VAE for fast latent encode/decode. A distilled `DreamLiteMobilePipeline` targets on-device, low-latency generation.
- PR: [https://github.com/huggingface/diffusers/pull/13815](https://github.com/huggingface/diffusers/pull/13815)
- Docs: [https://huggingface.co/docs/diffusers/main/api/pipelines/dreamlite](https://huggingface.co/docs/diffusers/main/api/pipelines/dreamlite)
Thanks to @Carlofkl for the contribution.
### PRX Pixel
[**PRXPixel**](https://huggingface.co/docs/diffusers/main/api/pipelines/prx_pixel) is a pixel-space text-to-image generation model by Photoroom. A ~7B `PRXTransformer2DModel` denoises raw RGB images directly — no VAE is needed. The model is conditioned on a Qwen3-VL text encoder and uses flow matching where the transformer predicts the clean image at each step (x-prediction).
- PR: [https://github.com/huggingface/diffusers/pull/13928](https://github.com/huggingface/diffusers/pull/13928)
- Docs: [https://huggingface.co/docs/diffusers/main/api/pipelines/prx_pixel](https://huggingface.co/docs/diffusers/main/api/pipelines/prx_pixel)
Thanks to @DavidBert for the contribution.
### Motif-Video
[**Motif-Video**](https://huggingface.co/docs/diffusers/main/api/pipelines/motif_video) is a 2B parameter diffusion transformer for text-to-video and image-to-video generation. It features a three-stage architecture (12 dual-stream + 16 single-stream + 8 DDT decoder layers), Shared Cross-Attention for stable text-video alignment over long sequences, a T5Gemma2 text encoder, and rectified flow matching for velocity prediction.
- PR: [https://github.com/huggingface/diffusers/pull/13551](https://github.com/huggingface/diffusers/pull/13551)
- Docs: [https://huggingface.co/docs/diffusers/main/api/pipelines/motif_video](https://huggingface.co/docs/diffusers/main/api/pipelines/motif_video)
Thanks to @waitingcheung for the contribution.
### AnyFlow
[**AnyFlow**](https://huggingface.co/docs/diffusers/main/api/pipelines/anyflow) from NVIDIA, NUS, and MIT is the first any-step video diffusion framework built on flow maps, enabling a single model (bidirectional or causal) to adapt to arbitrary inference budgets. It ships both bidirectional and FAR causal pipelines built on Wan2.1 backbones, covering text-to-video, image-to-video, and video-to-video.
- PR: [https://github.com/huggingface/diffusers/pull/13745](https://github.com/huggingface/diffusers/pull/13745)
- Docs: [https://huggingface.co/docs/diffusers/main/api/pipelines/anyflow](https://huggingface.co/docs/diffusers/main/api/pipelines/anyflow)
Thanks to @Enderfga for the contribution.
### JoyAI-Image-Edit
[**JoyAI-Image**](https://huggingface.co/docs/diffusers/main/api/pipelines/joyimage_edit) is a unified multimodal foundation model for image understanding, text-to-image generation, and instruction-gu

## Related Articles

- [[release-notes-ollama-vv0312]]
- [[issue-2848-implement-multi-do[Issue #47256: [serge] integration failure triage -](https://github.com/pytorch/pytorch/issues/47256) #47256: [serge] integration failure triage -]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14168-fix-batching-and-precomputed-embeddings-in-kandinsky-5-pipelines]]
