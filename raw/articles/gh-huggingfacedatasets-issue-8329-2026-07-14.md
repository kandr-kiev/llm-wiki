---
source_url: https://github.com/huggingface/datasets/issues/8329
ingested: 2026-07-14
sha256: 8e8d296162deafe1bff224de3cb42b402b9c2a2086654f2b4b82632445085320
blog_source: github:huggingface/datasets
---
# Issue #8329: fix: replace list/List with Sequence in function parameter annotations

**State:** open | **Author:** gautamkishore | **Created:** 2026-07-14T10:16:04Z

Fixes #5354

Replaces `list[T]` with `Sequence[T]` in function parameter type annotations across `arrow_dataset.py`, `dataset_dict.py`, and `iterable_dataset.py`.

The built-in `list` is invariant in its type parameter, so passing a `List[str]` where `list[PathLike]` is expected causes a mypy error.  `Sequence` is covariant and accepts both `list` and its subtypes.

### Changes

- Added `Sequence`/ `Sequence_` import from `collections.abc`
- Replaced `list[...]` with `Sequence[...]` in all function parameter annotations
- Updated corresponding docstring references
- Did **not** change return type annotations or local variable annotations (only parameters that accept input sequences)