---
title: "Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ci-cd
  - data
  - foundation-model
  - open-source
  - pytorch
  - review
  - self-supervised
  - use-case
---

# Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set

> **Source:** gh-huggingfaceaccelerate-issue-4116-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/accelerate/issues/4116 ingested: 2026-07-14 sha256: 3aedaf5a7b779487efe14f45cc1c114c38b00b7513bdf282eb0888653aa21e13 blog_source: github:huggingface/acce...
> **Sources:**
>   - gh-huggingfaceaccelerate-issue-4116-2026-07-14.md
> **Links:**
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]
- [Issue #2848: Implement multi-domain intake architecture and related specs]
- [Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end]
- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]

## Key Findings

---
source_url: https://github.com/huggingface/accelerate/issues/4116
ingested: 2026-07-14
sha256: 3aedaf5a7b779487efe14f45cc1c114c38b00b7513bdf282eb0888653aa21e13
blog_source: github:huggingface/accelerate
---
# Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set
**State:** open | **Author:** sohumt123 | **Created:** 2026-07-14T14:39:57Z
# What does this PR do?
Fixes a bug in `get_non_persistent_buffers` where the function mutates the
module's private `_non_persistent_buffers_set` instead of returning a fresh set.
In the worst case this silently drops a persistent buffer from `state_dict()`.
## Problem
`get_non_persistent_buffers` (in `src/accelerate/utils/modeling.py`) binds its
accumulator directly to the module's live private set:
```python
non_persistent_buffers_set = module._non_persistent_buffers_set
if recurse:
for n, m in module.named_modules():
if fqns:
non_persistent_buffers_set |= {n + "." + b for b in m._non_persistent_buffers_set}
else:
non_persistent_buffers_set |= m._non_persistent_buffers_set
```
`set.__ior__` (`|=`) is an **in-place** update, so when `recurse=True` this
mutates `module._non_persistent_buffers_set` rather than building a separate
result. The returned object *is* the module's internal set (verified with an
`is` identity check). Consequences:
- **Idempotence is broken.** `named_modules()` yields the module itself first
with name `""`, so with `fqns=True` the call injects dot-prefixed names like
`".sub.np_buf"` into the live set, and repeated calls keep accumulating.
- **Silent data loss.** PyTorch's `Module._save_to_state_dict` skips any buffer
whose name is in `_non_persistent_buffers_set`. If a descendant leaf buffer
shares its name with a persistent buffer on an ancestor, injecting that leaf
name into the ancestor's set makes the ancestor's persistent buffer vanish
from `state_dict()`.
This is reachable on a normal path, not just a synthetic one:
`named_module_tensors(recurse=True, remove_non_persistent=True)` calls it, which
is exactly what `AlignDevicesHook` does during `device_map` / CPU offload
(`hooks.py`), and `fsdp_utils.py` calls it with `fqns=True` on the live model.
Minimal reproduction:
```python
import torch
from torch import nn
from accelerate.utils.modeling import get_non_persistent_buffers
class Sub(nn.Module):
def __init__(self):
super().__init__()
self.register_buffer("np_buf", torch.rand(4), persistent=False)
class Root(nn.Module):
def __init__(self):
super().__init__()
self.register_buffer("persistent_buf", torch.rand(4))
self.sub = Sub()
m = Root()
assert m._non_persistent_buffers_set == set()
get_non_persistent_buffers(m, recurse=True)
print(m._non_persistent_buffers_set) # {'np_buf'} <-- module was mutated
```
## Fix
Copy the set instead of aliasing it:
```python
non_persistent_buffers_set = set(module._non_persistent_buffers_set)
```
The function now returns a fresh set, leaves the module's private state
untouched, and is idempotent. Every in-repo caller

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]
- [Issue #2848: Implement multi-domain intake architecture and related specs]
- [Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end]
- [Issue #3423: FIX LN Tuning re-initializing new adapters from a previously merged adapter]
