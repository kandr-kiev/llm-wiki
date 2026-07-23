---
title: "Issue #189938: Gate nccl2 backend NCCL code behind USE_C10D_NCCL"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - backend
  - batch
  - cuda
  - distributed
  - open-source
  - pytorch
  - system-design
  - use-case
---

# Issue #189938: Gate nccl2 backend NCCL code behind USE_C10D_NCCL

> **Source:** gh-pytorchpytorch-issue-189938-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/pytorch/pytorch/issues/189938 ingested: 2026-07-14 sha256: 4cdb7bc7ae41f3e291bdaf924592f2e59285f40ba6003198695794673f83d8e8 blog_source: github:pytorch/pytorch --- #...
> **Sources:**
>   - gh-pytorchpytorch-issue-189938-2026-07-14.md
> **Links:**
- [[Issue #189937: [lint] Bump remaining shim-linter git timeouts to 60s]]
- [Issue #6385: AsyncGRPO fork-independent epoch counting]
- [Issue #8330: Dataset Studio and Viewer down]
- [Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer]
- [Issue #8332: Raise on length mismatch in batched IterableDataset.map]

## Key Findings

---
source_url: https://github.com/pytorch/pytorch/issues/189938
ingested: 2026-07-14
sha256: 4cdb7bc7ae41f3e291bdaf924592f2e59285f40ba6003198695794673f83d8e8
blog_source: github:pytorch/pytorch
---
# Issue #189938: Gate nccl2 backend NCCL code behind USE_C10D_NCCL
**State:** open | **Author:** d4l3k | **Created:** 2026-07-14T20:19:25Z
Stack from [ghstack](https://github.com/ezyang/ghstack/tree/0.15.0) (oldest at bottom):
* __->__ #189938
The in-tree nccl2 c10d backend (torch/csrc/distributed/c10d/nccl2/) is added to torch_cuda whenever CUDA and distributed are enabled, independent of whether NCCL is available. Most of its files were already wrapped in #ifdef USE_C10D_NCCL, but NcclApi, NCCLBootstrap, ProcessGroupNCCL.cpp, ProcessGroupNCCLUtils.cpp and WorkNCCLQueue.cpp were not. Those files #include (or reference the USE_C10D_NCCL-guarded WorkNCCL class), so a non-NCCL-compliant backend such as libtorch_mtia_simt -- which defines no USE_C10D_NCCL and has no nccl.h on its include path -- fails to compile:
torch/csrc/distributed/c10d/nccl2/ProcessGroupNCCLUtils.cpp:5:10: fatal error: 'nccl.h' file not found
This wraps the remaining NCCL-dependent nccl2 files in #ifdef USE_C10D_NCCL / #endif, matching the guard the sibling files already use, so they reduce to empty translation units when NCCL is not built. The NCCL-free helpers (CudaApi, StoreManager, TracingGuard, Utils, Batch, Logging) are intentionally left untouched: they have no nccl.h dependency, compile standalone, and are only ever included from within already-guarded regions.
Gating is done at the source level with #ifdef rather than by excluding the sources in the build system, so a single set of guards covers both the OSS CMake build and the internal buck build without duplicating conditional source lists.
Test Plan:
With USE_C10D_NCCL defined (normal CUDA build), the affected translation units still compile:
```
ninja \
caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/distributed/c10d/nccl2/NcclApi.cpp.o \
caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/distributed/c10d/nccl2/NCCLBootstrap.cpp.o \
caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/distributed/c10d/nccl2/ProcessGroupNCCL.cpp.o \
caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/distributed/c10d/nccl2/ProcessGroupNCCLUtils.cpp.o \
caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/distributed/c10d/nccl2/WorkNCCLQueue.cpp.o
```
With USE_C10D_NCCL undefined, each guarded file preprocesses to an empty translation unit, so is no longer reached and the backend compiles out cleanly for non-NCCL backends (e.g. libtorch_mtia_simt).
lintrunner on the changed files reports no issues.

## Summary

See Key Findings for full content.

## Related Articles

- [[Issue #189937: [lint] Bump remaining shim-linter git timeouts to 60s]]
- [Issue #6385: AsyncGRPO fork-independent epoch counting]
- [Issue #8330: Dataset Studio and Viewer down]
- [Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer]
- [Issue #8332: Raise on length mismatch in batched IterableDataset.map]
