---
title: "Release v5.13.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - architecture
  - audio-generation
  - batch
  - computer-vision
  - devops
  - efficiency
  - embedding
  - foundation-model
  - image-generation
  - multi-agent
  - multimodal
  - nlp
  - onnx
  - open-source
  - optimization
  - parallel
  - performance
  - real-time
  - research
  - speech-to-text
  - standards
  - streaming
  - video-generation
  - web
  - whisper
---
# Release v5.13.0

> **Source:** release-v5130-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/releases/tag/v5.13.0 ingested: 2026-07-10 sha256: f78983f21bd12b926ef84385ba3596cba40e4a4ac703677621845400e05eab27 blog_source: github --- #...
> **Sources:**
>   - release-v5130-2026-07-10.md
> **Links:**
- [[release-v5120]]
- [[release-v5110]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[patch-release-v5104]]
- [[release-v0390]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/releases/tag/v5.13.0
ingested: 2026-07-10
sha256: f78983f21bd12b926ef84385ba3596cba40e4a4ac703677621845400e05eab27
blog_source: github
---
# Release v5.13.0
## Release Notes
# Release v5.13.0
## New Model additions
### KimiK 2.5, 2.6, and 2.7
![image](https://github.com/user-attachments/assets/c24d2232-a9b4-413b-a2c8-58d013b6dfbd)
This release includes the architecture for Kimi 2.5 which is used by 2.5-2.7:
Kimi K2.5 is an open-source, native multimodal agentic model that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration. The model was proposed in [Kimi K2.5: Visual Agentic Intelligence](https://www.kimi.com/en/blog/kimi-k2-5) and further improved in [Kimi K2.6: Advancing Open-Source Coding](Kimi K2.5: Visual Agentic Intelligence).
Kimi K2.5 achieves significant improvements on complex, end-to-end coding tasks, generalizing robustly across programming languages (Rust, Go, Python) and domains spanning front-end, DevOps, and performance optimization. The model is capable of transforming simple prompts and visual inputs into production-ready interfaces and lightweight full-stack workflows, generating structured layouts, interactive elements, and rich animations with deliberate aesthetic precision.
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/kimi_k25)
* Add new model: Kimi2-6 (#45630) by @zucchini-nlp in [#45630](https://github.com/huggingface/transformers/pull/45630)
### MiMo-V2-Flash
![image](https://github.com/user-attachments/assets/8bd8d5f0-0381-4f8c-8ada-0203e11ff494)
**MiMo-V2-Flash** is a Mixture-of-Experts (MoE) language model developed by the Xiaomi MiMo team. Designed to establish a new balance between long-context modeling capabilities and inference efficiency, the model is built for strong performance in complex reasoning and agentic tasks. Trained on 27T tokens with native 32k sequence lengths, MiMo-V2-Flash seamlessly supports an extended **256K context window** while significantly reducing KV-cache storage compared to standard global attention models.
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/mimo_v2_flash)
* Add Xiaomi MiMo-V2 (#45144) by @casinca in [#45144](https://github.com/huggingface/transformers/pull/45144)
### Nemotron 3.5 ASR
![image](https://github.com/user-attachments/assets/597bbb9c-b046-4e47-b9fd-f242e0a5b04d)
Nemotron 3.5 ASR is a 600M-parameter multilingual speech recognition model from NVIDIA, built for high-quality transcription in both low-latency streaming and high-throughput batch settings, with native punctuation and capitalization. For streaming, it offers configurable chunk sizes—80ms, 160ms, 560ms, and 1120ms, letting users trade off latency against accuracy to suit their application. Its cache-aware FastConformer-RNNT architecture is central to this capability: unlike trad

## Summary

itional buffered streaming, which repeatedly reprocesses overlapping audio windows, the model processes only each new incoming chunk while reusing cached encoder context from prior chunks. This eliminates redundant computation, significantly improves efficiency, and minimizes end-to-end delay without sacrificing accuracy, making it well suited to real-time transcription workloads.
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron3_5_asr)
* Add Nemotron 3.5 ASR Streaming (#46565) by @eustlb in [#46565](https://github.com/huggingface/transformers/pull/46565)
### NemotronAsrStreaming
Nemotron ASR Streaming is a 600M-parameter English speech recognition model from NVIDIA, built for high-quality transcription in both low-latency streaming and high-throughput batch settings, with native punctuation and capitalization. For streaming, it offers configurable chunk sizes—80ms, 160ms, 560ms, and 1120ms, letting users trade off latency against accuracy to suit their application. Its cache-aware FastConformer-RNNT architecture is central to this capability: unlike traditional buffered streaming, which repeatedly reprocesses overlapping audio windows, the model processes only each new incoming chunk while reusing cached encoder context from prior chunks. This eliminates redundant computation, significantly improves efficiency, and minimizes end-to-end delay without sacrificing accuracy, making it well suited to real-time transcription workloads.
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron_asr_streaming)
* Add Nemotron ASR Streaming (#46332) by @eustlb in [#46332](https://github.com/huggingface/transformers/pull/46332)
### Qwen3 ASR
![image](https://github.com/user-attachments/assets/41ed13e3-a0bf-463a-8473-bc6beb8ebd73)
Qwen3 ASR is an automatic speech recognition model from Alibaba's Qwen team that combines a Whisper-style audio encoder with a Qwen3 language model decoder for speech-to-text transcription. The model supports automatic language detection and multilingual transcription.
A forced aligner model is also included. It can be used to timestamp a provided transcript and its audio. It uses the same audio encoder model with a classification head that predicts a word's length. This model can be used with the transcript from any ASR model (see the example below with Parakeet CTC).
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/qwen3_asr)
* Qwen3 ASR and Forced Aligner (#43838) by @mbtariq82 in [#43838](https://github.com/huggingface/transformers/pull/43838)
### ZAYA
![image](https://github.com/user-attachments/assets/2935eba8-ab74-455c-9d44-f088636b2785)
ZAYA1 is a 760M active / 8.4B total parameter MoE language model trained by Zyphra. It combines Compressed
Convolutional Attention (CCA), a nonlinear ZAYA1 router, and residual scaling.
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/za

## Related Articles

- [[release-v5120]]
- [[release-v5110]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[patch-release-v5104]]
- [[release-v0390]]
