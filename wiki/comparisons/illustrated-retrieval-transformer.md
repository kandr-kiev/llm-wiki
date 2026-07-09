---
title: "illustrated retrieval transformer"
type: comparison
tags:
description: Comparison page for illustrated retrieval transformer

sources: []
links: []
description: Comparison page for illustrated retrieval transformer

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
---

# illustrated retrieval transformer

> **Source:** the-illustrated-retrieval-transformer-2026-07-07.md
> **Type:** comparison
> **Created:** 2026-07-08

## Key Findings

[![](https://avatars0.githubusercontent.com/u/1007956?s=460&v=4)](/)
# [Jay Alammar](/)
Visualizing machine learning one concept at a time.
Read our book, [Hands-On Large Language Models](https://www.LLM-book.com) and follow me on [LinkedIn](https://www.linkedin.com/in/jalammar/), [Bluesky](https://bsky.app/profile/jayalammar.bsky.social), [Substack](https://newsletter.languagemodels.co/), [X](https://x.com/JayAlammar),[YouTube ](https://www.youtube.com/channel/UCmOwsoHty5PrmE-3QhUBfPQ)
[Blog](/)
[About](/about)
# The Illustrated Retrieval Transformer
Discussion: [Discussion Thread](https://github.com/jalammar/jalammar.github.io/discussions/21) for comments, corrections, or any feedback. 
Translations: [Korean](https://chloamme.github.io/2022/01/08/illustrated-retrieval-transformer-korean.html), [Russian](https://habr.com/ru/post/648705/)
**Summary**: The latest batch of language models can be much smaller yet achieve GPT-3 like performance by being able to query a database or search the web for information. A key indication is that building larger and larger models is not the only way to improve performance.
## Video
---
The last few years saw the rise of Large Language Models (LLMs) – machine learning models that rapidly improve how machines process and generate language. Some of the highlights since 2017 include:
- The original [Transformer](/illustrated-transformer/) breaks previous performance records for machine translation.
- [BERT](/illustrated-bert/) popularizes the pre-training then finetuning process, as well as Transformer-based contextualized word embeddings. It then rapidly starts to power [Google Search](https://blog.google/products/search/search-language-understanding-bert/) and [Bing Search](https://azure.microsoft.com/en-us/blog/bing-delivers-its-largest-improvement-in-search-experience-using-azure-gpus/).
- [GPT-2](/illustrated-gpt2/) demonstrates the machine’s ability to write as well as humans do.
- First [T5](https://arxiv.org/abs/1910.10683), then [T0](https://huggingface.co/bigscience/T0pp) push the boundaries of transfer learning (training a model on one task, and then having it do well on other adjacent tasks) and posing a lot of different tasks as text-to-text tasks.
- [GPT-3](/how-gpt3-works-visualizations-animations/) showed that massive scaling of generative models can lead to shocking emergent applications (the industry continues to train larger models like [Gopher](https://deepmind.com/research/publications/2021/scaling-language-models-methods-analysis-insights-from-training-gopher), [MT-NLG](https://www.microsoft.com/en-us/research/blog/using-deepspeed-and-megatron-to-train-megatron-turing-nlg-530b-the-worlds-largest-and-most-powerful-generative-language-model/)…etc).
For a while, it seemed like scaling larger and larger models is the main way to improve performance. Recent developments in the field, like DeepMind’s [RETRO Transformer](https://deepmind.com/research/publications/2021/improving-language-models-by-re

## Summary

trieving-from-trillions-of-tokens) and OpenAI’s [WebGPT](https://openai.com/blog/improving-factual-accuracy/), reverse this trend by showing that smaller generative language models can perform on par with massive models if we augment them with a way to search/query for information.
This article breaks down DeepMind’s RETRO (**R**etrieval-**E**nhanced **TR**ansf**O**rmer) and how it works. The model performs on par with GPT-3 despite being 4% its size (7.5 billion parameters vs. 185 billion for GPT-3 Da Vinci).
![](/images/retro/deepmind-retro-retrieval-transformer.png)
RETRO incorporates information retrieved from a database to free its parameters from being an expensive store of facts and world knowledge.
RETRO was presented in the paper [Improving Language Models by Retrieving from Trillions of Tokens](https://arxiv.org/abs/2112.04426). It continues and builds on a wide variety of retrieval [work](http://www.crm.umontreal.ca/2018/Langue18/pdf/Cheung.pdf) [in](https://ai.facebook.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/) [the](https://openreview.net/forum?id=HklBjCEKvH) [research](https://arxiv.org/abs/2102.02557) [community](https://openreview.net/forum?id=B184E5qee). This article explains the model and not what is especially novel about it.
## Why This is Important: Separating Language Information from World Knowledge Information
Language modeling trains models to predict the next word–to fill-in-the-blank at the end of the sentence, essentially.
Filling the blank sometimes requires knowledge of factual information (e.g. names or dates). For example:
![](/images/retro/prompt-1.png)
Input prompt: The Dune film was released in ....
Other times, familiarity with the language is enough to guess what goes in the blank. For example:
![](/images/retro/prompt-2.png)
Input prompt: its popularity spread by word-of-mouth to allow Herbert to start working full ....
This distinction is important because LLMs encoded everything they know in their model parameters. While this makes sense for language information, it is inefficient for factual and world-knowledge information.
By including a retrieval method in the language model, the model can be much smaller. A neural database aids it with retrieving factual information it needs during text generation.
![](/images/retro/Large-GPT-vs-Retro-transformer-world-knowledge-information.png)
Aiding language models with retrieval methods allows us to reduce the amount of information a language model needs to encode in its parameters to perform well at text generation.
Training becomes fast with small language models, as training data memorization is reduced. Anyone can deploy these models on smaller and more affordable GPUs and tweak them as per need.
Mechanically, RETRO is an encoder-decoder model just like the original transformer. However, it augments the input sequence with the help of a retrieval database. The model finds the most probabl

## Related Articles

- [[the-illustrated-retrieval-transformer-2026-07-07]]
- 
- 
- [[the-illustrated-retrieval-transformer-2026-07-07]]
- 
