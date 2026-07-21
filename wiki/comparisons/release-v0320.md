---
title: "Release v0.32.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - cloud
  - integration
  - llama
  - mistral
  - prompt-tuning
  - real-time
  - search
  - use-case
  - web
---

# Release v0.32.0

> **Source:** gh-v0320-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/ollama/ollama/releases/tag/v0.32.0 ingested: 2026-07-14 sha256: 2074e97c0de0a32be5e892fa43a32c3bbae03d8ec68636eacb39df646e94f9c3 blog_source: github:ollama/ollama --...
> **Sources:**
>   - gh-v0320-2026-07-14.md
> **Links:**
- [[Release 5.0.0]]
- [[Release Notes: Ollama vv0.31.2]]
- [[Release v0.25.1]]
- [[Release v0.1.481-beta]]
- [[v3.14.0]]

## Key Findings

---
source_url: https://github.com/ollama/ollama/releases/tag/v0.32.0
ingested: 2026-07-14
sha256: 2074e97c0de0a32be5e892fa43a32c3bbae03d8ec68636eacb39df646e94f9c3
blog_source: github:ollama/ollama
---
# Release v0.32.0
## What's Changed
- New interactive agent experience: running `ollama` now launches an agent to help you code and delegate work
```
❯ ollama
Ollama 0.32.0
▸ Chat, Code, & Work (glm-5.2:cloud)
Chat with models, code, search the web, and delegate real work
```
- Renamed the Codex App integration to ChatGPT: use ollama launch chatgpt (and --restore to return to your usual ChatGPT profile)
- Simplified integration selection: the ollama launch menu now only offers the most popular integrations (other integrations can be accessed through `ollama launch`
- Warns before launching older agent models: CodeLlama, Qwen2.5(-coder), Llama 3.x, Mistral, StarCoder, and the base DeepSeek-R1 tags now prompt a deprecation warning before ollama launch continues
**Full Changelog**: https://github.com/ollama/ollama/compare/v0.31.2...v0.32.0

## Summary

See Key Findings for full content.

## Related Articles

- [[Release 5.0.0]]
- [[Release Notes: Ollama vv0.31.2]]
- [[Release v0.25.1]]
- [[Release v0.1.481-beta]]
- [[v3.14.0]]
