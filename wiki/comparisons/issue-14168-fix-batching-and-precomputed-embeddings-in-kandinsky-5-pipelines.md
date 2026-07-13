---
title: "Issue #14168: Fix batching and precomputed embeddings in Kandinsky 5 pipelines"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - batch
  - claude
  - cuda
  - embedding
  - foundation-model
  - guide
  - image-generation
  - open-source
  - pipeline
  - prompt-tuning
  - review
  - self-supervised
  - use-case
---
# Issue #14168: Fix batching and precomputed embeddings in Kandinsky 5 pipelines

> **Source:** gh-huggingfacediffusers-issue-14168-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/diffusers/issues/14168 ingested: 2026-07-11 sha256: 3bd4c1e261f4d3479ca5cd110e9fd8f3ab9805243d91dc35afe2958f93d04333 blog_source: github:huggingface/diff...
> **Sources:**
>   - gh-huggingfacediffusers-issue-14168-2026-07-11.md
> **Links:**
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[chemical-hygiene]]
- [[how-to-engineer-prompts]]
- [[llm-deployment-qa]]

## Key Findings

---
source_url: https://github.com/huggingface/diffusers/issues/14168
ingested: 2026-07-11
sha256: 3bd4c1e261f4d3479ca5cd110e9fd8f3ab9805243d91dc35afe2958f93d04333
blog_source: github:huggingface/diffusers
---
# Issue #14168: Fix batching and precomputed embeddings in Kandinsky 5 pipelines
**State:** open | **Author:** pzarzycki | **Created:** 2026-07-11T01:05:38Z
# What does this PR do?
Kandinsky 5 pipelines expanded the latent batch for `num_images_per_prompt` and `num_videos_per_prompt`, but did not always expand the matching text and visual conditioning. This caused batch mismatches when generating multiple outputs, especially when callers supplied precomputed prompt embeddings.
This PR makes batching consistent across the T2I, I2I, T2V, and I2V pipelines. It:
- repeats Qwen and CLIP embeddings in per-prompt output order;
- rebuilds cumulative Qwen sequence lengths for the expanded batch;
- supports precomputed positive and negative embeddings with multiple outputs per prompt;
- handles classifier-free guidance when `prompt=None`;
- passes `num_videos_per_prompt` through the T2V text-encoding path;
- expands I2I and I2V visual conditioning to the effective batch size;
- accepts PIL, NumPy, tensor, and list image inputs in the I2I prompt-encoding path;
- validates that precomputed embedding components have consistent batch sizes.
Focused regression tests cover all four pipelines. This addresses the batching and precomputed-embedding findings in #13639.
## Tests
- Full Kandinsky 5 suite excluding the existing unsupported fp16 cases: `122 passed, 16 skipped, 4 deselected`
- Focused new and changed CPU regressions: `9 passed`
- CUDA fp32 smoke matrix for T2I, I2I, T2V, and I2V with precomputed CFG and two outputs per prompt
- CUDA bf16-autocast smoke matrix for all four pipelines
- `make fix-copies`
- Ruff check and formatting
- `python -m compileall -q src/diffusers/pipelines/kandinsky5 tests/pipelines/kandinsky5`
- `git diff --check`
## Before submitting
- [x] Did you use an AI agent (Claude Code, Codex, Cursor, etc.) to help with this PR? If so:
- [ ] Did you read the [Coding with AI agents](https://huggingface.co/docs/diffusers/main/en/conceptual/contribution#coding-with-ai-agents) guide?
- [x] Did you self-review the diff against [`.ai/review-rules.md`](https://github.com/huggingface/diffusers/blob/main/.ai/review-rules.md)?
- [ ] Did you read the [contributor guideline](https://huggingface.co/docs/diffusers/main/en/conceptual/contribution)?
- [ ] Did you read our [philosophy doc](https://huggingface.co/docs/diffusers/main/en/conceptual/philosophy)? (important for complex PRs)
- [x] Was this discussed/approved via a GitHub issue or the [forum](https://discuss.huggingface.co/c/discussion-related-to-httpsgithubcomhuggingfacediffusers/63)? See #13639.
- [x] Did you make sure to update the documentation with your changes? No public arguments changed; existing docstrings already describe the supported inputs.
- [x] Did you write any new necessary

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[chemical-hygiene]]
- [[how-to-engineer-prompts]]
- [[llm-deployment-qa]]
