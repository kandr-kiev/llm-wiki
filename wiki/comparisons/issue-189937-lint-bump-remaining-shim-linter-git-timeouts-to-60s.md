---
title: "Issue #189937: [lint] Bump remaining shim-linter git timeouts to 60s"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ci-cd
  - claude
  - open-source
  - pytorch
---

# Issue #189937: [lint] Bump remaining shim-linter git timeouts to 60s

> **Source:** gh-pytorchpytorch-issue-189937-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/pytorch/pytorch/issues/189937 ingested: 2026-07-14 sha256: 329de4ecd2c69b1f626aecb77adfe2cb7904850a866a10720de8487d77107524 blog_source: github:pytorch/pytorch --- #...
> **Sources:**
>   - gh-pytorchpytorch-issue-189937-2026-07-14.md
> **Links:**
- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]
- [[Issue #2450: Fix #2407: Fix get_wikitext2 tokenization bug causing sequence length warning]]
- [[Issue #6385: AsyncGRPO fork-independent epoch counting]]
- [[Issue #8138: Add governance process page to deepspeed.ai]]
- [[Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse]]

## Key Findings

---
source_url: https://github.com/pytorch/pytorch/issues/189937
ingested: 2026-07-14
sha256: 329de4ecd2c69b1f626aecb77adfe2cb7904850a866a10720de8487d77107524
blog_source: github:pytorch/pytorch
---
# Issue #189937: [lint] Bump remaining shim-linter git timeouts to 60s
**State:** open | **Author:** frgossen | **Created:** 2026-07-14T20:14:39Z
Stack from [ghstack](https://github.com/ezyang/ghstack/tree/0.15.0) (oldest at bottom):
* __->__ #189937
#189444 bumped the git cat-file timeout in merge_base_with_main but left four
sibling git calls in the shim linters at timeout=5: the git diff calls in
stable_shim_version_linter.get_added_lines, the git show in
generated_shims_version_linter._read_at_merge_base, and the git merge-base in
_stable_shim_utils. On a partial-clone CI checkout these lazily fetch blobs from
the remote and intermittently exceed 5s, crashing the STABLE_SHIM_VERSION and
GENERATED_SHIMS_VERSION linters with TimeoutExpired. Bump them all to 60s to
match the calls #189444 already fixed.
Test Plan: Ran lintrunner on the three adapters locally; the STABLE_SHIM_VERSION
and GENERATED_SHIMS_VERSION linters pass. The flake is a CI-only partial-clone
network timeout that cannot be reproduced deterministically locally.
Authored with Claude.

## Summary

See Key Findings for full content.

## Related Articles

- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]
- [[Issue #2450: Fix #2407: Fix get_wikitext2 tokenization bug causing sequence length warning]]
- [[Issue #6385: AsyncGRPO fork-independent epoch counting]]
- [[Issue #8138: Add governance process page to deepspeed.ai]]
- [[Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse]]
