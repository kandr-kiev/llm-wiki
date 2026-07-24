---
title: "Release v0.20.1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - api
  - ci-cd
  - foundation-model
  - mobile
  - open-source
  - parallel
  - prompt-tuning
  - real-time
  - review
  - streaming
  - tool
  - web
---
backlinks:
  - release-v220
---

backlinks:
  - release-v2026772
---

backlinks:
  - release-v2026720
---

backlinks:
  - release-v0321
---

backlinks:
  - release-v0320
---

backlinks:
  - release-v0251
---

backlinks:
  - release-v0231
---

backlinks:
  - release-v0201
---

backlinks:
  - release-v0200
---

backlinks:
  - release-v005
---

backlinks:
  - release-500
---


# Release v0.20.1

> **Source:** gh-v0201-2026-07-21.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://github.com/QwenLM/qwen-code/releases/tag/v0.20.1 ingested: 2026-07-21 sha256: 15a36c4ec33470cf4cdfb73567eeb62a41aee07ec71f2aa770f256369486bdb8 blog_source: github:QwenLM/qwen-c...
> **Sources:**
>   - gh-v0201-2026-07-21.md
> **Links:**
- [[Release v0.20.0]]
- [[Release v0.19.11]]
- [[Hermes Agent v0.18.0 → v0.22.1 Deep Dive & 2026 Trends]]
- [[Release 5.0.0]]
- [[Release v0.23.1]]

## Key Findings

