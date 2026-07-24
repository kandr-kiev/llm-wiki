---
title: "Release v5.14.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - audio-generation
  - backend
  - batch
  - benchmark
  - ci-cd
  - design-pattern
  - docker
  - fine-tuning
  - foundation-model
  - image-generation
  - instruction-tuning
  - integration
  - multi-agent
  - multimodal
  - nlp
  - open-source
  - optimization
  - performance
  - postprocessing
  - preprocessing
  - research
  - retrieval
  - tool
  - training
  - use-case
  - workflow
---

# Release v5.14.0

> **Source:** gh-v5140-2026-07-15.md
> **Type:** comparison
> **Created:** 2026-07-16
> **Updated:** 2026-07-16
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/releases/tag/v5.14.0 ingested: 2026-07-15 sha256: 68999245e18888716007954f12c075b1bd7f732e40e267a974998d57f72162eb blog_source: github:huggi...
> **Sources:**
>   - gh-v5140-2026-07-15.md
> **Links:**
- [[release-v560]]
- [[release-v0251]]
- [[release-v080]]
- [[v0.22.1]]
- [[v0.23.0]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/releases/tag/v5.14.0
ingested: 2026-07-15
sha256: 68999245e18888716007954f12c075b1bd7f732e40e267a974998d57f72162eb
blog_source: github:huggingface/transformers
---
# Release v5.14.0
# Release v5.14.0
## New Model additions
### Inkling (fresh from Thinking Machines): 975B total, 41B active
* Add Inkling model #47347 by @molbap @Cyrilvallez @eustlb and @zucchini-nlp 
![image](https://github.com/user-attachments/assets/051f819a-512f-4987-9bee-6e2fa2af3db7)
Inkling is a general-purpose multimodal model that accepts text, image and audio inputs and
generates text outputs. It is intended for use in English and other languages, and across
multiple coding languages. The model is designed to be used by developers building AI-
powered applications, including agentic and tool-use systems, coding assistants, chatbots, and
retrieval-augmented generation systems, and is suitable for general-purpose conversational
use, instruction-following, and other natural language and multimodal tasks. It is released with
open weights to support research, fine-tuning and integration into third-party products by
downstream developers.
### TIPSv2
![image](https://github.com/user-attachments/assets/2d9f21e5-05f8-4c36-93ef-22f03c089f52)
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/tipsv2)
* Add TIPSv2 (#46347) by @Ternura143 in [#46347](https://github.com/huggingface/transformers/pull/46347)
### TIPSv2 DPT
![image](https://github.com/user-attachments/assets/09c0d4da-6c1c-4229-bf02-a512ed435e50)
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/tipsv2_dpt)
* Add TIPSv2 (#46347) by @Ternura143 in [#46347](https://github.com/huggingface/transformers/pull/46347)
## :rotating_light: Breaking changes
GPTNeoX now remaps `embed_out` to `lm_head` and GPTBigCode has `_supports_attention_backend = True` enabled for vLLM compatibility; users relying on the previous weight naming or attention backend behavior for these models should update their code accordingly.
* :rotating_light: Fix GPTBigCode and GPTNeoX for the Transformers modelling backend for vLLM (#47198) by @hmellor
## Kernels
Several kernel-related fixes and improvements were made, including pinning the `kernels` dependency to a compatible version in the benchmark workflow, removing a deprecated `package_name` argument from `LocalLayerRepository`, and making the DeepGEMM Triton fallback more robust when `CUDA_HOME` is unset or misconfigured. Additionally, SDPA prefill was updated to leverage the FlashAttention kernel with `StaticCache`, yielding significant performance gains (up to 260% faster for large input sizes).
* Pin kernels to compatible version in benchmark workflow (#47339) by @tarekziade in [#47339]
* [Fix] Remove deprecated argument from `kernels` call (#47100) by @remi-or in [#47100]
* [Fix] Make DeepGEMM triton fallback more robust (#47126) by @remi-or in [#47126]
* [sdpa] Allow pre

## Summary

fill to use FA kernel with StaticCache (#47094) by @Cyrilvallez in [#47094]
## Generation
Generation improvements include adding Multi-Token Prediction (MTP) decoding support, static ensemble verification for speculative decoding to improve draft token acceptance rates, and a fix for crashes in greedy assisted generation with different tokenizers. A misleading double-negative warning message for `synced_gpus` in continuous batching mode was also corrected.
* [generation] Fix misleading synced_gpus warning in continuous batching (#47158) by @Partha-Shankar in [#47158]
* [generate] Add proper MTP support (#46229) by @Cyrilvallez in [#46229]
* Fix crash in greedy assisted generation with different tokenizers (#46936) by @Sunt-ing in [#46936]
* [Generation] Add static ensemble verification for lossy speculative decoding (#45979) by @kasakh in [#45979]
## Performance
Fixed a Flash Attention performance regression affecting models like Qwen3-VL and resolved a MoE decode optimization bug where the grouped-to-batched matrix multiplication switch was not applied to experts residing in submodels (e.g., VLMs with a nested text config).
* Fix FA performance regression (#47134) by @andreasgoulas in [#47134]
* Fix MoE decode optimization for experts living in a submodel (#47107) by @IlyasMoutawwakil in [#47107]
* Make doc builds faster (#47099) by @mishig25 in [#47099]
## Cache
Cache dispatch logic was simplified by introducing explicit layer-type mappings for sliding and static layers, reducing complexity in cache routing. Additionally, fixes were made for read-only cache failures in CPU CI environments and for MPS graph cache growth during variable-length batch training on Apple Silicon.
* Fix CI read-only cache failures by patching cached_files in conftest (#47043) by @ydshieh in [#47043]
* trainer: clear MPS graph cache via torch_empty_cache_steps (#45818) by @anagnorisis2peripeteia in [#45818]
* [cache] Simplify cache dispatch based on layer_types (#47118) by @Cyrilvallez in [#47118]
## Bugfixes and improvements
* ci: cover xet as well (runtime error) (#47338) by @tarekziade in [#47338]
* [docs] TokenizersBackend fallback (#47302) by @stevhliu in [#47302]
* Resolve continuous batching XPU availability checks at runtime (#47185) by @kaixuanliu in [#47185]
* [Nit] Add kernels_fallback_ok kwarg to is_flash_attn_N_available (#47318) by @remi-or in [#47318]
* [Nit] Add expectations for gemma4 tests on H100 (#47311) by @remi-or in [#47311]
* [docs] DeepGEMM requirements (#47324) by @stevhliu in [#47324]
* DeepGEMM shouldn't pad on SM90 (#47313) by @IlyasMoutawwakil in [#47313]
* Fix half-precision torch.compile crash in DETR-family sine position embeddings (#47238) by @David-Wu1119 in [#47238]
* Fix hardcoded paths in siglip checkpoint/vocab loading (#47178) by @XanxusCrypto in [#47178]
* Update AMD CI runner groups to amd-mi300 (#47307) by @Abdennacer-Badaoui in [#47307]
* Point to Gemma 4 model in Gemma4ForCausalLM docstring example (#47255) by @lefft in [#47

## Related Articles

- [[release-v560]]
- [[release-v0251]]
- [[release-v080]]
- [[v0.22.1]]
- [[v0.23.0]]
