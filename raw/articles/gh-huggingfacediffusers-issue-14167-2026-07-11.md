---
source_url: https://github.com/huggingface/diffusers/issues/14167
ingested: 2026-07-11
sha256: 6a3612bd8ff3face2c073bc28b604b628c39c1f925cbb4638c54b6e3d0231097
blog_source: github:huggingface/diffusers
---
# Issue #14167: FlashPack support for transformers pipeline components

**State:** open | **Author:** rumutaydin | **Created:** 2026-07-10T23:04:00Z

# What does this PR do?

Follow-up to #14166 (stacked on it). `use_flashpack=True` currently applies
only to diffusers models; transformers components (text encoders) silently keep
safetensors, so a "FlashPack pipeline" never actually is one end to end the gap
noted when FlashPack+DDUF support was discussed in
huggingface/huggingface_hub#3716.

- **Save:** transformers' `save_pretrained` has no FlashPack support, so
  `DiffusionPipeline.save_pretrained(use_flashpack=True)` now saves a transformers
  component's config as usual and packs its weights to `model.flashpack` the same
  call `ModelMixin.save_pretrained(use_flashpack=True)` makes for diffusers models.
- **Load:** when `use_flashpack=True` and a transformers component's folder ships
  `model.flashpack`, initialize the model from its config on empty weights and assign
  the packed weights onto it, mirroring the existing diffusers-model FlashPack path
  (same device_map handling and warnings). Folders without a flashpack file load
  exactly as before, so existing mixed-format repos are unaffected.

With this, saving `tiny-flux-pipe` with `use_flashpack=True` produces zero safetensors
(CLIP, T5, transformer, VAE all packed), the filtered Hub snapshot round-trips
bitwise-equal, and the reloaded pipeline runs inference on CPU.

One difference from the diffusers-model FlashPack path: loaded transformers
components are returned in eval mode, matching what `transformers.from_pretrained`
does. (The diffusers-model FlashPack path currently returns models in train mode,
happy to fix that separately if wanted.)


# Tests
a new test saves tiny-flux-pipe with use_flashpack=True and asserts the transformers components (CLIP and T5 text encoders) produce model.flashpack and no safetensors, then applies the real Hub download filter to the saved folder and reloads it checking the restored weights are bitwise-equal to the originals and the components are in eval mode. The existing round-trip test now builds the mixed layout explicitly (diffusers models as FlashPack, text encoders as safetensors, i.e. what save_pretrained(use_flashpack=True) produced before this PR), so repos saved with the old behavior are covered and keep loading.

Related: #12564.


## Before submitting
- [x ] Did you use an AI agent (Claude Code, Codex, Cursor, etc.) to help with this PR? If so:
  - [x ] Did you read the [Coding with AI agents](https://huggingface.co/docs/diffusers/main/en/conceptual/contribution#coding-with-ai-agents) guide?
  - [x ] Did you self-review the diff against [`.ai/review-rules.md`](https://github.com/huggingface/diffusers/blob/main/.ai/review-rules.md)?
- [x ] Did you read the [contributor guideline](https://huggingface.co/docs/diffusers/main/en/conceptual/contribution)?
- [x ] Did you read our [philosophy doc](https://huggingface.co/docs/diffusers/main/en/conceptual/philosophy)? (important for complex PRs)
- [x ] Was this discussed/approved via a GitHub issue #12564
- [x ] Did you make sure to update the documentation with your changes? Here are the
      [documentation guidelines](https://github.com/huggingface/diffusers/tree/main/docs), and
      [here are tips on formatting docstrings](https://github.com/huggingface/diffusers/tree/main/docs#writing-source-documentation).
- [x ] Did you write any new necessary tests?
- [ ] Are you the author (or part of the team) of the model/pipeline (only applicable for model/pipeline related PRs)?


## Who can review?
@DN6 @yiyixuxu