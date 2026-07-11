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

Give `LNTuningLayer` the same explicit `original_module` reference used elsewhere in PEFT: a copy of the pretrained layer captured once at construction time, never touched by `merge`/`unmerge`. `_create_new_module` now initializes new adapters from `target.original_module` instead of `target.base_layer`. The existing merge/unmerge swap behavior for the currently active adapter is untouched.

`original_module`'s parameters are automatically frozen by the existing generic `_mark_only_adapters_as_trainable` sweep (it freezes every parameter whose name doesn't contain the `ln_tuning_` prefix) and are excluded from saved adapter checkpoints by the same prefix-based filtering `get_peft_model_state_dict` already uses, so this doesn't change the on-disk checkpoint format or trainable-parameter counts.

### Why this isn't a duplicate

`gh pr list --repo huggingface/peft --search "ln_tuning" --state all` and `gh pr list --repo huggingface/peft --search "LN Tuning merge" --state all` surface only the original feature PR (#1301) and unrelated docstring/benchmark/cleanup PRs (#3291, #3082, #3067, #2846, #2433, #1324). `gh issue list --repo huggingface/peft --search "ln_tuning" --state all` surfaces only an unrelated closed BOFT issue (#2219). No open PR or issue addresses this.

## Tests

Added `TestLNTuningMerge.test_add_adapter_after_merge_is_initialized_from_pretrained_weights` to `tests/test_custom_models.py`: wraps a model with LN Tuning, sets the `"default"` adapter's weight to a sentinel value, merges it, then adds a second adapter and asserts its initial weight matches the pretrained weight (captured independently, before the model was ever wrapped) rather than the sentinel.

Verified fail-before/pass-after with pytest: before the fix, the new test fails because the new adapter's weight equals the sentinel (`999.0`) instead of the pretrained value (`1.0`); after the fix, it passes. Also ran the full existing LN Tuning-related test surface across the repo (`pytest tests/ -k "ln_tuning or LNTuning or lntuning"`, covering `test_custom_models.py`'s generic parametrized suite plus `TestRequiresGrad`, `test_config.py`, and the saved-checkpoint `test_regression.py::TestMlp::test_ln_tuning`) — all pass, no regressions.

## AI assistance disclosure

This PR was prepared with AI assistance (Claude Code). There is no pre-existing issue for this bug — I found it myself while auditing tuner `merge()` implementations that deviate from the standard additive-delta pattern. I independently verified the root cause (traced the `base_layer`/`ln_tuning_layers` swap through `merge()` into `_create_new_module`, confirmed the analogous `original_module` pattern already used by `AuxiliaryTrainingWrapper`, and checked how the freeze/save-filtering logic treats the new attribute), reproduced the bug and its fix end-to-end against the real library, and reviewed every changed line before proposing this change.
