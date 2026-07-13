---
title: "llm research open challenges"
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
  - open-source
  - research
  - use-case
---# llm research open challenges

> **Source:** open-challenges-in-llm-research-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** # Open challenges in LLM research Aug 16, 2023 • Chip Huyen [*[LinkedIn discussion](https://www.linkedin.com/posts/chiphuyen_llm-airesearch-generativeai-activity-7097619722363408385-s5Cp), [Twitter th...
> **Sources:**
>   - open-challenges-in-llm-research-2026-07-10.md
> **Links:**
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[animals-vs-ghosts]]
- [[finding-the-best-sleep-tracker]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]

## Key Findings

# Open challenges in LLM research
Aug 16, 2023
• Chip Huyen
[*[LinkedIn discussion](https://www.linkedin.com/posts/chiphuyen_llm-airesearch-generativeai-activity-7097619722363408385-s5Cp), [Twitter thread](https://twitter.com/chipro/status/1691858084824838427)*]
Never before in my life had I seen so many smart people working on the same goal: making LLMs better. After talking to many people working in both industry and academia, I noticed the 10 major research directions that emerged. The first two directions, hallucinations and context learning, are probably the most talked about today. I’m the most excited about numbers 3 (multimodality), 5 (new architecture), and 6 (GPU alternatives).
## 1. Reduce and measure hallucinations
[Hallucination](https://huyenchip.com/2023/05/02/rlhf.html#rlhf_and_hallucination) is a heavily discussed topic already so I’ll be quick. Hallucination happens when an AI model makes stuff up. For many creative use cases, hallucination is a feature. However, for most other use cases, hallucination is a bug. I was at a panel on LLM with Dropbox, Langchain, Elastics, and Anthropic recently, and the #1 roadblock they see for companies to adopt LLMs in production is hallucination.
Mitigating hallucination and developing metrics to measure hallucination is a blossoming research topic, and I’ve seen many startups focus on this problem. There are also ad-hoc tips to reduce hallucination, such as adding more context to the prompt, chain-of-thought, self-consistency, or asking your model to be concise in its response.
To learn more about hallucination:
- [Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629) (Ji et al., 2022)
- [How Language Model Hallucinations Can Snowball](https://arxiv.org/abs/2305.13534) (Zhang et al., 2023)
- [A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity](https://arxiv.org/abs/2302.04023) (Bang et al., 2023)
- [Contrastive Learning Reduces Hallucination in Conversations](https://arxiv.org/abs/2212.10400) (Sun et al., 2022)
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) (Wang et al., 2022)
- [SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models](https://arxiv.org/abs/2303.08896) (​​Manakul et al., 2023)
- A simple example of fact-checking and hallucination by [NVIDIA’s NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/examples/grounding_rail/README.md#grounding-fact-checking-and-hallucination)
## 2. Optimize context length and context construction
A vast majority of questions require context. For example, if we ask ChatGPT: “What’s the best Vietnamese restaurant?”, the context needed would be “where” because the best Vietnamese restaurant in Vietnam would be different from the best Vietnamese in the US.
According to this cool paper [SituatedQA](https://arxiv.org/pdf/2109.06157.pdf) (Zhang 

## Summary

& Choi, 2021), a significant proportion of information-seeking questions have context-dependent answers, e.g. roughly 16.5% of the [Natural Questions NQ-Open dataset](https://ai.google.com/research/NaturalQuestions). Personally, I suspect that this percentage would be even higher for enterprise use cases. For example, say a company builds a chatbot for customer support, for this chatbot to answer any customer question about any product, the context needed might be that customer’s history or that product’s information.
Because the model “learns” from the context provided to it, this process is also called context learning.
![Context needed for a customer support query](/assets/pics/llm-research/2-context.png)
Context length is especially important for RAG – [Retrieval Augmented Generation](https://arxiv.org/abs/2005.11401) (Lewis et al., 2020) – which has emerged to be the predominant pattern for LLM industry use cases. For those not yet swept away in the RAG rage, RAG works in two phases:
Phase 1: chunking (also known as indexing)
- Gather all the documents you want your LLM to use
- Divide these documents into chunks that can be fed into your LLM to generate embeddings and store these embeddings in a vector database.
Phase 2: querying
- When user sends a query, like “*Does my insurance policy pay for this drug X*”, your LLM converts this query into an embedding, let’s call it QUERY_EMBEDDING
- Your vector database fetches the chunks whose embeddings are the most similar to QUERY_EMBEDDING
Screenshot from [Jerry Liu’s talk on LlamaIndex](https://www.youtube.com/watch?v=njzB6fm0U8g) (2023)
![Context needed for a customer support query](/assets/pics/llm-research/2-rag.jpg)
The longer the context length, the more chunks we can squeeze into the context. The more information the model has access to, the better its response will be, right?
Not always. How much context a model can use and how efficiently that model will use it are two different questions. In parallel with the effort to increase model context length is the effort to make the context more efficient. Some people call it “prompt engineering” or “prompt construction”. For example, a paper that has made the rounds recently is about how models are much better at understanding information at the beginning and the end of the index rather than in the middle of it – [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) (Liu et al., 2023).
## 3. Incorporate other data modalities
Multimodality, IMO, is so powerful and yet so underrated. There are many reasons for multimodality.
First, there are many use cases where multimodal data is required, especially in industries that deal with a mixture of data modalities such as healthcare, robotics, e-commerce, retail, gaming, entertainment, etc. Examples:
- Oftentimes, medical predictions require both text (e.g. doctor’s notes, patients’ questionnaires) and images (e.g. CT, X-ray, MRI scans).
- Product metadata often 

## Related Articles

- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[animals-vs-ghosts]]
- [[finding-the-best-sleep-tracker]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
