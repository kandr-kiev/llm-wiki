---
title: "genai platform"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - architecture
  - async
  - best-practice
  - edge
  - guide
  - image-generation
  - llama
  - llm
  - mlops
  - open-source
---
# genai platform

> **Source:** building-a-generative-ai-platform-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://huyenchip.com//2024/07/25/genai-platform.html ingested: 2026-07-10 sha256: a8c3af6327ac07c17d8a607d6d501d4e29daa646d7a1d71f73eb7fa134c45dcd blog_source: Chip Huyen --- Building...
> **Sources:**
>   - building-a-generative-ai-platform-2026-07-10.md
> **Links:**
- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[the-illustrated-retrieval-transformer-2026-07-07]]
- [[animals-vs-ghosts]]
- [[open-domain-question-answering]]

## Key Findings

---
source_url: https://huyenchip.com//2024/07/25/genai-platform.html
ingested: 2026-07-10
sha256: a8c3af6327ac07c17d8a607d6d501d4e29daa646d7a1d71f73eb7fa134c45dcd
blog_source: Chip Huyen
---
Building A Generative AI Platform
- 
- 
- 
- 
Building A Generative AI Platform | Chip Huyen
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
[Step 1. Enhance Context](#step_1_enhance_context)
- [RAGs](#rags)
- [RAGs with tabular data](#rags_with_tabular_data)
- [Agentic RAGs](#agentic_rags)
- [Query rewriting](#query_rewriting)
[Step 2. Put in Guardrails](#step_2_put_in_guardrails)
- [Input guardrails](#input_guardrails)
- [Leaking private information to external APIs](#leaking_private_information_to_external_apis)
- [Model jailbreaking](#jailbreaking)
- [Output guardrails](#output_guardrails)
- [Output quality measurement](#output_quality_measurement)
- [Failure management](#failure_management)
- [Guardrail tradeoffs](#guardrail_tradeoffs)
[Step 3. Add Model Router and Gateway](#step_3_add_model_router_and_gateway)
- [Router](#router)
- [Gateway](#gateway)
[Step 4. Reduce Latency with Cache](#step_4_reduce_latency_with_cache)
- [Prompt cache](#prompt_cache)
- [Exact cache](#exact_cache)
- [Semantic cache](#semantic_cache)
[Step 5. Add Complex Logic and Write Actions](#step_5_add_complex_logic_and_write_actions)
- [Complex logic](#complex_logic)
- [Write actions](#write_actions)
[Observability](#observability)
- [Metrics](#metrics)
- [Logs](#logs)
- [Traces](#traces)
[AI Pipeline Orchestration](#ai_pipeline_orchestration)
[Conclusion](#conclusion)
[References and Acknowledgments](#references_and_acknowledgments)
Table of Contents **
# Building A Generative AI Platform
Jul 25, 2024
• Chip Huyen
After studying how companies deploy generative AI applications, I noticed many similarities in their platforms. This post outlines the common components of a generative AI platform, what they do, and how they are implemented. I try my best to keep the architecture general, but certain applications might deviate. This is what the overall architecture looks like.
![Overview of a genai platform](/assets/pics/genai-platform/1-genai-platform.png)
This is a pretty complex system. This post will start from the simplest architecture and progressively add more components. In its simplest form, your application receives a query and sends it to the model. The model generates a response, which is returned to the user. There are no guardrails, no augmented context, and no optimization. The **Model API** box refers to both third-party APIs (e.g., OpenAI, Google, Anthropic) and self-hosted APIs.
![Overview of a genai platform](/assets/pics/genai-platform/2.png)
From this, you can add more components

## Summary

 as needs arise. The order discussed in this post is common, though you don’t need to follow the exact same order. A component can be skipped if your system works well without it. Evaluation is necessary at every step of the development process.
- Enhance context input into a model by giving the model access to external data sources and tools for information gathering.
- Put in guardrails to protect your system and your users.
- Add model router and gateway to support complex pipelines and add more security.
- Optimize for latency and costs with cache.
- Add complex logic and write actions to maximize your system’s capabilities.
Observability, which allows you to gain visibility into your system for monitoring and debugging, and orchestration, which involves chaining all the components together, are two essential components of the platform. We will discuss them at the end of this post.
**» What this post is not «**
*This post focuses on the overall architecture for deploying AI applications. It discusses what components are needed and considerations when building these components. It’s not about how to build AI applications and, therefore, does NOT discuss model evaluation, application evaluation, prompt engineering, finetuning, data annotation guidelines, or chunking strategies for RAGs. All these topics are covered in my upcoming book [AI Engineering](https://oreillymedia.pxf.io/GmaeBn).*
## Step 1. Enhance Context
The initial expansion of a platform usually involves adding mechanisms to allow the system to augment each query with the necessary information. Gathering the relevant information is called context construction.
Many queries require context to answer. The more relevant information there is in the context, the less the model has to rely on its internal knowledge, which can be unreliable due to its training data and training methodology. Studies have shown that having access to relevant information in the context can help the model generate more detailed responses while reducing hallucinations ([Lewis et al.](https://arxiv.org/abs/2005.11401), 2020).
For example, given the query “Will Acme’s fancy-printer-A300 print 100pps?”, the model will be able to respond better if it’s given the specifications of fancy-printer-A300. (Thanks Chetan Tekur for the example.)
Context construction for foundation models is equivalent to feature engineering for classical ML models. They serve the same purpose: giving the model the necessary information to process an input.
In-context learning, learning from the context, is a form of continual learning. It enables a model to incorporate new information continually to make decisions, preventing it from becoming outdated. For example, a model trained on last-week data won’t be able to answer questions about this week unless the new information is included in its context. By updating a model’s context with the latest information, e.g. fancy-printer-A300’s latest specifications, the model remains up-to-date an

## Related Articles

- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[the-illustrated-retrieval-transformer-2026-07-07]]
- [[animals-vs-ghosts]]
- [[open-domain-question-answering]]
