---
title: "understanding gnns"
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
# understanding gnns

> **Source:** understanding-convolutions-on-graphs-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://distill.pub/2021/understanding-gnns ingested: 2026-07-10 sha256: 0ce9f6677ebdad8240d6350501c37b49f13eb8b657f03b9bafba2532aae7d0ee blog_source: Distill AI --- Understanding Conv...
> **Sources:**
>   - understanding-convolutions-on-graphs-2026-07-10.md
> **Links:**
- [[gnn-intro]]
- [[curve-circuits]]
- [[animals-vs-ghosts]]
- [[distill-hiatus]]
- [[adversarial]]

## Key Findings

---
source_url: https://distill.pub/2021/understanding-gnns
ingested: 2026-07-10
sha256: 0ce9f6677ebdad8240d6350501c37b49f13eb8b657f03b9bafba2532aae7d0ee
blog_source: Distill AI
---
Understanding Convolutions on Graphs
- 
- 
- 
Understanding Convolutions on Graphs
- 
[
Distill
](/)
[About](/about/)
[Prize](/prize/)
[Submit](/journal/)
# Understanding Convolutions on Graphs
Understanding the building blocks and design choices of graph neural networks.
### Authors
### Affiliations
[Ameya Daigavane](https://ameya98.github.io/)
[Google Research](https://research.google/)
[Balaraman Ravindran](https://www.cse.iitm.ac.in/~ravi/)
[Google Research](https://research.google/)
[Gaurav Aggarwal](https://research.google/people/GauravAggarwal/)
[Google Research](https://research.google/)
### Published
Sept. 2, 2021
### DOI
[10.23915/distill.00032](https://doi.org/10.23915/distill.00032)
### Contents
[Introduction](#introduction)
[The Challenges of Computation on Graphs](#challenges)
- [Lack of Consistent Structure](#lack-of-consistent-structure)
- [Node-Order Equivariance](#node-order)
- [Scalability](#scalability)
[Problem Setting and Notation](#problem-and-notation)
[Extending Convolutions to Graphs](#extending)
[Polynomial Filters on Graphs](#polynomial-filters)
[Modern Graph Neural Networks](#modern-gnns)
[Interactive Graph Neural Networks](#interactive)
[From Local to Global Convolutions](#from-local-to-global)
- [Spectral Convolutions](#spectral)
- [Global Propagation via Graph Embeddings](#graph-embeddings)
[Learning GNN Parameters](#learning)
[Conclusions and Further Reading](#further-reading)
- [GNNs in Practice](#practical-techniques)
- [Different Kinds of Graphs](#different-kinds-of-graphs)
- [Pooling](#pooling)
[Supplementary Material](#supplementary)
- [Reproducing Experiments](#experiments-notebooks)
- [Recreating Visualizations](#visualizations-notebooks)
*
This article is one of two Distill publications about graph neural networks.
Take a look at
[A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/)
for a companion view on many things graph and neural network related.
*
Many systems and interactions - social networks, molecules, organizations, citations, physical models, transactions - can be represented quite naturally as graphs.
How can we reason about and make predictions within these systems?
One idea is to look at tools that have worked well in other domains: neural networks have shown immense predictive power in a variety of learning tasks.
However, neural networks have been traditionally used to operate on fixed-size and/or regular-structured inputs (such as sentences, images and video).
This makes them unable to elegantly process graph-structured data.
![Neural networks generally operate on fixed-size input vectors. How do we input a graph to a neural network?](images/standard-neural-networks.svg)
Graph neural networks (GNNs) are a family of neural networks that can operate naturally on graph-structured d

## Summary

ata. 
By extracting and utilizing features from the underlying graph,
GNNs can make more informed predictions about entities in these interactions,
as compared to models that consider individual entities in isolation.
GNNs are not the only tools available to model graph-structured data:
graph kernels 
and random-walk methods 
were some of the most popular ones.
Today, however, GNNs have largely replaced these techniques
because of their inherent flexibility to model the underlying systems
better.
In this article, we will illustrate
the challenges of computing over graphs, 
describe the origin and design of graph neural networks,
and explore the most popular GNN variants in recent times.
Particularly, we will see that many of these variants
are composed of similar building blocks.
First, let’s discuss some of the complications that graphs come with.
## 
The Challenges of Computation on Graphs
### 
Lack of Consistent Structure
Graphs are extremely flexible mathematical models; but this means they lack consistent structure across instances.
Consider the task of predicting whether a given chemical molecule is toxic  :
![The molecular structure of non-toxic 1,2,6-trigalloyl-glucose.](images/1,2,6-trigalloyl-glucose-molecule.svg)
![The molecular structure of toxic caramboxin.](images/caramboxin-molecule.svg)
**Left:** A non-toxic 1,2,6-trigalloyl-glucose molecule.
**Right:** A toxic caramboxin molecule.
Looking at a few examples, the following issues quickly become apparent:
- Molecules may have different numbers of atoms.
- The atoms in a molecule may be of different types.
- Each of these atoms may have different number of connections.
- These connections can have different strengths.
Representing graphs in a format that can be computed over is non-trivial,
and the final representation chosen often depends significantly on the actual problem.
### 
Node-Order Equivariance
Extending the point above: graphs often have no inherent ordering present amongst the nodes.
Compare this to images, where every pixel is uniquely determined by its absolute position within the image!
![Representing the graph as one vector requires us to fix an order on the nodes. But what do we do when the nodes have no inherent order?](images/node-order-alternatives.svg)
Representing the graph as one vector requires us to fix an order on the nodes.
But what do we do when the nodes have no inherent order?
**Above:** 
The same graph labelled in two different ways. The alphabets indicate the ordering of the nodes.
As a result, we would like our algorithms to be node-order equivariant:
they should not depend on the ordering of the nodes of the graph.
If we permute the nodes in some way, the resulting representations of 
the nodes as computed by our algorithms should also be permuted in the same way.
### 
Scalability
Graphs can be really large! Think about social networks like Facebook and Twitter, which have over a billion users. 
Operating on data this large is not easy.
Luckily, most

## Related Articles

- [[gnn-intro]]
- [[curve-circuits]]
- [[animals-vs-ghosts]]
- [[distill-hiatus]]
- [[adversarial]]
