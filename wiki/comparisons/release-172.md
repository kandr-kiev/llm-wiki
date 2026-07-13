---
title: "Release 1.7.2"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - async
  - data
  - docker
  - foundation-model
  - gpu
  - image-generation
  - machine-learning
  - multi-agent
  - nlp
  - optimization
  - pytorch
  - tutorial
  - zero-shot
---
# Release 1.7.2

> **Source:** gh-172-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/facebookresearch/parlai/releases/tag/1.7.2 ingested: 2026-07-11 sha256: 7387f4b5045c6a69e52de469d159b09ee5893df93e24c8638d035d1b7097c014 blog_source: github:facebook...
> **Sources:**
>   - gh-172-2026-07-11.md
> **Links:**
- [[year-in-review]]
- [[agentic-internet-bot-report]]
- [[arxiv260707760]]
- [[explainable-ai]]
- [[hidden-states]]

## Key Findings

---
source_url: https://github.com/facebookresearch/parlai/releases/tag/1.7.2
ingested: 2026-07-11
sha256: 7387f4b5045c6a69e52de469d159b09ee5893df93e24c8638d035d1b7097c014
blog_source: github:facebookresearch/parlai
---
# Release 1.7.2
## New Releases
* K2R: [Reason first, then respond: Modular Generation for Knowledge-infused Dialogue](https://arxiv.org/abs/2111.05204) (#4828)
* [ROSCOE: A Suite of Metrics for Scoring Step-by-Step Reasoning](https://arxiv.org/abs/2212.07919) (#4839, #4856, #4860, #4862)
* [The CRINGE Loss: Learning what language not to model](https://arxiv.org/abs/2211.05826) (#4871, #4876, #5036)
* Multi-party LIGHT: [Multi-Party Chat: Conversational Agents in Group Settings with Humans and Models](https://arxiv.org/abs/2304.13835) (aka MultiLIGHT) (#5043, #5041, #5045)
## New Features
* New releases coming with a public Docker image (#4868, #4874)
* flan-t5 models in ParlAI with fp16 (#4875)
* Factual Nucleus Sampling (#4890)
* [FSDP] Zero 3 Optimization Support (#4903, #4911)
* [BB3] New Module; New Customization (#4944, #4946)
* Workers' qualifications for the model chat (#4956)
* ClearML Logger (#4896)
* Async multi-party model chat (#4993)
* jsonfile retains original fields (#5033)
## Metrics
* Masked metrics (#4894)
* Custom compute loss (#4913)
## Bug fixes
* `GRM`: (#4796)
* Module Level Tasks (#4798)
* Display data with utf-16 (#4864) and emojis (#4833, #4934 (revert #4666))
* Reasoning task (#4883)
* TGA Compatibility with Pytorch>=1.13 (#4887)
* T5 Init Bug (#4897)
* Delay Loading NGram-Blocking on GPU (#4886)
* Fix starspace (#5003)
* Datatype option for Wizard of Internet task (#4962)
* T5 and GPT2 fixes (#5016, #5032)
## Datasets & Teachers
* Names Bias (#4836)
## Developers & Documentation
* Minor fixes and typos (#4841, #4873, #4879, #4892, #4901, #4902, #4912, #4947, #4949, #4954, #4959, #4975, #4987, #5026, #5044)
* Docker usage tutorial (#4874)
* Installation Instructions #5015
## Repository maintenance
* CircleCI (#4865, #4900, #4991, #4996, #4999, #5001, #5002, #5010, #5017, #5018, #5038)
* Skip crowdsourcing test decorator (#4957)

## Summary

See Key Findings for full content.

## Related Articles

- [[year-in-review]]
- [[agentic-internet-bot-report]]
- [[arxiv260707760]]
- [[explainable-ai]]
- [[hidden-states]]
