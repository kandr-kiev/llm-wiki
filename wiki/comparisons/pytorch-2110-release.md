---
title: "PyTorch 2.11.0 Release"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - backend
  - cuda
  - distributed
  - foundation-model
  - frontend
  - gpu
  - open-source
  - performance
  - prompt-engineering
  - prompt-tuning
  - pytorch
  - security
  - training
  - use-case
---
# PyTorch 2.11.0 Release

> **Source:** pytorch-2110-release-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/pytorch/pytorch/releases/tag/v2.11.0 ingested: 2026-07-10 sha256: a1b844717a4500eec8fc558c1c73b53eb7547bb3d39c70b083566101b251a073 blog_source: github --- # PyTorch...
> **Sources:**
>   - pytorch-2110-release-2026-07-10.md
> **Links:**
- [[pytorch-2100-release]]
- [[train-large-neural-networks]]
- [[release-v1140]]
- [[release-v180]]
- [[llm-quantization-gguf-gptq-awq]]

## Key Findings

---
source_url: https://github.com/pytorch/pytorch/releases/tag/v2.11.0
ingested: 2026-07-10
sha256: a1b844717a4500eec8fc558c1c73b53eb7547bb3d39c70b083566101b251a073
blog_source: github
---
# PyTorch 2.11.0 Release
## Release Notes
# PyTorch 2.11.0 Release Notes
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
Added Support for **Differentiable Collectives** for Distributed Training
**FlexAttention** now has a **FlashAttention-4** backend on **Hopper** and **Blackwell** GPUs
**MPS (Apple Silicon)** Comprehensive Operator Expansion
Added **RNN/LSTM** GPU Export Support
Added **XPU Graph** Support
For more details about these highlighted features, you can look at the [release blogpost](https://pytorch.org/blog/pytorch-2-11-release-blog/). Below are the full release notes for this release.
# Backwards Incompatible Changes
## Release Engineering
### Volta (SM 7.0) GPU support removed from CUDA 12.8 and 12.9 binary builds (#172598)
Starting with PyTorch 2.11, the CUDA 12.8 and 12.9 pre-built binaries no longer include support for Volta GPUs (compute capability 7.0, e.g. V100). This change was necessary to enable updating to CuDNN 9.15.1, which is incompatible with Volta.
Users with Volta GPUs who need CUDA 12.8+ should use the CUDA 12.6 builds, which continue to include Volta support. Alternatively, build PyTorch from source with Volta included in `TORCH_CUDA_ARCH_LIST`.
Version 2.10:
```
# CUDA 12.8 builds supported Volta (SM 7.0)
pip install torch --index-url https://download.pytorch.org/whl/cu128
# Works on V100
```
Version 2.11:
```
# CUDA 12.8 builds no longer support Volta
# For V100 users, use CUDA 12.6 builds instead:
pip install torch --index-url https://download.pytorch.org/whl/cu126
```
### PyPI wheels now ship with CUDA 13.0 instead of CUDA 12.x ([#172663](https://github.com/pytorch/pytorch/issues/172663), [announcement](https://dev-discuss.pytorch.org/t/transitioning-pypi-cuda-wheels-to-cuda-13-0-as-the-stable-release-2-11/3325))
Starting with PyTorch 2.11, `pip install torch` on PyPI installs CUDA 13.0 wheels by default for both Linux x86_64 and Linux aarch64. Previously, PyPI wheels shipped with CUDA 12.x and only Linux x86_64 CUDA wheels were available on PyPI. Users whose systems have only CUDA 12.x drivers installed may encounter errors when running `pip install torch` without specifying an index URL.
Additionally, CUDA 13.0 only supports Turing (SM 7.5) and newer GPU architectures on Linux x86_64. Maxwell and Pascal GPUs are no longer supported under CUDA 13.0. Users with these older GPUs should use the CUDA 12.6 builds instead.
CUDA 12.6 and 12.8 binaries remain available via `download.pytorch.org`.
Version 2.10:
```bash
# PyPI wheel used 

## Summary

CUDA 12.x
pip install torch
```
Version 2.11:
```bash
# PyPI wheel now uses CUDA 13.0
pip install torch
# To get CUDA 12.8 wheels instead:
pip install torch --index-url https://download.pytorch.org/whl/cu128
# To get CUDA 12.6 wheels (includes Maxwell/Pascal/Volta support):
pip install torch --index-url https://download.pytorch.org/whl/cu126
```
## Python Frontend
### `torch.hub.list()`, `torch.hub.load()`, and `torch.hub.help()` now default the `trust_repo` parameter to `"check"` instead of `None`. The `trust_repo=None` option has been removed. (#174101)
Previously, passing `trust_repo=None` (or relying on the default) would silently download and run code from untrusted repositories with only a warning. Now, the default `"check"` behavior will prompt the user for explicit confirmation before running code from repositories not on the trusted list.
Users who were explicitly passing `trust_repo=None` must update their code. Users who were already passing `trust_repo=True`, `trust_repo=False`, or `trust_repo="check"` are not affected.
Version 2.10:
```python
# Default trust_repo=None — downloads with a warning
torch.hub.load("user/repo", "model")
# Explicit None — same behavior
torch.hub.load("user/repo", "model", trust_repo=None)
```
Version 2.11:
```python
# Default trust_repo="check" — prompts for confirmation if repo is not trusted
torch.hub.load("user/repo", "model")
# To skip the prompt, explicitly trust the repo
torch.hub.load("user/repo", "model", trust_repo=True)
```
## torch.nn
### Add sliding window support to `varlen_attn` via `window_size`, making optional arguments keyword-only (#172238)
The signature of `torch.nn.attention.varlen_attn` has changed: a `*` (keyword-only separator) has been inserted before the optional arguments. Previously, optional arguments like `is_causal`, `return_aux`, and `scale` could be passed positionally; they must now be passed as keyword arguments. A new `window_size` keyword argument has also been added.
```python
# Before (2.10)
output = varlen_attn(query, key, value, cu_seq_q, cu_seq_k, max_q, max_k, True, None, 1.0)
# After (2.11) — pass as keyword argument
output = varlen_attn(query, key, value, cu_seq_q, cu_seq_k, max_q, max_k, window_size=(-1, 0), return_aux=None, scale=1.0)
```
### Remove `is_causal` flag from `varlen_attn` (#172245)
The `is_causal` parameter has been removed from `torch.nn.attention.varlen_attn`. Causal attention is now expressed through the `window_size` parameter: use `window_size=(-1, 0)` for causal masking, or `window_size=(W, 0)` for causal attention with a sliding window of size `W`. The default `window_size=(-1, -1)` corresponds to full (non-causal) attention.
```python
# Before (2.10)
output = varlen_attn(query, key, value, cu_seq_q, cu_seq_k, max_q, max_k, is_causal=True)
# After (2.11) — use window_size instead
output = varlen_attn(query, key, value, cu_seq_q, cu_seq_k, max_q, max_k, window_size=(-1, 0))
```
## Distributed
### `DebugInfoWriter` now honors `$XDG_CACHE_HOME`

## Related Articles

- [[pytorch-2100-release]]
- [[train-large-neural-networks]]
- [[release-v1140]]
- [[release-v180]]
- [[llm-quantization-gguf-gptq-awq]]
