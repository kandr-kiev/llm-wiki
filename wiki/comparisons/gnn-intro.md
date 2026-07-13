---
title: "gnn intro"
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
# gnn intro

> **Source:** a-gentle-introduction-to-graph-neural-networks-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://distill.pub/2021/gnn-intro ingested: 2026-07-10 sha256: ffc2dabc60bba8442dea2dcbbcb99a64661db4841cfb0896663175855e8e1c95 blog_source: Distill AI --- -  -  A Gentle Introduction...
> **Sources:**
>   - a-gentle-introduction-to-graph-neural-networks-2026-07-10.md
> **Links:**
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[semi-supervised-learning]]
- [[automating-ai-away-2026-07-07]]
- [[diffusion-models]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]

## Key Findings

---
source_url: https://distill.pub/2021/gnn-intro
ingested: 2026-07-10
sha256: ffc2dabc60bba8442dea2dcbbcb99a64661db4841cfb0896663175855e8e1c95
blog_source: Distill AI
---
- 
- 
A Gentle Introduction to Graph Neural Networks
- 
[
Distill
](/)
[About](/about/)
[Prize](/prize/)
[Submit](/journal/)
A Gentle Introduction to Graph Neural Networks
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
# A Gentle Introduction to Graph Neural Networks
Neural networks have been adapted to leverage the structure and properties of graphs. We explore the components needed for building a graph neural network - and motivate the design choices behind them.
Hover over a node in the diagram below to see how it accumulates information from nodes around it through the layers of the network.
### Authors
### Affiliations
Benjamin Sanchez-Lengeling
Google Research
Emily Reif
Google Research
[Adam Pearce](https://roadtolarissa.com)
Google Research
Alexander B. Wiltschko
Google Research
### Published
Sept. 2, 2021
### DOI
[10.23915/distill.00033](https://doi.org/10.23915/distill.00033)
*This article is one of two Distill publications about graph neural networks. Take a look at [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/) to understand how convolutions over images generalize naturally to convolutions over graphs.*
Graphs are all around us; real world objects are often defined in terms of their connections to other things. A set of objects, and the connections between them, are naturally expressed as a *graph*. Researchers have developed neural networks that operate on graph data (called graph neural networks, or GNNs) for over a decade. Recent developments have increased their capabilities and expressive power. We are starting to see practical applications in areas such as antibacterial discovery , physics simulations , fake news detection , traffic prediction and recommendation systems .
This article explores and explains modern graph neural networks. We divide this work into four parts. First, we look at what kind of data is most naturally phrased as a graph, and some common examples. Second, we explore what makes graphs different from other types of data, and some of the specialized choices we have to make when using graphs. Third, we build a modern GNN, walking through each of the parts of the model, starting with historic modeling innovations in the field. We move gradually from a bare-bones implementation to a state-of-the-art GNN model. Fourth and finally, we provide a GNN playground where you can play around with a real-word task and dataset to build a stronger intuition of how each component of a GNN model contributes to the predictions it makes.
To start, let’s establish what a graph is. A graph represents the relations (*edges*) between a collection of entities (*nodes*). 
Three types of attributes we might find in a graph, hover over to highlight each attribute. Other types of graphs and attributes are explored in the [Other types of graphs

## Summary

See Key Findings for full content.

## Related Articles

- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[semi-supervised-learning]]
- [[automating-ai-away-2026-07-07]]
- [[diffusion-models]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
