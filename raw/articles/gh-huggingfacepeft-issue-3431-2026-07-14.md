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

model.delete_adapter("default")     # drains to zero active adapters, this is fine
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

- `ModulesToSaveWrapper.set_adapter` / `TrainableTokensWrapper.set_adapter` (the very method `check_set_adapter` is a gatekeeper for) already special-case `len(adapter_names) == 0` and handle it gracefully, with the comment *"when calling model.add_adapter, the new adapter is not automatically active"* -- describing precisely this scenario.
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
            target.delete_adapter(adapter_to_delete)
            if new_adapter is None:
                new_adapter = target.active_adapters[:]

self.active_adapter = new_adapter or []
if adapter_to_delete in adapter_names:
    _delete_auxiliary_adapter(self.model, adapter_to_delete, new_active_adapters=new_adapter)
```

`target.delete_adapter(adapter_to_delete)` correctly runs once per name inside the loop, updating every `BaseTunerLayer`. But `_delete_auxiliary_adapter` (which cleans up `ModulesToSaveWrapper`/`TrainableTokensWrapper`, i.e. actually removes the adapter's entry from `modules_to_save`) runs only **once, after the loop**, using `adapter_to_delete`/`new_adapter` left over from the *last* iteration only. So `mixed_model.delete_adapter(["adapter0", "adapter1"])` fully removes `adapter1` from the auxiliary wrappers but leaves `adapter0`'s entry in `ModulesToSaveWrapper.modules_to_save` (and its `_adapters` set) dangling forever, even though `adapter0` is otherwise fully deleted (gone from `peft_config` and every `BaseTunerLayer`). The `if adapter_to_delete in adapter_names:` guard is a no-op -- `adapter_to_delete` is always drawn from `adapter_names` by the loop itself, so the condition is always true; it looks like it survived a ruff-lint-driven loop-variable rename (to avoid shadowing the `adapter_name` parameter) that didn't touch the actual logic.

Fix: move both statements inside the loop, so the auxiliary cleanup happens once per deleted adapter, right next to the per-adapter `BaseTunerLayer.delete_adapter` calls it's supposed to mirror. Dropped the always-true guard.

## Tests

- `tests/test_custom_models.py::TestPeftCustomModel::test_delete_adapter_to_zero_then_add_adapter_with_modules_to_save` -- drains to zero adapters, then `add_adapter` with `modules_to_save`, confirms it no longer raises and the new adapter's `modules_to_save` entry is set up correctly.
- `tests/test_custom_models.py::TestPeftCustomModel::test_delete_adapter_to_zero_then_add_adapter_with_trainable_token_indices` -- same, for `trainable_token_indices` (needs a real transformers model, following the existing convention in this file for that config option).
- `tests/test_mixed.py::TestMixedAdapterTypes::test_delete_multiple_adapters_at_once_cleans_up_modules_to_save_for_all_of_them` -- regression test for the bundled `MixedModel.delete_adapter` fix: 3 adapters with the same `modules_to_save` target, delete 2 of them in one call, confirm neither leaks into `modules_to_save`/`_adapters`.

For both bugs, verified fail-before/pass-after by reverting just the `src/` fix via a patch file (not `git stash`) and re-running: all 3 new tests (plus a standalone script exercising `get_peft_model` + `modules_to_save`, + `trainable_token_indices` on a real transformers model, + `PeftMixedModel`) fail with the exact reported `ValueError`/leak on unmodified `main`, and pass with the fix applied.

### Test runs

- `tests/test_mixed.py`: 34 passed (includes the new regression test and the pre-existing `test_delete_adapter`/`test_modules_to_save`).
- `tests/test_tuners_utils.py`: 234 passed, 1 skipped.
- `tests/test_decoder_models.py`, full suite restricted to `LoraConfig`/`BOFTConfig` across 3 real tiny models (OPT, Llama, Gemma3): 1035 passed, 393 skipped (expected feature-incompatible combos), 0 failed.
- `tests/test_decoder_models.py -k delete_adapter`, all ~14 applicable tuner types (LoRA variants, BOFT, Delora, Gralora, Glora, IA3, VBLoRA, UniLora, TinyLora, ...) across the same 3 models: 42 passed, 3 skipped (AdaLoRA, which doesn't support multiple adapters).

I was unable to run `tests/test_custom_models.py`, `tests/test_trainable_tokens.py`, and `tests/test_initialization.py` directly through pytest in my local environment: importing them crashes the interpreter (native access violation) for reasons unrelated to this change -- I confirmed the same crash occurs on a completely unmodified checkout of `main` before making any changes, and narrowed it down to something in the import graph of those specific files (not present in `test_mixed.py`/`test_tuners_utils.py`/`test_decoder_models.py`, which all import and run cleanly) on my local Windows setup. I'm flagging this so a maintainer/CI can double check `test_custom_models.py`'s two new tests specifically; I'm confident in their correctness since they were written and fail/pass-verified via a standalone script that exercises the exact same real `peft` public API calls the tests themselves make (`get_peft_model`, `add_adapter`, `delete_adapter`, with `modules_to_save`, `trainable_token_indices`, and `PeftMixedModel`), just not through the pytest collector for that particular file.

## Lint

`ruff check` / `ruff format --check` (line-length 119, matching `setup.py`) clean on all changed files.

## AI assistance disclosure

I used AI assistance (an agentic coding assistant) to help investigate this bug, implement the fix, and write the tests described above. I read and understood the full call chain end-to-end before making changes, verified the crash against a fresh checkout of `main` with a standalone reproduction script before touching any code, made the design decision on the `check_set_adapter` fix (and its considered alternative/tradeoff) myself, and ran the test suites listed above myself to confirm the results reported here.
