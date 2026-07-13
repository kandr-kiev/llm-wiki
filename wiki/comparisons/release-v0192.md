---
title: "Release v0.19.2"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ci-cd
  - integration
  - multi-agent
  - policy
  - pytorch
  - quantization
  - transformers
  - use-case
  - workflow
  - zero-shot
---
# Release v0.19.2

> **Source:** gh-v0192-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/microsoft/DeepSpeed/releases/tag/v0.19.2 ingested: 2026-07-11 sha256: 50fb3cad352c33a31f8370d2c74c02eb6872841a6c67d4dc496df0c201cfc672 blog_source: github:microsoft/...
> **Sources:**
>   - gh-v0192-2026-07-11.md
> **Links:**
- [[release-notes-ollama-vv0312]]
- [[release-notes-llamacpp-vb9956]]
- [[release-notes-langchain-vlangchain-openai135]]
- [[release-v005]]
- [[release-notes-pytorch-vv2130]]

## Key Findings

---
source_url: https://github.com/microsoft/DeepSpeed/releases/tag/v0.19.2
ingested: 2026-07-11
sha256: 50fb3cad352c33a31f8370d2c74c02eb6872841a6c67d4dc496df0c201cfc672
blog_source: github:microsoft/DeepSpeed
---
# Release v0.19.2
## What's Changed
* fix(fp16): filter requires_grad in FP16 optimizer flat buffer init by @avicooper1 in https://github.com/deepspeedai/DeepSpeed/pull/8029
* Run AutoSP compile tests sequentially by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8020
* Fix PR-target workflow concurrency groups by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8017
* Fix full CI test isolation for ZeRO chmod and NVMe quantization tests by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8008
* Keep required CI checks visible for ignored paths by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8019
* Bump version by @sfc-gh-truwase in https://github.com/deepspeedai/DeepSpeed/pull/8030
* Add engine.coalesce_grad_reduction() for ZeRO 1/2/3 multi-backward by @roycho96 in https://github.com/deepspeedai/DeepSpeed/pull/7992
* feat(zero): enable torch.func transforms on engine for ZeRO 0/1/2 by @roycho96 in https://github.com/deepspeedai/DeepSpeed/pull/8026
* Simplify module_inject.transpose by @xbcReal in https://github.com/deepspeedai/DeepSpeed/pull/8028
* Fix DeepCompile all-gather scheduler candidate selection by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8033
* Version fix to unblock pypi by @sfc-gh-truwase in https://github.com/deepspeedai/DeepSpeed/pull/8039
* Bump version after 0.19.1 release by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8040
* Fix DeepCompile ZeRO-3 release parameter lifetime by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8032
* Fix ZenFlow ZeRO-3 selective optimizer crash with parameter offload on nvme by @Antlera in https://github.com/deepspeedai/DeepSpeed/pull/8042
* Add test coverage for Muon muon_lr/adam_lr overrides by @sowndappan5 in https://github.com/deepspeedai/DeepSpeed/pull/8047
* Avoid HF Hub access in CPU unit test setup by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8053
* Fix DeepCompile ZeRO-1 grad target lifetime by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8036
* Normalize ZeRO-3 DeepCompile grad dtype before reduction by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8038
* Remove AutoSP assertion against Transformers version by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/8044
* fix(transformer): use correct stride in Transpose_Kernel shared memory indexing to eliminate bank conflicts by @flutist in https://github.com/deepspeedai/DeepSpeed/pull/8055
* zero3: invalidate coordinator trace on hook re-registration by @roycho96 in https://github.com/deepspeedai/DeepSpeed/pull/8043
* Consistent fp32 grads flow by @sfc-gh-truwase in https://github.com/deepspeedai/DeepSpeed/pull/8056
* Add AutoEP by @tohtana in https://github.com/deepspeedai/DeepSpeed/pull/7938
* Fix: Z

## Summary

See Key Findings for full content.

## Related Articles

- [[release-notes-ollama-vv0312]]
- [[release-notes-llamacpp-vb9956]]
- [[release-notes-langchain-vlangchain-openai135]]
- [[release-v005]]
- [[release-notes-pytorch-vv2130]]
