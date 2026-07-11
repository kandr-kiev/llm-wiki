---
type: concept
title: Active Learning
description: ML paradigm where the learning algorithm iteratively queries an oracle for labels on the most informative unlabeled instances, maximizing performance with minimal labeled data.
created: 2026-07-07
updated: 2026-07-07
tags: [ml, active-learning, data-efficiency, query-strategy]
sources: [raw/articles/active-learning-2026-07-07.md]
confidence: high
contested: false
links: [semi-supervised-learning, contrastive-representation-learning]
---

# Active Learning

## Overview

Active learning is a semi-supervised paradigm where a learning algorithm can request labels for the most informative instances from an oracle (e.g., a human annotator). This contrasts with standard supervised learning where the training data is fixed and passively received.

## Core Query Strategies

### Uncertainty Sampling
The model selects instances where it is least confident about the prediction. Common heuristics:
- **Least confident:** Select instance with lowest max probability
- **Margin sampling:** Select instance with smallest difference between top-2 class probabilities
- **Entropy:** Select instance with highest prediction entropy

### Density-weighted Sampling
Combines uncertainty with data density — prefer uncertain instances in dense regions of feature space. Avoids querying outliers.

### Expected Model Change
Select instances that would cause the largest change in the model parameters if labeled.

### Committee-Based Methods
Train multiple models (a "committee") and query instances where they disagree most (e.g., vote entropy).

## Applications in LLM Era

Active learning remains relevant for:
- **Instruction tuning datasets** — selectively labeling prompts for SFT
- **RLHF annotation** — prioritizing edge-case responses for preference labeling
- **Domain adaptation** — efficient labeling for target domain data

## Related Pages

- [[semi-supervised-learning]] — Broader context of using unlabeled data
- [[contrastive-representation-learning]] — Representation learning that benefits from efficient data curation
