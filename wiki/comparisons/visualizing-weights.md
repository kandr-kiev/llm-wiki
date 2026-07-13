---
title: "visualizing weights"
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
# visualizing weights

> **Source:** visualizing-weights-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://distill.pub/2020/circuits/visualizing-weights ingested: 2026-07-10 sha256: c2c3f01bfd6db0f21471388a000fd3a7e94940bd2dfc1d4bab64746c87103919 blog_source: Distill AI --- -  -  Vi...
> **Sources:**
>   - visualizing-weights-2026-07-10.md
> **Links:**
- [[branch-specialization]]
- [[curve-circuits]]
- [[finding-the-best-sleep-tracker]]
- [[vibe-coding-menugen]]
- [[distill-hiatus]]

## Key Findings

---
source_url: https://distill.pub/2020/circuits/visualizing-weights
ingested: 2026-07-10
sha256: c2c3f01bfd6db0f21471388a000fd3a7e94940bd2dfc1d4bab64746c87103919
blog_source: Distill AI
---
- 
- 
Visualizing Weights
- 
[
Distill
](/)
[About](/about/)
[Prize](/prize/)
[Submit](/journal/)
# Visualizing Weights
### Authors
### Affiliations
[Chelsea Voss](https://csvoss.com)
[OpenAI](https://openai.com)
[Nick Cammarata](http://nickcammarata.com)
[OpenAI](https://openai.com)
[Gabriel Goh](https://gabgoh.github.io)
[OpenAI](https://openai.com)
[Michael Petrov](https://twitter.com/mpetrov)
[OpenAI](https://openai.com)
[Ludwig Schubert](https://schubert.io)
Ben Egan
[Mount Royal University](https://mtroyal.ca)
[Swee Kiat Lim](https://greentfrapp.github.io/)
[Stanford University](https://stanford.edu)
[Chris Olah](https://colah.github.io)
### Published
Feb. 4, 2021
### DOI
[10.23915/distill.00024.007](https://doi.org/10.23915/distill.00024.007)
![](images/multiple-pages.svg)
This article is part of the [Circuits thread](/2020/circuits/), an experimental format collecting invited short articles and critical commentary delving into the inner workings of neural networks.
[Curve Circuits](/2020/circuits/curve-circuits/)
[Branch Specialization](/2020/circuits/branch-specialization/)
## Introduction
The problem of understanding a neural network is a little bit like reverse engineering a large compiled binary of a computer program. In this analogy, the weights of the neural network are the compiled assembly instructions. At the end of the day, the weights are the fundamental thing you want to understand: how does this sequence of convolutions and matrix multiplications give rise to model behavior?
Trying to understand artificial neural networks also has a lot in common with neuroscience, which tries to understand biological neural networks. As you may know, one major endeavor in modern neuroscience is mapping the [connectomes](https://en.wikipedia.org/wiki/Connectome) of biological neural networks: which neurons connect to which. These connections, however, will only tell neuroscientists which weights are non-zero. Getting the weights – knowing whether a connection excites or inhibits, and by how much – would be a significant further step. One imagines neuroscientists might give a great deal to have the access to weights that those of us studying artificial neural networks get for free.
And so, it’s rather surprising how little attention we actually give to looking at the weights of neural networks. There are a few exceptions to this, of course. It’s quite common for researchers to show pictures of the first layer weights in vision models (these are directly connected to RGB channels, so they’re easy to understand as images). In some work, especially historically, we see researchers reason about the weights of toy neural networks by hand. And we quite often see researchers discuss aggregate statistics of weights. But actually looking at the weights of a neural

## Summary

 network other than the first layer is quite uncommon – to the best of our knowledge, mapping weights between hidden layers to meaningful algorithms is novel to the circuits project.
## What’s the difference between visualizing activations, weights, and attributions?
In this article, we’re focusing on visualizing weights. But people often visualize activations, attributions, gradients, and much more. How should we think about the meaning of visualizing these different objects?
- 
**Activations:** We generally think of these as being “what” the network saw. If understanding a neural network is like reverse compiling a computer program, the neurons are the variables, and the activations are the values of those variables.
- 
**Weights:** We generally think of these as being “how” the neural network computes one layer from the previous one. In the reverse engineering analogy, these are compiled assembly instructions.
- 
**Attributions:** Attributions try to tell us the extent to which one neuron influenced a later neuron.We often think of this as “why” the neuron fired. We need to be careful with attributions, because they’re a human-defined object on top of a neural network rather than a fundamental object. They aren’t always well defined, and people mean different things by them. (They are very well defined if you are only operating across adjacent layers!)
## Why it’s non-trivial to study weights in hidden layers
It seems to us that there are three main barriers to making sense of the weights in neural networks, which may have contributed to researchers tending to not directly inspect them:
- 
**Lack of Contextualization:** Researchers often visualize weights in the first layer, because they are linked to RGB values that we understand. That connection makes weights in the first layer meaningful. But weights between hidden layers are meaningless by default: knowing nothing about either the source or the destination, how can we make sense of them?
- 
**Indirect Interaction:** Sometimes, the meaningful weight interactions are between neurons which aren’t literally adjacent in a neural network. For example, in a residual network, the output of one neuron can pass through the additive residual stream and linearly interact with a neuron much later in the network. In other cases, neurons may interact through intermediate neurons without significant nonlinear interactions. How can we efficiently reason about these interactions?
- 
**Dimensionality and Scale:** Neural networks have lots of neurons. Those neurons connect to lots of other neurons. There’s a lot of data to display! How can we reduce it to a human-scale amount of information?
Many of the methods we’ll use to address these problems were previously explored in [Building Blocks](https://distill.pub/2018/building-blocks/) in the context of understanding activation vectors. The goal of this article is to show how similar ideas can be applied to weights instead of activations. Of course, we’ve alrea

## Related Articles

- [[branch-specialization]]
- [[curve-circuits]]
- [[finding-the-best-sleep-tracker]]
- [[vibe-coding-menugen]]
- [[distill-hiatus]]
