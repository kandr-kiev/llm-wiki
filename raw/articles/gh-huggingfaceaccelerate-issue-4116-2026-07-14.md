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
print(m._non_persistent_buffers_set)  # {'np_buf'}  <-- module was mutated
```

## Fix

Copy the set instead of aliasing it:

```python
non_persistent_buffers_set = set(module._non_persistent_buffers_set)
```

The function now returns a fresh set, leaves the module's private state
untouched, and is idempotent. Every in-repo caller only reads the returned set
(`hooks.py` iterates it, `fsdp_utils.py` and `modeling.py` do membership tests),
so there is no other behavioural change. The docstring already promises to
"gather ... into a set", not to return a live view.

## Testing

Two CPU-only tests added to `tests/test_modeling_utils.py`
(`ModelingUtilsTester`):

- `test_get_non_persistent_buffers_does_not_mutate_module` — asserts the module
  set is left empty across `recurse`/`fqns` variants, that results are
  idempotent (no dot-prefixed accumulation), and that the returned set is a copy.
- `test_named_module_tensors_does_not_corrupt_state_dict` — runs the exact
  `named_module_tensors(recurse=True, remove_non_persistent=True)` call
  `AlignDevicesHook` makes and asserts a colliding persistent buffer survives in
  `state_dict()`.

Both fail on `main` and pass with the fix.

```
$ python -m pytest tests/test_modeling_utils.py -k "non_persistent or state_dict" -q
4 passed, 40 deselected

$ python -m pytest tests/test_modeling_utils.py -q
42 passed, 2 skipped, 12 subtests passed

$ python -m pytest tests/test_hooks.py -q
12 passed, 3 skipped

$ python -m pytest tests/test_big_modeling.py -q -k offload
6 passed, 4 skipped, 24 deselected

$ make quality
All checks passed!
```

(`tests/test_modeling_utils.py` runs under its own CI shard rather than
`make test_core`, so I've cited the direct pytest command above.)

## Note for reviewers

There is a pre-existing quirk this minimal fix intentionally leaves alone: with
`fqns=True` and a non-persistent buffer registered *directly on the root*,
`named_modules()` yields the root as `n=""`, so line 484 produces a spurious
`"." + b` entry alongside the correct one. It's harmless to the only `fqns`
caller (`fsdp_utils.py`, membership tests — the correct name is also present),
but I kept this PR to the one-line data-corruption fix. Happy to fold in the
trivial `n + "." + b if n else b` guard here or as a follow-up if you'd prefer.

## Before submitting

- [x] Did you read the [contributor guideline](https://github.com/huggingface/accelerate/blob/main/CONTRIBUTING.md#submitting-a-pull-request-pr)?
- [x] Did you write any new necessary tests?

## Who can review?

@SunMarc (big modeling / owns hooks and modeling utils)
