---
title: "Issue #2196: Upgrade hf-hub to 1.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - open-source
---

# Issue #2196: Upgrade hf-hub to 1.0

> **Source:** gh-huggingfacetokenizers-issue-2196-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/tokenizers/issues/2196 ingested: 2026-07-14 sha256: ca2b5d28426fe962be125cf94826954e522b01e6f675657de92fc5b27bbdbc0c blog_source: github:huggingface/toke...
> **Sources:**
>   - gh-huggingfacetokenizers-issue-2196-2026-07-14.md
> **Links:**
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [[release-v180]]
- [Issue #14188: [Quantization] Fix ModelOpt pre-quantized loading](https://github.com/pytorch/pytorch/issues/14188)
- [Issue #2460: Bump the actions group across 1 directory with 4 updates]
- [Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`]

## Key Findings

---
source_url: https://github.com/huggingface/tokenizers/issues/2196
ingested: 2026-07-14
sha256: ca2b5d28426fe962be125cf94826954e522b01e6f675657de92fc5b27bbdbc0c
blog_source: github:huggingface/tokenizers
---
# Issue #2196: Upgrade hf-hub to 1.0
**State:** open | **Author:** assafvayner | **Created:** 2026-07-14T01:08:55Z
Upgrades the `hf-hub` dependency from 0.4 to 1.0 and migrates `from_pretrained` to the new API: the `ureq` feature is replaced by `blocking`, and the old `ApiBuilder`/`Repo` flow is replaced with `HFClientSync` + the `download_file` builder. Behavior is unchanged (env token/endpoint fallback, bare identifiers, and revisions all work as before); verified with `cargo test --features http --test from_pretrained` against the live Hub. cc @mcpotato

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #14166: Fix Hub download filtering f[Issue #14188: [Quantization] Fix ModelOpt pre-quantized loading](https://github.com/pytorch/pytorch/issues/14188)ntization] Fix ModelOpt pre-quantized loading]]
- [Issue #2460: Bump the actions group across 1 directory with 4 updates]
- [Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`]
