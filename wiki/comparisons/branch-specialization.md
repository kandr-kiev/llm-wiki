---
title: "branch specialization"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - compliance
  - data
  - distributed
  - edge
  - image-generation
  - nlp
  - self-supervised
  - software
  - system-design
  - use-case
---
# branch specialization

> **Source:** branch-specialization-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://distill.pub/2020/circuits/branch-specialization ingested: 2026-07-10 sha256: 2b5a03a7865f580bb8eb215790d3c5a36bf8ea014f7206c8ede4959534140b90 blog_source: Distill AI --- -  -...
> **Sources:**
>   - branch-specialization-2026-07-10.md
> **Links:**
- [[gnn-intro]]
- [[automating-ai-away-2026-07-07]]
- [[animals-vs-ghosts]]
- [[away]]
- [[the-illustrated-retrieval-transformer-2026-07-07]]

## Key Findings

---
source_url: https://distill.pub/2020/circuits/branch-specialization
ingested: 2026-07-10
sha256: 2b5a03a7865f580bb8eb215790d3c5a36bf8ea014f7206c8ede4959534140b90
blog_source: Distill AI
---
- 
- 
Branch Specialization
- 
[
Distill
](/)
[About](/about/)
[Prize](/prize/)
[Submit](/journal/)
# Branch Specialization
### Authors
### Affiliations
[Chelsea Voss](https://csvoss.com)
[OpenAI](https://openai.com)
[Gabriel Goh](https://gabgoh.github.io)
[OpenAI](https://openai.com)
[Nick Cammarata](http://nickcammarata.com)
[OpenAI](https://openai.com)
[Michael Petrov](https://twitter.com/mpetrov)
[OpenAI](https://openai.com)
[Ludwig Schubert](https://schubert.io)
[Chris Olah](https://colah.github.io)
### Published
April 5, 2021
### DOI
[10.23915/distill.00024.008](https://doi.org/10.23915/distill.00024.008)
![](images/multiple-pages.svg)
This article is part of the [Circuits thread](/2020/circuits/), an experimental format collecting invited short articles and critical commentary delving into the inner workings of neural networks.
[Visualizing Weights](/2020/circuits/visualizing-weights/)
[Weight Banding](/2020/circuits/weight-banding/)
## Introduction
If we think of interpretability as a kind of “anatomy of neural networks,” most of the circuits thread has involved studying tiny little veins – looking at the small-scale, at individual neurons and how they connect. However, there are many natural questions that the small-scale approach doesn’t address.
In contrast, the most prominent abstractions in biological anatomy involve larger-scale structures: individual organs like the heart, or entire organ systems like the respiratory system. And so we wonder: is there a “respiratory system” or “heart” or “brain region” of an artificial neural network? Do neural networks have any emergent structures that we could study that are larger-scale than circuits?
This article describes *branch specialization*, one of three larger “structural phenomena” we’ve been able observe in neural networks. (The other two, [equivariance](https://distill.pub/2020/circuits/equivariance/) and [weight banding](https://distill.pub/2020/circuits/weight-banding/), have separate dedicated articles.) Branch specialization occurs when neural network layers are split up into branches. The neurons and circuits tend to self-organize, clumping related functions into each branch and forming larger functional units – a kind of “neural network brain region.” We find evidence that these structures implicitly exist in neural networks without branches, and that branches are simply reifying structures that otherwise exist.
The earliest example of branch specialization that we’re aware of comes from AlexNet. AlexNet is famous as a jump in computer vision, arguably starting the deep learning revolution, but buried in the paper is a fascinating, rarely-discussed detail.
The first two layers of AlexNet are split into two branches which can’t communicate until they rejoin after the second layer. This str

## Summary

See Key Findings for full content.

## Related Articles

- [[gnn-intro]]
- [[automating-ai-away-2026-07-07]]
- [[animals-vs-ghosts]]
- [[away]]
- [[the-illustrated-retrieval-transformer-2026-07-07]]
