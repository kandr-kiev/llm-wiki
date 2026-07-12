---
type: concept
title: Semi-Supervised Learning
description: ML approach that leverages both labeled and unlabeled data for training, bridging supervised and unsupervised paradigms.
created: 2026-07-07
updated: 2026-07-07
tags: [ml, semi-supervised, self-training, consistency-regularization]
sources: [raw/articles/semi-supervised-learning-2026-07-07.md]
confidence: high
contested: false
links: [active-learning, contrastive-representation-learning]
---# Semi-Supervised Learning

## Overview

Semi-supervised learning (SSL) uses a small amount of labeled data together with a large amount of unlabeled data for training. It exploits the underlying structure in the data distribution, assuming that the data lies on or near a low-dimensional manifold.

## Key Approaches

### Self-Training
1. Train a model on labeled data
2. Predict labels for unlabeled data
3. Add high-confidence predictions to the training set
4. Retrain on the expanded dataset
5. Iterate

### Co-Training
Train two models on different views/features of the data. Each model labels unlabeled data for the other.

### Consistency Regularization
Enforce that the model's predictions remain consistent under small perturbations of the input (noise, augmentation, paraphrasing). Popular in modern SSL for NLP.

### Pseudo-Labeling
Assign predicted labels to unlabeled data and train on them alongside true labels. Temperature scaling controls confidence thresholds.

### Graph-Based Methods
Construct a graph over all data points (labeled + unlabeled). Propagate label information through graph edges based on similarity.

## Relevance to LLMs

- **Pre-training** is essentially SSL — massive unlabeled text + implicit supervision from next-token prediction
- **Prompting** leverages the learned representations from SSL pre-training
- **Fine-tuning** often uses small labeled sets augmented by SSL techniques

## Related Pages

- [[concepts/active-learning]] — Query strategy for selecting which unlabeled data to label
- [[concepts/contrastive-representation-learning]] — SSL technique that learns representations by contrasting positive/negative pairs
