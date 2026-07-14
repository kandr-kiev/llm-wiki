---
source_url: https://github.com/huggingface/trl/issues/6384
ingested: 2026-07-14
sha256: 125c0d7d7f83280c1257ccfe10504537cf132be7703f3c1bd3bdb06d7957defd
blog_source: github:huggingface/trl
---
# Issue #6384: Fix SDPO/SDFT use_liger_kernel under DeepSpeed ZeRO-3 during evaluation

**State:** open | **Author:** DaoyuanLi2816 | **Created:** 2026-07-14T05:47:32Z

## What this fixes

`training_step` already gathers the sharded `lm_head` weights for the fused Liger JSD loss under DeepSpeed ZeRO-3:

```python
def training_step(self, model, inputs, num_items_in_batch):
    # Gather spans forward+backward: the fused JSD computes the lm_head grad in backward.
    with self._get_liger_zero3_lm_head_gather_ctx(model):
        output = super().training_step(model, inputs, num_items_in_batch)
```

`prediction_step` (the path `trainer.evaluate()` uses) calls `compute_loss` directly, with no such wrapping:

```python
def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys=None):
    ...
    with torch.no_grad():
        with self.compute_loss_context_manager():
            loss = self.compute_loss(model, inputs)
```

`compute_loss` → `_compute_liger_loss` reads `student_head.weight` / `teacher_head.weight` directly — that's the point of the fused kernel, it bypasses the module forward that would otherwise trigger ZeRO-3's gather hook (see `_get_liger_zero3_lm_head_gather_ctx`'s own docstring). So `use_liger_kernel=True` + DeepSpeed ZeRO-3 + any `eval_dataset`/`eval_strategy` runs that matmul against an ungathered, sharded weight during evaluation, even though training under the exact same config gathers it correctly.

This affects both `SDPOTrainer` and `SDFTTrainer`, which duplicate the same helper and `training_step`/`prediction_step` structure by design (per this repo's convention for experimental trainers).

## Fix

Wrap `prediction_step`'s `compute_loss` call in the same `_get_liger_zero3_lm_head_gather_ctx(model)` that `training_step` already uses, scoped to the forward only (evaluation never calls backward).

This is the same underlying issue as #5891 (GRPO) and #6372 (DPO/KTO), but a different shape than #6372's fix. #6372 moves the gather into `compute_loss` itself (via the new shared `maybe_gather_lm_head_ctx`) so `training_step` and `prediction_step` share it automatically, because for the fused DPO/KTO/GRPO losses "the weight gradient is computed and stashed during this forward, so the parameters need not stay gathered for the backward" (`maybe_gather_lm_head_ctx`'s docstring). SDPO/SDFT's own comment on `training_step` says the opposite for the fused JSD loss here: the gather must span forward *and* backward, since the JSD grad is computed in the backward pass. Folding the gather into `compute_loss` alone would end it before backward runs during training, silently dropping that existing coverage. Wrapping `prediction_step` the same way `training_step` already does closes the eval gap without disturbing that constraint.

Note: `GOLDTrainer` and `DistillationTrainer` duplicate the identical `_get_liger_zero3_lm_head_gather_ctx` / `training_step` / `prediction_step` pattern and appear to have the same gap. I've left them out of this PR to keep it focused on SDPO/SDFT; happy to send a follow-up if that's useful.

## Verification

I don't have DeepSpeed ZeRO-3 hardware to reproduce the exact downstream numeric failure (crash vs. a silently-wrong eval loss), the way #5891/#6372 did on real GPUs. What I verified directly, with `liger_kernel` stubbed out as a no-op passthrough (Triton/liger-kernel aren't installable in my environment) so trl's own control flow runs completely unmodified:

- Built real `SDPOTrainer`/`SDFTTrainer` instances with `use_liger_kernel=True` (same fixtures as the existing `test_liger_loss_matches_non_liger_loss` tests) and instrumented `_get_liger_zero3_lm_head_gather_ctx` to count invocations.
- On current `main`: `trainer.train()` enters the gather-context helper once per training step; `trainer.evaluate()` enters it zero times, for both trainers.
- With this fix: `trainer.evaluate()` also enters it (once per eval batch), for both trainers.

Added `test_prediction_step_gathers_liger_zero3_lm_head_like_training_step` to `tests/experimental/test_sdpo_trainer.py` and `tests/experimental/test_sdft_trainer.py`, asserting this call-count invariant. It doesn't require `use_liger_kernel`/DeepSpeed/liger-kernel to be installed — the helper simply no-ops when neither is active — so it runs in ordinary CI, and it fails on current `main`.

So the control-flow gap itself (train enters the gather, eval doesn't) is fully demonstrated end-to-end through trl's real code. That this produces the same real-world failure mode as #5891/#6372 under an actual ZeRO-3 cluster is inferred from the same reasoning those PRs' own descriptions use (a fused kernel reading a sharded `nn.Parameter` by attribute bypasses the module forward that DeepSpeed hooks to gather it) — I did not independently reproduce a crash or a silently-wrong eval loss on real multi-GPU ZeRO-3 hardware.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Touches distributed training paths for experimental trainers when Liger + ZeRO-3 + eval are combined; change is narrow and mirrors existing training_step behavior.
> 
> **Overview**
> Fixes **eval** when `use_liger_kernel` runs under **DeepSpeed ZeRO-3**: `training_step` already wraps loss in `_get_liger_zero3_lm_head_gather_ctx`, but `prediction_step` did not, so fused JSD could read sharded `lm_head` weights during `trainer.evaluate()`.
> 
> **SDPOTrainer** and **SDFTTrainer** now wrap `compute_loss` inside `prediction_step` with the same gather context (forward-only for eval, since there is no backward).
> 
> Adds `test_prediction_step_gathers_liger_zero3_lm_head_like_training_step` in both experimental test modules to assert the helper is invoked on `evaluate()` as well as `train()` (works in CI without DeepSpeed/Liger installed because the helper is a no-op when inactive).
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit aaeaf5d70ccfec4b2ff116333345226068f2e65f. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->