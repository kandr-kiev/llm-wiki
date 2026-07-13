---
title: "Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - benchmark
  - claude
  - closed-source
  - data
  - deep-learning
  - design-pattern
  - fine-tuning
  - foundation-model
  - library
  - lora
  - open-source
  - real-time
  - search
  - self-supervised
  - standards
---
# Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter

> **Source:** gh-huggingfacepeft-issue-3423-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/peft/issues/3423 ingested: 2026-07-11 sha256: 4e11d1da4feaa0a39debd99c01cdb1f134ddd59578bdc694f90b013dd4dabdbe blog_source: github:huggingface/peft --- #...
> **Sources:**
>   - gh-huggingfacepeft-issue-3423-2026-07-11.md
> **Links:**
- [[issue-3421-fix-x-lora-adapter-name-mismatch-and-delete_adapter-desync]]
- [[issue-3422-fix-tinylora-weight_tying-corruption-when-adding-overlapping-adapters]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]

## Key Findings

---
source_url: https://github.com/huggingface/peft/issues/3423
ingested: 2026-07-11
sha256: 4e11d1da4feaa0a39debd99c01cdb1f134ddd59578bdc694f90b013dd4dabdbe
blog_source: github:huggingface/peft
---
# Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter
**State:** open | **Author:** DaoyuanLi2816 | **Created:** 2026-07-11T04:47:51Z
## What does this PR do?
LN Tuning (`LNTuningLayer`) merges an adapter by swapping `self.base_layer` with the trained `ln_tuning_layers[adapter]` module, rather than computing and applying a delta like other tuners do. If a second adapter is then added (via `add_adapter`/`get_peft_model`) while the first one is still merged — a normal, documented state reachable with a plain `model.merge_adapter()` call — the new adapter is silently initialized from the first adapter's *trained* weights instead of the pristine pretrained layer.
### Root cause
```python
# LNTuningLayer.merge()
self.base_layer, self.ln_tuning_layers[adapter_names[0]] = (
self.ln_tuning_layers[adapter_names[0]],
self.base_layer,
)
```
After this swap, `self.base_layer` holds the *trained* copy, not the pretrained one. `LNTuningModel._create_new_module` then does:
```python
new_module.update_layer(target.base_layer, adapter_name, config=peft_config)
```
`update_layer` deep-copies whatever it's given as the new adapter's starting point:
```python
def update_layer(self, layer, adapter_name, config, **kwargs):
self.ln_tuning_layers[adapter_name] = deepcopy(layer)
```
So if `target.base_layer` currently holds a previously merged adapter's trained weights, that's exactly what the new adapter gets deep-copied from — silently violating the assumption that every adapter is trained independently starting from the same pretrained base.
I confirmed this with a minimal repro against latest `main`: wrap a tiny model with LN Tuning, set adapter `"default"`'s weight to a distinctive sentinel, `merge_adapter()`, then `add_adapter("adapter2", ...)` — `adapter2`'s initial weight comes out equal to the sentinel instead of the pretrained LayerNorm's `1.0`.
I looked for a pre-existing "keep the pristine original around" mechanism to reuse. LoRA and most other tuners avoid this class of bug entirely because they merge via an additive delta (`base_layer.weight.data += delta`, reversed by subtracting the same delta), so `base_layer`'s identity/reference never changes. `AuxiliaryTrainingWrapper` (used by `modules_to_save` and `trainable_tokens`) already solves the same "we replace/copy a whole module per adapter" problem with an explicit `self.original_module` reference that every new adapter is copied from, set once and never touched by merging. LN Tuning has no such mechanism — it relies solely on `base_layer` always being the pretrained layer, which the swap-based `merge()` breaks.
### Fix
Give `LNTuningLayer` the same explicit `original_module` reference used elsewhere in PEFT: a copy of the pretrained layer captured once at construction tim

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-3421-fix-x-lora-adapter-name-mismatch-and-delete_adapter-desync]]
- [[issue-3422-fix-tinylora-weight_tying-corruption-when-adding-overlapping-adapters]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]
