---
title: "Release v0.32.1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - foundation-model
  - multi-agent
  - performance
  - search
  - tool
  - use-case
  - web
---

# Release v0.32.1

> **Source:** gh-v0321-2026-07-16.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://github.com/ollama/ollama/releases/tag/v0.32.1 ingested: 2026-07-16 sha256: f1e4a010e86a77d0b7ab1f117bafdf541dbb64e09e41ebe7f3cfd34b39c6c05e blog_source: github:ollama/ollama --...
> **Sources:**
>   - gh-v0321-2026-07-16.md
> **Links:**
- [[Release v0.32.0]]
- [[Release Notes: Ollama vv0.31.2]]
- [[v0.21.0]]
- [[v0.22.1]]
- [[Release v0.1.481-beta]]

## Key Findings

---
source_url: https://github.com/ollama/ollama/releases/tag/v0.32.1
ingested: 2026-07-16
sha256: f1e4a010e86a77d0b7ab1f117bafdf541dbb64e09e41ebe7f3cfd34b39c6c05e
blog_source: github:ollama/ollama
---
# Release v0.32.1
## What's Changed
- Improved Gemma 4 tool calling and multi-turn reasoning, including more reliable tool-response continuations
- Fixed a recurrent MLX model cache leak that could increase memory use across requests, and improved cache snapshot performance
- MLX text model loading now respects `OLLAMA_LOAD_TIMEOUT`
- Agent web search and fetch now tell users to run `ollama signin` when authentication is required
- The interactive agent now receives the current working directory for better project context
- Fixed `ollama launch` so choosing **Pick another model** for a deprecated model passed with `--model` opens the model picker
- Updated VS Code setup documentation for the official Ollama extension
**Full Changelog**: https://github.com/ollama/ollama/compare/v0.32.0...v0.32.1-rc0

## Summary

See Key Findings for full content.

## Related Articles

- [[Release v0.32.0]]
- [[Release Notes: Ollama vv0.31.2]]
- [[v0.21.0]]
- [[v0.22.1]]
- [[Release v0.1.481-beta]]
