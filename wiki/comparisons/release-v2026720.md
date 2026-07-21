---
title: "Release v2026.7.20"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - claude
  - closed-source
  - cost
  - data
  - dataset
  - deep-learning
  - design-pattern
  - foundation-model
  - gpt
  - llm
  - prompt-tuning
  - real-time
  - review
  - security
  - streaming
  - tool
---

# Release v2026.7.20

> **Source:** gh-v2026720-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.20 ingested: 2026-07-20 sha256: c404c064573d26ce82ae1c98a3b2252741ff8bacb15f2e9758c85ccde689d5ef blog_source: github:N...
> **Sources:**
>   - gh-v2026720-2026-07-20.md
> **Links:**
- [[Automating Ai Away]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[5 Agent Skills I Use Every Day]]
- [[ai music video arena claude vs gpt 5.6]]

## Key Findings

---
source_url: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.20
ingested: 2026-07-20
sha256: c404c064573d26ce82ae1c98a3b2252741ff8bacb15f2e9758c85ccde689d5ef
blog_source: github:NousResearch/hermes-agent
---
# Release v2026.7.20
# Hermes Agent v0.19.0 (v2026.7.20)
**Release Date:** July 20, 2026
**Since v0.18.0:** ~2,245 commits · ~1,065 merged PRs · ~2,465 files changed · ~300,000 insertions · ~36,000 deletions · **~3,300 issues closed** · **450+ community contributors**
> **The Quicksilver Release.** Hermes is the messenger god, and this window we made him move like it. First-turn time-to-first-token dropped **~80% on every platform**, reasoning streams live by default, the desktop app got a ~20-PR speed overhaul (14× faster streaming markdown, virtualized diffs, snappy session switching), and the TUI renders markdown incrementally. Around that speed spine: you can now **manage your Nous subscription without leaving the terminal**, plug **Bitwarden and 1Password** straight into Hermes, let **smart approvals** judge flagged commands for you by default, **watch your subagents work live**, and trust that a finished response **survives a gateway crash** thanks to a durable delivery ledger. This release also rolls up everything from the v0.18.1 and v0.18.2 infrastructure patch tags — those windows are fully documented here.
---
## ✨ Highlights
- **Hermes got dramatically faster — first token in a fraction of the time** — Cold-start "Initializing agent..." used to eat ~4.3 seconds before your first turn even reached the model; it's now ~0.9s, an ~80% cut that applies to the CLI, gateway, TUI, desktop, and cron alike. Round 2 attacked what you *see* while waiting: reasoning models now stream their thinking live by default (no more staring at a spinner for 30 seconds), and the response box paints per token instead of per line. If Hermes ever felt like it took a deep breath before answering, that breath is gone. ([#59332](https://github.com/NousResearch/hermes-agent/pull/59332), [#59389](https://github.com/NousResearch/hermes-agent/pull/59389) — @teknium1)
- **The desktop app speed wave — 20+ targeted perf PRs** — Long replies used to cost 14× more CPU in the markdown splitter than they do now; giant diffs froze the review pane until we virtualized it; switching sessions thrashes layout no more. Streaming no longer re-renders the sidebar and every tool row per token, profile backends pre-warm on hover intent, and boot-hidden panes mount at idle instead of on the cold-start critical path. The net effect: the desktop app feels like a native app under load, even with huge transcripts and busy agents. ([#67154](https://github.com/NousResearch/hermes-agent/pull/67154), [#67818](https://github.com/NousResearch/hermes-agent/pull/67818), [#65898](https://github.com/NousResearch/hermes-agent/pull/65898), [#66033](https://github.com/NousResearch/hermes-agent/pull/66033), [#66747](https://github.com/NousResearch/hermes-agent/pull/66747), [#677

## Summary

42](https://github.com/NousResearch/hermes-agent/pull/67742) and more — @OutThisLife)
- **Manage your Nous plan from the terminal — `/subscription` and `/topup`** — Changing your subscription used to mean a trip to the billing website. Now `/subscription` opens a full flow right in the TUI or classic CLI: see your plan and remaining allowance, preview exactly what an upgrade costs ("Pay $46.30 & upgrade now") or when a downgrade takes effect, and apply it — with scheduled-change banners and undo. The desktop app got a matching billing settings tab. Your wallet never has to leave the keyboard. ([#51639](https://github.com/NousResearch/hermes-agent/pull/51639), [#61054](https://github.com/NousResearch/hermes-agent/pull/61054), [#61067](https://github.com/NousResearch/hermes-agent/pull/61067) — @alt-glitch)
- **Smart approvals are now the default** — When Hermes wants to run a flagged command, an LLM reviewer now assesses it independently instead of asking you to approve every single one — and each verdict covers only that exact command, so a later command matching the same pattern gets its own review. Combined with the new **user-defined deny rules** (which block commands even under yolo mode) and `/deny ` (which tells the agent *why* you refused so it course-corrects), day-to-day approval fatigue drops sharply without giving up control. ([#62661](https://github.com/NousResearch/hermes-agent/pull/62661), [#59164](https://github.com/NousResearch/hermes-agent/pull/59164), [#54518](https://github.com/NousResearch/hermes-agent/pull/54518) — @teknium1)
- **Plug your password manager into Hermes — Bitwarden & 1Password secret sources** — API keys no longer have to live in a plaintext `.env`. A new pluggable `SecretSource` interface lets Hermes fetch secrets from Bitwarden and 1Password (`op://` references) at load time, with multiple vaults enabled simultaneously, deterministic precedence, conflict warnings, and per-variable provenance. This consolidated eleven competing community PRs into one orchestrated interface — future vault providers drop in as plugins. ([#59498](https://github.com/NousResearch/hermes-agent/pull/59498) — @teknium1, 1Password provider salvaged from @hwrdprkns)
- **Watch your subagents work — live transcripts + durable background delegation** — `delegate_task` dispatches now return live transcript files you can `tail -f` the moment the subagents launch: every tool call, result, and streamed reply, one human-readable log per child. And background delegation completions are now **durable** — if the process restarts mid-run, results are restored and delivered through an ownership-checked ledger instead of vanishing. Fan out a fleet, watch any worker live, and never lose the results. ([#67479](https://github.com/NousResearch/hermes-agent/pull/67479), [#63494](https://github.com/NousResearch/hermes-agent/pull/63494) — @teknium1)
- **A finished answer can no longer be lost — the delivery-obligation ledger** — If the gateway died between g

## Related Articles

- [[Automating Ai Away]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[5 Agent Skills I Use Every Day]]
- [[ai music video arena claude vs gpt 5.6]]
