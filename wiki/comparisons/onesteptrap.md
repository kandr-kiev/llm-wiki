---
title: "OneStepTrap"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - architecture
  - best-practice
  - foundation-model
  - framework
  - machine-learning
  - news
  - policy
  - real-time
  - reinforcement-learning
  - research
  - scalability
  - semi-supervised
  - unsupervised
---

# OneStepTrap

> **Source:** the-one-step-trap-in-ai-research-2026-07-12.md
> **Type:** comparison
> **Created:** 2026-07-13
> **Updated:** 2026-07-13
> **Confidence:** high
> **Description:** # The One-Step Trap (in AI Research) ## Rich Sutton ### Written up for X on July 18, 2024 The one-step trap is the common mistake of thinking that all or most of an AI agents learned predictions can...
> **Sources:**
>   - the-one-step-trap-in-ai-research-2026-07-12.md
> **Links:**
- [[How Gpt3 Works Visualizations And Animations]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Automating Ai Away]]
- [[Mesh LLM: distributed AI computing on iroh]]

## Key Findings

# The One-Step Trap (in AI Research)
## Rich Sutton
### Written up for X on July 18, 2024
The one-step trap is the common mistake of thinking that all or
most of an AI agents learned predictions can be one-step ones,
with all longer-term predictions generated as needed by iterating
the one-step predictions. The most important place where the trap
arises is when the one-step predictions constitute a model of the
world and of how it evolves over time. It is appealing to think
that one can learn just a one-step transition model and then roll
it out to predict all the longer-term consequences of a way of
behaving. The one-step model is thought of as being analogous to
physics, or to a realistic simulator.
The appeal of this mistake is that it contains a grain of truth:
if all one-step predictions can be made with perfect accuracy,
then they can be used to make all longer-term prediction with
perfect accuracy. However, if the one-step predictions are not
perfectly accurate, then all bets are off. In practice, iterating
one-step predictions usually produces poor results. The one-step
errors compound and accumulate into large errors in the long-term
predictions. In addition, computing long-term predictions from
one-step ones is prohibitively computationally complex. In a
stochastic world, or for a stochastic policy, the future is not a
single trajectory, but a tree of possibilities, each of which must
be imagined and weighted by its probability. As a result, the
computational complexity of computing a long-term prediction from
one-step predictions is exponential in the length of the
prediction, and thus generally infeasible. 
The bottom line is that one-step models of the world are hopeless,
yet extremely appealing, and are widely used in POMDPs, Bayesian
analyses, control theory, and in compression theories of AI.
The solution, in my opinion, is to form temporally abstract models
of the world using options and GVFs, as in the following
references.
Sutton, R.S., Precup, D., Singh, S. (1999). Between MDPs and
semi-MDPs: A Framework for Temporal Abstraction in Reinforcement
Learning. Artificial Intelligence 112:181-211.
Sutton, R. S., Modayil, J., Delp, M., Degris, T., Pilarski, P. M.,
White, A., Precup, D. (2011). Horde: A scalable real-time
architecture for learning knowledge from unsupervised sensorimotor
interaction. In Proceedings of the Tenth International Conference
on Autonomous Agents and Multiagent Systems, Taipei, Taiwan.
Sutton, R. S., Machado, M. C., Holland, G. Z., Timbers, D. S. F.,
Tanner, B., & White, A. (2023). Reward-respecting subtasks for
model-based reinforcement learning. Artificial Intelligence 324.

## Summary

See Key Findings for full content.

## Related Articles

- [[How Gpt3 Works Visualizations And Animations]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Automating Ai Away]]
- [[Mesh LLM: distributed AI computing on iroh]]
