---
title: "Issue #3421: Fix X-LoRA adapter name mismatch and delete_adapter desync"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - claude
  - closed-source
  - few-shot
  - foundation-model
  - library
  - lora
  - open-source
  - real-time
  - search
  - self-supervised
  - training
---
# Issue #3421: Fix X-LoRA adapter name mismatch and delete_adapter desync

> **Source:** gh-huggingfacepeft-issue-3421-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/peft/issues/3421 ingested: 2026-07-11 sha256: 94f246c8b3bde7607e23bb219701cbbae654dbd1e7b713baf0dfa808b5ce2342 blog_source: github:huggingface/peft --- #...
> **Sources:**
>   - gh-huggingfacepeft-issue-3421-2026-07-11.md
> **Links:**
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[away]]
- [[automating-ai-away-2026-07-07]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]

## Key Findings

---
source_url: https://github.com/huggingface/peft/issues/3421
ingested: 2026-07-11
sha256: 94f246c8b3bde7607e23bb219701cbbae654dbd1e7b713baf0dfa808b5ce2342
blog_source: github:huggingface/peft
---
# Issue #3421: Fix X-LoRA adapter name mismatch and delete_adapter desync
**State:** open | **Author:** DaoyuanLi2816 | **Created:** 2026-07-11T04:46:11Z
## What does this PR do?
This fixes two related adapter-lifecycle bugs in `XLoraModel` (`src/peft/tuners/xlora/model.py`), found while auditing how X-LoRA registers and manages its expert LoRA adapters internally.
### Bug 1: the names used to register experts and the names used to activate them don't match
`XLoraModel.__init__` loads each expert LoRA checkpoint into the internal `LoraModel` under a **positional** name:
```python
for i, (_adapter_name, model_id) in enumerate(adapters_items):
_load_adapter_into_lora_model(
lora_model=self.lora_model,
adapter_name=str(i), # <-- "0", "1", "2", ... -- discards the user's own key
...
)
self.lora_model.set_adapter(list(peft_config.adapters.keys())) # <-- but activates by the ORIGINAL keys
```
If the user's `adapters` dict keys are not literally `"0"`, `"1"`, `"2"`, ... (e.g. the class docstring's own example uses `"adapter_1"`, `"adapter_2"`, `"adapter_n"`), the two calls disagree: the experts get registered as `"0"`/`"1"`/`"2"`, but `set_adapter` activates `"adapter_1"`/`"adapter_2"`/`"adapter_n"` -- names that were never registered anywhere.
Every X-LoRA forward pass runs a pre-hook that calls `self.lora_model.disable_adapter_layers()`, which iterates `self.active_adapters` and does `self.peft_config[active_adapter]`:
```python
# tuners_utils.py, BaseTuner.disable_adapter_layers
for active_adapter in self.active_adapters:
bias_val = getattr(self.peft_config[active_adapter], "bias", "none") # KeyError
```
Since `self.lora_model.peft_config` never got an entry for `"adapter_1"`, this raises `KeyError: 'adapter_1'` on the very first forward pass. This exact symptom (it only works if the adapter dict keys happen to be `"0"`, `"1"`, ...) was also reported as a comment on #2015 ("The adapters must be named "0", "1", etc in the adapters dict() otherwise training won't start and will say that the adapters don't exist"), acknowledged by @EricLBuehler ("Hmm ok, thanks for reporting this, I'll see what could be causing it") but left unaddressed; the issue was later closed by the stale bot. That issue's *main* topic is a separate, still-unresolved problem (the X-LoRA classifier's own parameters not ending up trainable, causing `requires_grad=None` gradients during training) that this PR does not touch, so I'm referencing it here for context rather than using a closing keyword.
**Fix**: register each expert under its own original key (the same one already used for `set_adapter` a few lines later) instead of `str(i)`. This matches how `XLoraLinearLayer`/`XLoraEmbeddingLayer`/`XLoraConv2dLayer.forward` already look up adapters -- by name, out of `self.target.lora_A`/`lo

## Summary

ra_embedding_A` -- and how `XLoraConfig`'s own docstring describes the `adapters` dict ("only the keys matter during loading"), so the user-facing key becomes the one identifier used everywhere, with no silent renaming in between.
### Bug 2: `delete_adapter` desyncs `active_adapter` between the outer `XLoraModel` and the inner `LoraModel`
`XLoraModel` has no `delete_adapter` override, so it inherits `BaseTuner.delete_adapter`, whose last line is:
```python
self.active_adapter = new_adapter or []
```
`XLoraModel.__getattr__` forwards missing attribute *reads* to `self.lora_model`, but `__getattr__` is only ever consulted when normal attribute lookup fails -- it is never involved in attribute *writes*. So `self.active_adapter = ...` (with `self` being the outer `XLoraModel`) just creates/overwrites a plain instance attribute on `self`, completely disconnected from `self.lora_model.active_adapter`, which is what `disable_adapter_layers()`/`enable_adapter_layers()` (called on `self.lora_model` from the forward pre-hook) actually consult. A few lines earlier in the same method, the deleted adapter's entry is correctly removed from `self.lora_model.peft_config` (this part works, since reading `self.peft_config` returns the same underlying dict object). So after calling `delete_adapter` on a model with 2+ experts, `self.lora_model.active_adapter` still lists the just-deleted name, whose config entry no longer exists -- and the next forward pass raises a `KeyError` for it.
**Fix**: add an explicit `active_adapter` property/setter on `XLoraModel` that forwards both reads *and* writes to `self.lora_model.active_adapter`, mirroring the read-forwarding `__getattr__` already does. This fixes `delete_adapter` generically (and any other inherited `BaseTuner` method that writes `self.active_adapter`, e.g. `set_adapter`), rather than special-casing `delete_adapter` alone.
### Duplicate check
- `gh issue view 2015 --repo huggingface/peft`: covered above.
- `gh pr list --repo huggingface/peft --search "xlora" --state all` and `gh issue list --repo huggingface/peft --search "xlora adapter" --state all`: no open PR or issue addresses either bug. The closest related items are already resolved or unrelated: #2485 ("X-LoRA keyerror if expert project not exists", fixed by #2488), #2132 (a `ValueError` from a state-dict key mismatch specific to `SEQ_CLS`/`modules_to_save` models -- still open, but a different failure mode entirely, unrelated to adapter naming or deletion), and #3235 (an already-merged, unrelated one-line typo fix in `xlora/config.py`'s warning message).
## Tests
Added two regression tests to `tests/test_xlora.py`:
- `test_non_numeric_adapter_names_forward`, using a new `model_named_adapters` fixture that builds an X-LoRA model with the same adapter-naming convention as the class docstring example (`"adapter_1"`, `"adapter_2"`, ...) instead of this file's usual `"0"`, `"1"`, ... convention, then calls `.generate()`.
- `test_delete_adapter`, reusing the exi

## Related Articles

- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[away]]
- [[automating-ai-away-2026-07-07]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
