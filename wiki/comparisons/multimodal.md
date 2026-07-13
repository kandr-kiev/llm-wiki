---
title: "multimodal"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - architecture
  - async
  - audio-generation
  - best-practice
  - data
  - edge
  - foundation-model
  - guide
  - image-generation
  - llama
  - llm
  - mlops
  - multimodal
  - nlp
  - open-source
  - real-time
  - speech-to-text
  - use-case
---
# multimodal

> **Source:** multimodality-and-large-multimodal-models-lmms-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://huyenchip.com//2023/10/10/multimodal.html ingested: 2026-07-10 sha256: 6cd29537a72654c122e6ca4d8ee567f4aa636d180a4d867e24eef13f617a6699 blog_source: Chip Huyen --- Multimodalit...
> **Sources:**
>   - multimodality-and-large-multimodal-models-lmms-2026-07-10.md
> **Links:**
- [[animals-vs-ghosts]]
- [[generative-ai-strategy]]
- [[personal-growth]]
- [[ai-engineering-pitfalls]]
- [[diffusion-models]]

## Key Findings

---
source_url: https://huyenchip.com//2023/10/10/multimodal.html
ingested: 2026-07-10
sha256: 6cd29537a72654c122e6ca4d8ee567f4aa636d180a4d867e24eef13f617a6699
blog_source: Chip Huyen
---
Multimodality and Large Multimodal Models (LMMs)
- 
- 
- 
- 
Multimodality and Large Multimodal Models (LMMs) | Chip Huyen
- 
- 
[Chip Huyen](/)
[Blog](/blog/)
[Books](/books/)
[Events](/events/)
AI Guide**
- [AI Roadmap](/mlops/)
- [Good AI List](https://goodailist.com)
- [ML Interviews](https://huyenchip.com/ml-interviews-book/)
[List 100](/list-100/)
[Chip's Lib](https://instagram.com/chipslib)
[VN](https://huyenchip.com/vn/)
- 
**Table of Contents**
**
[Part 1. Understanding Multimodal](#part_1_understanding_multimodal)
- [Why multimodal](#why_multimodal)
- [Data modalities](#data_modalities)
- [Multimodal tasks](#multimodal_tasks)
- [Generation](#generation)
- [Vision-language understanding](#vision_language_understanding)
[Part 2. Fundamentals of Multimodal Training](#part_2_multimodal_training)
- [CLIP: Contrastive Language-Image Pre-training](#clip)
- [CLIP's high-level architecture](#clip_s_high_level_architecture)
- [Natural language supervision](#natural_language_supervision)
- [Contrastive learning](#contrastive_learning)
- [Classifier objective](#classifier_objective)
- [Language model objective](#lm_objective)
- [Contrastive objective](#contrastive_objective)
- [CLIP applications](#clip_applications)
- [Flamingo: the dawns of LMMs](#flamingo)
- [Flamingo's high-level architecture](#flamingo_s_high_level_architecture)
- [Data](#data)
- [Flamingo's vision encoder](#flamingo_s_vision_encoder)
- [Flamingo's language model](#flamingo_s_language_model)
- [TL;DR: CLIP vs. Flamingo](#clip_vs_flamingo)
[Part 3. Research Directions for LMMs](#part_3_research_directions_for_lmms)
- [Incorporating more data modalities](#incorporating_more_data_modalities)
- [Multimodal systems for instruction-following](#multimodal_systems_for_instruction_following)
- [Adapters for more efficient multimodal training](#adapters_for_more_efficient_multimodal_training)
- [Generating multimodal outputs](#generating_multimodal_outputs)
[Conclusion](#conclusion)
[Resources](#resources)
Table of Contents **
# Multimodality and Large Multimodal Models (LMMs)
Oct 10, 2023
• Chip Huyen
For a long time, each ML model operated in one data mode – text (translation, language modeling), image (object detection, image classification), or audio (speech recognition).
However, natural intelligence is not limited to just a single modality. Humans can read, talk, and see. We listen to music to relax and watch out for strange noises to detect danger. Being able to work with multimodal data is essential for us or any AI to operate in the real world.
OpenAI noted in their [GPT-4V system card](https://cdn.openai.com/papers/GPTV_System_Card.pdf) that “*incorporating additional modalities (such as image inputs) into LLMs is viewed by some as a key frontier in AI research and development*.”
Incorporating

## Summary

 additional modalities to LLMs (Large Language Models) creates LMMs (Large Multimodal Models). Not all multimodal systems are LMMs. For example, text-to-image models like Midjourney, Stable Diffusion, and Dall-E are multimodal but don’t have a language model component. Multimodal can mean one or more of the following:
- Input and output are of different modalities (e.g. text-to-image, image-to-text)
- Inputs are multimodal (e.g. a system that can process both text and images)
- Outputs are multimodal (e.g. a system that can generate both text and images)
This post covers multimodal systems in general, including LMMs. It consists of 3 parts.
- Part 1 covers the context for multimodality, including why multimodal, different data modalities, and types of multimodal tasks.
- Part 2 discusses the fundamentals of a multimodal system, using the examples of CLIP, which lays the foundation for many future multimodal systems, and Flamingo, whose impressive performance gave rise to LMMs.
- Part 3 discusses some active research areas for LMMs, including generating multimodal outputs and adapters for more efficient multimodal training, covering newer multimodal systems such as BLIP-2, LLaVA, LLaMA-Adapter V2, LAVIN, etc.
The post is long. Feel free to skip to the sections most interesting to you.
**⚠ Ambiguous terminology ⚠**
Multimodal data can also refer to multimodal distributions, e.g. bimodal distribution, which is different from multimodal data in this post.
---
**Table of contents**
[Part 1. Understanding Multimodal](#part_1_understanding_multimodal)
…. [Why multimodal](#why_multimodal)
…. [Data modalities](#data_modalities)
…. [Multimodal tasks](#multimodal_tasks)
…….. [Generation](#generation)
…….. [Vision-language understanding](#vision_language_understanding)
[Part 2. Fundamentals of Multimodal Training](#part_2_multimodal_training)
…. [CLIP: Contrastive Language-Image Pre-training](#clip)
…….. [CLIP’s high-level architecture](#clip_s_high_level_architecture)
…….. [Natural language supervision](#natural_language_supervision)
…….. [Contrastive learning](#contrastive_learning)
…….. [CLIP applications](#clip_applications)
…. [Flamingo: the dawns of LMMs](#flamingo)
…….. [Flamingo’s high-level architecture](#flamingo_s_high_level_architecture)
…….. [Data](#data)
…….. [Flamingo’s vision encoder](#flamingo_s_vision_encoder)
…….. [Flamingo’s language model](#flamingo_s_language_model)
…. [TL;DR: CLIP vs. Flamingo](#clip_vs_flamingo)
[Part 3. Research Directions for LMMs](#part_3_research_directions_for_lmms)
…. [Incorporating more data modalities](#incorporating_more_data_modalities)
…. [Multimodal systems for instruction-following](#multimodal_systems_for_instruction_following)
…. [Adapters for more efficient multimodal training](#adapters_for_more_efficient_multimodal_training)
…. [Generating multimodal outputs](#generating_multimodal_outputs)
[Conclusion](#conclusion)
[Resources](#resources)
---
## Part 1. Understanding Multimodal
## Why multimodal
Man

## Related Articles

- [[animals-vs-ghosts]]
- [[generative-ai-strategy]]
- [[personal-growth]]
- [[ai-engineering-pitfalls]]
- [[diffusion-models]]
