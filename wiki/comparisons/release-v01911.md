---
title: "Release v0.19.11"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ci-cd
  - claude
  - computer-vision
  - deep-learning
  - foundation-model
  - image-generation
  - nlp
  - open-source
  - parallel
  - prompt-tuning
  - review
  - search
  - self-supervised
  - tool
  - use-case
  - web
---

# Release v0.19.11

> **Source:** gh-v01911-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** --- source_url: https://github.com/QwenLM/qwen-code/releases/tag/v0.19.11 ingested: 2026-07-18 sha256: 07755a572abb71b878263dbb1b97e49c90a3498caa7b1a12bbffc2da8ef8b130 blog_source: github:QwenLM/qwen-...
> **Sources:**
>   - gh-v01911-2026-07-18.md
> **Links:**
- [[Release Notes: Ollama vv0.31.2]]
- [[Release python-v0.7.5]]
- [[Release v0.25.1]]
- [[v0.22.1]]
- [[v3.13.0]]

## Key Findings

---
source_url: https://github.com/QwenLM/qwen-code/releases/tag/v0.19.11
ingested: 2026-07-18
sha256: 07755a572abb71b878263dbb1b97e49c90a3498caa7b1a12bbffc2da8ef8b130
blog_source: github:QwenLM/qwen-code
---
# Release v0.19.11
## Highlights
_See the complete change list below._
## Breaking Changes
No known breaking changes.
## Complete Change List
### Features
- feat(web-shell): add workspace path lock ([#6853](https://github.com/QwenLM/qwen-code/pull/6853)) by @ytahdn
- feat(web-shell): add extension management page ([#6815](https://github.com/QwenLM/qwen-code/pull/6815)) by @ytahdn
- feat(core): emit liveness heartbeats for silent foreground shell commands ([#6876](https://github.com/QwenLM/qwen-code/pull/6876)) by @doudouOUC
- feat(cli): VP mode UX improvements ([#6885](https://github.com/QwenLM/qwen-code/pull/6885)) by @chiga0
- feat(acp): expose tool-call preparation lifecycle ([#6819](https://github.com/QwenLM/qwen-code/pull/6819)) by @ran411285752
- feat(channels): add structured channel memory management ([#6860](https://github.com/QwenLM/qwen-code/pull/6860)) by @qqqys
- feat(ci): add automated PR failure patrol ([#6766](https://github.com/QwenLM/qwen-code/pull/6766)) by @yiliang114
- feat(scripts): add local PR verification gate ([#6873](https://github.com/QwenLM/qwen-code/pull/6873)) by @callmeYe
- feat(web-shell): expose session controls to hosts ([#6906](https://github.com/QwenLM/qwen-code/pull/6906)) by @dreamWB
- feat(channels): support DingTalk webhook delivery to direct messages ([#6891](https://github.com/QwenLM/qwen-code/pull/6891)) by @BenGuanRan
- feat(core): add PDF vision bridge fallback ([#6846](https://github.com/QwenLM/qwen-code/pull/6846)) by @doudouOUC
- feat(cli): add general.notificationMode to silence per-approval notifications (#6898) ([#6922](https://github.com/QwenLM/qwen-code/pull/6922)) by @C0d3N1nja97342
- feat(web-shell): use popovers for composer controls ([#6877](https://github.com/QwenLM/qwen-code/pull/6877)) by @ytahdn
- feat(cli): change default approval mode from default to auto ([#6899](https://github.com/QwenLM/qwen-code/pull/6899)) by @pomelo-nwu
- feat(cli): add /learn command for user-initiated skill creation ([#6440](https://github.com/QwenLM/qwen-code/pull/6440)) by @LaZzyMan
- feat(web-shell): auto-post visual previews (screenshots + flow GIFs) on PRs ([#6880](https://github.com/QwenLM/qwen-code/pull/6880)) by @wenshao
- feat(daemon): add immutable session source metadata ([#6932](https://github.com/QwenLM/qwen-code/pull/6932)) by @ytahdn
- feat(web-shell): add zoom, pan and drag controls to Mermaid diagrams ([#6881](https://github.com/QwenLM/qwen-code/pull/6881)) by @yuanyuanAli
- feat(review): build the Step 4 verifier and Step 5 reverse-audit prompts in code ([#6942](https://github.com/QwenLM/qwen-code/pull/6942)) by @wenshao
- feat(web-shell): maximize a single split pane ([#6951](https://github.com/QwenLM/qwen-code/pull/6951)) by @wenshao
- feat(cli): Add archived session export ([#6911](h

## Summary

ttps://github.com/QwenLM/qwen-code/pull/6911)) by @doudouOUC
- feat(web-shell): show sessions awaiting user action ([#6956](https://github.com/QwenLM/qwen-code/pull/6956)) by @ytahdn
- feat(review): prove Step 4 (verify) and Step 5 (reverse audit) actually ran ([#6965](https://github.com/QwenLM/qwen-code/pull/6965)) by @wenshao
- feat(channels): support natural memory references ([#6952](https://github.com/QwenLM/qwen-code/pull/6952)) by @qqqys
- feat(daemon): add stateless generation SSE ([#6947](https://github.com/QwenLM/qwen-code/pull/6947)) by @ytahdn
- feat(daemon): Aggregate deep health across workspaces ([#6961](https://github.com/QwenLM/qwen-code/pull/6961)) by @doudouOUC
- feat(serve): add workspace MCP management ([#6954](https://github.com/QwenLM/qwen-code/pull/6954)) by @ytahdn
- feat(web-shell): color-code each split pane by workspace ([#6971](https://github.com/QwenLM/qwen-code/pull/6971)) by @wenshao
- feat(review): fold the findings list into the verify/reverse-audit prompt ([#6994](https://github.com/QwenLM/qwen-code/pull/6994)) by @wenshao
- feat(channels): tag daemon sessions with channel source ([#6991](https://github.com/QwenLM/qwen-code/pull/6991)) by @xurik
### Bug Fixes
- fix(web-shell): improve file search and composer focus ([#6845](https://github.com/QwenLM/qwen-code/pull/6845)) by @ytahdn
- fix(web-shell): prevent composer tag update loop ([#6859](https://github.com/QwenLM/qwen-code/pull/6859)) by @ytahdn
- fix(web-shell): make composer height adaptive ([#6872](https://github.com/QwenLM/qwen-code/pull/6872)) by @dreamWB
- fix(web-shell): remove duplicate useWebShellPortalRoot import in ChatEditor ([#6890](https://github.com/QwenLM/qwen-code/pull/6890)) by @C0d3N1nja97342
- fix(ci): skip empty SDK release PR ([#6861](https://github.com/QwenLM/qwen-code/pull/6861)) by @yiliang114
- fix(ci): avoid apt on self-hosted Playwright smoke ([#6865](https://github.com/QwenLM/qwen-code/pull/6865)) by @yiliang114
- fix(webui): honor follow-up accept callback suppression ([#6862](https://github.com/QwenLM/qwen-code/pull/6862)) by @yiliang114
- fix(cli): wrap long compact tool summaries ([#6847](https://github.com/QwenLM/qwen-code/pull/6847)) by @han-dreamer
- fix(web-shell): persist collapsed session group sections across reload ([#6878](https://github.com/QwenLM/qwen-code/pull/6878)) by @samuelhsin
- fix(cli): avoid updating active CLI processes ([#6874](https://github.com/QwenLM/qwen-code/pull/6874)) by @yiliang114
- fix(dingtalk): refresh token for inbound media ([#6903](https://github.com/QwenLM/qwen-code/pull/6903)) by @qqqys
- fix(vscode): run ACP process in Electron Node mode ([#6866](https://github.com/QwenLM/qwen-code/pull/6866)) by @yiliang114
- fix(cli): keep exit_plan_mode plan visible inside the pending viewport clamp (#6867) ([#6882](https://github.com/QwenLM/qwen-code/pull/6882)) by @C0d3N1nja97342
- fix(test): isolate WeCom temporary files across concurrent CI jobs ([#6908](https://github.com/QwenLM/qwen-code/pull/69

## Related Articles

- [[Release Notes: Ollama vv0.31.2]]
- [[Release python-v0.7.5]]
- [[Release v0.25.1]]
- [[v0.22.1]]
- [[v3.13.0]]
