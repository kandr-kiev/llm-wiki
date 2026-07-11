---
source_url: https://github.com/huggingface/peft/issues/3422
ingested: 2026-07-11
sha256: aa6fa8812ea6e5e4b63b042c8466ad2c911aa73df1b94785c35fe0abc7aee7e6
blog_source: github:huggingface/peft
---
# Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters

**State:** open | **Author:** DaoyuanLi2816 | **Created:** 2026-07-11T04:46:26Z

## What does this PR do?

`TinyLoraModel._create_and_replace` caches a model-level mapping from target-module key to a deterministic layer index (`_target_key_to_idx`), which is used to compute how many `weight_tying` groups exist and which group each module falls into. The mapping is (re)built lazily:

```python
if not hasattr(self, "_target_key_to_idx") or current_key not in self._target_key_to_idx:
    self._target_key_to_idx = self._build_target_key_mapping(tinylora_config)
```

This rebuild condition only checks whether the *current module's key* is missing from the *existing* mapping — it does not check whether the mapping was built for the *current adapter*. `PeftModel.add_adapter` calls `inject_adapter` directly (bypassing `_pre_injection_hook`), so when a second adapter is added whose `target_modules` overlap with (but differ from) a prior adapter's, any module that happens to also be a key in the first adapter's stale mapping skips the rebuild and reuses that adapter's layer index and module count. This silently corrupts the number of `weight_tying` groups (and hence the trainable parameter count / sharing structure) computed for the second adapter, with no error or warning.

### Root cause

Concretely: adapter "default" targets `["lin0", "lin1", "lin2", "lin3"]`, building `_target_key_to_idx = {"lin0": 0, "lin1": 1, "lin2": 2, "lin3": 3}` (4 entries). A second adapter "b" then targets only `["lin1", "lin2"]` with `weight_tying=1/3`. Both `"lin1"` and `"lin2"` are already keys in the stale 4-entry mapping from "default", so the rebuild never triggers for adapter "b" — its group count gets computed from `num_target_layers=4` (adapter "default"'s count) instead of the correct `num_target_layers=2` (adapter "b"'s own count). With `weight_tying=1/3`, this yields 2 groups instead of the correct 1, i.e. `lin1`/`lin2` silently fail to share a `v` even though `weight_tying` says they should.

### Why this isn't a duplicate

`gh pr list --repo huggingface/peft --search "tinylora" --state all` and `gh issue list --repo huggingface/peft --search "tinylora weight_tying" --state all` (and a broader `"tinylora"` issue search) surface only #3024 (original TinyLoRA implementation, merged — this is where `_target_key_to_idx` and the buggy condition originate) and #3180 (fixes non-determinism in the projection seeding by threading `layer_idx` through the layer constructor instead of a `set_layer_idx` setter). I read #3180's diff: it only touches `tinylora/layer.py`'s seeding plumbing and how `layer_idx` is passed into `_create_new_module`/`update_layer`; it does not change the `_target_key_to_idx` rebuild condition at all. No open PR or issue addresses this.

## Tests

Added `tests/test_tinylora.py` with two regression tests:
- `test_second_adapter_overlapping_target_modules_matches_fresh_control`: adds adapter "default" targeting 4 linear layers, then adapter "b" targeting a different (strict subset) but overlapping pair with `weight_tying=1/3`, and asserts adapter "b" ends up with the same number of groups / trainable parameters / shared-`v` structure as a freshly-built control model containing only adapter "b".
- `test_second_adapter_overlapping_target_modules_after_delete_and_readd`: same idea, but through `delete_adapter` + re-`add_adapter` with the same adapter name and different `target_modules`, to cover the same staleness bug reappearing through deletion/recreation rather than only through a second distinct adapter name.

Ran `tests/test_tinylora.py` via pytest: both pass. Verified fail-before / pass-after: reverting only the fix (keeping the new tests) makes both tests fail with exactly the corruption described above (`assert 2 == 1`, i.e. adapter "b" ends up with 2 groups instead of the correct 1); re-applying the fix makes them pass.

Also verified the pre-existing TinyLoRA parametrizations in `tests/test_custom_models.py` (the 8 single-adapter configs under "TinyLoRA", plus the disjoint-target-modules "TinyLoRA Same"/"TinyLoRA Different" two-adapter cases) by exercising the same configs directly against the real library: results (group counts, parameter counts, shared-`v` identity, forward-pass outputs) are identical before and after this fix, confirming no regression to the existing behavior.

## AI assistance disclosure

This PR was prepared with AI assistance (Claude Code). There is no pre-existing issue for this bug — I found it myself while auditing TinyLoRA's multi-adapter handling. I independently verified the root cause (traced `_create_and_replace`'s rebuild condition, confirmed `add_adapter` bypasses `_pre_injection_hook` via `inject_adapter`, read #3180's diff to confirm it never touched this code path), reproduced the corruption and its fix end-to-end against the real library, and reviewed every changed line before proposing this change.
