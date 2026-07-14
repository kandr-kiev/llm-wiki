---
source_url: https://github.com/huggingface/peft/issues/3425
ingested: 2026-07-14
sha256: d839bfd32dadadb6e50cb07330504eacb1a4fe16479699ecfa673d1410300a64
blog_source: github:huggingface/peft
---
# Issue #3425: FIX Accept layers_to_transform=0 together with layers_pattern

**State:** open | **Author:** winklemad | **Created:** 2026-07-11T19:51:25Z

No linked issue — found by reading the code.

### What this fixes

Every tuner config validates the `layers_pattern` / `layers_to_transform` pairing in `__post_init__` with:

```python
if self.layers_pattern and not self.layers_to_transform:
    raise ValueError("When `layers_pattern` is specified, `layers_to_transform` must also be specified.")
```

Because `0` is falsy, passing the **valid first-layer index** `layers_to_transform=0` together with a `layers_pattern` wrongly raises — even though `layers_to_transform` *was* specified:

```python
from peft import LoraConfig

LoraConfig(target_modules=["q_proj"], layers_to_transform=0, layers_pattern="blocks")
# ValueError: When `layers_pattern` is specified, `layers_to_transform` must also be specified.

LoraConfig(target_modules=["q_proj"], layers_to_transform=1,  layers_pattern="blocks")  # OK
LoraConfig(target_modules=["q_proj"], layers_to_transform=[0], layers_pattern="blocks")  # OK
```

Only index `0` is affected — `1` and `[0]` (the same logical request) are accepted.

### Why `is None` is the correct check

- The consuming matcher already treats `0` as a valid index — `check_target_module_exists` in `src/peft/tuners/tuners_utils.py` gates on `layer_indexes is not None`, and the sibling check a few lines above in the same `__post_init__` also uses `self.layers_to_transform is not None`.
- The docstring states the pattern is *"used only if `layers_to_transform` is different from `None`."*

So the guard should compare against `None`, not truthiness. The check was added in #2159 and its message improved in #2169, but the falsy-`0` case remained.

### Scope

The identical guard is duplicated across **all 19 tuner configs** that support layer indexing (lora, adalora, boft, deft, delora, fourierft, frod, hra, lily, loha, lokr, oft, peanut, psoft, pvera, tinylora, vblora, vera, waveft), so the one-line fix is applied to every one.

### Testing

Added `test_config_layers_to_transform_index_zero`, parametrized over every config in `ALL_CONFIG_CLASSES` that supports `layers_to_transform` (25 configs), asserting `layers_to_transform=0` + `layers_pattern` is accepted. It fails before this change (19 of the configs raise) and passes after. `ruff check` / `ruff format --check` are clean and `tests/test_config.py` passes (1218 passed).