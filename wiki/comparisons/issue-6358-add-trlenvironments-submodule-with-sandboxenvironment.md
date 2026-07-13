---
title: "Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - async
  - cloud
  - foundation-model
  - library
  - open-source
  - parallel
  - tool
  - use-case
---
# Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`

> **Source:** gh-huggingfacetrl-issue-6358-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/trl/issues/6358 ingested: 2026-07-11 sha256: ca6ebef58b3bf5afa28b0ba88d03b14e7486c2268b3229a649660f209174e567 blog_source: github:huggingface/trl --- # I...
> **Sources:**
>   - gh-huggingfacetrl-issue-6358-2026-07-11.md
> **Links:**
- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-47254-checkpointerror-with-peft-deepspeed-zero-3-gradient-checkpointing]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[Issue #47256: [serge] integration failure triage -]]

## Key Findings

---
source_url: https://github.com/huggingface/trl/issues/6358
ingested: 2026-07-11
sha256: ca6ebef58b3bf5afa28b0ba88d03b14e7486c2268b3229a649660f209174e567
blog_source: github:huggingface/trl
---
# Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`
**State:** open | **Author:** qgallouedec | **Created:** 2026-07-11T03:51:37Z
New `trl.environments` submodule (parallel to `trl.rewards`), with a first environment: `SandboxEnvironment`.
**Scope.** The goal is *not* for TRL to become an environments library. Like `trl.rewards`, it ships a small set of genuinely useful, ready-to-use environments that double as worked examples users can copy and customize for their own tasks.
`SandboxEnvironment` gives the model a `run` tool backed by an isolated [Hugging Face Sandbox](https://huggingface.co/docs/huggingface_hub/main/guides/sandbox), a cloud VM the model uses to execute shell/Python during generation. It plugs into `GRPOTrainer`/`AsyncGRPOTrainer` via `environment_factory`. Reward is left entirely to `reward_funcs`; the environment only provides the execution surface.
```python
from trl.environments import SandboxEnvironment
trainer = GRPOTrainer(..., environment_factory=SandboxEnvironment)
```
The sandbox boots once per environment instance (off the calling thread, so it doesn't block the async rollout loop) and is reused across the instance's rollouts. Requires `huggingface_hub>=1.22.0`.
## Also
- Example: `examples/scripts/async_grpo_sandbox.py`, async GRPO on GSM8K where the model computes answers in the sandbox; dependency-free exact-match reward on the final `\boxed{}` number.
- `is_huggingface_hub_available(min_version=...)` helper in `import_utils`.
- Docs page + API toctree entry.

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-47254-checkpointerror-with-peft-deepspeed-zero-3-gradient-checkpointing]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[Issue #47256: [serge] integration failure triage -]]
