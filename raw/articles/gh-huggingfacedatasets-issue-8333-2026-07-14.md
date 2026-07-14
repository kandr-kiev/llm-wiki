---
source_url: https://github.com/huggingface/datasets/issues/8333
ingested: 2026-07-14
sha256: 01b80a5d98fa8248532b8b93644823a69fe80e98078a80dd78d40553b79ee012
blog_source: github:huggingface/datasets
---
# Issue #8333: Support batched=True in Dataset.to_dict

**State:** open | **Author:** vineethsaivs | **Created:** 2026-07-14T16:03:25Z

## What does this do?

`Dataset.to_dict(batch_size=..., batched=True)` silently ignores both arguments and always returns the full dict, even though its signature, docstring ("Set to `True` to return a generator that yields the dataset as batches"), and `-> Union[dict, Iterator[dict]]` return type all promise batching. The sibling methods `to_pandas` and `to_polars` implement batching; `to_dict` was missing the branch.

Because it returns a plain `dict` instead of the promised generator, iterating the result as documented walks the dict *keys* and raises:

```python
from datasets import Dataset
ds = Dataset.from_dict({"a": list(range(10))})
out = ds.to_dict(batched=True, batch_size=3)
type(out)                 # dict, not a generator
for batch in out:
    batch["a"]            # TypeError: string indices must be integers, not 'str'
```

## Fix

Mirror the `to_pandas`/`to_polars` structure: return the full dict when `batched=False`, otherwise return a generator that yields `batch_size`-row slices (defaulting `batch_size` to `config.DEFAULT_MAX_BATCH_SIZE`). A small local closure keeps the per-batch JSON-field decoding from being duplicated across the two branches.

After the fix:

```python
[len(b["a"]) for b in ds.to_dict(batched=True, batch_size=3)]   # [3, 3, 3, 1]
```

Backward compatible: `batched` defaults to `False`, so every existing `.to_dict()` call still returns a plain dict (verified byte-identical). Index mapping (`select(...)`) and `Json()`-feature decoding both work in batched and non-batched modes.

## Test

Added a "Batched" block to `tests/test_arrow_dataset.py::test_to_dict`, mirroring the existing `test_to_pandas`/`test_to_polars` coverage: it asserts each yielded batch is a `dict` with the right columns and no more than `batch_size` rows. It fails before this change (the returned dict is iterated as keys) and passes after.
