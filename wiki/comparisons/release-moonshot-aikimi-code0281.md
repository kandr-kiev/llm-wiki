---
title: "Release @moonshot-ai/kimi-code@0.28.1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - foundation-model
  - web
---

# Release @moonshot-ai/kimi-code@0.28.1

> **Source:** gh-moonshot-aikimi-code0281-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://github.com/moonshotai/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.28.1 ingested: 2026-07-20 sha256: 8ac9545067057601f2072edbc295887ccf46a218feaf4dbd983046cacfe35293 blog_so...
> **Sources:**
>   - gh-moonshot-aikimi-code0281-2026-07-20.md
> **Links:**
- [[release-moonshot-aikimi-code0280]]
- [[release-moonshot-aikimi-code0270]]
- [[release-v0860]]
- [[v0.28.0]]
- [[v0.22.1]]

## Key Findings

---
source_url: https://github.com/moonshotai/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.28.1
ingested: 2026-07-20
sha256: 8ac9545067057601f2072edbc295887ccf46a218feaf4dbd983046cacfe35293
blog_source: github:moonshotai/kimi-code
---
# Release @moonshot-ai/kimi-code@0.28.1
### Patch Changes
- [#934](https://github.com/MoonshotAI/kimi-code/pull/934) [`c5b6103`](https://github.com/MoonshotAI/kimi-code/commit/c5b6103bb9b0a163d48cbce0034c3fc7dea7c344) Thanks [@tt-a1i](https://github.com/tt-a1i)! - Allow ACP sessions to start with configured non-OAuth model credentials instead of requiring terminal login.
- [#1967](https://github.com/MoonshotAI/kimi-code/pull/1967) [`ad8cc85`](https://github.com/MoonshotAI/kimi-code/commit/ad8cc8525198a08bc1181cee9a15bbb4521cd9bc) Thanks [@sailist](https://github.com/sailist)! - Run web servers foreground-only end to end: the /web slash command now always starts a new server, and the `kimi web kill` / `kimi web ps` subcommands are removed — foreground servers stop with Ctrl+C. `kimi server kill` remains as a deprecated fallback that only stops servers started by a version before 0.28.0.
- [#1948](https://github.com/MoonshotAI/kimi-code/pull/1948) [`f6f4192`](https://github.com/MoonshotAI/kimi-code/commit/f6f4192957ace3f0cceb734a04b3b26b1d2f88be) Thanks [@sailist](https://github.com/sailist)! - Fix running subagents not observing permission mode switches made after they started.

## Summary

See Key Findings for full content.

## Related Articles

- [[release-moonshot-aikimi-code0280]]
- [[release-moonshot-aikimi-code0270]]
- [[release-v0860]]
- [[v0.28.0]]
- [[v0.22.1]]
