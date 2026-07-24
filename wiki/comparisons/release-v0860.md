---
title: "Release v0.86.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - api
  - foundation-model
  - gemini
  - gpt
---

# Release v0.86.0

> **Source:** gh-v0860-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://github.com/Aider-AI/aider/releases/tag/v0.86.0 ingested: 2026-07-17 sha256: 36ebee791ae6f42aab3bdc90c85e8d61f16d301ee2aa7254b52d2de2bc179cf7 blog_source: github:Aider-AI/aider...
> **Sources:**
>   - gh-v0860-2026-07-17.md
> **Links:**
- [[release-v0251]]
- [[release-v0231]]
- [[release-v0149-beta]]
- [[Release Notes: Ollama vv0.31.2]]
- [[v0.22.1]]

## Key Findings

---
source_url: https://github.com/Aider-AI/aider/releases/tag/v0.86.0
ingested: 2026-07-17
sha256: 36ebee791ae6f42aab3bdc90c85e8d61f16d301ee2aa7254b52d2de2bc179cf7
blog_source: github:Aider-AI/aider
---
# Release v0.86.0
- Added support for all GPT-5 models.
- Added support for Grok-4 via `xai/grok-4` and `openrouter/x-ai/grok-4` model names.
- Added support for `gemini/gemini-2.5-flash-lite-preview-06-17` model, by Tamir Zahavi-Brunner.
- `/clear` now prints “All chat history cleared.” so you know it worked, by Zexin Yuan.
- `/undo` output now shows only the first line of each commit message, making it easier to read.
- Added support for `openrouter/moonshotai/kimi-k2` model, by Jack Harrington.
- Display model announcements with no-arg `/model` command.
- Fixed an issue where new settings for an existing model didn't replace the old ones, by Andrew Grigorev.
- Fixed analytics to support the latest PostHog SDK event-capture API.
- Bumped dependencies to pick up latest litellm==1.75.0.
- Aider wrote 88% of the code in this release.

## Summary

See Key Findings for full content.

## Related Articles

- [[release-v0251]]
- [[release-v0231]]
- [[release-v0149-beta]]
- [[Release Notes: Ollama vv0.31.2]]
- [[v0.22.1]]
