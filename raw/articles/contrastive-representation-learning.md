---
type: concept
title: Contrastive Representation Learning
description: Representation learning method that pulls similar instances together and pushes dissimilar ones apart in embedding space, forming the basis of modern self-supervised learning.
created: 2026-07-07
updated: 2026-07-07
tags: [ml, self-supervised, representation-learning, embeddings, contrastive-loss]
sources: [raw/articles/contrastive-representation-learning-2026-07-07.md]
confidence: high
contested: false
links: [semi-supervised-learning, diffusion-models]
---

# Contrastive Representation Learning

## Overview

Contrastive learning is a self-supervised representation learning approach where the model learns by distinguishing between similar (positive) and dissimilar (negative) pairs of data. The core idea: representations of similar data should be close in embedding space, while dissimilar data should be far apart.

## Core Framework

### Positive and Negative Pairs
- **Positive pair:** Two augmented views of the same instance (e.g., two crops of the same image, or a sentence and its paraphrase)
- **Negative pair:** Instances from different sources

### Contrastive Loss
The model is trained to maximize agreement between positive pairs while minimizing agreement between negative pairs:

L = -log(exp(sim(u, v)/τ) / Σ exp(sim(u, z_i)/τ))

Where u, v are positive pair embeddings, z_i are negative embeddings, sim is cosine similarity, and τ is temperature.

## Key Methods

### SimCLR
- Uses data augmentations (crop, color, blur) to create positive pairs
- Simple MLP projector on top of encoder
- Large batch sizes needed for sufficient negatives
- Foundation for many subsequent methods

### MoCo (Momentum Contrast)
- Maintains a dynamic queue of negative embeddings
- Uses momentum encoder to keep representations consistent
- Allows smaller batch sizes
- Real-time dictionary update

### SimSiam / BYOL
- Remove the need for negative samples entirely
- Use stopping gradient trick to avoid collapse
- Symmetric prediction architecture
- Achieve comparable performance with simpler design

### CLIP (Contrastive Language-Image Pre-training)
- Contrastive learning across modalities
- Positive pairs: image + corresponding text
- Trained on internet-scale image-text pairs
- Foundation for zero-shot transfer and text-to-image generation

## Relevance to LLMs

- **Embedding quality** — Contrastive learning produces high-quality text embeddings for retrieval (RAG)
- **Instruction tuning** — Similar contrastive objectives align model outputs with human preferences
- **Multimodal models** — CLIP-style contrastive objectives power vision-language models

## Related Pages

- [[semi-supervised-learning]] — Broader SSL framework
- [[diffusion-models]] — Complementary generative approach
