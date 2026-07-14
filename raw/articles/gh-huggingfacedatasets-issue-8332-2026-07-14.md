---
source_url: https://github.com/huggingface/datasets/issues/8332
ingested: 2026-07-14
sha256: b6126570bdbd359c21c808f6ad47ab1e76b31c260930bc71c4dbad07251398b3
blog_source: github:huggingface/datasets
---
# Issue #8332: Raise on length mismatch in batched IterableDataset.map

**State:** open | **Author:** sohumt123 | **Created:** 2026-07-14T14:44:36Z

## Problem

`IterableDataset.map(fn, batched=True)` can silently drop or misalign rows when the mapping function changes the batch's row count but does not re-emit every retained input column.

In `MappedExamplesIterable._iter`, `prepare_outputs` merges the batch with `transformed_inputs = {**inputs, **processed_inputs}` without checking that the retained original input columns have the same length as the processed output. `validate_function_output` only checks length consistency *within* `processed_inputs`, never against the untouched input columns. `_batch_to_examples` then derives the row count from whichever column is first in insertion order (usually a retained input column at `batch_size` length).

The result depends on which column ends up first:

```python
from datasets import Dataset, IterableDataset

data = [{"a": i, "b": i} for i in range(6)]

# (a) shrink: returns only "a" (3 rows) but keeps "b" (6 rows)
ds = IterableDataset.from_generator(lambda: iter(data)).map(
    lambda b: {"a": [x for x in b["a"] if x >= 3]}, batched=True, batch_size=6
)
print(list(ds))
# [{'a': 3, 'b': 0}, {'a': 4, 'b': 1}, {'a': 5, 'b': 2}]
# -> 3 rows silently lost, stale "b" zipped positionally, no warning

# (b) expand / (c) new shorter column -> bare "IndexError: list index out of range"
```

The eager `Dataset.map` raises a clear error on the identical input:

```
pyarrow.lib.ArrowInvalid: Column 1 named b expected length 3 but got length 6
```

So the streaming path silently diverges from the eager API it explicitly intends to mimic (the `# this logic mimics the one in Dataset.map` comment right above the merge).

## Fix

In `prepare_outputs`, after the `remove_columns` deletion and before the merge, validate for batched maps that every retained input column (a key in `inputs` not overwritten by `processed_inputs`) matches the processed output length. If not, raise a `ValueError` reusing the existing `"Column lengths mismatch"` wording from `validate_function_output`, plus a hint.

The check is placed **after** the `remove_columns` block on purpose: a legitimate and already-tested pattern returns a new column at a length different from the batch while removing all input columns via `remove_columns` (see `test_mapped_examples_iterable_remove_columns`), which must keep working.

All legitimate length-changing patterns are preserved: returning every column at a new consistent length (grow/shrink), same-length overwrite of an existing column, and adding a new column at batch length. `FilteredExamplesIterable` inherits this path; correct batched filters return only the mask column at batch length and are unaffected, while a wrong-length mask now raises instead of silently misfiltering. Both the sync and async map paths funnel through `prepare_outputs`, so one change covers both.

### Behavior change

Pipelines that today silently produce misaligned/truncated rows will now raise `ValueError` — matching what eager `Dataset.map` already does with `ArrowInvalid` on the same input.

## Testing

Added to `tests/test_iterable_dataset.py`, next to the existing eager-vs-streaming parity test:

- `test_iterable_dataset_map_batched_shrink_without_all_columns_raises` — the shrink case must raise (and asserts eager `Dataset.map` raises `ArrowInvalid` on the same input).
- `test_iterable_dataset_map_batched_expand_without_all_columns_raises` — the expand case must raise `ValueError` instead of a bare `IndexError`.
- `test_iterable_dataset_map_batched_new_shorter_column_raises` — new-shorter-column must raise `ValueError` instead of a bare `IndexError`.
- `test_iterable_dataset_map_batched_length_change_valid_patterns` — regression guard for the five legitimate patterns.

```
python -m pytest tests/test_iterable_dataset.py -k map -q     # 119 passed
python -m pytest tests/test_iterable_dataset.py -k filter -q  # 18 passed, 4 skipped
python -m pytest tests/test_iterable_dataset.py -q            # 454 passed, 31 skipped
python -m pytest tests/test_arrow_dataset.py -k map -q        # 54 passed, 6 skipped (eager path untouched)
make quality                                                 # ruff check + format --check pass
```
