---
title: "Issue #47257: Avoid ~2x transient host memory when loading to a unified-memory device"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ci-cd
  - cuda
  - foundation-model
  - framework
  - gpu
  - open-source
  - real-time
  - self-supervised
  - zero-shot
---
# Issue #47257: Avoid ~2x transient host memory when loading to a unified-memory device

> **Source:** gh-huggingfacetransformers-issue-47257-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/issues/47257 ingested: 2026-07-11 sha256: 3a95093ede16b602138d2687b1f25234b1c80bd2f08c6b9777ccd934a34ad60c blog_source: github:huggingface/t...
> **Sources:**
>   - gh-huggingfacetransformers-issue-47257-2026-07-11.md
> **Links:**
- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[llm-deployment-qa]]
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/issues/47257
ingested: 2026-07-11
sha256: 3a95093ede16b602138d2687b1f25234b1c80bd2f08c6b9777ccd934a34ad60c
blog_source: github:huggingface/transformers
---
# Issue #47257: Avoid ~2x transient host memory when loading to a unified-memory device
**State:** open | **Author:** cgu2022 | **Created:** 2026-07-11T01:22:43Z
[![CI](https://transformers-ci.lor-e.huggingface.cool/badge/pr?pr=47257)](https://transformers-ci.lor-e.huggingface.cool/d/pytest-observability-by-pr/pytest-observability-branch?var-pr=47257)
## What & why
On integrated (unified-memory) accelerators — NVIDIA GB10 / GH200, Jetson — the CPU and GPU share one physical memory pool. `_materialize_copy` copies each weight to the device straight from the `MAP_PRIVATE` safetensors mmap; pinning those pages for the H2D DMA **copy-on-write-duplicates** every transferred page into unreclaimable host (anonymous) memory. Tensors stream in with all shard handles still open, so the duplicate grows ~1 byte per byte loaded and is only released at the end — a model of size `M` transiently needs **~2·M** and OOMs when `2·M` exceeds unified RAM.
Measured on a GB10 (128 GB): `Qwen/Qwen3.6-35B-A3B` bf16 (~70 GB) climbs toward ~148 GB and is **OOM-killed at ~60% of loading**, every time. Throughout the load `RssAnon` tracks `torch.cuda.memory_allocated()` 1:1, and `/proc/self/smaps` shows the growing `Anonymous` bytes charged to the checkpoint file's mappings.
## Fix
When copying a CPU tensor to an **integrated** device **without a dtype cast**, `clone()` it off the mmap first. The clone's read-faults are ordinary reclaimable page cache and it frees the moment the copy lands, so the peak drops back to ~M. Discrete GPUs keep the current zero-copy path byte-for-byte (their separate-VRAM copy never enters the host budget), and a dtype cast already allocates a fresh tensor.
On the same GB10 the Qwen3.6-35B bf16 load then completes at **~80 GB peak / ~77.6 GB steady in ~50 s** instead of OOM-ing — and faster, because COW-faulting every page was itself a large part of the load time.
## Minimal reproducer (no model download, needs an integrated GPU)
```python
import os, torch
from safetensors.torch import save_file
from safetensors import safe_open
PATH = os.path.expanduser("~/cow_repro.safetensors") # must be on a real disk, not tmpfs
def file_anon_gb(real):
total, cur = 0, False
for line in open("/proc/self/smaps"):
h = line.split()
if h and "-" in h[0] and (line[0].isdigit() or line[0] in "abcdef"):
cur = real in line
elif cur and line.startswith("Anonymous:"):
total += int(h[1])
return total / 1048576
save_file({"w": torch.zeros(1024**3, dtype=torch.bfloat16)}, PATH) # 2 GB
real = os.path.realpath(PATH)
f = safe_open(PATH, framework="pt")
f.get_slice("w")[...].to("cuda"); torch.cuda.synchronize()
print("direct .to('cuda'): Anonymous =", round(file_anon_gb(real), 2), "GB")
```
```
NVIDIA GB10 is_integrated=1
direct .to('cuda'): file-mapping Anonymous =

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[llm-deployment-qa]]
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]
