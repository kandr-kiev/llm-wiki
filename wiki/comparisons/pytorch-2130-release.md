---
title: "PyTorch 2.13.0 Release"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - backend
  - ci-cd
  - cost
  - cuda
  - data
  - distributed
  - fine-tuning
  - foundation-model
  - gpu
  - image-generation
  - library
  - nlp
  - open-source
  - performance
  - pytorch
  - real-time
  - standards
  - system-design
  - training
  - use-case
  - zero-shot
---
# PyTorch 2.13.0 Release

> **Source:** pytorch-2130-release-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/pytorch/pytorch/releases/tag/v2.13.0 ingested: 2026-07-10 sha256: da51305a24d068e2730082e813ea6904f1cfc4320597547058dbd2356f1e4a13 blog_source: github --- # PyTorch...
> **Sources:**
>   - pytorch-2130-release-2026-07-10.md
> **Links:**
- [[train-large-neural-networks]]
- [[llm-quantization-gguf-gptq-awq]]
- [[how-to-deploy-with-vllm]]
- [[release-v180]]
- [[release-v1140]]

## Key Findings

---
source_url: https://github.com/pytorch/pytorch/releases/tag/v2.13.0
ingested: 2026-07-10
sha256: da51305a24d068e2730082e813ea6904f1cfc4320597547058dbd2356f1e4a13
blog_source: github
---
# PyTorch 2.13.0 Release
## Release Notes
# PyTorch 2.13.0 Release Notes
- [Highlights](#highlights)
- [Backwards Incompatible Changes](#backwards-incompatible-changes)
- [Deprecations](#deprecations)
- [New Features](#new-features)
- [Improvements](#improvements)
- [Bug fixes](#bug-fixes)
- [Performance](#performance)
- [Documentation](#documentation)
- [Developers](#developers)
# Highlights
**FlexAttention** lands on Apple Silicon (MPS), with up to ~12x speedup over SDPA on sparse patterns, and gains a deterministic backward path on CUDA for reproducible gradient computation.
**CuTeDSL "Native DSL" backend** gives Inductor a second high-performance code path (alongside Triton) for key GPU operations, with faster compilation. [Prototype]
**`nn.LinearCrossEntropyLoss`** combines the final prediction and loss computation to cut peak GPU memory by up to 4x for large-vocabulary language model training.
**torchcomms**, a new communications backend for PyTorch Distributed, improves fault tolerance, scalability, and debuggability for large-cluster training.
**FSDP2** now overlaps reduce-scatter and all-gather communications via a dedicated process group (opt-in), increasing distributed training throughput.
**Python 3.15 wheel support** for PyTorch on Linux via the pytorch repository index, including builds compatible with free-threaded 3.15t.
**Broader platform support**: ROCm gains AOTriton 0.12b with native HIP CMake, Arm adds Armv9-A `torch.compile` targeting, and Intel XPU exposes new device telemetry APIs.
For more details about these highlighted features, you can look at the release blogpost. Below are the full release notes for this release.
# Tracked Regressions
### ROCm wheels break `torch.compile` on CPU in environments without a GPU
Running a `torch==2.13.0+rocm7.2` wheel in an environment where no GPU is available (`torch.cuda.is_available()` is `False`) breaks `torch.compile` on the CPU path: the first compile raises `RuntimeError: Can't detect vectorized ISA for CPU` ([#189194](https://github.com/pytorch/pytorch/issues/189194)). This is a regression from `torch==2.12.1+rocm7.2`, which compiles CPU code fine (detecting e.g. `VecAVX2`) in the same setup. The 2.13 ROCm wheel appears to rely on something present in the ROCm builder image to detect the CPU vectorized ISA, so it works when run on a ROCm image but fails on a plain CPU-only image.
Workaround: run the `+rocm` wheel on a ROCm image, or install a standard CPU/CUDA build for GPU-less environments.
# Backwards Incompatible Changes
- Stop building CPython 3.13t (free-threaded) binaries (#182951)
Upstream `pypa/manylinux` removed CPython 3.13t (free-threaded) on 2026-05-07, because 3.13t
was experimental and has been superseded by the now-non-experimental CPython 3.14t. As a result,
PyTorch 2.13 no l

## Summary

onger ships `cp313t` wheels (Linux, Triton, and related artifacts). Users on the
free-threaded interpreter should move to Python 3.14t.
PyTorch 2.12:
```bash
# cp313t (free-threaded 3.13) wheels were available
python3.13t -m pip install torch
```
PyTorch 2.13:
```bash
# Use free-threaded Python 3.14t instead
python3.14t -m pip install torch
```
- Bare `PyObject` is no longer allowed in operator schemas (#184209)
Bare `PyObject` was accidentally accepted in operator schema strings in
PyTorch 2.12. This was undocumented and is now rejected, since `torch.compile`
does not support arbitrary `PyObject` inputs to custom ops. If
you parse or register a schema with a bare `PyObject` argument or return type,
you will now get a schema parse error.
PyTorch 2.12:
```python
>>> from torch._C import parse_schema
>>> parse_schema("foo(PyObject x) -> ()") # accepted
```
PyTorch 2.13:
```python
>>> from torch._C import parse_schema
>>> parse_schema("foo(PyObject x) -> ()") # raises a schema parse error
```
- Remove Bazel build support (#180883)
The Bazel build was never broadly adopted and still depended on the antiquated Bazel 6,
while the wider ecosystem has since moved to Bazel 9. All Bazel build files and CI jobs have
been removed. Users building PyTorch with Bazel should migrate to the supported CMake/`pip install`
build flow.
PyTorch 2.12:
```bash
# Build PyTorch with Bazel
bazel build //:torch
```
PyTorch 2.13:
```bash
# Bazel build files have been removed; build from source with pip instead
pip install --no-build-isolation -e .
```
- Enforce C++20 minimum in header guards (#178150). In PyTorch 2.13, C++20 is now required to import PyTorch headers.
- `StorageImpl`'s built-in copy-on-write (COW) materialization is replaced by a pluggable materializer hook (#179063)
`StorageImpl` no longer knows about COW directly. Its internal COW entry points
`StorageImpl::is_cow()`, `StorageImpl::maybe_materialize_cow()`, and the friend
`cow::materialize_cow_storage()` have been removed in favor of a single pluggable
`MaterializeFn` hook (`void(*)(StorageImpl*)`) that a backend registers to run once,
on the first mutable data-pointer access. COW is now just one consumer of this hook
(`c10::impl::cow::materialize_cow`), and all COW behavior (lazy clone, refcounted
shared data, copy-on-write) is unchanged. This also gives accelerator backends and
eager-mode graph compilers a zero-fast-path-cost place to commit deferred allocations
or materialize symbolic buffers on first mutation.
This is a C++-only change. It affects out-of-tree backends/extensions that called the
removed `StorageImpl` COW symbols directly; they will fail to compile against 2.13
with errors such as `no member named 'is_cow' in 'c10::StorageImpl'`. Migrate to the
new hook API (`set_materializer()` / `has_materializer()` / `clear_materializer()`).
PyTorch 2.12:
```cpp
// Detect a COW storage and force it to materialize.
if (storage.is_cow()) {
storage.maybe_materialize_cow();
}
```
PyTorch 2.13:
```cpp
// Re

## Related Articles

- [[train-large-neural-networks]]
- [[llm-quantization-gguf-gptq-awq]]
- [[how-to-deploy-with-vllm]]
- [[release-v180]]
- [[release-v1140]]
