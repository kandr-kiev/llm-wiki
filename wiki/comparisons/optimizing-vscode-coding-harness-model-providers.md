---
title: "optimizing vscode coding harness model providers"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - api
  - application
  - comparison
  - container
  - data
  - fine-tuning
  - foundation-model
  - gpt
  - image-generation
  - open-source
  - prompt-tuning
  - search
  - system-design
  - tool
  - web
---

# optimizing vscode coding harness model providers

> **Source:** how-prompt-tuning-improved-gpt-55-in-vs-code-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** #### Blog posts -  [GPT-5.5 Prompt Tuning](/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers) -  [Iterating faster with TypeScript 7](/blogs/2026/06/26/iterating-faster-with-ts-7) -...
> **Sources:**
>   - how-prompt-tuning-improved-gpt-55-in-vs-code-2026-07-17.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[automating-ai-away-2026-07-07]]

## Key Findings

#### Blog posts
- 
[GPT-5.5 Prompt Tuning](/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers)
- 
[Iterating faster with TypeScript 7](/blogs/2026/06/26/iterating-faster-with-ts-7)
- 
[50,000 Runs, One Eval](/blogs/2026/06/19/what-50000-runs-taught-us)
- 
[Bring Your Own Key](/blogs/2026/06/18/byok-vscode)
- 
[Improving Token Efficiency](/blogs/2026/06/17/improving-token-efficiency-in-github-copilot)
- 
[Coding Harness](/blogs/2026/05/15/agent-harnesses-github-copilot-vscode)
- 
[How VS Code Builds with AI](/blogs/2026/03/13/how-VS-Code-Builds-with-AI)
- 
[Agents for Real-World Dev](/blogs/2026/03/05/making-agents-practical-for-real-world-development)
- 
[Long Distance NES](/blogs/2026/02/26/long-distance-nes)
- 
[Multi-Agent Development](/blogs/2026/02/05/multi-agent-development)
- 
[MCP Apps Support](/blogs/2026/01/26/mcp-apps-support)
- 
[Building docfind](/blogs/2026/01/15/docfind)
- 
[Introducing the VS Code Insiders Podcast](/blogs/2025/12/03/introducing-vs-code-insiders-podcast)
- 
[Announcing Private Marketplace for VS Code](/blogs/2025/11/18/PrivateMarketplace)
- 
[Open Source AI Editor: Second Milestone](/blogs/2025/11/04/openSourceAIEditorSecondMilestone)
- 
[A Unified Agent Experience](/blogs/2025/11/03/unified-agent-experience)
- 
[Expanding Model Choice](/blogs/2025/10/22/bring-your-own-key)
- 
[Introducing auto model selection (preview)](/blogs/2025/09/15/autoModelSelection)
- 
[Command GitHub's Coding Agent from VS Code](/blogs/2025/07/17/copilot-coding-agent)
- 
[Open Source AI Editor: First Milestone](/blogs/2025/06/30/openSourceAIEditorFirstMilestone)
- 
[Full MCP Spec Support](/blogs/2025/06/12/full-mcp-spec-support)
- 
[Enhance productivity with AI + Remote Dev](/blogs/2025/05/27/ai-and-remote)
- 
[Open Source AI Editor](/blogs/2025/05/19/openSourceAIEditor)
- 
[Adding MCP in VS Code](/blogs/2025/05/12/agent-mode-meets-mcp)
- 
[Better AI results with custom instructions](/blogs/2025/03/26/custom-instructions)
- 
[View All Posts](/blogs/archive)
Blogs
GPT-5.5 Prompt Tuning
Iterating faster with TypeScript 7
50,000 Runs, One Eval
Bring Your Own Key
Improving Token Efficiency
Coding Harness
How VS Code Builds with AI
Agents for Real-World Dev
Long Distance NES
Multi-Agent Development
MCP Apps Support
Building docfind
Introducing the VS Code Insiders Podcast
Announcing Private Marketplace for VS Code
Open Source AI Editor: Second Milestone
A Unified Agent Experience
Expanding Model Choice
Introducing auto model selection (preview)
Command GitHub's Coding Agent from VS Code
Open Source AI Editor: First Milestone
Full MCP Spec Support
Enhance productivity with AI + Remote Dev
Open Source AI Editor
Adding MCP in VS Code
Better AI results with custom instructions
View All Posts
# How Prompt Tuning Improved GPT-5.5 in VS Code
July 6, 2026 by VS Code Team, [@code](https://x.com/code)
In our [previous post](https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode), we introduced the VS Code co

## Summary

ding harness, the layer that connects the model to tools, context, instructions, and the agent loop, giving the model the ability to perform coding tasks.
Each model responds to tool calls and instructions differently, and the harness can adapt to improve results. This post walks through a two-week experiment we ran in partnership with OpenAI to tune the `GPT-5.5` system prompt in VS Code. The question was simple: if we nudge the agent to explore less and validate sooner, can it get faster and cheaper without getting worse? With OpenAI's model expertise and our harness data, we tested two small prompt changes, measured them against a control on live traffic, and shipped the winner.
This matters more with usage-based billing in place. Token efficiency isn't only an infrastructure metric: every token the agent spends wandering is a token you pay for and wait on. An agent that reaches a grounded edit sooner is both a better experience and a smaller bill.
## The hypothesis: explore less, validate sooner
Following the launch of `GPT-5.5`, we looked at how the model spent tokens inside the VS Code agent harness, as part of the work described in [Improving token efficiency in GitHub Copilot](https://code.visualstudio.com/blogs/2026/06/17/improving-token-efficiency-in-github-copilot/). Two patterns stood out: where the model spent tokens, and where it over-explored before acting. Agents can spend a lot of effort searching, rereading, and comparing nearby paths before making a useful edit.
That pointed to a single, testable idea: the agent should spend less effort wandering and more effort moving through a deliberate loop of evidence, action, and validation.
![Diagram contrasting an agent that over-explores with many scattered search and read steps before its first edit, versus a Treatment B agent that moves through a deliberate anchor, gather minimal context, edit, and validate loop.](/assets/blogs/2026/07/06/gpt55-agent-loop.svg)
After testing different hypotheses and running offline evaluations, we turned that idea into two variants of the `GPT-5.5` system prompt, both were promising in offline evals, and we tested them against the current default on live traffic.
## Inside the experiment
We ran the experiment in VS Code over a two-week window, splitting `GPT-5.5` agent traffic across two treatment groups and one control group with a 25/25/25 split. Both treatments test the same hypothesis but differ in how much structure they add to the prompt.
Group
Variant name
Description
Traffic allocation
Control
`PRPT_CTRL`
Current default prompt
25%
Treatment A
`PRPT_SRCH`
Economical search and edit: single, compact reminder to limit exploration before acting
25%
Treatment B
`PRPT_LRG`
Large prompt sections: broader restructure covering the full edit-and-validate loop
25%
>**Note:** The allocations add up to 75% because the experiment scorecard compares evenly sized groups. The remaining `GPT-5.5` traffic continued to use the default prompt outside this scoreca

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[automating-ai-away-2026-07-07]]
