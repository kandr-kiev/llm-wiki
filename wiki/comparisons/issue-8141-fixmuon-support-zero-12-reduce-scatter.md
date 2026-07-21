---
title: "Issue #8141: fix(muon): support ZeRO-1/2 reduce scatter"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - data
  - gpu
  - multi-agent
  - open-source
  - parallel
  - standards
  - zero-shot
---

# Issue #8141: fix(muon): support ZeRO-1/2 reduce scatter

> **Source:** gh-microsoftdeepspeed-issue-8141-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/microsoft/DeepSpeed/issues/8141 ingested: 2026-07-14 sha256: f2732f35ebf699a886d6b4154c868ffa605584260219de51e139eedd52eccbfa blog_source: github:microsoft/DeepSpeed...
> **Sources:**
>   - gh-microsoftdeepspeed-issue-8141-2026-07-14.md
> **Links:**
- [[Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`]]
- [[Issue #8333: Support batched=True in Dataset.to_dict]]
- [[Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]]
- [[Issue #3427: FIX grouped Conv2d LoRA rank padding for hotswapping (#3416)]]
- [[Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end]]

## Key Findings

---
source_url: https://github.com/microsoft/DeepSpeed/issues/8141
ingested: 2026-07-14
sha256: f2732f35ebf699a886d6b4154c868ffa605584260219de51e139eedd52eccbfa
blog_source: github:microsoft/DeepSpeed
---
# Issue #8141: fix(muon): support ZeRO-1/2 reduce scatter
**State:** open | **Author:** Micuks | **Created:** 2026-07-14T11:13:05Z
## Problem
#8090 made `Muon + ZeRO-1/2 + reduce_scatter` fail fast because a Muon matrix that crosses a ZeRO partition boundary does not have a fully reduced gradient on any owner rank.
The reduce-scatter path copies each averaged slice only to that slice's owner. Muon, however, runs the nonlinear Newton-Schulz update on the full matrix before `get_flat_partition()` selects the local ZeRO slice. Each owner therefore sees a different matrix: its own reduced slice plus local, unreduced slices owned by other ranks.
## Change
For a Muon parameter that spans more than one ZeRO partition, each reduced slice is copied to every rank that owns part of that parameter. Those ranks then run `muon_update` on the same full reduced gradient, and the existing code keeps only the local ZeRO partition.
Parameters that stay within one partition keep the current owner-only copy path. With the default multi-rank bucket all-reduce, this does not add a collective. When `use_multi_rank_bucket_allreduce=false`, only ranges belonging to split Muon parameters switch to all-reduce. The copy helper still accepts the integer rank form used by ZenFlow.
Optimizer offload remains unsupported because that path keeps only partition-local gradients.
## Tests
The numerical test compares the applied update with `muon_update` on the full data-parallel gradient. The 2-GPU cases cover:
- ZeRO stages 1 and 2
- `gram` and `standard` Newton-Schulz methods on the existing all-reduce path
- reduce-scatter with gradient accumulation and overlap communication
- `use_multi_rank_bucket_allreduce=false`
- extra-large parameters and non-contiguous gradients
- optimizer offload rejection
Focused helper tests cover both the existing integer copy target and the new multi-owner target.
Refs #7807
Alternative to #7878; replaces the fail-fast behavior added by #8090 with a targeted reduction path.

## Summary

See Key Findings for full content.

## Related Articles

- [[Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`]]
- [[Issue #8333: Support batched=True in Dataset.to_dict]]
- [[Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]]
- [[Issue #3427: FIX grouped Conv2d LoRA rank padding for hotswapping (#3416)]]
- [[Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end]]
