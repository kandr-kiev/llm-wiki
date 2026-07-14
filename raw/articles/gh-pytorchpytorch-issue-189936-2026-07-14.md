---
source_url: https://github.com/pytorch/pytorch/issues/189936
ingested: 2026-07-14
sha256: afe48822b9ab19eee200d1735b13985fcfcf7d5dfc89f1e0224ff89e22a80a62
blog_source: github:pytorch/pytorch
---
# Issue #189936: c10 IntrusiveList: add [[nodiscard]] to observer methods

**State:** open | **Author:** r-barnes | **Created:** 2026-07-14T20:02:34Z

Summary:
Annotate the pure-query methods of IntrusiveListHook (is_linked), ListIterator (operator==, operator!=, operator*, operator->) and IntrusiveList (begin/end, rbegin/rend, iterator_to, size, empty). insert() keeps no annotation since discarding its returned iterator is a common and valid use of its linking side effect.

Mirrored across the fbcode and xplat copies of the header.

Test Plan: [[nodiscard]] is enforced at compile time via -Werror; relies on CI to surface external discarding call sites. Local `arc lint` is clean.

Differential Revision: D111955863


