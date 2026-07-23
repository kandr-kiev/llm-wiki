---
title: "Issue #123251: PR #44403: [XLA:CPU] onednn_threadpool: cap num_workers at n in parallel_for"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - design-pattern
  - open-source
  - tensorflow
---

# Issue #123251: PR #44403: [XLA:CPU] onednn_threadpool: cap num_workers at n in parallel_for

> **Source:** gh-tensorflowtensorflow-issue-123251-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/tensorflow/tensorflow/issues/123251 ingested: 2026-07-14 sha256: 166a3b16dc0122270d5b07c88b8a31ae101c50321873e98b8386de557274900a blog_source: github:tensorflow/tens...
> **Sources:**
>   - gh-tensorflowtensorflow-issue-123251-2026-07-14.md
> **Links:**
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse]
- [Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]
- [Issue #3419: FIX Bug in forgetting metric in MetaMathQA]
- [Issue #3429: FIX C3ALinear.forward chaining multiple active adapters instead of summing]

## Key Findings

---
source_url: https://github.com/tensorflow/tensorflow/issues/123251
ingested: 2026-07-14
sha256: 166a3b16dc0122270d5b07c88b8a31ae101c50321873e98b8386de557274900a
blog_source: github:tensorflow/tensorflow
---
# Issue #123251: PR #44403: [XLA:CPU] onednn_threadpool: cap num_workers at n in parallel_for
**State:** open | **Author:** copybara-service[bot] | **Created:** 2026-07-14T19:12:36Z
PR #44403: [XLA:CPU] onednn_threadpool: cap num_workers at n in parallel_for
Imported from GitHub PR https://github.com/openxla/xla/pull/44403
📝 Summary of Changes
`OneDnnThreadPool::parallel_for` (xla/backends/cpu/runtime/onednn/onednn_threadpool.h) was passing `thread_pool_- NumThreads()` as `num_workers` regardless of `n`. Before #42581, `Worker::Parallelize` had an entry-point clamp (`num_workers = std::min(num_work_items, num_workers)`) that silently fixed this up. #42581 replaced that clamp with a branch that triggers when `num_workers > num_work_items`:
```cpp
if (num_workers > num_work_items) {
num_partitions = ceil(num_work_items / 8);
num_workers = std::min(num_workers, num_partitions);
}
```
For oneDNN's small-n dispatches (reorders, packing, eltwise/softmax tiles), this collapses parallelism to ceil(n/8) cores. 
eg: On a 56-thread host, n = 20 drops from 20 active cores to 3; n (static_cast(n),
thread_pool_->NumThreads());
```
With num_workers = NumThreads(), the cap is a no-op and the heap/cacheline win from #42581 is fully preserved.
🎯 Justification
It fixes the significant regression (25%-60%) across multiple models run on CPU with onednn 
🚀 Kind of Contribution
Please remove what does not apply: 🐛 Bug Fix
Copybara import of the project:
--
edbf833e7f90aeed3393815c5a4d112201d5d857 by Gauri Deshpande :
[XLA:CPU] onednn_threadpool: cap num_workers at n in parallel_for
Merging this change closes #44403
FUTURE_COPYBARA_INTEGRATE_REVIEW=https://github.com/openxla/xla/pull/44403 from Intel-tensorflow:gaurides/onednn-cap-num-workers edbf833e7f90aeed3393815c5a4d112201d5d857

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #14184: Fix AuraFlow VAE dtype mismatch on pipeline reuse]
- [Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]
- [Issue #3419: FIX Bug in forgetting metric in MetaMathQA]
- [Issue #3429: FIX C3ALinear.forward chaining multiple active adapters instead of summing]
