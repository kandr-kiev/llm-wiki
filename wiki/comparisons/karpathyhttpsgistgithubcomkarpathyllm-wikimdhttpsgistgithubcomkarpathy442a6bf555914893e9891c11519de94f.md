---
title: "[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - analysis
  - architecture
  - batch
  - best-practice
  - claude
  - data
  - deep-learning
  - design-pattern
  - few-shot
  - guide
  - image-generation
  - llm
  - open-source
  - rag
  - real-time
  - research
  - retrieval
  - search
  - self-supervised
  - synthesis
  - use-case
  - web
---
# [karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**

> **Source:** karpathy-llm-wiki-2026.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md ingested: 2026-07-04 sha256: 62e40a2e6ba3668dafaae...
> **Sources:**
>   - karpathy-llm-wiki-2026.md
> **Links:**
- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[chemical-hygiene]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[animals-vs-ghosts]]

## Key Findings

---
source_url: https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md
ingested: 2026-07-04
sha256: 62e40a2e6ba3668dafaae724811b136f325e98c876222d8099cae697c277d5b5
---
[Skip to content](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#start-of-content)
[](https://gist.github.com/)
Search Gists Search Gists
[All gists](https://gist.github.com/discover)[Back to GitHub](https://github.com/)[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)[Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f&source=header-gist)
[](https://gist.github.com/)
[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)[Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f&source=header-gist)
You signed in with another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.You signed out in another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.You switched accounts on another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.Dismiss alert
{{ message }}
Instantly share code, notes, and snippets.
[![Image 1: @karpathy](https://avatars.githubusercontent.com/u/241138?s=64&v=4)](https://gist.github.com/karpathy)
# [karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**
Created April 4, 2026 16:25
Show Gist options
* [Download ZIP](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/archive/ac46de1ad27f92b28ac95459c782c07f6b8c964a.zip)
* [Star 5,000+(5,000+)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)You must be signed in to star a gist
* [Fork 5,000+(5,000+)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)You must be signed in to fork a gist
* 
Embed # Select an option 
* Embed Embed this gist in your website.
* Share Copy sharable link for this gist.
* Clone via HTTPS Clone using the web URL.
## No results found
[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)
Clone this repository at <script src="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js"></script> 
* Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.
[Code](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)[Revisions 1](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/revisio

## Summary

ns)[Stars 5,000+](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/stargazers)[Forks 5,000+](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/forks)
Embed 
# Select an option
* Embed Embed this gist in your website.
* Share Copy sharable link for this gist.
* Clone via HTTPS Clone using the web URL.
## No results found
[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)
Clone this repository at <script src="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js"></script> 
Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.
[Download ZIP](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/archive/ac46de1ad27f92b28ac95459c782c07f6b8c964a.zip)
llm-wiki 
[Raw](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md)
[**llm-wiki.md**](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#file-llm-wiki-md)
# LLM Wiki
[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki)
A pattern for building personal knowledge bases using LLMs.
This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you.
## The core idea
[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#the-core-idea)
Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.
The idea here is different. Instead of just retrieving from raw documents at query time, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then _kept current_, not re-derived on every query.
This is the key difference: **the wiki is a persistent, compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every q

## Related Articles

- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[chemical-hygiene]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[animals-vs-ghosts]]
