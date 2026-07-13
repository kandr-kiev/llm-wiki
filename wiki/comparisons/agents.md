---
title: "agents"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - async
  - best-practice
  - design-pattern
  - edge
  - guide
  - image-generation
  - llama
  - llm
  - mlops
  - open-source
  - research
  - use-case
---
# agents

> **Source:** agents-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://huyenchip.com//2025/01/07/agents.html ingested: 2026-07-10 sha256: 059f0521cfb1d22b0d7cd325b88bc0b022b3eb2d7144bb7a02ce3f51d3f2a42d blog_source: Chip Huyen --- Agents -  -  -...
> **Sources:**
>   - agents-2026-07-10.md
> **Links:**
- [[automating-ai-away-2026-07-07]]
- [[how-to-engineer-prompts]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]

## Key Findings

---
source_url: https://huyenchip.com//2025/01/07/agents.html
ingested: 2026-07-10
sha256: 059f0521cfb1d22b0d7cd325b88bc0b022b3eb2d7144bb7a02ce3f51d3f2a42d
blog_source: Chip Huyen
---
Agents
- 
- 
- 
- 
Agents | Chip Huyen
- 
- 
[Chip Huyen](/)
[Blog](/blog/)
[Books](/books/)
[Events](/events/)
AI Guide**
- [AI Roadmap](/mlops/)
- [Good AI List](https://goodailist.com)
- [ML Interviews](https://huyenchip.com/ml-interviews-book/)
[List 100](/list-100/)
[Chip's Lib](https://instagram.com/chipslib)
[VN](https://huyenchip.com/vn/)
- 
**Table of Contents**
**
[Agent Overview](#agent_overview)
[Tools](#tools)
- [Knowledge augmentation](#knowledge_augmentation)
- [Capability extension](#capability_extension)
- [Write actions](#write_actions)
[Planning](#planning)
- [Planning overview](#planning_overview)
- [Foundation models as planners](#foundation_models_as_planners)
- [Plan generation](#plan_generation)
- [Function calling](#function_calling)
- [Planning granularity](#planning_granularity)
- [Complex plans](#complex_plans)
- [Reflection and error correction](#reflection_and_error_correction)
- [Tool selection](#tool_selection)
[Agent Failure Modes and Evaluation](#agent_failure_modes_and_evaluation)
- [Planning failures](#planning_failures)
- [Tool failures](#tool_failures)
- [Efficiency](#efficiency)
[Conclusion](#conclusion)
Table of Contents **
# Agents
Jan 7, 2025
• Chip Huyen
Intelligent agents are considered by many to be the ultimate goal of AI. The classic book by Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (Prentice Hall, 1995), defines the field of AI research as “*the study and design of rational agents.*”
The unprecedented capabilities of foundation models have opened the door to agentic applications that were previously unimaginable. These new capabilities make it finally possible to develop autonomous, intelligent agents to act as our assistants, coworkers, and coaches. They can help us create a website, gather data, plan a trip, do market research, manage a customer account, automate data entry, prepare us for interviews, interview our candidates, negotiate a deal, etc. The possibilities seem endless, and the potential economic value of these agents is enormous.
This section will start with an overview of agents and then continue with two aspects that determine the capabilities of an agent: tools and planning. Agents, with their new modes of operations, have new modes of failure. This section will end with a discussion on how to evaluate agents to catch these failures.
*This post is adapted from the **Agents** section of [**AI Engineering**](https://amzn.to/49j1cGS) (2025) with minor edits to make it a standalone post.*
**Notes**:
- AI-powered agents are an emerging field with no established theoretical frameworks for defining, developing, and evaluating them. This section is a best-effort attempt to build a framework from the existing literature, but it will evolve as the field does. Compared to the r

## Summary

est of the book, this section is more experimental. I received helpful feedback from early reviewers, and I hope to get feedback from readers of this blog post, too.
- Just before this book came out, Anthropic published a blog post on [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (Dec 2024). I’m glad to see that Anthropic’s blog post and my agent section are [conceptually aligned](https://cedricchee.com/blog/the-dna-of-ai-agents/), though with slightly different terminologies. However, Anthropic’s post focuses on isolated patterns, whereas my post covers why and how things work. I also focus more on planning, tool selection, and failure modes.
- The post contains a lot of background information. Feel free to skip ahead if it feels a little too in the weeds!
## Agent Overview
The term *agent* has been used in many different engineering contexts, including but not limited to a software agent, intelligent agent, user agent, conversational agent, and reinforcement learning agent. So, what exactly is an agent?
An agent is anything that can perceive its environment and act upon that environment. *Artificial Intelligence: A Modern Approach* (1995) defines an agent as anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.
This means that an agent is characterized by the *environment* it operates in and *the set of actions* it can perform.
The *environment* an agent can operate in is defined by its use case. If an agent is developed to play a game (e.g., *Minecraft,* Go, *Dota*), that game is its environment. If you want an agent to scrape documents from the internet, the environment is the internet. A self-driving car agent’s environment is the road system and its adjacent areas.
The *set of actions* an AI agent can perform is augmented by the *tools* it has access to. Many generative AI-powered applications you interact with daily are agents with access to tools, albeit simple ones. ChatGPT is an agent. It can search the web, execute Python code, and generate images. RAG systems are agents—text retrievers, image retrievers, and SQL executors are their tools.
There’s a strong dependency between an agent’s environment and its set of tools. The environment determines what tools an agent can potentially use. For example, if the environment is a chess game, the only possible actions for an agent are the valid chess moves. However, an agent’s tool inventory restricts the environment it can operate in. For example, if a robot’s only action is swimming, it’ll be confined to a water environment.
Figure 6-8 shows a visualization of [SWE-agent](https://arxiv.org/abs/2405.15793) (Yang et al., 2024), an agent built on top of GPT-4. Its environment is the computer with the terminal and the file system. Its set of actions include navigate repo, search files, view files, and edit lines.
![A coding agent](/assets/pics/agents/1-swe-agent.png)
Figure 6-8. SWE

## Related Articles

- [[automating-ai-away-2026-07-07]]
- [[how-to-engineer-prompts]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
