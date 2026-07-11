---
source_url: https://github.com/huggingface/diffusers/issues/14166
ingested: 2026-07-11
sha256: b34f166785bb70aa689171052bfd36141e9ca254dbb3a674dce3846717e813d0
blog_source: github:huggingface/diffusers
---
# Issue #14166: Fix Hub download filtering for FlashPack pipelines

**State:** open | **Author:** rumutaydin | **Created:** 2026-07-10T22:49:14Z

# What does this PR do?
Pipelines saved with `save_pretrained(use_flashpack=True)` currently cannot be loaded
back through the Hub. Such a pipeline stores diffusers models as `model.flashpack` and
transformers components (text encoders) as safetensors but the download path breaks
on this layout three ways:

1. `_get_ignore_patterns` takes the `elif use_flashpack:` branch and ignores **all**
   `*.safetensors`. Since `use_flashpack` is only forwarded to diffusers models, text
   encoders can only load safetensors which are now missing from the snapshot:

   ```python
   from diffusers import AutoPipelineForText2Image

   pipe = AutoPipelineForText2Image.from_pretrained("hf-internal-testing/tiny-flux-pipe")
   pipe.save_pretrained("flashpack-repo", use_flashpack=True)   # + push to Hub
   AutoPipelineForText2Image.from_pretrained("<user>/flashpack-repo", use_flashpack=True)
   # OSError: Error no file named model.safetensors, or pytorch_model.bin,
   #          found in directory .../text_encoder
   ```

   With explicit `use_safetensors=True` it raises `EnvironmentError` instead, because
   the flashpack-only folders make `is_safetensors_compatible` fail.

2. FlashPack files are missing from `variant_compatible_siblings`' weight names, so
   they never enter the download allow-patterns combined with (1), a FlashPack
   pipeline snapshot contains **no weights at all**.

3. `use_flashpack=False`: the `download` docstring says FlashPack weights "will never
   be downloaded", but `*.flashpack` appears in no ignore pattern, so default users of
   dual-format repos download FlashPack blobs they never read.

# Fixes  (issue)

judge safetensors compatibility over non-flashpack folders only, keep just the
flashpack file inside flashpack-covered folders (per-folder ignore patterns), register
`FLASHPACK_WEIGHTS_NAME` as a weight name, ignore `*.flashpack` whenever
`use_flashpack=False`, and forward `use_flashpack` from `from_pretrained` to `download`
(it was popped but never passed on, so the flag had no effect on Hub downloads).

Repos with no FlashPack files behave exactly as before, with or without the flag.

# Tests 
an end-to-end regression test that saves a FlashPack pipeline, applies the real
allow/ignore download filter, and round-trips the filtered snapshot (fails on `main`),
plus direct `_get_ignore_patterns` cases for the mixed/dual/flashpack-only/no-flashpack
layouts and a test that `from_pretrained` forwards the flag.


# Related: 
#12564, #12700.

## Before submitting
- [x ] Did you use an AI agent (Claude Code, Codex, Cursor, etc.) to help with this PR? If so:
  - [x ] Did you read the [Coding with AI agents](https://huggingface.co/docs/diffusers/main/en/conceptual/contribution#coding-with-ai-agents) guide?
  - [x ] Did you self-review the diff against [`.ai/review-rules.md`](https://github.com/huggingface/diffusers/blob/main/.ai/review-rules.md)?
- [ x] Did you read the [contributor guideline](https://huggingface.co/docs/diffusers/main/en/conceptual/contribution)?
- [x ] Did you read our [philosophy doc](https://huggingface.co/docs/diffusers/main/en/conceptual/philosophy)? (important for complex PRs)
- [ ] Was this discussed/approved via a GitHub issue or the [forum](https://discuss.huggingface.co/c/discussion-related-to-httpsgithubcomhuggingfacediffusers/63)? Please add a link to it if that's the case.
- [ ] Did you make sure to update the documentation with your changes? Here are the
      [documentation guidelines](https://github.com/huggingface/diffusers/tree/main/docs), and
      [here are tips on formatting docstrings](https://github.com/huggingface/diffusers/tree/main/docs#writing-source-documentation).
- [x ] Did you write any new necessary tests?
- [ ] Are you the author (or part of the team) of the model/pipeline (only applicable for model/pipeline related PRs)?


## Who can review?
@DN6 @yiyixuxu

