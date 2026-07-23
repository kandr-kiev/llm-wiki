---
title: "Issue #8139: [DeepCompile] Add lightweight pass contracts for optimization passes"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - backend
  - efficiency
  - open-source
  - optimization
  - real-time
---

# Issue #8139: [DeepCompile] Add lightweight pass contracts for optimization passes

> **Source:** gh-microsoftdeepspeed-issue-8139-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/microsoft/DeepSpeed/issues/8139 ingested: 2026-07-14 sha256: 06931e7c4709f1051d00874bc7ec259615c06a6ca23972fb224c4d89b603a43e blog_source: github:microsoft/DeepSpeed...
> **Sources:**
>   - gh-microsoftdeepspeed-issue-8139-2026-07-14.md
> **Links:**
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [Issue #2797: feat: add progress_callback parameter to transcribe()]
- [Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`]
- [Issue #6383: Return HTTP 400 with diagnostic detail for get_sequence_logprobs errors]
- [Issue #8330: Dataset Studio and Viewer down]

## Key Findings

---
source_url: https://github.com/microsoft/DeepSpeed/issues/8139
ingested: 2026-07-14
sha256: 06931e7c4709f1051d00874bc7ec259615c06a6ca23972fb224c4d89b603a43e
blog_source: github:microsoft/DeepSpeed
---
# Issue #8139: [DeepCompile] Add lightweight pass contracts for optimization passes
**State:** open | **Author:** jahnavi-yelamanchi | **Created:** 2026-07-14T00:44:04Z
### Summary
Based on the DeepCompile efficiency and robustness track in the Q3 2026 roadmap #8104 , this PR implements: _Formal pass contracts and validation of optimization passes: Add lightweight optimization pass contracts for automatic compatibility validation and ordering_
### Motivation
DeepCompile passes execute in the order given by the schedule (`init_schedule`, `backend.py`), with no validation of that order. Inter-pass dependencies are implicit: `prefetch` and `selective_gather` rewrite the all-gather/release ops inserted by `zero3_compile` and require it to run first (cf. the default schedule in `init_z3.py`). An invalid order currently surfaces as a downstream failure rather than a diagnostic at schedule time.
### Changes
- `deepspeed/compile/passes/contract.py`: `PassContract` dataclass (`provides` / `requires` / `conflicts_with` / `phase`), a contract registry, and `validate_schedule()`, which raises `PassContractError` on the first unmet requirement or conflict. No torch dependency.
- Contracts declared for the four built-in passes: `zero3_compile` provides `z3_gather_release`; `prefetch` and `selective_gather` require it.
- `register_compile_pass(name, fn, contract=None)`: optional `contract` argument, backward compatible.
- `validate_schedule()` invoked on user-supplied schedules in the compile path (`engine.py`).
### Design
- Passes without a contract are unconstrained; existing and custom passes are unaffected. Internal default schedules are not validated, only user-supplied ones.
- Dependencies are expressed as capability tags (`z3_gather_release`) rather than pass names, so passes can be added or swapped without editing dependents.
- Conflicts are symmetric: either pass may declare the incompatibility, and both orderings are rejected.
- Scope is limited to metadata and validation, not dependency resolution or automatic reordering.
### Testing
- `tests/unit/compile/test_pass_contract.py`: unit tests for valid ordering, missing requirements, same-step providers, symmetric conflicts, uncontracted-pass pass-through, and callable resolution.

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [Issue #2797: feat: add progress_callback parameter to transcribe()]
- [Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`]
- [Issue #6383: Return HTTP 400 with diagnostic detail for get_sequence_logprobs errors]
- [Issue #8330: Dataset Studio and Viewer down]
