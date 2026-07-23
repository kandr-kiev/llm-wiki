---
title: "Issue #14188: [Quantization] Fix ModelOpt pre-quantized loading"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - container
  - data
  - foundation-model
  - open-source
  - quantization
  - real-time
  - review
  - standards
---

# Issue #14188: [Quantization] Fix ModelOpt pre-quantized loading

> **Source:** gh-huggingfacediffusers-issue-14188-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/diffusers/issues/14188 ingested: 2026-07-14 sha256: 9fc6165a59cd56a745da335aefbc49498e0141c9cca7a272410b7a3accd22a5d blog_source: github:huggingface/diff...
> **Sources:**
>   - gh-huggingfacediffusers-issue-14188-2026-07-14.md
> **Links:**
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]
- [[Automating away]]

## Key Findings

---
source_url: https://github.com/huggingface/diffusers/issues/14188
ingested: 2026-07-14
sha256: 9fc6165a59cd56a745da335aefbc49498e0141c9cca7a272410b7a3accd22a5d
blog_source: github:huggingface/diffusers
---
# Issue #14188: [Quantization] Fix ModelOpt pre-quantized loading 
**State:** open | **Author:** yzhautouskay | **Created:** 2026-07-14T17:03:34Z
## What does this PR do?
Fixes loading of **pre-quantized ModelOpt models** via `from_pretrained(..., device_map=...)`,
which currently crashes with:
> NotImplementedError: Cannot copy out of meta tensor; no data! ...
Note: this is required for the pre-quantized path to work at all with HF checkpointing enabled —
no combination of `device_map` / `.to(device)` load options works around it without this change.
### Root cause
For pre-quantized models, `NVIDIAModelOptQuantizer.check_if_quantized_param` returned `True`
for every tensor. That routes the quantizer buffers ModelOpt recreates on restore
(`_amax`, `_scale`) through `create_quantized_param`, which assigns them into
`module._parameters`. Those buffers are then never materialized by the low-memory loader and
stay on the `meta` device, so the later device move fails.
### Fix
- `check_if_quantized_param`: for pre-quantized models, only claim real **parameters**
(`return tensor_name in module._parameters`); buffers fall back to the standard loader, which
materializes `_amax`/`_scale` on their target device.
- `create_quantized_param`: guard the pre-quantized branch so a non-parameter reaching it
raises clearly instead of silently mis-assigning.
### TODO (follow-up)
Add a real regression test: enable `enable_huggingface_checkpointing()` before save+load (current tests don't do that), load
the round-tripped model with `device_map`, and assert no `meta` params/buffers remain (fails on
`main`, passes with this fix). Not included here.
## Environment
Single ModelOpt version on **both** export and load (ModelOpt state is version-sensitive, so
producer and consumer must match):
- `diffusers` 0.40.0.dev0 (this branch)
- `nvidia-modelopt` 0.44.0 (quantize + load)
- `torch` 2.9.0a0+145a3a7bda.nv25.10 (NVIDIA NGC container build)
## Who can review?
<>

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]
- [[Automating away]]
