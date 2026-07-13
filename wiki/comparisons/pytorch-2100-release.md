---
title: "PyTorch 2.10.0 Release"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - cuda
  - data
  - distributed
  - frontend
  - guide
  - onnx
  - performance
  - prompt-engineering
  - pytorch
  - real-time
  - security
  - tool
  - training
  - use-case
---
# PyTorch 2.10.0 Release

> **Source:** pytorch-2100-release-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/pytorch/pytorch/releases/tag/v2.10.0 ingested: 2026-07-10 sha256: f9f9a3d70f2b5f84e532fab2f5a63d55f95cc68fc43bc9111e8df478e0b48b58 blog_source: github --- # PyTorch...
> **Sources:**
>   - pytorch-2100-release-2026-07-10.md
> **Links:**
- [[train-large-neural-networks]]
- [[release-v180]]
- [[release-notes-pytorch-vv2130]]
- [[release-v1140]]
- [[llm-quantization-gguf-gptq-awq]]

## Key Findings

---
source_url: https://github.com/pytorch/pytorch/releases/tag/v2.10.0
ingested: 2026-07-10
sha256: f9f9a3d70f2b5f84e532fab2f5a63d55f95cc68fc43bc9111e8df478e0b48b58
blog_source: github
---
# PyTorch 2.10.0 Release
## Release Notes
# PyTorch 2.10.0 Release Notes
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
**Python 3.14** support for `torch.compile()`. Python 3.14t (freethreaded build) is experimentally supported as well.
Reduced kernel launch overhead with **combo-kernels** horizontal fusion in torchinductor 
A new **varlen_attn()** op providing support for ragged and packed sequences 
Efficient eigenvalue decompositions with **DnXgeev** 
`torch.compile()` now respects **use_deterministic_mode** 
**DebugMode** for tracking dispatched calls and debugging numerical divergence - This makes it simpler to track down subtle numerical bugs. 
**Intel GPUs support:** Expand PyTorch support to the latest Panther Lake on Windows and Linux by enabling FP8 (core ops and scaled matmul) and complex MatMul support, and extending SYCL support in the C++ Extension API for Windows custom ops. 
For more details about these highlighted features, you can look at the [release blogpost](https://pytorch.org/blog/pytorch-2-10-release-blog/). Below are the full release notes for this release.
# Backwards Incompatible Changes
## Dataloader Frontend
- Removed unused `data_source` argument from Sampler ([#163134](https://github.com/pytorch/pytorch/pull/163134)). This is a no-op, unless you have a custom sampler that uses this argument. Please update your custom sampler accordingly.
- Removed deprecated imports for torch.utils.data.datapipes.iter.grouping ([#163438](https://github.com/pytorch/pytorch/pull/163438)). `from torch.utils.data.datapipes.iter.grouping import SHARDING_PRIORITIES, ShardingFilterIterDataPipe` is no longer supported. Please import from `torch.utils.data.datapipes.iter.sharding` instead.
## torch.nn
- Remove Nested Jagged Tensor support from `nn.attention.flex_attention` ([#161734](https://github.com/pytorch/pytorch/pull/161734))
## ONNX
- `fallback=False` is now the default in `torch.onnx.export` ([#162726](https://github.com/pytorch/pytorch/pull/162726))
- The exporter now uses the `dynamo=True` option without fallback. This is the recommended way to use the ONNX exporter. To preserve 2.9 behavior, manually set `fallback=True` in the `torch.onnx.export` call.
## Release Engineering
- Rename pytorch-triton package to triton ([#169888](https://github.com/pytorch/pytorch/pull/169888))
# Deprecations
## Distributed
- DeviceMesh
- Added a warning for slicing flattened dim from root mesh and types for _get_slice_mesh_layout ([#164993](https://github.com/pytorch/

## Summary

pytorch/pull/164993))
We decided to deprecate an existing behavior which goes against the PyTorch design principle (explicit over implicit) for device mesh slicing of flattened dim.
### Version =2.10
```python
import torch
from torch.distributed.device_mesh import
device_type = (
acc.type
if (acc := torch.accelerator.current_accelerator(check_available=True))
else "cpu"
)
mesh_shape = (2, 2, 2)
mesh_3d = init_device_mesh(
device_type, mesh_shape, mesh_dim_names=("dp", "cp", "tp")
)
mesh_3d["dp", "cp"]._flatten()
mesh_3["dp_cp"] # This will come with a warning because it implicitly change the state of the original mesh. We will eventually remove this behavior in future release. User should do the bookkeeping of flattened mesh explicitly.
```
## Ahead-Of-Time Inductor (AOTI)
- Move `from`/`to` to `torch::stable::detail` ([#164956](https://github.com/pytorch/pytorch/pull/164956))
## JIT
- `torch.jit` is not guaranteed to work in Python 3.14. Deprecation warnings have been added to user-facing `torch.jit` API ([#167669](https://github.com/pytorch/pytorch/pull/167669)).
`torch.jit` should be replaced with `torch.compile` or `torch.export`.
## ONNX
- The `dynamic_axes` option in `torch.onnx.export` is deprecated ([#165769](https://github.com/pytorch/pytorch/pull/165769))
Users should supply the `dynamic_shapes` argument instead. See https://docs.pytorch.org/docs/stable/export.html#expressing-dynamism for more documentation.
## Profiler
- Deprecate `export_memory_timeline` method ([#168036](https://github.com/pytorch/pytorch/pull/168036))
The `export_memory_timeline` method in `torch.profiler` is being deprecated in favor of the newer memory snapshot API (`torch.cuda.memory._record_memory_history` and `torch.cuda.memory._export_memory_snapshot`). This change adds the deprecated decorator from `typing_extensions` and updates the docstring to guide users to the recommended alternative.
# New Features
## Autograd
- Allow setting grad_dtype on leaf tensors ([#164751](https://github.com/pytorch/pytorch/pull/164751))
- Add Default Autograd Fallback for PrivateUse1 in PyTorch ([#165315](https://github.com/pytorch/pytorch/pull/165315))
- Add API to annotate disjoint backward for use with `torch.utils.checkpoint.checkpoint` ([#166536](https://github.com/pytorch/pytorch/pull/166536))
## Complex Frontend
- Add `ComplexTensor` subclass ([#167621](https://github.com/pytorch/pytorch/pull/167621))
## Composability
- Support autograd in torch.cond ([#165908](https://github.com/pytorch/pytorch/pull/165908))
## cuDNN
- BFloat16 support added to cuDNN RNN ([#164411](https://github.com/pytorch/pytorch/pull/164411))
- [cuDNN][submodule] Upgrade to cuDNN frontend 1.16.1 (#170591)
## Distributed
- LocalTensor:
- `LocalTensor` is a powerful debugging and simulation tool in PyTorch's distributed tensor ecosystem. It allows you to simulate distributed tensor computations across multiple SPMD (Single Program, Multiple Data) ranks on a single process. This is incredibly valuable f

## Related Articles

- [[train-large-neural-networks]]
- [[release-v180]]
- [[release-notes-pytorch-vv2130]]
- [[release-v1140]]
- [[llm-quantization-gguf-gptq-awq]]
