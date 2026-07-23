---
title: "Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - gptq
  - onnx
  - open-source
  - quantization
  - review
  - security
  - use-case
---

# Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning

> **Source:** gh-huggingfaceoptimum-issue-2455-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/optimum/issues/2455 ingested: 2026-07-14 sha256: 0412321f5ec85cf91d1448a25181d531d68e2eb713a087df84e6b37eeb7db073 blog_source: github:huggingface/optimum...
> **Sources:**
>   - gh-huggingfaceoptimum-issue-2455-2026-07-14.md
> **Links:**
- [Issue #14169: Remove JAX/Flax]
- [Issue #14185: ask to share self-review notes]
- [Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]
- [Issue #8332: Raise on length mismatch in batched IterableDataset.map]
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]

## Key Findings

---
source_url: https://github.com/huggingface/optimum/issues/2455
ingested: 2026-07-14
sha256: 0412321f5ec85cf91d1448a25181d531d68e2eb713a087df84e6b37eeb7db073
blog_source: github:huggingface/optimum
---
# Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning
**State:** open | **Author:** vigneshkumar25 | **Created:** 2026-07-01T13:49:40Z
- Relax transformers upper bound to <6.0 to unblock v5 users
- Add weights_only=True to torch.load to fix CVE security warning
Fixes #2432
# What does this PR do?
Fixes # (issue)
## Before submitting
- [ ] This PR fixes a typo or improves the docs (you can dismiss the other checks if that's the case).
- [ ] Did you make sure to update the documentation with your changes?
- [ ] Did you write any new necessary tests?
## Who can review?

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #14169: Remove JAX/Flax]
- [Issue #14185: ask to share self-review notes]
- [Issue #4116: Fix get_non_persistent_buffers mutating module._non_persistent_buffers_set]
- [Issue #8332: Raise on length mismatch in batched IterableDataset.map]
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
