---
title: "fable 5 gpt 5 6 sol goal"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - claude
  - data
  - deep-learning
  - gpt
  - image-generation
  - mobile
  - news
  - open-source
  - optimization
  - search
---

# fable 5 gpt 5 6 sol goal

> **Source:** fable-5-vs-gpt-56-sol-on-an-np-hard-problem-does-goal-help-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** [  CA Charles Azam ](/) [ Home ](/)[ Projects ](/projects)[ Blog ](/blog)[ Consulting ](/consulting)[ Books ](/books) [ fr ](/fr/blog/fable-5-gpt-5-6-sol-goal/) [ fr ](/fr/blog/fable-5-gpt-5-6-sol-goa...
> **Sources:**
>   - fable-5-vs-gpt-56-sol-on-an-np-hard-problem-does-goal-help-2026-07-18.md
> **Links:**
- [[ai music video arena claude vs gpt 5.6]]
- [[kimi k3]]
- [[Automating Ai Away]]
- [[Automating away]]
- [[sequoia ascent]]

## Key Findings

[ 
CA
Charles Azam
](/) [ Home ](/)[ Projects ](/projects)[ Blog ](/blog)[ Consulting ](/consulting)[ Books ](/books) [ fr ](/fr/blog/fable-5-gpt-5-6-sol-goal/) [ fr ](/fr/blog/fable-5-gpt-5-6-sol-goal/) [ Home ](/)[ Projects ](/projects)[ Blog ](/blog)[ Consulting ](/consulting)[ Books ](/books) On this page
- [The problem](#the-problem)
- [How large is the search space?](#how-large-is-the-search-space)
- [What I tested](#what-i-tested)
- [Results](#results)
- [Deep dive into the goal command](#deep-dive-into-the-goal-command)
- [The same command hides two different systems](#the-same-command-hides-two-different-systems)
- [Claude Code: a separate evaluator](#claude-code-a-separate-evaluator)
- [Codex: persisted state and lifecycle tools](#codex-persisted-state-and-lifecycle-tools)
- [Why /goal can win most runs and still be a bad default](#why-goal-can-win-most-runs-and-still-be-a-bad-default)
- [Limitations](#limitations)
- [Reproducing this](#reproducing-this)
[ 
Blog
](/blog) # Fable 5 vs. GPT-5.6 Sol on an NP-Hard Problem: Does /goal Help? 
July 17, 2026 / 6 min read **TL;DR:** I gave Claude Fable 5 and GPT-5.6 Sol the same unpublished NP-hard
optimization problem, with and without their native `/goal` mode. Fable 5 is an absolute beast;
`/goal` is not a game changer.
![Clean score distributions](/_astro/fig3_clean_distributions.Ct-GZQ3W_2lndA9.webp)
**Context:** This is an operations research problem originally submitted to students at a
hackathon. I spent a week years
ago writing C++ to solve it, so I have a useful human baseline.
Fable 5 was an absolute beast on this benchmark. It produced the best solution overall, and its
consistency is unlike anything I have seen from a model on this problem. This is pure raw
intelligence. Incredible.
The other result is that `/goal` is not a generic “try harder” switch. It changes the control
loop and the search path. Sometimes that finds a better basin. Sometimes it gives a bad idea
more time to mature.
All code, prompts, result tables, exclusions, and trajectory notes are in
[CLIArena](https://github.com/charles-azam/CLIArena). This is a follow-up to my
[first article about this benchmark](https://charlesazam.com/blog/kiro-benchmark/).
---
## The problem
KIRO is a fiber-network design problem I worked on as an engineering student in 2018. Given
directed distance matrices for Grenoble, Nice, and Paris, the solver has to connect distribution
points and terminals using loops and short chains while respecting several structural
constraints. The objective is total cable length. Lower is better.
![KIRO network structure: a directed loop rooted at a hub with a short branch](/_astro/fig0_kiro_problem.CYvcjsCU_Z1X0vi6.webp)
A valid network consists of redundant loops rooted at distribution hubs, with short branches
hanging from towers on those loops. Every tower must appear exactly once, and reversing a cable
segment can change its cost.
### How large is the search space?
There is no single closed-form coun

## Summary

t because a solution can use any number of loops, variable
loop sizes, and differently anchored and ordered branches. But Paris alone gives a useful lower
bound.
Even if we ignore ordering and branches and only assign each of the 532 terminals to one of
11 distribution hubs, there are `11^532` possible assignments.
A stronger lower bound comes from one deliberately restricted family of valid solutions:
exactly 19 loops of 28 terminals each, with no branches. This covers all 532 terminals because
`19 x 28 = 532`, while staying below the 30-terminal limit for a loop. Order the 532 terminals,
split that ordering into 19 consecutive groups, divide by `19!` because the set of loops is
unordered, and choose one of the 11 hubs for each loop:
`(532! / 19!) x 11^19 ~= 10^1223`
## What I tested
The primary experiment was intentionally narrow:
SettingValueModelsClaude Fable 5, Opus 4.8, Sonnet 5; GPT-5.6 Sol, Terra, LunaModesPlain; native `/goal`Optimization budget30 minutesOuter agent timeout1,900 secondsReasoningMaximum available setting for every modelExecutionHarbor 0.1.43, Docker, subscription authentication
## Results
Before concentrating repetitions on the flagship pair, I ran one matched 30-minute no-hint
pair for every model in the sweep. For Fable and Sol, the chart uses Pair 1 from the replicated
headline set; the other four models have one pair each.
![All six models in one matched 30-minute no-hint pair](/_astro/fig6_all_models_30min.Cp2VuCKx_Z2jLU4Y.webp)
I then repeated the flagship comparison until I had three matched runs for Fable 5 and three
for Sol.
![Clean score distributions](/_astro/fig3_clean_distributions.Ct-GZQ3W_2lndA9.webp)
ModelRunPlain`/goal`Goal minus plainFable 5132,197**31,934**-263Fable 5232,516**32,324**-192Fable 53**32,446**35,178+2,732GPT-5.6 Sol1**33,581**39,371+5,790GPT-5.6 Sol235,539**32,703**-2,836GPT-5.6 Sol333,663**33,313**-350
Negative means `/goal` was better. Goal won four of six trials, so win rate alone makes the
feature look useful. The means tell the other half:
ModelPlain mean`/goal` meanMean effectMedian effectFable 5**32,386**33,145+759 worse-192 betterGPT-5.6 Sol**34,261**35,129+868 worse-350 better
Both models usually got a small benefit and occasionally suffered a large regression. That is
why `/goal` won most runs but made both means worse.
Fable was also clearly stronger. Its plain mean beat Sol’s by 1,875 points, and its goal mean
beat Sol’s by 1,984. More importantly, Fable plain stayed inside a tiny 319-point range while
Sol plain spanned 1,958 points. Fable goal produced the best clean score, 31,934; Fable plain
was the safest configuration.
## Deep dive into the goal command
## The same command hides two different systems
Claude Code and Codex both expose `/goal`, but the implementations are fundamentally different.
![Claude Code and Codex goal architecture](/_astro/fig4_goal_architecture.CUL-v7ck_ZQOPcm.webp)
### Claude Code: a separate evaluator
Claude Code implements `/goal` as a session-scop

## Related Articles

- [[ai music video arena claude vs gpt 5.6]]
- [[kimi k3]]
- [[Automating Ai Away]]
- [[Automating away]]
- [[sequoia ascent]]
