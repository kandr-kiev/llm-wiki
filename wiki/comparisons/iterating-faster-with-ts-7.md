---
title: "iterating faster with ts 7"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - api
  - application
  - computer-vision
  - container
  - data
  - image-generation
  - open-source
  - search
  - system-design
  - web
---

# iterating faster with ts 7

> **Source:** iterating-faster-with-typescript-7-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** [Visual Studio Code](/) -  Features  - Agents -  Docs  - Documentation - API - FAQ - Release Notes - Blog - Learn - Events -  Resources  - Extensions - MCP -  [ Download ](/download) ![](/assets/icons...
> **Sources:**
>   - iterating-faster-with-typescript-7-2026-07-17.md
> **Links:**
- [[optimizing vscode coding harness model providers]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[The Illustrated Stable Diffusion]]
- [[Automating away]]

## Key Findings

[Visual Studio Code](/)
- 
Features 
- Agents
- 
Docs 
- Documentation
- API
- FAQ
- Release Notes
- Blog
- Learn
- Events
- 
Resources 
- Extensions
- MCP
- 
[
Download
](/download)
![](/assets/icons/search-dark.svg)
![](/assets/icons/search.svg)
Search
![Switch to the dark theme](/assets/icons/theme-light.svg)
![Switch to the light theme](/assets/icons/theme-dark.svg)
[
Download
](/Download)
[📼 Rewatch VS Code Live at MS Build 2026](https://aka.ms/VSCode/Livestage?source=vsc-website-banner)
Dismiss this update
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
Introducing auto 

## Summary

model selection (preview)
Command GitHub's Coding Agent from VS Code
Open Source AI Editor: First Milestone
Full MCP Spec Support
Enhance productivity with AI + Remote Dev
Open Source AI Editor
Adding MCP in VS Code
Better AI results with custom instructions
View All Posts
# Iterating faster with TypeScript 7
June 26, 2026 by VS Code Team, [@code](https://x.com/code)
VS Code and TypeScript practically grew up together. We made a bet early on to write VS Code in TypeScript, and we have always worked closely with the TypeScript team to provide great built-in TypeScript and JavaScript language support in VS Code. This post is about the next step of that journey: TypeScript 7, and how collaborating on adopting TypeScript 7 sped up our builds, improved the day-to-day editing loop for both developers and agents, and helped the TypeScript team ship a more tested release.
TypeScript 7 is a [complete port of the TypeScript compiler and language tooling in Go](https://devblogs.microsoft.com/typescript/typescript-native-port/). That means it's fast, more than 10x faster in many cases. VS Code had a lot to gain from those speedups, so we were naturally eager to adopt TypeScript 7 as soon as we could.
However, we also knew that this would take time. When we started this process in the summer of 2025, TypeScript 7 was actually already shockingly far along for a complete rewrite, but it still had type checking inconsistencies and lacked many features we needed. Even so, we wanted to start testing and providing feedback right away. Adopting TypeScript 7 while it was still being built may sound a little crazy, but it turned out to be a great decision for both VS Code and TypeScript.
## An incremental migration
The VS Code team has never been afraid to take on large engineering efforts, whether that's enabling [strict null checking in our codebase](https://code.visualstudio.com/blogs/2019/05/23/strict-null), adding [remote development support](https://code.visualstudio.com/blogs/2019/05/02/remote-development), or addressing and preventing dangerous code patterns across thousands of files. A common theme across these efforts is that we try to take an incremental approach. This means breaking big, complex problems down into small steps. Those steps happen in the main codebase (no forks or long-lived branches), and each one usually brings a small improvement as it lands. Take enough little steps, and eventually you can look back and realize that you've quietly conquered that once seemingly insurmountable challenge.
We wanted to take the same approach to adopting TypeScript 7. For us, that meant gradually introducing TypeScript 7 into different parts of our workflows and codebases, starting with lower-impact, lower-risk areas before eventually moving on to the main areas of VS Code. There are many benefits to working incrementally, but two were especially important for this effort:
- 
Reduced risk. Each step of the adoption was relatively small, so if something went w

## Related Articles

- [[optimizing vscode coding harness model providers]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[The Illustrated Stable Diffusion]]
- [[Automating away]]
