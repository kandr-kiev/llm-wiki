---
title: "Issue #14170: fix wan i2v num_videos batching, vace latent trim, config scale factors, processor config, modular dtype"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - batch
  - open-source
  - pipeline
  - review
  - transformers
  - use-case
---
# Issue #14170: fix wan i2v num_videos batching, vace latent trim, config scale factors, processor config, modular dtype

> **Source:** gh-huggingfacediffusers-issue-14170-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/diffusers/issues/14170 ingested: 2026-07-11 sha256: 61a27992f34ffa83dd10be79f791fbae6f6a87b471082e7a1ff69f8c093a0355 blog_source: github:huggingface/diff...
> **Sources:**
>   - gh-huggingfacediffusers-issue-14170-2026-07-11.md
> **Links:**
- [[issue-14169-remove-jaxflax]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14168-fix-batching-and-precomputed-embeddings-in-kandinsky-5-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[away]]

## Key Findings

---
source_url: https://github.com/huggingface/diffusers/issues/14170
ingested: 2026-07-11
sha256: 61a27992f34ffa83dd10be79f791fbae6f6a87b471082e7a1ff69f8c093a0355
blog_source: github:huggingface/diffusers
---
# Issue #14170: fix wan i2v num_videos batching, vace latent trim, config scale factors, processor config, modular dtype
**State:** open | **Author:** akshan-main | **Created:** 2026-07-11T11:30:15Z
# What does this PR do?
Part of #13578 (wan review). Same families of issues as the qwenimage review:
- `WanImageToVideoPipeline`: `image_embeds` was repeated by `batch_size` but not `num_videos_per_prompt`, while the latents are expanded to `batch_size * num_videos_per_prompt`, so `num_videos_per_prompt > 1` failed the transformer concat. Now repeated to the effective batch.
- `WanVACEPipeline(output_type="latent")`: the decode path trims the prepended reference latents but the latent path returned them untrimmed, so latent output carried extra frames. The trim now runs before the branch.
- `WanVACEPipeline`, `WanVideoToVideoPipeline`, and the modular Wan pipeline derived scale factors from `len(vae.temperal_downsample)` and a hardcoded spatial `8` instead of `vae.config.scale_factor_spatial` / `scale_factor_temporal`. Now read from config, matching the base `WanPipeline`.
- `WanAnimateImageProcessor.__init__` accepted `vae_scale_factor` / `vae_latent_channels` / `resample` etc. but called `super().__init__()` with no args, so the base re-registered defaults over the subclass config. Now forwards them.
- Modular `WanTextInputStep` derived `block_state.dtype` from `prompt_embeds.dtype`; the denoise blocks cast scheduler timesteps to it, losing precision on bf16/fp16 paths. Now uses `transformer.dtype`, matching the comment.
## Before submitting
- [ ] This PR fixes a typo or improves the docs (you can dismiss the other checks if that's the case).
- [x] Did you read the [contributor guideline](https://github.com/huggingface/diffusers/blob/main/CONTRIBUTING.md)?
- [x] Did you read our [philosophy doc](https://github.com/huggingface/diffusers/blob/main/PHILOSOPHY.md) (important for complex PRs)?
- [x] Was this discussed/approved via a GitHub issue or the [forum](https://discuss.huggingface.co/c/discussion-related-to-httpsgithubcomhuggingfacediffusers/63)? Discussed on Slack with @yiyixuxu
- [ ] Did you make sure to update the documentation with your changes?
- [ ] Did you write any new necessary tests?
## Who can review?
@yiyixuxu

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-14169-remove-jaxflax]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14168-fix-batching-and-precomputed-embeddings-in-kandinsky-5-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[away]]
