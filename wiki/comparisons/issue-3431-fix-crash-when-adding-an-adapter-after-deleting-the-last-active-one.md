---
title: "Issue #3431: FIX Crash when adding an adapter after deleting the last active one"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - fine-tuning
  - foundation-model
  - llama
  - lora
  - multi-agent
  - open-source
  - real-time
  - self-supervised
  - use-case
  - zero-shot
---

# Issue #3431: FIX Crash when adding an adapter after deleting the last active one

> **Source:** gh-huggingfacepeft-issue-3431-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/peft/issues/3431 ingested: 2026-07-14 sha256: 3fc541d9bb94fb57be9c42025bfe7c5e37609d13b1966457e76a7d3f9e7e1eab blog_source: github:huggingface/peft --- #...
> **Sources:**
>   - gh-huggingfacepeft-issue-3431-2026-07-14.md
> **Links:**
- [Issue #3430: FIX HiRA ConvNd layers with groups > 1 crash on forward, not just merge]
- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]
- [Issue #14167: FlashPack support for transformers pipeline components]

## Key Findings

---
source_url: https://github.com/huggingface/peft/issues/3431
ingested: 2026-07-14
sha256: 3fc541d9bb94fb57be9c42025bfe7c5e37609d13b1966457e76a7d3f9e7e1eab
blog_source: github:huggingface/peft
---
# Issue #3431: FIX Crash when adding an adapter after deleting the last active one
**State:** open | **Author:** DaoyuanLi2816 | **Created:** 2026-07-14T05:48:35Z
## Problem
Adding a new adapter after the model has zero active adapters crashes, if any adapter (past or present) used `modules_to_save` or `trainable_token_indices`:
```python
from transformers import AutoModelForSequenceClassification
from peft import LoraConfig, get_peft_model
model = AutoModelForSequenceClassification.from_pretrained("facebook/opt-125m")
config = LoraConfig(task_type="SEQ_CLS", modules_to_save=["score"])
model = get_peft_model(model, config)
model.delete_adapter("default") # drains to zero active adapters, this is fine
model.add_adapter("second", config) # ValueError: Please specify at least one adapter to set
```
Deleting the last remaining adapter leaving zero active adapters is an already-supported, legitimate state (`tests/testing_common.py::_test_delete_adapter` asserts `model.active_adapters == []` after doing exactly this). But once in that state, adding a new adapter crashes with a message that never even mentions `add_adapter`, three internal calls removed from what the user actually did. The same crash reproduces with `trainable_token_indices`, and with `PeftMixedModel`.
### Call chain
1. `BaseTuner.delete_adapter` (`tuners_utils.py`) sets `self.active_adapter = new_adapter or []` once the last adapter is gone.
2. `BaseTuner.inject_adapter`, which runs on every `add_adapter`, unconditionally does the "housekeeping" call `self.set_adapter(self.active_adapters, ...)`, i.e. `set_adapter([])` when there are currently zero active adapters.
3. That reaches the module-level `set_adapter()` function, which calls `_set_adapter(model, [], ...)` to update auxiliary modules.
4. `_set_adapter` calls `module.check_set_adapter([])` on every `ModulesToSaveWrapper` / `TrainableTokensWrapper` in the model (including ones left over, now empty, from a previously-deleted adapter).
5. `check_set_adapter` unconditionally raised `ValueError("Please specify at least one adapter to set")` for an empty list -- this is the crash.
## Fix: `check_set_adapter` should accept "no active adapter" as valid
`check_set_adapter`'s own docstring says it should "return the name of the adapter to be set **or None if no adapter should be set**". An empty list is exactly the "no adapter should be set" case, not a caller mistake -- it's the same state produced by draining the last adapter, which the codebase already treats as legitimate elsewhere:
- `ModulesToSaveWrapper.set_adapter` / `TrainableTokensWrapper.set_adapter` (the very method `check_set_adapter` is a gatekeeper for) already special-case `len(adapter_names) == 0` and handle it gracefully, with the comment *"when calling model.add_adapter, th

## Summary

e new adapter is not automatically active"* -- describing precisely this scenario.
- `BaseTunerLayer.set_adapter([])` (the sibling concept for the actual adapter layers, as opposed to the auxiliary wrappers) has no special case at all; `[]` just works, and `BaseTunerLayer.delete_adapter` itself calls `self.set_adapter([])` when draining the last adapter on a layer.
So `check_set_adapter` was the odd one out: it rejected an input that its own caller (`set_adapter`) already knew how to handle. The fix makes it return `None` for an empty list instead of raising, which is then treated by `_set_adapter` exactly like "no matching adapter in this module" (`module.set_adapter([], ...)`), the same code path already exercised whenever a new adapter's `modules_to_save`/`trainable_token_indices` isn't immediately activated.
### Alternative considered
An alternative, narrower fix would be to have `inject_adapter` skip the "housekeeping" `set_adapter` call when `self.active_adapters` is already empty (nothing changed, so nothing to re-notify). I went with the `check_set_adapter` fix instead because the narrower fix only patches this one call site: any other caller that legitimately reaches `_set_adapter`/`check_set_adapter` with an empty list (e.g. calling `model.base_model.set_adapter([])` directly to deactivate every adapter on a multi-adapter-capable tuner like LoRA, which `BaseTunerLayer.set_adapter([])` already supports) would still crash. Fixing `check_set_adapter` addresses the actual inconsistency at its source.
### Tradeoff
`check_set_adapter` can no longer distinguish "deliberately no active adapters" from "caller accidentally passed an empty list where they meant a real adapter name" (e.g. an upstream bug producing an unexpectedly-empty list). Previously the latter would fail loudly and immediately; after this change it silently succeeds as "deactivate this module's adapter". I don't believe there's a realistic path where this swallows a genuine mistake: the actual user-facing entry point, `PeftModel.set_adapter(adapter_name: str)`, only accepts a single string and already fails with a clear `TypeError` (unhashable list) long before reaching this code if someone passes a list by mistake. The only callers that can reach `check_set_adapter([])` are internal ones (`BaseTuner`/`MixedModel`/`PeftMixedModel` `set_adapter`/`inject_adapter`), where `[]` is always a deliberate "no active adapters" signal, never a typo. Still, flagging this tradeoff explicitly in case a reviewer sees a path I missed.
## Bundled fix: `PeftMixedModel.delete_adapter` leaks `modules_to_save` state when deleting multiple adapters at once
Same theme (delete_adapter's interaction with auxiliary wrappers), found while reading this code path, so bundling it here rather than opening a separate one-line PR:
```python
for adapter_to_delete in adapter_names:
del self.peft_config[adapter_to_delete]
...
for key in key_list:
...
if isinstance(target, BaseTunerLayer):
target.delete_adapter(ad

## Related Articles

- [Issue #3430: FIX HiRA ConvNd layers with groups > 1 crash on forward, not just merge]
- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]
- [Issue #14167: FlashPack support for transformers pipeline components]
