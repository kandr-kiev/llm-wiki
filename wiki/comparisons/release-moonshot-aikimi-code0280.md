---
title: "Release @moonshot-ai/kimi-code@0.28.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - backend
  - foundation-model
  - mobile
  - prompt-tuning
  - tool
  - web
---

# Release @moonshot-ai/kimi-code@0.28.0

> **Source:** gh-moonshot-aikimi-code0280-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://github.com/moonshotai/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.28.0 ingested: 2026-07-20 sha256: 62244779fab137acffb142a232467c195e17b51abeb268f68c9e2e699efde24e blog_so...
> **Sources:**
>   - gh-moonshot-aikimi-code0280-2026-07-20.md
> **Links:**
- [[Release @moonshot-ai/kimi-code@0.27.0]]
- [[Release v0.86.0]]
- [[kimi k3]]
- [[Release Notes: Ollama vv0.31.2]]
- [[Release v0.1.49-beta]]

## Key Findings

---
source_url: https://github.com/moonshotai/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.28.0
ingested: 2026-07-20
sha256: 62244779fab137acffb142a232467c195e17b51abeb268f68c9e2e699efde24e
blog_source: github:moonshotai/kimi-code
---
# Release @moonshot-ai/kimi-code@0.28.0
### Minor Changes
- [#1826](https://github.com/MoonshotAI/kimi-code/pull/1826) [`a41a09c`](https://github.com/MoonshotAI/kimi-code/commit/a41a09c33c8e432fbc306f5882692c967ed5ea17) Thanks [@sailist](https://github.com/sailist)! - Replace the `kimi server` command tree with `kimi web`: the server runs in the foreground (the background daemon and OS-service lifecycle commands are removed), and multiple servers can now share one home directory, each taking the next free port. Manage instances with `kimi web kill [server-id|all]`, `kimi web ps`, and `kimi web rotate-token`; any `kimi server …` invocation prints a deprecation notice and exits 1.
- [#1933](https://github.com/MoonshotAI/kimi-code/pull/1933) [`11c1683`](https://github.com/MoonshotAI/kimi-code/commit/11c1683a1cd2adab276562419d2d353629063d80) Thanks [@liruifengv](https://github.com/liruifengv)! - Thinking effort persists only levels below the model's top tier (max).
### Patch Changes
- [#1867](https://github.com/MoonshotAI/kimi-code/pull/1867) [`3086e47`](https://github.com/MoonshotAI/kimi-code/commit/3086e4703992fbbe7a41379405ee243713ad9ced) Thanks [@RealKai42](https://github.com/RealKai42)! - Rename the stale "afk" reference to "auto" in the built-in MCP config skill guidance.
- [#1867](https://github.com/MoonshotAI/kimi-code/pull/1867) [`3086e47`](https://github.com/MoonshotAI/kimi-code/commit/3086e4703992fbbe7a41379405ee243713ad9ced) Thanks [@RealKai42](https://github.com/RealKai42)! - Correct the YOLO and Auto permission mode descriptions in CLI --help output and in the ACP session mode selector shown by IDE clients.
- [#1867](https://github.com/MoonshotAI/kimi-code/pull/1867) [`3086e47`](https://github.com/MoonshotAI/kimi-code/commit/3086e4703992fbbe7a41379405ee243713ad9ced) Thanks [@RealKai42](https://github.com/RealKai42)! - web: Correct the YOLO and Auto permission mode descriptions in the slash command list and the mobile permission sheet.
- [#1867](https://github.com/MoonshotAI/kimi-code/pull/1867) [`3086e47`](https://github.com/MoonshotAI/kimi-code/commit/3086e4703992fbbe7a41379405ee243713ad9ced) Thanks [@RealKai42](https://github.com/RealKai42)! - Fix the YOLO and Auto permission mode descriptions to match their actual behavior: YOLO auto-approves tool actions but the agent may still ask questions, while Auto is fully autonomous and never asks.
- [#1867](https://github.com/MoonshotAI/kimi-code/pull/1867) [`3086e47`](https://github.com/MoonshotAI/kimi-code/commit/3086e4703992fbbe7a41379405ee243713ad9ced) Thanks [@RealKai42](https://github.com/RealKai42)! - Correct the YOLO mode notice shown when replaying a session: tool actions are auto-approved, but the agent may still ask questions.
- [#1843](https://gi

## Summary

See Key Findings for full content.

## Related Articles

- [[Release @moonshot-ai/kimi-code@0.27.0]]
- [[Release v0.86.0]]
- [[kimi k3]]
- [[Release Notes: Ollama vv0.31.2]]
- [[Release v0.1.49-beta]]