---
source_url: https://github.com/QwenLM/qwen-code/releases/tag/v0.20.1
ingested: 2026-07-21
sha256: 15a36c4ec33470cf4cdfb73567eeb62a41aee07ec71f2aa770f256369486bdb8
blog_source: github:QwenLM/qwen-code
---
# Release v0.20.1
## Highlights
_See the complete change list below._
## Breaking Changes
No known breaking changes.
## Complete Change List
### Features
- feat(autofix): label-driven takeover and release; fix forced-dispatch green no-op ([#7165](https://github.com/QwenLM/qwen-code/pull/7165)) by @wenshao
- feat(autofix): direct takeover of maintainer-fork PRs ([#7213](https://github.com/QwenLM/qwen-code/pull/7213)) by @wenshao
- feat(daemon): Advertise ACP preheat readiness ([#7200](https://github.com/QwenLM/qwen-code/pull/7200)) by @doudouOUC
- feat(autofix): surface the running model in every autofix report ([#7226](https://github.com/QwenLM/qwen-code/pull/7226)) by @wenshao
- feat(review): retry transient API failures once; surface quota clearly ([#7233](https://github.com/QwenLM/qwen-code/pull/7233)) by @wenshao
- feat(core): inspect persisted conversation branches ([#7185](https://github.com/QwenLM/qwen-code/pull/7185)) by @doudouOUC
- feat(core): Route Plan-mode shell commands by safety ([#7172](https://github.com/QwenLM/qwen-code/pull/7172)) by @doudouOUC
- feat(ci): auto-open a deflake fix issue for confirmed flaky tests ([#7231](https://github.com/QwenLM/qwen-code/pull/7231)) by @wenshao
- feat(autofix): auto-manage the bot's own fork PRs without a label ([#7243](https://github.com/QwenLM/qwen-code/pull/7243)) by @wenshao
- feat(web-shell): worktree-isolated sessions for parallel tasks ([#7221](https://github.com/QwenLM/qwen-code/pull/7221)) by @wenshao
- feat(i18n): update catalan translaiton ([#7253](https://github.com/QwenLM/qwen-code/pull/7253)) by @jordimas
- feat: add CODEOWNERS for core harness modules ([#7304](https://github.com/QwenLM/qwen-code/pull/7304)) by @pomelo-nwu
- feat(web-shell): support custom slash command actions ([#7267](https://github.com/QwenLM/qwen-code/pull/7267)) by @ytahdn
- feat(web-shell): add git commit history browser ([#7204](https://github.com/QwenLM/qwen-code/pull/7204)) by @wenshao
- feat: support workspace display names ([#7179](https://github.com/QwenLM/qwen-code/pull/7179)) by @samuelhsin
- feat(channels): add content-safe memory recall telemetry ([#7338](https://github.com/QwenLM/qwen-code/pull/7338)) by @qqqys
- feat(daemon): restore worktree isolation on session load/resume ([#7262](https://github.com/QwenLM/qwen-code/pull/7262)) by @wenshao
- feat(autofix): re-arm a stranded PR with @qwen-code /retry instead of deleting a marker ([#7354](https://github.com/QwenLM/qwen-code/pull/7354)) by @wenshao
- feat(serve): make ACP initialize handshake timeout configurable ([#7246](https://github.com/QwenLM/qwen-code/pull/7246)) by @qwen-code-dev-bot
- feat(autofix): pick up managed fork PRs in real time instead of waiting for the throttled schedule ([#7350](https://github.com/QwenLM/qwen-code/pull/73

## Summary

50)) by @wenshao
- feat(autofix): resolve the review threads whose findings it implemented ([#7364](https://github.com/QwenLM/qwen-code/pull/7364)) by @wenshao
- feat(autofix): render the managed fleet into the scan's run summary ([#7355](https://github.com/QwenLM/qwen-code/pull/7355)) by @wenshao
- feat(core): add fork_turns to fork subagents ([#7346](https://github.com/QwenLM/qwen-code/pull/7346)) by @DragonnZhang
- feat(auth): add Singapore Token Plan region ([#7280](https://github.com/QwenLM/qwen-code/pull/7280)) by @han-dreamer
- feat(web-shell): surface worktree isolation in the new-session empty state ([#7365](https://github.com/QwenLM/qwen-code/pull/7365)) by @wenshao
- feat(core): add opt-in built-in web_search backed by the DashScope Responses API ([#7215](https://github.com/QwenLM/qwen-code/pull/7215)) by @tanzhenxin
- feat(web-shell): Add sidebar customization API for branding, navigation, session actions, and footer ([#7379](https://github.com/QwenLM/qwen-code/pull/7379)) by @yuanyuanAli
- feat(autofix): raise the strict round cap from 5 to 10 ([#7412](https://github.com/QwenLM/qwen-code/pull/7412)) by @wenshao
- feat(autofix): feed the gate's rejection back so the retry can fix what it broke ([#7368](https://github.com/QwenLM/qwen-code/pull/7368)) by @wenshao
### Bug Fixes
- fix(autofix): stage SKILL.md beside run-agent.mjs so review-address boots (P0, regression from #7165) ([#7225](https://github.com/QwenLM/qwen-code/pull/7225)) by @wenshao
- fix(ci): consolidate issue triage ownership ([#7180](https://github.com/QwenLM/qwen-code/pull/7180)) by @yiliang114
- fix(cli): allow goal controls during active loops ([#7202](https://github.com/QwenLM/qwen-code/pull/7202)) by @yiliang114
- fix(cli): show mode indicator alongside steering hint during streaming ([#7219](https://github.com/QwenLM/qwen-code/pull/7219)) by @qwen-code-dev-bot
- fix(scripts): allow multiple dev:daemon instances by probing Vite port ([#7212](https://github.com/QwenLM/qwen-code/pull/7212)) by @wenshao
- fix(review): say an unread chunk once, under its cause ([#7234](https://github.com/QwenLM/qwen-code/pull/7234)) by @wenshao
- fix(autofix): a no-output crash must not advance the review watermark ([#7229](https://github.com/QwenLM/qwen-code/pull/7229)) by @wenshao
- fix(review): prohibit isolation param in roster output and SKILL.md ([#7235](https://github.com/QwenLM/qwen-code/pull/7235)) by @wenshao
- fix(cli): align npm update checks with global registry ([#7224](https://github.com/QwenLM/qwen-code/pull/7224)) by @yiliang114
- fix(test): deflake tool-control E2E content assertions ([#7261](https://github.com/QwenLM/qwen-code/pull/7261)) by @qwen-code-dev-bot
- fix(sdk): abort SSE request on iterator exit to release daemon subscriber ([#7257](https://github.com/QwenLM/qwen-code/pull/7257)) by @chinesepowered
- fix(core): Enforce Plan mode entry boundary ([#7248](https://github.com/QwenLM/qwen-code/pull/7248)) by @doudouOUC
- fix(channels): exclude discrete ACP messa

## Related Articles

- [[Release v0.20.0]]
- [[Release v0.19.11]]
- [[Hermes Agent v0.18.0 → v0.22.1 Deep Dive & 2026 Trends]]
- [[Release 5.0.0]]
- [[Release v0.23.1]]
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "release-500")
```
