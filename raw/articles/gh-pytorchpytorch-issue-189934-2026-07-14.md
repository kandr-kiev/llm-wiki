---
source_url: https://github.com/pytorch/pytorch/issues/189934
ingested: 2026-07-14
sha256: 8eb971fbc12970c54122b3b25c9ce52507bbf30b7307f39b66dbcb55ce2401ea
blog_source: github:pytorch/pytorch
---
# Issue #189934: c10 intrusive_ptr: add [[nodiscard]] to raw::weak_intrusive_ptr helpers

**State:** open | **Author:** r-barnes | **Created:** 2026-07-14T20:02:33Z

Summary:
Annotate the raw pointer helpers in namespace c10::raw::weak_intrusive_ptr:
- lock returns a raw owning strong pointer; discarding it leaks.
- use_count is a pure query.

incref/decref stay unannotated since they are used for effect.

Mirrored across the fbcode and xplat copies of the header.

Test Plan: [[nodiscard]] is enforced at compile time via -Werror; relies on CI to surface external discarding call sites. Local `arc lint` is clean.

Differential Revision: D111955878


