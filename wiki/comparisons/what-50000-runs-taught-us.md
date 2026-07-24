---
title: "what 50000 runs taught us"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - application
  - computer-vision
  - container
  - cost
  - data
  - evaluation
  - foundation-model
  - image-generation
  - open-source
  - search
  - system-design
  - tool
  - use-case
  - web
---

# what 50000 runs taught us

> **Source:** what-50000-runs-of-a-5-line-eval-taught-us-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** #### Blog posts -  [GPT-5.5 Prompt Tuning](/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers) -  [Iterating faster with TypeScript 7](/blogs/2026/06/26/iterating-faster-with-ts-7) -...
> **Sources:**
>   - what-50000-runs-of-a-5-line-eval-taught-us-2026-07-17.md
> **Links:**
- [[optimizing-vscode-coding-harness-model-providers]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Mesh LLM: distributed AI computing on iroh]]

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
# What 50,000 Runs of a 5-Line Eval Taught Us
June 19, 2026 by VS Code Eval Team, [@code](https://x.com/code)
Over the last six months, we have run the same tiny eval more than 50,000 times. It gives the VS Code agent one instruction: write a s

## Summary

tring to a file. No large codebase to understand, no test suite to debug, no architectural decision to make. It is our smoke test, a quick way to confirm that the end-to-end model interaction still works.
A task this simple gives us an immediate read on the health of the system: how reliably the agent finishes the work and what kinds of failures show up in practice. We didn't intend it to be more than that. But at this scale, it became a surprisingly rich source of insight into how models approach even the simplest request.
In our [previous post](https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode), we introduced VSC-Bench, the offline evaluation suite we use to measure agent behavior in VS Code. In this blog post, we look at *how* models solve a simple task and what it tells us about efficiency, model selection, and the value of small, stable evals.
## The five-line eval
A simple task is valuable precisely because it removes variables. When the work is unambiguous and the correct answer is fixed, anything that changes between runs comes from the model or the system around it, not from the task itself. That makes a small eval a sensitive instrument: it reacts to harness regressions, infrastructure incidents, and differences in model behavior, without the noise of a complex problem to interpret.
The `say_hello` task we use for this is built around that idea. Every run starts in the same empty workspace, with the same tools and the same fixed prompt, using our VS Code agent harness. The task asks the agent to "Add HELLO to HELLO.txt" and checks two assertions: that the file exists and that it contains the expected content.
`promptSteps:
- text: Add HELLO to HELLO.txt.
assertions:
- check: file_exists("HELLO.txt")
- check: file_contains("HELLO.txt", "HELLO")
`
Because `say_hello` runs as a smoke test before every benchmark suite, it quietly accumulated 50,974 runs across 30 models over six months. That volume turned a basic sanity check into a useful dataset on how differently models handle even the simplest work.
A developer doing this task would recognize that the workspace is empty, create `HELLO.txt`, and add the requested content. In the most direct VS Code agent path, this translates into a single `create_file` tool call with `HELLO` as the file content.
`tool : create_file
args : {
"filePath": "/path/to/workspace/HELLO.txt",
"content": "HELLO"
}
`
Note
The VS Code eval harness includes the workspace state in the initial prompt context. We assume that the model should not perform redundant existence checks.
## How models solve `say_hello`
As expected, the `say_hello` task is easy enough that all models pass it most of the time. The interesting part is not whether they can do the work, but *how* they do it. Can the model recognize that this is a basic request that only requires a simple solution? Or does it still treat it like a complex problem that requires planning, exploration, and search?
To establish a base

## Related Articles

- [[optimizing-vscode-coding-harness-model-providers]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Mesh LLM: distributed AI computing on iroh]]
