---
source_url: https://github.com/huggingface/peft/issues/3430
ingested: 2026-07-14
sha256: c160859994bd1b55ecc82a54a976cc974e4c0c9888a8987f070d73c8e47af96a
blog_source: github:huggingface/peft
---
# Issue #3430: FIX HiRA ConvNd layers with groups > 1 crash on forward, not just merge

**State:** open | **Author:** DaoyuanLi2816 | **Created:** 2026-07-14T05:37:36Z

## What does this PR do?

HiRA's `_ConvNd` layers (`Conv1d`/`Conv2d`/`Conv3d`) crash with a confusing `RuntimeError` on the very first (unmerged) forward pass whenever the wrapped conv layer has `groups > 1` (e.g. depthwise/grouped convs, common in vision models). The existing `groups > 1` warning raised at construction only says "Merging is not supported", which is misleading — ordinary forward is equally broken, and it breaks immediately, not just on `merge()`.

Repro:

```python
import torch
from torch import nn
from peft import HiraConfig, get_peft_model

class Wrapper(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(4, 8, kernel_size=3, groups=2)
    def forward(self, x):
        return self.conv(x)

model = get_peft_model(Wrapper(), HiraConfig(target_modules=["conv"], r=4))
model(torch.randn(2, 4, 8, 8))
# RuntimeError: The size of tensor a (2) must match the size of tensor b (8) at non-singleton dimension 1
```

Reproduces identically for `Conv1d` and `Conv3d`.

### Root cause

`update_layer` builds the HiRA `A` factor using the full `in_channels`, never divided by `groups`, even though `groups` is read into a local variable right there and then never used:

```python
groups = getattr(base, "groups", 1)
...
weight_shape_A = (r, in_channels, *kernel_size)   # ignores groups entirely
```

The base conv's own weight is `(out_channels, in_channels // groups, *kernel_size)`. So whenever `groups > 1`, the delta weight computed by `get_delta_weight()` comes out shaped `(out_channels, in_channels, *kernel_size)` (full `in_channels`) instead of `(out_channels, in_channels // groups, *kernel_size)`. `forward()` then does an element-wise Hadamard product between the two:

```python
bia = self.get_delta_weight(active_adapter)   # wrong shape when groups > 1
base_weight = base.weight
eff_weight = base_weight * bia                # <-- crashes here
```

`get_delta_weight`'s shape-correcting `.transpose(0, 1)` compounds this — it was only applied `if self.get_base_layer().groups <= 1`, i.e. explicitly skipped for the grouped case, leaving the wrong shape *and* the wrong orientation.

### Why I chose a clear rejection instead of full `groups > 1` support

HiRA's forward/merge both materialize a single delta-weight tensor shaped exactly like the base layer's weight and Hadamard-multiply it with that weight (`eff_weight = base_weight * bia`) before one grouped `conv_fn` call. Making that mathematically correct for `groups > 1` would require the low-rank `hira_A`/`hira_B` factors to follow some new, specific parameterization (e.g. sharing the `A` basis across groups, or splitting the rank dimension per group) that isn't drawn from the HiRA paper or any existing precedent in this codebase — it would be inventing a new HiRA variant for grouped convs, not fixing a bug.

By contrast, LoRA's `_ConvNd` *does* support `groups > 1` for forward, but via an architecturally different mechanism: `lora_A`/`lora_B` are real, separate `nn.ConvNd` sub-modules chained sequentially (`lora_B(lora_A(dropout(x)))`), so PyTorch's own grouped-conv machinery resolves everything — there's no materialized combined weight tensor to get the shape of "right" or "wrong". That mechanism doesn't transfer to HiRA's single-tensor Hadamard design. Tellingly, LoRA's own `merge()` for `groups > 1` is *also* blocked, with the exact same `NotImplementedError` HiRA already raises for merge (both cite `#2403`), and `tests/testing_common.py` has a maintainer comment stating explicitly:

```python
if model_id.startswith("Conv2dGroups") and (config_cls == LoraConfig):
    # note: right now, only LoRA supports groups>1, if other PEFT methods add support, they might also need to skip
    pytest.skip("Merging conv layers with groups>1 and LoRA is not supported.")
```

i.e. `groups > 1` support for other tuners (HiRA included) is a known, accepted gap today, not an oversight to paper over with an unproven mathematical extension.

Given this, I moved the existing `groups > 1` restriction from a late, merge-only, easy-to-miss warning into an immediate `NotImplementedError` raised in `update_layer` (covers both `__init__` and any later `update_layer` call, e.g. adding another adapter), with a message that accurately states both the forward pass and merging are unsupported — instead of constructing "successfully" and then crashing deep inside `forward()` with a confusing shape-mismatch `RuntimeError`. I also removed the now-unreachable `if groups <= 1` branch inside `get_delta_weight` (dead after the new guard) in favor of an unconditional transpose, with a comment explaining why it's always correct now.

### Why this isn't a duplicate

```
gh pr list --repo huggingface/peft --search "hira" --state all
gh issue list --repo huggingface/peft --search "hira groups" --state all
gh issue list --repo huggingface/peft --search "hira conv" --state all
```

only surface the original HiRA integration PR (#2668, merged, no mention of `groups` anywhere in its description or discussion) plus unrelated doc/test PRs. No open PR or issue addresses this crash.

## Tests

Added `TestHiraInitialization` to `tests/test_initialization.py`, mirroring the existing `TestLoraInitialization.test_error_raised_if_rank_not_divisible_by_groups` pattern used for LoRA's analogous `groups`-related restriction, parametrized over `nn.Conv1d`/`Conv2d`/`Conv3d`:

- `test_error_raised_for_groups_greater_than_one`: constructing a HiRA adapter over a `groups=2` conv layer raises `NotImplementedError` immediately via `get_peft_model`.
- `test_no_error_and_correct_forward_for_groups_equal_to_one`: the default `groups=1` case still constructs and produces a correctly-shaped forward output (regression guard, since `get_delta_weight` was also touched).

Verified fail-before/pass-after by isolating the `src/peft/tuners/hira/layer.py` change as a standalone patch file and reverse-applying it while keeping the new tests: before the fix, the three `groups > 1` tests fail with "DID NOT RAISE NotImplementedError" (construction "succeeds" with only the old, misleading warning); after re-applying the fix, all 6 new tests pass.

Also ran the full existing HiRA test surface (`pytest tests/ -k "hira and not shira"`, 1075 collected across `test_custom_models.py`, `test_config.py`, `test_feature_extraction_models.py`, `test_seq_classifier.py`, `test_decoder_models.py`, `test_encoder_decoder_models.py`, `test_gpu_examples.py`, `test_initialization.py`): 960 passed, 116 skipped, 0 failed — no regressions to the still-supported (non-grouped) HiRA Conv/Linear/Embedding paths.

`ruff check --line-length 119` and `ruff format --check --line-length 119` both pass clean on the changed files.

## AI assistance disclosure

This PR was prepared with AI assistance (Claude Code). There is no pre-existing issue for this bug — I found it myself while auditing HiRA's `_ConvNd` support for correctness issues around `groups`. I independently verified the root cause (traced the exact shape mismatch back to `update_layer`'s unused `groups` variable and `get_delta_weight`'s wrong conditional transpose, and cross-checked LoRA's analogous but architecturally different `groups > 1` handling to confirm the scope of what is and isn't reasonably fixable here), reproduced the crash and its fix end-to-end against the real library for `Conv1d`/`Conv2d`/`Conv3d`, and reviewed every changed line before proposing this change.
