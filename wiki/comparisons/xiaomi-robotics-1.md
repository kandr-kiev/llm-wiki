---
title: "xiaomi robotics 1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - async
  - commercial
  - computer-vision
  - data
  - foundation-model
  - image-generation
  - instruction-tuning
  - news
  - nlp
  - open-source
  - pipeline
  - policy
  - real-time
  - scalability
  - training
  - use-case
  - video-generation
---

# xiaomi robotics 1

> **Source:** xiaomi-robotics-1-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** [XiaomiRobotics](/index.html)[Back to Home](/index.html)[Overview](#overview)[Data](#data)[Method](#method)[Applications](#applications)[Conclusion](#conclusion)[Citation](#citation)# Xiaomi-Robotics-...
> **Sources:**
>   - xiaomi-robotics-1-2026-07-20.md
> **Links:**
- [[kimi k3]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[ai music video arena claude vs gpt 5.6]]
- [[karpathy]]
- [[Automating away]]

## Key Findings

[XiaomiRobotics](/index.html)[Back to Home](/index.html)[Overview](#overview)[Data](#data)[Method](#method)[Applications](#applications)[Conclusion](#conclusion)[Citation](#citation)# Xiaomi-Robotics-1
July 16, 2026Xiaomi-Robotics-1 is a ready-to-use robot foundation model trained on over 100K hours of real-world manipulation trajectories.
[- - Report](https://arxiv.org/abs/2607.15330)[Code](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1)[Model](https://huggingface.co/XiaomiRobotics)Breaking the data barrier. Scaling robot policy models with embodiment-free pre-training.
Foundation models in language and vision keep moving the frontier by riding empirical scaling laws: capability tracks data, parameters, and compute. Robotics has missed out. Large-scale, high-quality data is hard to come by, and that scarcity, more than anything else, has capped how far policy models could scale. What robots can do under genuinely large-scale training remained largely an open question. We take a step toward answering it. Xiaomi-Robotics-1 combines large-scale embodiment-free (UMI) pre-training with a modest amount of real-robot data in a post-training stage. We study how the model behaves as it scales.
## Data
Everything Xiaomi-Robotics-1 can do starts from data. For pre-training, we use 100,000 hours of embodiment-free (UMI) trajectories spanning more than 1,700 scenarios (household, commercial premises, industrial sites, and outdoor spaces), covering a diverse range of tasks. We develop a scalable auto-labeling pipeline that first divides trajectories into fixed-length segments and then annotates each segment with language descriptions of scene state transitions.
![Pretrain data overview](https://robotics.xiaomi.com/robot-static-resource/xiaomi-robotics-1/pretrain_data.jpg)For post-training, we leverage cross-embodiment datasets containing in-house robot data, filtered open-sourced robot data, and a set of high-quality UMI data. For the in-house data, we collected over 7,200 hours of real-robot data in real homes, covering tasks like tidying a sofa, sorting a shoe cabinet, and putting away kitchenware. The UMI data are manually annotated with temporal segments and instruction prompts, which differ from the auto-labeled state-transition descriptions used in the pre-training data.
![Posttrain data overview](https://robotics.xiaomi.com/robot-static-resource/xiaomi-robotics-1/posttrain_data.jpg)## Method
Following the training paradigm of LLMs, the training of Xiaomi-Robotics-1 consists of two stages: pre-training and post-training. The first stage learns general representations for action generation from large-scale UMI data, while the post-training stage aligns the model with real robot embodiments and instruction-following capabilities.
### Pre-training
Pre-training is about breadth: exposing the model to as much of the real world as possible. We use the embodiment-free UMI data described above, which spans a broad range of environments and tasks. At this s

## Summary

cale, manual labeling is infeasible. Thus, we built an automatic annotation pipeline powered by a strong vision-language model. Long videos are split into fixed-length clips, and the VLM describes the state transition of grippers and interacting objects within each clip. The result is a large-scale corpus of real-world manipulation trajectories, each annotated with precise language descriptions. These allow the model to learn action generation that drives the scene toward the state transitions described by the language.
An encouraging finding is that pre-training shows a clean scaling behavior: as data and model size grow, validation action error steadily decreases.
![Pretrain scaling curve](https://robotics.xiaomi.com/robot-static-resource/xiaomi-robotics-1/pretrain_scaling.jpg)### Post-training
Post-training aims to align the strong action-generation capabilities acquired from pre-training with real robot embodiments and natural-language instruction following along two axes. Embodiment alignment uses high-quality cross-embodiment real-robot data to map the general action-generation ability onto actual robots. Instruction alignment shifts the model from "generating actions given a description of scene state transitions" to "understanding a natural-language instruction and executing it directly."
After post-training, Xiaomi-Robotics-1 can be used out-of-the-box to perform a wide range of mobile manipulation tasks in the real world. We evaluate the post-trained model in unseen environments with unseen object instances to understand whether the scaling behaviors from pre-training can transfer to real-robot performance after post-training.
The answer is yes. As we increase the amount of pre-training data and model size, real-robot success rate rises steadily and predictably. That is, a stronger pre-trained model yields better real-robot performance. The scaling gains show no signs of saturation: the real-robot success rate after post-training keeps improving as the model consumes more data or scales up during pre-training.
![Post-training scaling: real-robot success rate vs data ratio and model size](https://robotics.xiaomi.com/robot-static-resource/xiaomi-robotics-1/posttrain_scaling.jpg)## Applications
After post-training, Xiaomi-Robotics-1 can serve as a strong robot foundation model for downstream applications. We put Xiaomi-Robotics-1 to use in two complementary downstream settings. Efficient adaptation to new tasks specializes the model to brand-new, highly complex real-robot tasks from a few hours of data per task. Simulation benchmarks probe its capabilities in mainstream suites that emphasize generalization.
### Efficient Adaptation to New Tasks
Xiaomi-Robotics-1 can learn new tasks with high data efficiency. The model picks up tasks like phone packing, printer refilling, laundry loading, and box packing from just a few hours of real-robot demonstrations per task. With an average of under 10 hours of demonstrations per task, it already reac

## Related Articles

- [[kimi k3]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[ai music video arena claude vs gpt 5.6]]
- [[karpathy]]
- [[Automating away]]
