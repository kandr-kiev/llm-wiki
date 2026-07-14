---
source_url: https://github.com/pytorch/pytorch/issues/189935
ingested: 2026-07-14
sha256: e55476a7fed1ac2e92055912456166b636bd55d4827fce53cfb4031c0d2bcbcb
blog_source: github:pytorch/pytorch
---
# Issue #189935: c10 Bitset: add [[nodiscard]] to query methods

**State:** open | **Author:** r-barnes | **Created:** 2026-07-14T20:02:33Z

Summary:
Annotate the pure-query methods of c10::utils::bitset: NUM_BITS, get, is_entirely_unset, and the operator==/operator!= comparisons. Mutators (set, unset) and the functor-invoking for_each_set_bit are left untouched.

Mirrored across the fbcode and xplat copies of the header.

Test Plan: [[nodiscard]] is enforced at compile time via -Werror; relies on CI to surface external discarding call sites. Local `arc lint` is clean.

Differential Revision: D111955862


