---
title: "ai engineering pitfalls"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - async
  - edge
  - foundation-model
  - guide
  - image-generation
  - llama
  - llm
  - mlops
  - open-source
  - prompt-engineering
  - use-case
---# ai engineering pitfalls

> **Source:** common-pitfalls-when-building-generative-ai-applications-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** -  [Chip Huyen](/) [Blog](/blog/) [Books](/books/) [Events](/events/) AI Guide** - [AI Roadmap](/mlops/) - [Good AI List](https://goodailist.com) - [ML Interviews](https://huyenchip.com/ml-interviews-...
> **Sources:**
>   - common-pitfalls-when-building-generative-ai-applications-2026-07-10.md
> **Links:**
- [[animals-vs-ghosts]]
- [[away]]
- [[chemical-hygiene]]
- [[automating-ai-away-2026-07-07]]
- [[how-to-engineer-prompts]]

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
[1. Use generative AI when you don't need generative AI](#1_use_generative_ai_when_you_don_t_need_generative_ai)
[2. Confuse ‘bad product' with ‘bad AI'](#2_confuse_bad_product_with_bad_ai)
[3. Start too complex](#3_start_too_complex)
[4. Over-index on early success](#4_over_index_on_early_success)
[5. Forgo human evaluation](#5_forgo_human_evaluation)
[6. Crowdsource use cases](#6_crowdsource_use_cases)
[Summary](#summary)
Table of Contents **
# Common pitfalls when building generative AI applications
Jan 16, 2025
• Chip Huyen
As we’re still in the early days of building applications with foundation models, it’s normal to make mistakes. This is a quick note with examples of some of the most common pitfalls that I’ve seen, both from public case studies and from my personal experience.
Because these pitfalls are common, if you’ve worked on any AI product, you’ve probably seen them before.
## 1. Use generative AI when you don't need generative AI
Every time there’s a new technology, I can hear the collective sigh of senior engineers everywhere: “Not everything is a nail.” Generative AI isn’t an exception — its seemingly limitless capabilities only exacerbate the tendency to use generative AI for everything.
A team pitched me the idea of using generative AI to optimize energy consumption. They fed a household’s list of energy-intensive activities and hourly electricity prices into an LLM, then asked it to create a schedule to minimize energy costs. Their experiments showed that this could help reduce a household’s electricity bill by 30%. Free money. Why wouldn’t anyone want to use their app?
I asked: “How does it compare to simply scheduling the most energy-intensive activities when electricity is cheapest? Say, doing your laundry and charging your car after 10pm?”
They said they would try it later and let me know. They never followed up, but they abandoned this app soon after. I suspect that this greedy scheduling can be quite effective. Even if it’s not, there are other much cheaper and more reliable optimization solutions than generative AI, like linear programming.
I’ve seen this scenario over and over again. A big company wants to use generative AI to detect anomalies in network traffic. Another wants to predict upcoming customer call volume. A hospital wants to detect whether a patient is malnourished (really not recommended).
It can often be beneficial to explore a new approach to get a sense of what’s possible, as long as you’re aware that your goal isn’t to solve a problem but to test a solution. “We solve the problem” and “We use generative AI” are two very different headlines, and unfortunately, so many peopl

## Summary

e would rather have the latter.
## 2. Confuse 'bad product' with 'bad AI'
At the other end of the spectrum, many teams dismiss gen AI as a valid solution for their problems because they tried it out and their users hated it. However, other teams successfully used gen AI for similar use cases. I could only look into two of these teams. In both cases, the issue wasn’t with AI, but with product.
Many people have told me that the technical aspects of their AI applications are straightforward. The hard part is user experience (UX). What should the product interface look like? How to seamlessly integrate the product into the user workflow? How to incorporate human-in-the-loop?
UX has always been challenging, but it’s even more so with generative AI. While we know that generative AI is changing how we read, write, learn, teach, work, entertain, etc., we don’t quite know how yet. What will the future of reading/learning/working be like?
Here are some simple examples to show how what users want can be counter-intuitive and need rigorous user study.
- 
My friend works on an application that summarizes meeting transcripts. Initially, her team focused on getting the right summary length. Would users prefer 3-sentence summaries or 5-sentence summaries? 
However, it turned out that their users didn’t care about the actual summary. They only wanted action items specific to them from each meeting.
- 
When [LinkedIn](https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product?_l=en_US) developed a chatbot for skill fit assessment, they discovered that users didn’t want correct responses. Users wanted helpful responses. 
For example, if a user asks a bot whether they’re a fit for a job and the bot responds with: “You’re a terrible fit,” this response might be correct but not very helpful to the user. Users want tips on what the gaps are and what they can do to close the gaps.
- 
Intuit built a chatbot to help users answer tax questions. Initially, they got lukewarm feedback — users didn’t find the bot useful. After investigation, they found out that users actually hated typing. Facing a blank chatbot, users didn’t know what the bot could do and what to type. 
So, for each interaction, Intuit added a few suggested questions for users to click on. This reduced the friction for users to use the bot and gradually built users’ trust. The feedback from users then became much more positive. 
*(Shared by [Nhung Ho](https://www.linkedin.com/in/nhungho/), VP of AI at Intuit, during our panel at Grace Hopper.)*
Because everyone uses the same models nowadays, the AI components of AI products are similar, and the differentiation is product.
## 3. Start too complex
Examples of this pitfall:
- Use an agentic framework when direct API calls work.
- Agonize over what vector database to use when a simple term-based retrieval solution (that doesn’t require a vectordb) works.
- Insist on finetuning when prompting works.
- Use semantic caching.


## Related Articles

- [[animals-vs-ghosts]]
- [[away]]
- [[chemical-hygiene]]
- [[automating-ai-away-2026-07-07]]
- [[how-to-engineer-prompts]]
