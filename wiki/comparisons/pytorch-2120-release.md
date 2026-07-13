---
title: "PyTorch 2.12.0 Release"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - backend
  - cuda
  - data
  - distributed
  - foundation-model
  - frontend
  - multi-agent
  - open-source
  - performance
  - prompt-engineering
  - pytorch
  - quantization
  - real-time
  - security
  - training
  - use-case
---
# PyTorch 2.12.0 Release

> **Source:** pytorch-2120-release-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/pytorch/pytorch/releases/tag/v2.12.0 ingested: 2026-07-10 sha256: 245c56da070730cfaa6e2174c3ff764405d6eb6d54731c09abfab44d4f87dc84 blog_source: github --- # PyTorch...
> **Sources:**
>   - pytorch-2120-release-2026-07-10.md
> **Links:**
- [[train-large-neural-networks]]
- [[pytorch-2110-release]]
- [[llm-quantization-gguf-gptq-awq]]
- [[release-v1140]]
- [[pytorch-2100-release]]

## Key Findings

---
source_url: https://github.com/pytorch/pytorch/releases/tag/v2.12.0
ingested: 2026-07-10
sha256: 245c56da070730cfaa6e2174c3ff764405d6eb6d54731c09abfab44d4f87dc84
blog_source: github
---
# PyTorch 2.12.0 Release
## Release Notes
# PyTorch 2.12.0 Release Notes
- [Highlights](#highlights)
- [Backwards Incompatible Changes](#backwards-incompatible-changes)
- [Deprecations](#deprecations)
- [New Features](#new-features)
- [Improvements](#improvements)
- [Bug fixes](#bug-fixes)
- [Performance](#performance)
- [Documentation](#documentation)
- [Developers](#developers)
- [Security](#security)
# Highlights
**Batched linalg.eigh on CUDA** is up to 100x faster due to updated cuSolver backend selection.
New **torch.accelerator.Graph** API unifies graph capture and replay across CUDA, XPU, and out-of-tree backends.
**torch.export.save** now supports Microscaling (MX) quantization formats, enabling full export of aggressively compressed models.
**Adagrad** now supports `fused=True`, joining Adam, AdamW, and SGD with a single-kernel optimizer implementation.
**torch.cond** control flow can now be captured and replayed inside CUDA Graphs.
**ROCm** users gain expandable memory segments, rocSHMEM symmetric memory collectives, and FlexAttention pipelining.
For more details about these highlighted features, you can look at the release blogpost. Below are the full release notes for this release.
# Backwards Incompatible Changes
## Build Frontend
- Strengthened SVE compile checks in `FindARM.cmake`, which may reject previously accepted but incorrect SVE configurations ([#176646](https://github.com/pytorch/pytorch/pull/176646))
Source builds that enable SVE now validate the compiler configuration more strictly. If a build previously passed with an incomplete or mismatched SVE setup, it may now fail during CMake configuration instead of later in compilation. Update the compiler/toolchain flags so they accurately describe the target SVE support, or disable SVE for that build.
- Updated the minimum CUDA version required to build PyTorch from source to CUDA 12.6 ([#178925](https://github.com/pytorch/pytorch/pull/178925))
Building PyTorch from source with CUDA versions older than 12.6 is no longer supported. Users building custom binaries should install CUDA 12.6 or newer and make sure `CUDA_HOME` points to that installation.
Version 2.11:
```bash
CUDA_HOME=/usr/local/cuda-12.4 python setup.py develop
```
Version 2.12:
```bash
CUDA_HOME=/usr/local/cuda-12.6 python setup.py develop
```
- Enforced a C++20 minimum in CMake build files ([#178662](https://github.com/pytorch/pytorch/pull/178662))
Source builds now require a compiler and build configuration that support C++20. If you maintain custom build scripts or downstream extensions that build PyTorch from source, update the compiler and remove assumptions that PyTorch can be built as C++17.
## Distributed
- `torch.distributed.nn.functional` ops now raise `RuntimeError` under `torch.compile` ([#177342](https://github.com

## Summary

/pytorch/pytorch/pull/177342))
All ops in `torch.distributed.nn.functional` (e.g., `broadcast`, `all_reduce`, `all_gather`, `reduce_scatter`, `all_to_all_single`) now raise `RuntimeError` when called inside `torch.compile`. Users should migrate to the functional collectives API in `torch.distributed._functional_collectives`.
Version 2.11:
```python
@torch.compile
def my_func(x):
return torch.distributed.nn.functional.all_reduce(x, op=ReduceOp.SUM)
```
Version 2.12:
```python
@torch.compile
def my_func(x):
return torch.distributed._functional_collectives.all_reduce(x, reduceOp="sum", group=group)
```
## TorchElastic
- `torchrun` now defaults to an OS-assigned free port for single-node training instead of port 29500 ([#175699](https://github.com/pytorch/pytorch/pull/175699))
When running `torchrun --nproc-per-node=N script.py` without specifying `--master-port` or `--standalone`, the default behavior now automatically uses an OS-assigned free port via the `c10d` rendezvous backend. This eliminates "Address already in use" errors when running multiple training jobs concurrently. Multi-node training, explicit `--master-port`, `PET_MASTER_PORT` env var, and `--standalone` are unchanged.
Version 2.11:
```bash
# Used static rendezvous on port 29500 by default
torchrun --nproc-per-node=4 train.py
```
Version 2.12:
```bash
# Uses OS-assigned free port by default
torchrun --nproc-per-node=4 train.py
# To explicitly use a fixed port:
torchrun --nproc-per-node=4 --master-port=29500 train.py
```
## MPS
- All MPS tensors are now allocated in unified memory ([#175818](https://github.com/pytorch/pytorch/pull/175818))
Previously, MPS tensors could be allocated in either device-only or unified memory. Now all MPS tensors use unified memory unconditionally. This simplifies memory management and enables CPU access to MPS tensor data without explicit copies. Code that relied on device-only memory placement may observe different performance characteristics.
## Inductor
- The `max_autotune` layout-constraint deferral introduced in 2.11 is now opt-in ([#175330](https://github.com/pytorch/pytorch/pull/175330))
In 2.11, Inductor deferred layout freezing for `max_autotune` templates to expose more fusion opportunities. This caused a regional-inductor failure mode, so the default in 2.12 reverts to immediate layout freezing. Users who relied on the deferred behavior for fusion opportunities should opt in explicitly via `torch._inductor.config.max_autotune_defer_layout_freezing` or `TORCHINDUCTOR_MAX_AUTOTUNE_DEFER_LAYOUT_FREEZING=1`.
Version 2.11:
```python
# Deferred layout freezing was the default
torch.compile(model, mode="max-autotune")
```
Version 2.12:
```python
import torch._inductor.config as cfg
cfg.max_autotune_defer_layout_freezing = True
# or set TORCHINDUCTOR_MAX_AUTOTUNE_DEFER_LAYOUT_FREEZING=1
torch.compile(model, mode="max-autotune")
```
# Deprecations
## Release Engineering
- Deprecate CUDA 12.8 builds in favor of CUDA 13.0 ([#179072](https://github.com/pyt

## Related Articles

- [[train-large-neural-networks]]
- [[pytorch-2110-release]]
- [[llm-quantization-gguf-gptq-awq]]
- [[release-v1140]]
- [[pytorch-2100-release]]
