---
title: "Issue #3430: FIX HiRA ConvNd layers with groups > 1 crash on forward, not just merge"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - claude
  - computer-vision
  - deep-learning
  - design-pattern
  - embedding
  - foundation-model
  - integration
  - library
  - lora
  - open-source
  - pytorch
  - real-time
  - search
  - self-supervised
  - transfer-learning
  - use-case
---

# Issue #3430: FIX HiRA ConvNd layers with groups > 1 crash on forward, not just merge

> **Source:** gh-huggingfacepeft-issue-3430-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/peft/issues/3430 ingested: 2026-07-14 sha256: c160859994bd1b55ecc82a54a976cc974e4c0c9888a8987f070d73c8e47af96a blog_source: github:huggingface/peft --- #...
> **Sources:**
>   - gh-huggingfacepeft-issue-3430-2026-07-14.md
> **Links:**
- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]
- [Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters]
- [Issue #3429: FIX C3ALinear.forward chaining multiple active adapters instead of summing]
- [Issue #3421: Fix X-LoRA adapter name mismatch and delete_adapter desync]
- [Issue #3420: Fix hotswapping for LoRA adapters targeting grouped Conv2d]

## Key Findings

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
weight_shape_A = (r, in_channels, *kernel_size) # ignores groups entirely
```
The base conv's own weight is `(out_channels, in_channels // groups, *kernel_size)`. So whenever `groups > 1`, the delta weight computed by `get_delta_weight()` comes out shaped `(out_channels, in_channels, *kernel_size)` (full `in_channels`) instead of `(out_channels, in_channels // groups, *kernel_size)`. `forward()` then does an element-wise Hadamard product between the two:
```python
bia = self.get_delta_weight(active_adapter) # wrong shape when groups > 1
base_weight = base.weight
eff_weight = base_weight * bia # 1` support
HiRA's forward/merge both materialize a single delta-weight tensor shaped exactly like the base layer's weight and Hadamard-multiply it with that weight (`eff_weight = base_weight * bia`) before one grouped `conv_fn` call. Making that mathematically correct for `groups > 1` would require the low-rank `hira_A`/`hira_B` factors to follow some new, specific parameterization (e.g. sharing the `A` basis across groups, or splitting the rank dimension per group) that isn't drawn from the HiRA paper or any existing precedent in this codebase — it would be inventing a new HiRA variant for grouped convs, not fixing a bug.
By contrast, LoRA's `_ConvNd` *does* support `groups > 1` for forward, but via an architecturally different mechanism: `lora_A`/`lora_B` are real, separate `nn.Conv

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]
- [Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters]
- [Issue #3429: FIX C3ALinear.forward chaining multiple active adapters instead of summing]
- [Issue #3421: Fix X-LoRA adapter name mismatch and delete_adapter desync]
- [Issue #3420: Fix hotswapping for LoRA adapters targeting grouped Conv2d]
