---
title: "Release v0.8.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - backend
  - ci-cd
  - docker
  - efficiency
  - foundation-model
  - framework
  - governance
  - gpu
  - guide
  - hardware
  - image-generation
  - news
  - open-source
  - pytorch
  - security
  - use-case
  - workflow
---

# Release v0.8.0

> **Source:** gh-v080-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/safetensors/releases/tag/v0.8.0 ingested: 2026-07-14 sha256: 8ed2b18b7bacd56a4dd4f91702a12a2445fbe2e18303757d3967c14073f5f8f5 blog_source: github:hugging...
> **Sources:**
>   - gh-v080-2026-07-14.md
> **Links:**
- [[Release v0.23.1]]
- [[v0.22.1]]
- [[v0.27.0]]
- [[Release 5.0.0]]
- [[Release Notes: Ollama vv0.31.2]]

## Key Findings

---
source_url: https://github.com/huggingface/safetensors/releases/tag/v0.8.0
ingested: 2026-07-14
sha256: 8ed2b18b7bacd56a4dd4f91702a12a2445fbe2e18303757d3967c14073f5f8f5
blog_source: github:huggingface/safetensors
---
# Release v0.8.0
## News
safetensors joins the PyTorch foundation!
![image](https://github.com/user-attachments/assets/77418d98-0faf-484c-b910-3116f2eb3b63)
Read more on that: https://huggingface.co/blog/safetensors-joins-pytorch-foundation
## What's changed
Safetensors 0.8.0 brings direct to Metal loading on Apple Silicon, GIL-free serialization, broader hardware and dtype coverage, and a stronger Python API.
### Breaking
The `serialize` and `serialize_file` functions now release the GIL during writes, enabling true multithreaded saves from Python. Their input contract has also changed: tensor metadata is now passed via a `TensorSpec` class (exported from safetensors) instead of plain dicts, making API more explicit and robust to misinputs. This is a breaking change for anyone calling the low-level `serialize` / `serialize_file` API directly; the high-level wrappers (`safetensors.torch`, `safetensors.numpy`, `safetensors.paddle`) are updated internally and their public API is unchanged.
The minimum supported Python version is now 3.10 (was 3.9). Python 3.9 reached end-of-life in October 2025.
`TensorIndexer::Narrow` now carries a `step: NonZeroUsize` parameter, so a slice is now `start:stop:step`. This is a fix as this silent error was hidden behind the `Storage::Torch` variant which offloaded slicing logic to torch directly.
### CI
On the platform side, this release adds Windows ARM64 wheel builds, riscv64 Linux wheels, and CI has been hardened with pinned GitHub Actions SHAs.
Also dropped the anaconda CI we had as there's already an automatic tracker via conda-forge.
### New features
- Direct MPS load on Apple Silicon: tensors are directly loaded in an `MTLBuffer` and handed to the frameworks that support it (only torch atm) via DLPack, skipping needless copies.
- New `backend` parameter introduced, for the addition of the `pread` backend. We now support loading files via `pread(2)` syscall instead of just mmap. Useful for specific archs/platforms.
- `get_slice` now handles ellipsis `[...]` and strided slices `[:, ::8]` wherever safetensors does the slicing itself (`pread` for any framework, MPS, and `mmap` outside torch/paddle), which silently dropped the step or rejected `...` before.
- MUSA device support for MooreThreads GPUs.
- New dtype support includes `float8_e4m3fnuz` and `float8_e5m2fnuz` (AMD FNUZ FP8 formats).
- The reader is now explicitly lenient about leading whitespace in the JSON header, which keeps the door open for future page-aligned writes.
### Improvements/perf
- File writes on macOS now use `F_NOCACHE` for direct I/O, yielding roughly 30% faster `save_file` on Apple Silicon.
- The packaging dependency has been dropped from the `[torch]` extra, replaced by a simple `hasattr` probe for efficiency.
## What'

## Summary

s Changed
* Add arm64 windows support by @finnagin in https://github.com/safetensors/safetensors/pull/678
* feat(backend): support musa backend for MooreThreads GPU by @caizhi-mt in https://github.com/safetensors/safetensors/pull/671
* add gil free serialize_file(serialize_file_threadable) by @TomQunChao in https://github.com/safetensors/safetensors/pull/679
* refactor: remove outdated comment by @McPatate in https://github.com/safetensors/safetensors/pull/685
* feat: add direct io write fast path on macos by @McPatate in https://github.com/safetensors/safetensors/pull/687
* fix: keep dropped reference to tensor moved from gpu to cpu by @McPatate in https://github.com/safetensors/safetensors/pull/689
* feat: bump torch to `2.4` by @McPatate in https://github.com/safetensors/safetensors/pull/710
* Contribution guide security by @LysandreJik in https://github.com/safetensors/safetensors/pull/712
* Project Governance by @LysandreJik in https://github.com/safetensors/safetensors/pull/721
* Add riscv64 build, make Linux wheel build matrix more explicit by @threexc in https://github.com/safetensors/safetensors/pull/708
* 🔒 Pin GitHub Actions to commit SHAs by @paulinebm in https://github.com/safetensors/safetensors/pull/727
* fix: do not require `packaging` for Torch 2.3.0+ datatype support by @akx in https://github.com/safetensors/safetensors/pull/705
* Bump urllib3 from 2.4.0 to 2.6.3 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/715
* Bump protobuf from 5.29.4 to 5.29.6 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/716
* Bump filelock from 3.18.0 to 3.20.3 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/717
* Bump wheel from 0.45.1 to 0.46.2 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/718
* Bump werkzeug from 3.1.3 to 3.1.6 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/719
* Bump pillow from 11.2.1 to 12.1.1 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/720
* Bump markdown from 3.8 to 3.8.1 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/722
* Bump requests from 2.32.3 to 2.33.0 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/725
* Bump pygments from 2.19.1 to 2.20.0 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/726
* mark `__version__` as str in the stub by @tarekziade in https://github.com/safetensors/safetensors/pull/730
* Add a multithreaded stress test by @ngoldbaum in https://github.com/safetensors/safetensors/pull/637
* Bump torch from 2.7.0 to 2.8.0 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/safetensors/pull/732
* Bump mlx from 0.27.1 to 0.29.4 in /bindings/python by @dependabot[bot] in https://github.com/safetensors/

## Related Articles

- [[Release v0.23.1]]
- [[v0.22.1]]
- [[v0.27.0]]
- [[Release 5.0.0]]
- [[Release Notes: Ollama vv0.31.2]]
