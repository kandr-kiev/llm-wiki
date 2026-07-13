---
title: "Release v5.11.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - api
  - architecture
  - benchmark
  - ci-cd
  - computer-vision
  - cost
  - cuda
  - docker
  - efficiency
  - fine-tuning
  - foundation-model
  - gpu
  - image-generation
  - library
  - machine-learning
  - multi-agent
  - nlp
  - parallel
  - performance
  - pipeline
  - quantization
  - real-time
  - reinforcement-learning
  - scalability
  - search
  - stable-diffusion
  - standards
  - training
  - use-case
  - video-generation
  - workflow
---
# Release v5.11.0

> **Source:** release-v5110-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/releases/tag/v5.11.0 ingested: 2026-07-10 sha256: 06570ba36bc42e8c69cbf21fa439f531e574859e093adefa190e032843fa9bfc blog_source: github --- #...
> **Sources:**
>   - release-v5110-2026-07-10.md
> **Links:**
- [[release-v0390]]
- [[patch-release-v5104]]
- [[release-v180]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[pytorch-2130-release]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/releases/tag/v5.11.0
ingested: 2026-07-10
sha256: 06570ba36bc42e8c69cbf21fa439f531e574859e093adefa190e032843fa9bfc
blog_source: github
---
# Release v5.11.0
## Release Notes
# Release v5.11.0
## New Model additions
### DiffusionGemma
![image](https://github.com/user-attachments/assets/5081e449-6374-4076-bd96-d295c8334ca4)
DiffusionGemma is engineered to reduce the sequential bottlenecks of standard causal language models by employing an encoder-decoder architecture specifically optimized for inference speed. During inference, DiffusionGemma leverages multi-canvas sampling, where rather than generating one token at a time, the model iteratively denoises a full block of tokens using a diffusion sampler. This block-autoregressive approach facilitates text generation at higher speeds compared to traditional sequential generation methods.
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/diffusion_gemma)
* GPU go brr (#46540) by @gante in [#46540](https://github.com/huggingface/transformers/pull/46540)
### DeepSeek-V3.2
![image](https://github.com/user-attachments/assets/24c9694d-eeae-402c-9a98-f7a3971dd9d0)
DeepSeek-V3.2-Exp is an experimental model from DeepSeek-AI that introduces DeepSeek Sparse Attention (DSA), a trainable, fine-grained sparse attention mechanism designed to improve training and inference efficiency in long-context scenarios. Built on top of DeepSeek-V3.1-Terminus with a 685B-parameter Mixture-of-Experts backbone, it reduces the quadratic cost of attention over long sequences by attending only to a selected subset of past tokens while maintaining virtually identical benchmark performance. The work was extended in DeepSeek-V3.2 which pairs DSA with scalable reinforcement learning and achieves gold-medal level results on competition math and competitive programming benchmarks.
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_v32) | [Paper](https://huggingface.co/papers/2512.02556)
* Add deepseek 3.2 exp (#41251) by @ArthurZucker in [#41251](https://github.com/huggingface/transformers/pull/41251)
## Kernels
The `KernelConfig` API was extended to support n-to-1 module fusion and parameter transformation, simplifying how custom kernels are integrated with Transformers modules. Additional fixes include resolving a dtype mismatch in the Mamba2 CUDA kernel path for NemotronH/Zamba2, adding fine-grained fp8/fp4 Triton kernel support, and correcting the FalconMamba fast-path warning to recommend `pip install kernels` instead of `mamba-ssm`.
* Extended & simplified n-to-1 kernel fusion via KernelConfig (#46339) by @michaelbenayoun in [#46339]
* Triton finegrained fp8/fp4 (#46407) by @IlyasMoutawwakil in [#46407]
* Fix dtype mismatch in NemotronH/Zamba2 Mamba2 CUDA-kernel path (`out_proj`) (#46487) by @yuekaizhang in [#46487]
* fix(falcon_mamba): recommend `pip install kernels` in fast-path warning (#46

## Summary

343) by @Anai-Guo in [#46343]
## Parallelization
Fixed model parallel beam search bugs in the Qwen2-VL, Qwen2.5-VL, and Qwen3-VL MoE model families, and added documentation for tensor parallelism support with continuous batching.
* [docs] tp for continuous batching (#46019) by @stevhliu in [#46019]
* revisit history parallel beam search tests to avoid unnecessary fix (#46495) by @kaixuanliu in [#46495]
* fix qwen series VL model's model parallel bug (#46316) by @kaixuanliu in [#46316]
## Bugfixes and improvements
* Fix the offsets in processing (#46525) by @zucchini-nlp in [#46525]
* Fix buggy action sha pin (#46534) by @ydshieh in [#46534]
* Fix trailing comma bug in DataCollatorForLanguageModeling example (#46527) by @JemmaUZH in [#46527]
* Fix missing Gemma4Processor._compute_audio_num_tokens (#46416) by @csantosbh in [#46416]
* Fix InternVL models (#46524) by @hmellor in [#46524]
* fix(afmoe): reduce tokens in test_compile_static_cache to avoid flaky bfloat16 drift (#46521) by @ydshieh in [#46521]
* [CB] Add a "max_requests_per_batch" parameter (#46434) by @remi-or in [#46434]
* revamp cv docs and fix rf-detr (#46219) by @merveenoyan in [#46219]
* Update hub metadata (#46379) by @zucchini-nlp in [#46379]
* extend DeepseekV4FlashIntegrationTest to non-cuda device (#46517) by @sywangyi in [#46517]
* [docs] deepgemm (#46361) by @stevhliu in [#46361]
* [fix] regression introduced by #45534 (#46456) by @eustlb in [#46456]
* Use torchvision's native LANCZOS interpolation instead of PIL fallback (#46496) by @NicolasHug in [#46496]
* Add debugging info in `pr-ci-caller.yml` (#46505) by @ydshieh in [#46505]
* Fix tests: 'Cohere2MoeModel' object has no attribute 'hf_device_map' (#46337) by @kaixuanliu in [#46337]
* Bump the actions group across 1 directory with 19 updates (#46414) by @dependabot[bot] in [#46414]
* Log some information in `.github/workflows/pr-ci-post-dashboard-link.yml` (#46499) by @ydshieh in [#46499]
* feat(quantizers): support non-weight param names in TorchAo safetensors loading (#46325) by @agesf in [#46325]
* docs: fix typo in make_list_of_images docstring (#46469) by @ramkumar27072006 in [#46469]
* add XPU expectation for deepseek_ocr2 model tests (#46492) by @kaixuanliu in [#46492]
* Fix sapiens2 tests: add XPU device expectations (#46488) by @kaixuanliu in [#46488]
* Add vLLM smoke test to CI (#46383) by @hmellor in [#46383]
* extend deepseek v4 test to xpu (#46366) by @sywangyi in [#46366]
* Added cosmos3 model (#46146) by @MaciejBalaNV in [#46146]
* fbgemm_fp8:Keep the current device aligned with the input tensor (#46403) by @kaixuanliu in [#46403]
* [Modular] Add `no_inherit_decorators` and fixup wrong RoPE related inheritances (#46440) by @Bissmella in [#46440]
* skip deepgemm test except cuda (#46090) by @jiqing-feng in [#46090]
* Fix/video classification pipeline video processor (#46256) by @J3r3myPerera in [#46256]
* ci: less flaky test_assisted_decoding_matches_greedy_search_1_same (#46445) by @ydshieh in [#46445]
* Fi

## Related Articles

- [[release-v0390]]
- [[patch-release-v5104]]
- [[release-v180]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[pytorch-2130-release]]
