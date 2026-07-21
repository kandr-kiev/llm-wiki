---
title: "Issue #3429: FIX C3ALinear.forward chaining multiple active adapters instead of summing"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - claude
  - closed-source
  - foundation-model
  - library
  - multi-agent
  - open-source
  - real-time
  - self-supervised
  - use-case
---

# Issue #3429: FIX C3ALinear.forward chaining multiple active adapters instead of summing

> **Source:** gh-huggingfacepeft-issue-3429-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/peft/issues/3429 ingested: 2026-07-14 sha256: 28ae60a872ab6b7e17175a9dfd6567dd44dde57760da2bbaf6f2fb2cf5bc41a8 blog_source: github:huggingface/peft --- #...
> **Sources:**
>   - gh-huggingfacepeft-issue-3429-2026-07-14.md
> **Links:**
- [[Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]]
- [[Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse]]
- [[Issue #3419: FIX Bug in forgetting metric in MetaMathQA]]
- [[Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters]]
- [[Automating away]]

## Key Findings

---
source_url: https://github.com/huggingface/peft/issues/3429
ingested: 2026-07-14
sha256: 28ae60a872ab6b7e17175a9dfd6567dd44dde57760da2bbaf6f2fb2cf5bc41a8
blog_source: github:huggingface/peft
---
# Issue #3429: FIX C3ALinear.forward chaining multiple active adapters instead of summing
**State:** open | **Author:** DaoyuanLi2816 | **Created:** 2026-07-14T05:23:06Z
## What does this PR do?
When more than one C3A adapter is active simultaneously, `C3ALinear.forward` reassigns `x` to each adapter's `BlockCircularConvolution` output in turn:
```python
for active_adapter in self.active_adapters:
if active_adapter not in self.c3a_kernel.keys():
continue
c3a_kernel = self.c3a_kernel[active_adapter].to(torch.float32)
x = BlockCircularConvolution.apply(x, c3a_kernel) / x.size(-1)
result += x.to(result.dtype)
```
So adapter N's transform is applied to adapter N-1's *output* instead of the original layer input — the adapters get chained rather than summed. This contradicts `merge()`, which is correctly additive (each adapter's `get_delta_weight` is computed independently and added to the base weight one at a time).
Concretely, with 2+ simultaneously active C3A adapters:
- **Square layers** produce silently **wrong** output (the unmerged forward pass no longer matches merging the same adapters and running the merged model).
- **Non-square layers** (e.g. `Linear(10, 20)` with `block_size=2` — the exact shape of PEFT's own `MLP` test fixture's `lin0`) **crash outright** with `RuntimeError: shape '[...]' is invalid for input of size ...`, because adapter 1's *output* dimension (`out_features`) gets fed into `BlockCircularConvolution` as adapter 2's *input* dimension (`in_features`).
### Fix
Sum the active adapters' kernels first, then apply `BlockCircularConvolution` once:
```python
combined_kernel = None
for active_adapter in self.active_adapters:
if active_adapter not in self.c3a_kernel.keys():
continue
c3a_kernel = self.c3a_kernel[active_adapter].to(torch.float32)
combined_kernel = c3a_kernel if combined_kernel is None else combined_kernel + c3a_kernel
if combined_kernel is not None:
delta = BlockCircularConvolution.apply(x, combined_kernel) / x.size(-1)
result += delta.to(result.dtype)
```
This is mathematically equivalent to applying the convolution per adapter and summing the results (the operation is linear in the kernel), but every adapter now sees the original `x`, matching `merge()`'s semantics, and it only runs the FFT-based convolution once regardless of how many adapters are active.
### This completes the fix requested in #3164
#3164 (@Chessing234) reported this exact bug, with a diff that introduced a local `delta` variable instead of reassigning `x`. @BenjaminBossan [requested a cleaner approach](https://github.com/huggingface/peft/pull/3164#pullrequestreview-4120129328) instead:
> Regarding the proposed solution: I think it works but what we could do instead is to sum all the active `c3a_kernel`s and then send them through `BlockCircularConvol

## Summary

ution.apply` instead of the other way round. This should get the same result and be more efficient. WDYT?
Chessing234 [agreed and reported having implemented it](https://github.com/huggingface/peft/pull/3164#issuecomment-4559946994) ("I've updated the implementation to sum all the active `c3a_kernel`s first, and then apply `BlockCircularConvolution.apply` once. It's indeed much cleaner. I've also added the C3A configurations to the `MULTIPLE_ACTIVE_ADAPTERS_TEST_CASES` test matrix as requested."), but the revised commit was never pushed, and the PR went stale and was auto-closed without the fix landing. This PR implements exactly the approach that was agreed upon there.
Separately, #3361 (merged) added C3A to `MULTIPLE_ACTIVE_ADAPTERS_TEST_CASES`, but only the "different layers" case, with the comment:
```python
# Note: Multiple C3A adapters applied to the same layer fails with shape mismatch
```
This PR un-skips that deferred "same layer" case (`"C3A Same"`) now that it passes.
## Tests
- Un-skipped `"C3A Same"` in `MULTIPLE_ACTIVE_ADAPTERS_TEST_CASES` (`tests/test_custom_models.py`), which now runs the existing `test_multiple_active_adapters_forward` / `test_multiple_active_adapters_merge_and_unmerge` / `test_merge_layers_multi` parametrized suite against two C3A adapters targeting the very same (non-square) layer — the previously-crashing configuration.
- Added `test_c3a_multiple_active_adapters_forward_matches_independent_sum` (`TestMultipleActiveAdapters`): builds a model with 2 active C3A adapters on the same non-square layer, computes the "ground truth" by merging both adapters (`merge_and_unload`, which is independently additive by construction) and running a forward pass, then asserts the unmerged multi-adapter forward pass matches it (`atol=1e-4, rtol=1e-4`).
Verified fail-before / pass-after by reverting just the fix via a patch file (keeping the new/un-skipped tests in place): with the fix reverted, both the un-skipped `"C3A Same"` cases and the new dedicated test fail with the exact `RuntimeError: shape '[9, 5, 2]' is invalid for input of size 180` crash described above; with the fix restored, all pass. Before writing any code, I also independently reproduced both failure modes with a standalone script directly against the real library on a fresh checkout of `main`, to confirm the bug still reproduces: a silently-wrong square-layer output (max abs diff ≈ 17 vs. the correct independent-additive-sum ground truth) and a crashing non-square layer — both consistent with the bug description.
Ran the full C3A-relevant subset for regressions:
```
pytest tests/test_custom_models.py -k c3a # 290 passed, 9 skipped (pre-existing, unrelated)
pytest tests/test_config.py tests/test_initialization.py -k c3a # 30 passed
```
`ruff check --line-length 119` and `ruff format --check --line-length 119` are clean on both changed files.
## AI assistance disclosure
This PR was prepared with AI assistance (Claude Code). The bug and the requested fix approach 

## Related Articles

- [[Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]]
- [[Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse]]
- [[Issue #3419: FIX Bug in forgetting metric in MetaMathQA]]
- [[Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters]]
- [[Automating away]]
