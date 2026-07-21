---
title: "byok vscode"
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
  - foundation-model
  - gemini
  - image-generation
  - nlp
  - open-source
  - search
  - system-design
  - use-case
  - web
---

# byok vscode

> **Source:** use-your-own-language-model-key-in-vs-code-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** [Visual Studio Code](/) -  Features  - Agents -  Docs  - Documentation - API - FAQ - Release Notes - Blog - Learn - Events -  Resources  - Extensions - MCP -  [ Download ](/download) ![](/assets/icons...
> **Sources:**
>   - use-your-own-language-model-key-in-vs-code-2026-07-17.md
> **Links:**
- [[iterating faster with ts 7]]
- [[optimizing vscode coding harness model providers]]
- [[Automating Ai Away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
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
# Use your own language model key in VS Code
June 18, 2026 by [Kayla Cinnamon](https://github.com/cinnamon-msft)
At Microsoft Build this year, I had the opportunity to present in the opening keynote. One thing I showed was using local models inside VS Code on the new Surface RTX Spark Dev Box. My model was periodically analyzing my log files and giving me summaries, so I could easily diagnose issues without having to look through the logs myself. Check out the [recording at 12:18](https://build.microsoft.com/sessions/KEY01).
Using local models gives you even greater flexibility when working with agents. Sometimes you want the built-in models available through GitHub Copilot. Sometimes you want to try a new model from a provider your team already uses. Sometimes you want to experiment locally. VS Code allows you to do all of these workflows with bring your own language model key (BYOK) and bring your own local model.
With BYOK in VS Code, you can add models from providers like Azure, Anthropic, Huggingface, Gemini, OpenAI, OpenRouter, or you can run a model locally with Ollama, Foundry Local, and more, then use them directly from the Chat model picker.
![Screenshot of the VS Code Chat model picker showing available language models.](/assets/blogs/2026/06/18/model-dropdown-change-model-v2.png)
## What is BYOK?
BYOK lets you use a language model from a supported provider by adding your own API key or endpoint configuration in VS Code. Once configured, those models appear in the same Chat model picker you already use for Copilot. Support is built in for several providers and VS Code is extensible, so any model provider can enable support through an extension.
This gives you more choice for chat and agent workflows. For example, you can:
- Try models that are not built into VS Code.
- Use a provider your organization already has billing or governance set up for.
- Connect to local models through providers such as Ollama or Foundry Local.
- Pick different models for different tasks, such as quick Q&A, planning, or multi-step agent work.
The goal is to allow you to choose the right model and keep working.
## What BYOK works with
BYOK models are available for VS Code chat experiences, including agent workflows when the selected model supports the required capabilities.
There are a few important details to keep in mind:
- BYOK models work **without** signing into a GitHub account and **without** a Copilot plan. You can add and use models entirely with your own API keys, including fully **offline scenarios with local models**.
- BYOK applies to chat and utility tasks, not standard code completions.
- Some AI features, such as semantic search, inline suggestions, and features that rely on

## Related Articles

- [[iterating faster with ts 7]]
- [[optimizing vscode coding harness model providers]]
- [[Automating Ai Away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Automating away]]
