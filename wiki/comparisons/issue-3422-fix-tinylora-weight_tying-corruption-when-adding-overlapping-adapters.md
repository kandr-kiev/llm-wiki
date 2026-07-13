---
title: "Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - claude
  - foundation-model
  - library
  - multi-agent
  - open-source
  - real-time
  - search
  - self-supervised
---
# Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters

> **Source:** gh-huggingfacepeft-issue-3422-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/peft/issues/3422 ingested: 2026-07-11 sha256: aa6fa8812ea6e5e4b63b042c8466ad2c911aa73df1b94785c35fe0abc7aee7e6 blog_source: github:huggingface/peft --- #...
> **Sources:**
>   - gh-huggingfacepeft-issue-3422-2026-07-11.md
> **Links:**
- [[issue-3421-fix-x-lora-adapter-name-mismatch-and-delete_adapter-desync]]
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-3420-fix-hotswapping-for-lora-adapters-targeting-grouped-conv2d]]

## Key Findings

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
`gh pr list --repo huggingface/peft --search "tinylora" --state all` and `gh issue list --repo huggingface/peft --search "tinylora weight_tying" --state all` (and a broader `"tinylora"` issue search) surface only #3024 (original TinyLoRA implementation, merged — this is where `_target_key_to_idx` and the buggy condition originate) and #3180 (fixes non-determinism in the projection seeding by threading `layer_idx` through the layer constructor instead of a `set_layer_idx` setter). I read #3180's diff: it only touches `tinylora/layer.py`'s seeding plumbing and how `layer_idx` is passed into `_create_new_module`/`update_layer`; it does not change the `_target_key_to_idx` rebuild co

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-3421-fix-x-lora-adapter-name-mismatch-and-delete_adapter-desync]]
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-3420-fix-hotswapping-for-lora-adapters-targeting-grouped-conv2d]]
