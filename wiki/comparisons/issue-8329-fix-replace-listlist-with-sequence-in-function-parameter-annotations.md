---
title: "Issue #8329: fix: replace list/List with Sequence in function parameter annotations"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - open-source
---

# Issue #8329: fix: replace list/List with Sequence in function parameter annotations

> **Source:** gh-huggingfacedatasets-issue-8329-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/datasets/issues/8329 ingested: 2026-07-14 sha256: 8e8d296162deafe1bff224de3cb42b402b9c2a2086654f2b4b82632445085320 blog_source: github:huggingface/datase...
> **Sources:**
>   - gh-huggingfacedatasets-issue-8329-2026-07-14.md
> **Links:**
- [[Issue #3420: Fix hotswapping for LoRA adapters targeting grouped Conv2d]]
- [[Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]]
- [[Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]]
- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]
- [[Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters]]

## Key Findings

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
The built-in `list` is invariant in its type parameter, so passing a `List[str]` where `list[PathLike]` is expected causes a mypy error. `Sequence` is covariant and accepts both `list` and its subtypes.
### Changes
- Added `Sequence`/ `Sequence_` import from `collections.abc`
- Replaced `list[...]` with `Sequence[...]` in all function parameter annotations
- Updated corresponding docstring references
- Did **not** change return type annotations or local variable annotations (only parameters that accept input sequences)

## Summary

See Key Findings for full content.

## Related Articles

- [[Issue #3420: Fix hotswapping for LoRA adapters targeting grouped Conv2d]]
- [[Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]]
- [[Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]]
- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]
- [[Issue #3422: FIX TinyLoRA weight_tying corruption when adding overlapping adapters]]
