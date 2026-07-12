---
type: concept
title: Exploration Strategies in Deep Reinforcement Learning
description: Methods for balancing exploration and exploitation in DRL: ε-greedy, UCB, intrinsic motivation, curiosity-driven learning, and Thompson sampling.
created: 2026-07-07
updated: 2026-07-07
tags: [ml, reinforcement-learning, exploration, dqn, policy-gradient]
sources: [raw/articles/exploration-strategies-in-deep-reinforcement-learning-2026-07-07.md]
confidence: high
contested: false
links: [oyster-ii-reinforcement-learning-for-constructive-safety-alignment-in-large-language-models]
---# Exploration Strategies in Deep Reinforcement Learning

## Overview

In reinforcement learning, the agent must balance exploring new actions (to discover better strategies) with exploiting known good actions. Exploration strategies are critical for learning effective policies, especially in sparse-reward environments.

## Classical Methods

### ε-Greedy
- With probability ε, take a random action (explore)
- With probability 1-ε, take the best-known action (exploit)
- ε typically decays over time
- Simple but suboptimal in large action spaces

### Upper Confidence Bound (UCB)
- Select action with highest upper confidence bound
- Balances exploitation (mean reward) and exploration (uncertainty)
- Theoretical guarantees on regret

### Softmax (Boltzmann) Exploration
- Select actions probabilistically based on Q-values
- Higher Q-values get higher probability
- Temperature controls exploration vs exploitation

## Deep RL Exploration

### Intrinsic Motivation
- **Reward shaping:** Add bonus rewards for visiting new states
- **Count-based:** Bonus for visiting states with low visit count
- **State visitation frequency** as intrinsic reward

### Curiosity-Driven Exploration
- Train an intrinsic reward model to predict prediction error
- Novel states have high prediction error → high intrinsic reward
- Agent is motivated to explore unpredictable environments

### Thompson Sampling
- Maintain posterior distribution over Q-values
- Sample from posterior, select best action under sampled parameters
- Naturally balances exploration and exploitation

### Noisy Networks
- Add parameter-space noise to network weights
- Correlated noise across layers enables structured exploration
- Eliminates need for ε-decay schedules

## LLM-Relevant Exploration

- **RLHF exploration** — sampling diverse responses during preference collection
- **Self-play** — agents explore by competing against themselves
- **Multi-agent exploration** — diverse strategies emerge in multi-agent settings

## Related Pages

- [[oyster-ii-reinforcement-learning-for-constructive-safety-alignment-in-large-language-models]] — RL for LLM safety alignment
