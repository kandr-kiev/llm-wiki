---
title: "Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - analysis
  - cuda
  - design-pattern
  - image-generation
  - open-source
  - pipeline
  - review
  - self-supervised
---

# Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse

> **Source:** gh-huggingfacediffusers-issue-14184-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/diffusers/issues/14184 ingested: 2026-07-14 sha256: 914ab735abf57e26f49616d27f09f2c193a0e880f9e89740a8ba9e9f534ce148 blog_source: github:huggingface/diff...
> **Sources:**
>   - gh-huggingfacediffusers-issue-14184-2026-07-14.md
> **Links:**
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #14169: Remove JAX/Flax]
- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]
- [Issue #14170: fix wan i2v num_videos batching, vace latent trim, config scale factors, processor config, modular dtype]
- [Issue #3419: FIX Bug in forgetting metric in MetaMathQA]

## Key Findings

---
source_url: https://github.com/huggingface/diffusers/issues/14184
ingested: 2026-07-14
sha256: 914ab735abf57e26f49616d27f09f2c193a0e880f9e89740a8ba9e9f534ce148
blog_source: github:huggingface/diffusers
---
# Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse
**State:** open | **Author:** IvenHsu01 | **Created:** 2026-07-14T03:00:47Z
## What does this PR do?
Fixes a VAE dtype-mismatch `RuntimeError` in `AuraFlowPipeline` that occurs when
the same pipeline instance is called more than once.
`upcast_vae()` upcasts the whole VAE to float32 in place, so on the second call
`needs_upcasting` is `False` and the `latents.to(...)` cast (guarded by that
`if`) is skipped, feeding fp16 latents to the fp32 VAE. This applies the same
pattern already merged for `pixart_sigma` in #8391 — cast the latents to the VAE
dtype inline at the decode call so it always runs.
```diff
if needs_upcasting:
self.upcast_vae()
- latents = latents.to(next(iter(self.vae.post_quant_conv.parameters())).dtype)
- image = self.vae.decode(latents / self.vae.config.scaling_factor, return_dict=False)[0]
+ image = self.vae.decode(latents.to(self.vae.dtype) / self.vae.config.scaling_factor, return_dict=False)[0]
```
Companion PR to #14183, which has the full analysis and verification.
Happy to adjust the scope or approach based on maintainer feedback there.
## Coordination
- Issue: #14183
## Tests run
Applied this exact change, no other patches, ran warmup + 1 run (the 2nd call
triggers the bug) at 512x512, 50 steps, guidance 3.5, seed 42:
- NVIDIA RTX 5090 (CUDA): warmup 18.51s, 2nd call 7.31s — Pass, coherent image
- AMD gfx1151 (ROCm): warmup 64.23s, 2nd call 63.25s — Pass, coherent image
## Before submitting
- [x] Read the [contributor guideline](https://github.com/huggingface/diffusers/blob/main/CONTRIBUTING.md)
- [x] Discussed via a GitHub issue — see #14183
## Who can review?
@yiyixuxu @sayakpaul

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #14169: Remove JAX/Flax]
- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]
- [Issue #14170: fix wan i2v num_videos batching, vace latent trim, config scale factors, processor config, modular dtype]
- [Issue #3419: FIX Bug in forgetting metric in MetaMathQA]
