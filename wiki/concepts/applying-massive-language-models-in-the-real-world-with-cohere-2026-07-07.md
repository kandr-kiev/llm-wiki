---
type: concept
title: Applying Massive Language Models In The Real World With Cohere
description: Auto-generated wiki page
created: 2026-07-08
updated: 2026-07-08
tags: [llm-wiki, knowledge-base]
sources: [raw/articles/applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07.md]
confidence: high
contested: false
links: [[advanced-rag-techniques-2026], [course-ai-agents-software-engineer-future-skills-2026], [helping-build-shared-standards-for-advanced-ai-2026-07-07], [llm-fine-tuning-lora-qlora-dpo-2026], [open-source-llm-landscape-2026]]
---
# Applying Massive Language Models In The Real World With Cohere

> **Source:** [applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07.md](http://jalammar.github.io/applying-large-language-models-cohere/)
> **Relevance:** high
> **Type:** concept

---

Applying massive language models in the real world with Cohere

 
 A little less than a year ago, I joined the awesome Cohere team. The company trains massive language models (both GPT-like and BERT-like) and offers them as an API (which also supports finetuning). Its founders include Google Brain alums including co-authors of the original Transformers paper. It’s a fascinating role where I get to help companies and developers put these massive models to work solving real-world problems.

I love that I get to share some of the intuitions developers need to start problem-solving with these models. Even though I’ve been working very closely on pretrained Transformers for the past several years (for this blog and in developing Ecco), I’m enjoying the convenience of problem-solving with managed language models as it frees up the restrictions of model loading/deployment and memory/GPU management.

These are some of the articles I wrote and collaborated on with colleagues over the last few months:

Intro to Large Language Models with Cohere

 
 
 
 
 This is a high-level intro to large language models to people who are new to them. It establishes the difference between generative (GPT-like) and representation (BERT-like) models and examples use cases for them.
 This is one of the first articles I got to write. It's extracted from a much larger document that I wrote to explore some of the visual language to use in explaining the application of these models.
 

A visual guide to prompt engineering 

 
 
 
 
 Massive GPT models open the door for a new way of programming. If you structure the input text in the right way, you can useful (and often fascinating) results for a lot of taasks (e.g. text classification, copy writing, summarization...etc).
 
 This article visually demonstrates four principals to create prompts effectively. 
 

 Text Summarization

 
 
 
 
 This is a walkthrough of creating a simple summarization system. It links to a jupyter notebook which includes the code to start experimenting with text generation and summarization.
 The end of this notebook shows an important idea I want to spend more time on in the future. That of how to rank/filter/select the best from amongst multiple generations.
 

Semantic Search

 
 
 
 
 Semantic search has to be one of the most exciting applications of sentence embedding models. This tutorials implements a "similar questions" functionality using sentence embeddings and a a vector search library.
 The vector search library used here is Annoy from Spotify. There are a bunch of others out there. Faiss is used widely. I experiment with PyNNDescent as well.
 

 Finetuning Representation Models

 
 
 
 
 Finetuning tends to lead to the best results language models can achieve. This article explains the intuitions around finetuning representation/sentence embedding models. I've added a couple more visuals to the Twitter thread.
The research around this area is very interesting. I've highly enjoyed papers like Sentence BERT and Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval
 

Controlling Generation with top-k & top-p

 
 
 
 
 This one is a little bit more technical. It explains the parameters you tweak to adjust a GPT's decoding strategy -- the method with which the system picks output tokens. 
 
 

Text Classification Using Embeddings

 
 
 
 
 
 This is a walkthrough of one of the most common use cases of embedding models -- text classification. It is similar to A Visual Guide to Using BERT for the First Time, but uses Cohere's API.
 
 

You can find these and upcoming articles in the Cohere docs and notebooks repo. I have quite number of experiments and interesting workflows I’d love to be sharing in the coming weeks. So stay tuned!

 

 
 Written on March 7, 2022
 

 

 

 
 
 

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

Attribution example:

Alammar, J (2018). The Illustrated Transformer [Blog post]. Retrieved from https://jalammar.github.io/illustrated-transformer/

Note: If you translate any of the posts, let me know so I can link your translation to the original post. My email is in the about page.

---

*Auto-generated from raw source by LLM Wiki Integrator*
