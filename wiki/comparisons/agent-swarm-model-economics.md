---
title: "agent swarm model economics"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - async
  - best-practice
  - cost
  - data
  - dataset
  - foundation-model
  - frontend
  - image-generation
  - news
  - self-supervised
  - web
---

# agent swarm model economics

> **Source:** agent-swarms-and-the-new-model-economics-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://cursor.com/blog/agent-swarm-model-economics ingested: 2026-07-20 sha256: 87c3ef30138b3411c89d22282acb0fc70820d7f1f047198243aa4d891775cb90 blog_source: Hacker News --- - - - - -...
> **Sources:**
>   - agent-swarms-and-the-new-model-economics-2026-07-20.md
> **Links:**
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[Mesh LLM: distributed AI computing on iroh]]

## Key Findings

---
source_url: https://cursor.com/blog/agent-swarm-model-economics
ingested: 2026-07-20
sha256: 87c3ef30138b3411c89d22282acb0fc70820d7f1f047198243aa4d891775cb90
blog_source: Hacker News
---
- - - - - - Agent swarms and the new model economics · Cursor- - - - - - - - - - - - - - - - - - [Skip to content](#main)Cursor
- [Product](/product)↓
- [Agents](/product)
- [Cloud](/cloud)
- [Mobile](/mobile)
- [Automations](/automate)
- [CLI](/cli)
- Marketplace ↗
- [Review](/bugbot)
- [Enterprise](/enterprise)
- [Pricing](/pricing)
- [Resources](/changelog)↓
- [Changelog](/changelog)
- [Blog](/blog)
- [Docs](/docs)
- [Community](/community)
- Help ↗
- [Workshops](/workshops)
- Forum ↗
- [Careers](/careers)
- Product →
- [Enterprise](/enterprise)
- [Pricing](/pricing)
- Resources →
[Sign in](/dashboard)[ContactContact sales](/contact-sales?source=navbar)[Download](/download)[Blog](/blog) / [research](/blog/topic/research)Jul 20, 2026·[research](/blog/topic/research)# Agent swarms and the new model economics
![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fwilson-lin.jpeg&w=48&q=70)Wilson Lin · 17 min read### Table of Contents
↑
- [Trees and leaves](#trees-and-leaves)
- [What the tree does for memory](#what-the-tree-does-for-memory)
- [A version control system for agents](#a-version-control-system-for-agents)
- [Failure modes at 1,000 commits per second](#failure-modes-at-1000-commits-per-second)
- [Review lenses](#review-lenses)
- [Letting agents shape the environment](#letting-agents-shape-the-environment)
- [The SQLite experiment](#the-sqlite-experiment)
- [Results across model mixes](#results-across-model-mixes)
- [A deep dive into the runs](#a-deep-dive-into-the-runs)
- [Model economics](#model-economics)
- [Specs as prompts](#specs-as-prompts)
Earlier this year, we ran experiments to test the limits of scaling agents to cooperate toward a goal. Our hypothesis was that this would unlock a new tier of task scale and complexity.
The flagship project was a long-running swarm [building a web browser from scratch](/blog/scaling-agents). It succeeded as a proof of concept, but fell far short of polished software.
That work was deliberately empirical. We started from a blank canvas and [hill-climbed toward a stable, effective system](/blog/self-driving-codebases). Since then, our goal has been to understand the agent swarm well enough to engineer it deliberately.
To test that progress, we returned to a task the old swarm had struggled with: building SQLite from scratch, in Rust, from nothing but its documentation.
Our initial results have been promising. We ran the old and new swarms on the same task, with the same models and the same time budget, and measured how much of a held-out SQL test suite each could pass.
The new swarm did better in every model configuration. Using Grok 4.5, it reached 80% in four hours, while the old swarm spiraled and had to be paused before its second hour.
We 

## Summary

also varied which models did which jobs. In some runs, one model handled everything while in others, a frontier model planned while a fast, inexpensive model carried out the work. Every mix produced similar quality, but the costs varied enormously.[1](#fn-1)
![Cost to rebuild SQLite by model mix under old and new agent swarms](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcost-to-rebuild-sqlite-by-model-mix-light-2.png&w=1920&q=70)![Cost to rebuild SQLite by model mix under old and new agent swarms](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcost-to-rebuild-sqlite-by-model-mix-dark-2.png&w=1920&q=70)
## [#](#trees-and-leaves)Trees and leaves
Descriptions of large tasks naturally take the shape of trees, with a goal at the root that subdivides recursively into basic units of work. Our swarm has two roles, both organized around that same tree-like decomposition:
- Planner agents, powered by the smartest models, split a goal into pieces and delegate them.
- Worker agents, generally powered by faster and less expensive models, execute those pieces.
The design is a superset of more rigid orchestration systems. Rather than imposing a fixed topology on the problem, the swarm’s shape grows to cover the problem’s contours, and compute and context scale in proportion to the task’s complexity.
We think this is why the design generalizes to tasks as diverse as [building a browser](/blog/scaling-agents), [solving math problems](https://x.com/mntruell/status/2028903020847841336), and [optimizing GPU kernels](/blog/multi-agent-kernels). We’ve also used it internally to find and fix vulnerabilities in open-source software, raise test coverage on our own codebase, and generate billions of tokens of synthetic training data.
## [#](#what-the-tree-does-for-memory)What the tree does for memory
When a single agent takes on a complete task, it has to walk the entire tree itself, descending to each leaf while holding its ancestors, its current position, and the wider goal in context the whole time.
We think this explains why long-running single agents drift. They can either focus on the work in front of them and lose sight of the bigger picture, or hold the big picture and do a worse job on the piece.
In a swarm, a planner never implements, so its context never fills with low-level detail, and a worker never plans, so it can spend all its context on one narrow piece of work.
![Diagram of decomposing work across planner and worker agents in a task tree](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fdecomposing-work-light.png&w=1920&q=70)![Diagram of decomposing work across planner and worker agents in a task tree](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fdecomposing-work-dark-2.png&w=1920&q=70)
W

## Related Articles

- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[Mesh LLM: distributed AI computing on iroh]]
