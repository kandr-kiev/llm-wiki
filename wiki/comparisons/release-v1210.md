---
title: "Release v1.21.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - analysis
  - batch
  - computer-vision
  - dataset
  - foundation-model
  - gptq
  - image-generation
  - lora
  - multi-agent
  - nlp
  - preprocessing
  - prompt-tuning
  - pytorch
  - sft
  - speech-to-text
  - stable-diffusion
  - video-generation
  - whisper
---

# Release v1.21.0

> **Source:** gh-v1210-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/optimum-habana/releases/tag/v1.21.0 ingested: 2026-07-14 sha256: fc19767102c39d40e2efec8e50c8d179231864961bd92d9d480d22c7a9ab8eb2 blog_source: github:hug...
> **Sources:**
>   - gh-v1210-2026-07-14.md
> **Links:**
- [[Release v0.39.0]]
- [[Release 5.0.0]]
- [[v0.22.1]]
- [Issue #47321: AMD quark class not updated](http[Issue #8141: fix(muon): support ZeRO-1/2 reduce scatter](https://github.com/pytorch/pytorch/issues/8141)1: fix(muon): support ZeRO-1/2 reduce scatter]]

## Key Findings

---
source_url: https://github.com/huggingface/optimum-habana/releases/tag/v1.21.0
ingested: 2026-07-14
sha256: fc19767102c39d40e2efec8e50c8d179231864961bd92d9d480d22c7a9ab8eb2
blog_source: github:huggingface/optimum-habana
---
# Release v1.21.0
## Gemma3
- Gemma3 #2233 @imangohari1 
- Gemma3: Added Sliding Window Attention #2279 @imangohari1 
- fea(Gemma3/2): Added FusedRMSNorm #2281 @imangohari1 
## Qwen2.5-VL
- Add Qwen2.5-VL #2235 @mengker33 
- Qwen2.5VL: Fix pytorch sdpa path #2347 @mengker33 
## Wan2.2
- Add Wan2.2 support #2231 @miaojinc 
- Add multi-card inference support for Wan pipelines #2325 @dsocek 
## Qwen-Image
- Add Qwen-Image #2348 @atakaha 
## Model optimizations
- Added the SWA to Gemma2 #2210 @imangohari1 
- Add batch splitting in attention layer for decode to hide NIC latency #2334 @jthakurH 
- Pin bitsandbytes to 0.49.2 to fix ~43% perf regression #2369 @astachowiczhabana 
- Revert "Pin bitsandbytes to 0.49.2 to fix ~43% perf regression (#2369)" #2370 @astachowiczhabana 
## Diffusers
- Diffusers 0.35.1 #2288 @imangohari1 
## Other
- Update transformers test suite in Optimum-habana-4.55.4 #2294 @rkumar2patel 
- Fix readme table #2321 @regisss 
- Fix docs index table #2326 @dsocek 
- Update dataset names in README files #2330 @gplutop7 
- GaudiTrainer: Take accuracy measurement outside of timer #2331 @ugolowic 
- Remove redundant arguments from trl/sft ScriptArguments #2332 @AKloniecki 
- Apply correct attn_function for fsdp test cases #2335 @AKloniecki 
- Fix LlavaNext functional issues #2333 @pbielak 
- Fix .reshape(...) in GaudiCLIPAttention #2338 @pbielak 
- Fix gradient checkpointing conflicts with HPU graphs and improve dataset preprocessing in Whisper example #2337 @gplutop7 
- [video-comprehension] Fix failing example #2313 @ugolowic 
- Update flash attention args in grpo.py #2340 @pbielak 
- Set default generation config for TextGenerationPipeline and TextToAudioPipeline #2339 @AKloniecki 
- Align MLlama code with Transformers 4.55 #2319 @pbielak 
- Fix Mllama attention selection #2343 @pbielak 
- Fix None-handling in WhisperDecoder #2349 @gplutop7 
- Fix dead code in Gemma3TextModel forward and handle None attention_mask in gaudi_flash_attn_v1 #2346 @gplutop7 
- Add validation for negative_prompt_embeds to satisfy Coverity null-check analysis #2350 @gplutop7 
- Add validation ensuring negative_prompt_embeds is not None when CFG is enabled #2351 @gplutop7 
- Fix gradient checkpointing in GaudiGemmaDecoderLayer + align forward() signature with HF 4.55 #2353 @gplutop7 
- Add vision-language-modeling Lora finetuning support #2344 @mkpatel3-github 
- Fix GPT2 DynamicCache handling for Transformers 4.55 compatibility #2342 @gplutop7 
- Fix null handling when padding optional negative prompt batches #2357 @gplutop7 
- Pin optimum version (due to GPTQ deprecation) #2359 @karol-brejna-i 
- Fix incorrect indentation #2356 @AKloniecki 
- Temporarily remove broken examples for OH 1.21.0 release #2362 @gplutop7 
- Replace depreca

## Summary

See Key Findings for f[Issue #47321: AMD quark class not updated](http[Issue #8141: fix(muon): support ZeRO-1/2 reduce scatter](https://github.com/pytorch/pytorch/issues/8141)[Release 5.0.0]]
- [[v0.22.1]]
- [Issue #47321: AMD quark class not updated](http[Issue #8141: fix(muon): support ZeRO-1/2 reduce scatter](https://github.com/pytorch/pytorch/issues/8141)1: fix(muon): support ZeRO-1/2 reduce scatter]]
