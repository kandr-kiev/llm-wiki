---
source_url: https://github.com/huggingface/diffusers/issues/14186
ingested: 2026-07-14
sha256: c8a41e7d7521a3e844f338efc2a3003fcd3df71f0ac3860478837cfd052ff830
blog_source: github:huggingface/diffusers
---
# Issue #14186: Make `SD3Transformer2DModel` hidden states contiguous

**State:** open | **Author:** menglcai | **Created:** 2026-07-14T08:27:01Z

# What does this PR do?

Ensures hidden states are contiguous after each `JointTransformerBlock` call in `SD3Transformer2DModel`.

On ROCm, non-contiguous tensors produced by `JointTransformerBlock` cause performance degradation that accumulates across transformer blocks.

**Benchmarks** (SD3-medium, 512×512, 28 steps, fp16):

| Platform | PyTorch | Baseline | Patched | Speedup |
|---|---|---|---|---|
| AMD Radeon(TM) 8060S Graphics (gfx1151)  | 2.12.0+rocm7.15.0a20260711 | 8503 ms | 7470 ms | +12.1% |
| AMD RX 9070 XT (gfx1201)  | 2.12.0+rocm7.15.0a20260713 | 2547 ms | 2358 ms | +7.4% |
| NVIDIA RTX 5090  | 2.12.1+cu132 | 1042 ms | 1017 ms | within noise |



## Before submitting
- [ ] Did you use an AI agent (Claude Code, Codex, Cursor, etc.) to help with this PR? If so:
  - [ ] Did you read the [Coding with AI agents](https://huggingface.co/docs/diffusers/main/en/conceptual/contribution#coding-with-ai-agents) guide?
  - [ ] Did you self-review the diff against [`.ai/review-rules.md`](https://github.com/huggingface/diffusers/blob/main/.ai/review-rules.md)?
- [x]  Did you read the [contributor guideline](https://huggingface.co/docs/diffusers/main/en/conceptual/contribution)?
- [x]  Did you read our [philosophy doc](https://huggingface.co/docs/diffusers/main/en/conceptual/philosophy)? (important for complex PRs)
- [ ] Was this discussed/approved via a GitHub issue or the [forum](https://discuss.huggingface.co/c/discussion-related-to-httpsgithubcomhuggingfacediffusers/63)? Please add a link to it if that's the case.
- [ ] Did you make sure to update the documentation with your changes? Here are the
      [documentation guidelines](https://github.com/huggingface/diffusers/tree/main/docs), and
      [here are tips on formatting docstrings](https://github.com/huggingface/diffusers/tree/main/docs#writing-source-documentation).
- [ ] Did you write any new necessary tests?
- [ ] Are you the author (or part of the team) of the model/pipeline (only applicable for model/pipeline related PRs)?


## Who can review?

@sayakpaul @yiyixuxu

Anyone in the community is free to review the PR once the tests have passed. Feel free to tag
members/contributors who may be interested in your PR.