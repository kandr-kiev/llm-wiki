---
title: "ai oss"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - async
  - best-practice
  - edge
  - guide
  - image-generation
  - llama
  - llm
  - mlops
  - news
  - open-source
  - research
  - use-case
---# ai oss

> **Source:** what-i-learned-from-looking-at-900-most-popular-open-source-ai-tools-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** -  [Chip Huyen](/) [Blog](/blog/) [Books](/books/) [Events](/events/) AI Guide** - [AI Roadmap](/mlops/) - [Good AI List](https://goodailist.com) - [ML Interviews](https://huyenchip.com/ml-interviews-...
> **Sources:**
>   - what-i-learned-from-looking-at-900-most-popular-open-source-ai-tools-2026-07-10.md
> **Links:**
- [[generative-ai-strategy]]
- [[personal-growth]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[ai-engineering-pitfalls]]
- [[llm-research-open-challenges]]

## Key Findings

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
[Data](#data)
- [How to add missing repos](#add_missing_repos)
[The New AI Stack](#the_new_ai_stack)
- [AI stack over time](#ai_stack_over_time)
- [Applications](#applications)
- [AI engineering](#ai_engineering)
- [Model development](#model_development)
- [Infrastructure](#infrastructure)
[Open source AI developers](#open_source_ai_developers)
- [One-person billion-dollar companies?](#the_rise_of_one_person_companies)
- [1 million commits](#1_million_commits)
[The growing China's open source ecosystem](#the_growing_china_open_source_ecosystem)
[Live fast, die young](#live_fast_die_young)
[My personal favorite ideas](#my_personal_favorite_ideas)
[Conclusion](#conclusion)
Table of Contents **
# What I learned from looking at 900 most popular open source AI tools
Mar 14, 2024
• Chip Huyen
[*[Hacker News discussion](https://news.ycombinator.com/item?id=39709912), [LinkedIn discussion](https://www.linkedin.com/posts/chiphuyen_generativeai-aiapplications-llmops-activity-7174153467844820993-ztSE), [Twitter thread](https://twitter.com/chipro/status/1768388213008445837)*]
**Update (Feb 2026)**: *The full list of open source AI repos is hosted at [Good AI List](https://goodailist.com), updated daily. It’s balooned to 15K repos, and you can submit missing repos. You can also find some of them on my [cool-llm-repos](https://github.com/stars/chiphuyen/lists/cool-llm-repos) list on GitHub.*
Four years ago, I did an analysis of the [open source ML ecosystem](https://huyenchip.com/2020/06/22/mlops.html). Since then, the landscape has changed, so I revisited the topic. This time, I focused exclusively on the stack around foundation models.
## Data
I searched GitHub using the keywords `gpt`, `llm`, and `generative ai`. If AI feels so overwhelming right now, it’s because it is. There are 118K results for `gpt` alone.
To make my life easier, I limited my search to the repos with at least 500 stars. There were 590 results for `llm`, 531 for `gpt`, and 38 for `generative ai`. I also occasionally checked GitHub trending and social media for new repos.
After MANY hours, I found 896 repos. Of these, 51 are tutorials (e.g. [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)) and aggregated lists (e.g. [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)). While these tutorials and lists are helpful, I’m more interested in software. I still include them in the final list, but the analysis is done with the 845 software repositories.
It was a painful but rewarding process. It gave me a much better understanding of what people are working on, how incredibly collaborative the open source com

## Summary

munity is, and just how much China’s open source ecosystem diverges from the Western one.
## The New AI Stack
I think of the AI stack as consisting of 3 layers: infrastructure, model development, and application development.
![Generative AI Stack](/assets/pics/ai-oss/1-ai-stack.png)
- 
**Infrastructure**
At the bottom is the stack is infrastructure, which includes toolings for serving ([vllm](https://github.com/vllm-project/vllm), [NVIDIA’s Triton](https://github.com/triton-inference-server/server)), compute management ([skypilot](https://github.com/skypilot-org/skypilot)), vector search and database ([faiss](https://github.com/facebookresearch/faiss), [milvus](https://milvus.io/), [qdrant](https://github.com/qdrant/qdrant), [lancedb](https://github.com/lancedb/lancedb)), ….
- 
**Model development**
This layer provides toolings for developing models, including frameworks for modeling & training (transformers, pytorch, DeepSpeed), inference optimization (ggml, openai/triton), dataset engineering, evaluation, ….. Anything that involves changing a model’s weights happens in this layer, including finetuning.
- 
**Application development**
With readily available models, anyone can develop applications on top of them. This is the layer that has seen the most actions in the last 2 years and is still rapidly evolving. This layer is also known as AI engineering.
Application development involves prompt engineering, RAG, AI interface, …
Outside of these 3 layers, I also have two other categories:
- **Model repos**, which are created by companies and researchers to share the code associated with their models. Examples of repos in this category are `CompVis/stable-diffusion`, `openai/whisper`, and `facebookresearch/llama`.
- **Applications** built on top of existing models. The most popular types of applications are coding, workflow automation, information aggregation, …
**Note**: *In an older version of this post, **Applications** was included as another layer in the stack.*
### AI stack over time
I plotted the cumulative number of repos in each category month-over-month. There was an explosion of new toolings in 2023, after the introduction of Stable Diffusion and ChatGPT. The curve seems to flatten in September 2023 because of three potential reasons.
- I only include repos with at least 500 stars in my analysis, and it takes time for repos to gather these many stars.
- Most low-hanging fruits have been picked. What is left takes more effort to build, hence fewer people can build them.
- People have realized that it’s hard to be competitive in the generative AI space, so the excitement has calmed down. Anecdotally, in early 2023, all AI conversations I had with companies centered around gen AI, but the recent conversations are more grounded. Several even brought up scikit-learn. I’d like to revisit this in a few months to verify if it’s true.
![Generative AI Stack Over Time](/assets/pics/ai-oss/2-ai-timeline.png)
In 2023, the layers that saw the highest in

## Related Articles

- [[generative-ai-strategy]]
- [[personal-growth]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[ai-engineering-pitfalls]]
- [[llm-research-open-challenges]]
