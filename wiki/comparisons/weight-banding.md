---
title: "weight banding"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - compliance
  - distributed
  - edge
  - nlp
  - software
  - system-design
  - use-case
---
# weight banding

> **Source:** weight-banding-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://distill.pub/2020/circuits/weight-banding ingested: 2026-07-10 sha256: 074ff44860d6e9b39d27240ad0429cee919642a9a246bf6a4ec0293d4584c399 blog_source: Distill AI --- -  -  Weight...
> **Sources:**
>   - weight-banding-2026-07-10.md
> **Links:**
- [[branch-specialization]]
- [[visualizing-weights]]
- [[curve-circuits]]
- [[multimodal-neurons]]
- [[gnn-intro]]

## Key Findings

---
source_url: https://distill.pub/2020/circuits/weight-banding
ingested: 2026-07-10
sha256: 074ff44860d6e9b39d27240ad0429cee919642a9a246bf6a4ec0293d4584c399
blog_source: Distill AI
---
- 
- 
Weight Banding
- 
[
Distill
](/)
[About](/about/)
[Prize](/prize/)
[Submit](/journal/)
# Weight Banding
### Authors
### Affiliations
[Michael Petrov](http://twitter.com/mpetrov)
[OpenAI](https://openai.com)
[Chelsea Voss](https://csvoss.com)
[OpenAI](https://openai.com)
[Ludwig Schubert](https://schubert.io/)
[Nick Cammarata](http://nickcammarata.com)
[OpenAI](https://openai.com)
[Gabriel Goh](https://gabgoh.github.io)
[OpenAI](https://openai.com)
[Chris Olah](https://colah.github.io)
### Published
April 8, 2021
### DOI
[10.23915/distill.00024.009](https://doi.org/10.23915/distill.00024.009)
![](images/multiple-pages.svg)
This article is part of the [Circuits thread](/2020/circuits/), an experimental format collecting invited short articles and critical commentary delving into the inner workings of neural networks.
[Branch Specialization](/2020/circuits/branch-specialization/)
## Introduction
Open up any ImageNet conv net and look at the weights in the last layer. You’ll find a uniform spatial pattern to them, dramatically unlike anything we see elsewhere in the network. No individual weight is unusual, but the uniformity is so striking that when we first discovered it we thought it must be a bug. Just as different biological tissue types jump out as distinct under a microscope, the weights in this final layer jump out as distinct when visualized with NMF. We call this phenomenon *weight banding*.
Microscope slides of different tissues
Muscle tissue
Epithelial tissue
Typical layer
Layer with weight banding
NMF of weights at different layers
[1](#figure-1). When [visualized with NMF](https://drafts.distill.pub/distillpub/post--circuits-visualizing-weights#one-simple-trick), the weight banding in layer `mixed_5b` is as visually striking compared to any other layer in InceptionV1 (here shown: `mixed_3a`) as the smooth, regular striation of muscle tissue is when compared to any other tissue (here shown: cardiac muscle tissue and epithelial tissue).
So far, the [Circuits thread](https://distill.pub/2020/circuits/) has mostly focused on studying very small pieces of neural network – [individual neurons](https://distill.pub/2020/circuits/early-vision/) and small circuits. In contrast, weight banding is an example of what we call a “structural phenomenon,” a larger-scale pattern in the circuits and features of a neural network. Other examples of structural phenomena are the recurring symmetries we see in [equivariance](https://distill.pub/2020/circuits/equivariance/) motifs and the specialized slices of neural networks we see in [branch specialization](https://distill.pub/2020/circuits/branch-specialization/).
In the case of weight banding, we think of it as a structural phenomenon because the pattern appears at the scale of an entire layer.
Weight banding also see

## Summary

ms similar in flavor to the [checkerboard artifacts](https://distill.pub/2016/deconv-checkerboard/) that form during deconvolution.
In addition to describing weight banding, we’ll explore when and why it occurs. We find that there appears to be a causal link between whether a model uses global average pooling or fully connected layers at the end, suggesting that weight banding is part of an algorithm for preserving information about larger scale structure in images. Establishing causal links like this is a step towards closing the loop between practical decisions in training neural networks and the phenomena we observe inside them.
## Where weight banding occurs
Weight banding consistently forms in the final convolutional layer of vision models with global average pooling.
In order to see the bands, we need to visualize the spatial structure of the weights, as shown below. We typically do this using NMF, [as described in](https://drafts.distill.pub/distillpub/post--circuits-visualizing-weights/#one-simple-trick) Visualizing Weights. For each neuron, we take the weights connecting it to the previous layer. We then use NMF to reduce the number of dimensions corresponding to channels in the previous layer down to 3 factors, which we can map to RGB channels. Since which factor is which is arbitrary, we use a heuristic to make the mapping consistent across neurons. This reveals a very prominent pattern of horizontalThe stripes aren’t always perfectly horizontal - sometimes they exhibit a slight preference for extra weight in the center of the central band, as seen in some examples below. stripes.
[2](#figure-2).
These common networks have pooling operations before their fully
connected layers and consistently show banding at their last
convolutional layers.
InceptionV1
mixed 5b
ResNet50
block 4 unit 3
VGG19
conv5
Interestingly, AlexNet does not exhibit this phenomenon.
[3](#figure-3).
AlexNet does not have a pooling operation before its fully connected
layers and does not show banding at its last convolutional
layer.
To make it easier to look for groups of similar weights, we
sorted the neurons at each layer by similarity of their reduced
forms.
AlexNet
conv5
Unlike most modern vision models, AlexNet does not use global average pooling. Instead, it has a fully connected layer directly connected to its final convolutional layer, allowing it to treat different positions differently. If one looks at the weights of this fully connected layer, the weights strongly vary as a function of the global y position.
The horizontal stripes in weight banding mean that the filters don’t care about horizontal position, but are strongly encoding relative vertical position. Our hypothesis is that weight banding is a learned way to preserve spatial information as it gets lost through various pooling operations.
In the next section, we will construct our own simplified vision network and investigate variations on its architecture in order to understand exactly which condi

## Related Articles

- [[branch-specialization]]
- [[visualizing-weights]]
- [[curve-circuits]]
- [[multimodal-neurons]]
- [[gnn-intro]]
