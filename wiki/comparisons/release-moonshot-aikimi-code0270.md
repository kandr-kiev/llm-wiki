---
title: "Release @moonshot-ai/kimi-code@0.27.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - backend
  - foundation-model
  - open-source
  - policy
  - security
  - streaming
  - tool
  - vector-database
  - web
---

# Release @moonshot-ai/kimi-code@0.27.0

> **Source:** gh-moonshot-aikimi-code0270-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** --- source_url: https://github.com/moonshotai/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.27.0 ingested: 2026-07-18 sha256: 0df6e32e2e038eb64f149f4c139e0dd998169eff8a236f8ba1ca2fc7007c9cf0 blog_so...
> **Sources:**
>   - gh-moonshot-aikimi-code0270-2026-07-18.md
> **Links:**
- [[Release v0.86.0]]
- [[v3.13.0]]
- [[v0.26.1]]
- [[v3.14.0]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]

## Key Findings

---
source_url: https://github.com/moonshotai/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.27.0
ingested: 2026-07-18
sha256: 0df6e32e2e038eb64f149f4c139e0dd998169eff8a236f8ba1ca2fc7007c9cf0
blog_source: github:moonshotai/kimi-code
---
# Release @moonshot-ai/kimi-code@0.27.0
### Minor Changes
- [#1822](https://github.com/MoonshotAI/kimi-code/pull/1822) [`a5c568d`](https://github.com/MoonshotAI/kimi-code/commit/a5c568dc7a84962bae70a16858709c453fc90a07) Thanks [@liruifengv](https://github.com/liruifengv)! - Add the /copy slash command to copy the last assistant message to the clipboard.
- [#1824](https://github.com/MoonshotAI/kimi-code/pull/1824) [`bfecd01`](https://github.com/MoonshotAI/kimi-code/commit/bfecd0128fe7d88971a84095e24ef8a56ba34e71) Thanks [@liruifengv](https://github.com/liruifengv)! - Using an API key for Kimi coding models now also fetches the latest model list automatically.
### Patch Changes
- [#1811](https://github.com/MoonshotAI/kimi-code/pull/1811) [`cec15e2`](https://github.com/MoonshotAI/kimi-code/commit/cec15e2188b24e0f904e5ca660a2e72c06364647) Thanks [@liruifengv](https://github.com/liruifengv)! - Fix Esc and Ctrl+C cancelling compaction instead of closing an open /btw panel.
- [#1806](https://github.com/MoonshotAI/kimi-code/pull/1806) [`9b49694`](https://github.com/MoonshotAI/kimi-code/commit/9b496946dcb3c7fa9507e6d5c251c1941e44a316) Thanks [@sailist](https://github.com/sailist)! - Mount the dev-only /api/v1/debug RPC surface behind the --debug-endpoints flag, exposing every scoped service for local debugging on loopback binds. Pass --debug-endpoints to kimi server run to enable it.
- [#1788](https://github.com/MoonshotAI/kimi-code/pull/1788) [`365ba00`](https://github.com/MoonshotAI/kimi-code/commit/365ba0001de206863ff1de8e106c85d7f187c192) Thanks [@RealKai42](https://github.com/RealKai42)! - Fix `/export-debug-zip` and `kimi export` overwriting the previous ZIP archive when run repeatedly on the same session; the default export filename now includes a timestamp.
- [#1840](https://github.com/MoonshotAI/kimi-code/pull/1840) [`fa7e4ba`](https://github.com/MoonshotAI/kimi-code/commit/fa7e4ba4218703bb1ef3112ab2493496983b0539) Thanks [@7Sageer](https://github.com/7Sageer)! - Fix AGENTS.md files installed as symbolic links being ignored by the web backend.
- [#1829](https://github.com/MoonshotAI/kimi-code/pull/1829) [`1b907b0`](https://github.com/MoonshotAI/kimi-code/commit/1b907b07cdcc0e9cba5203fe40dacae85a4b768d) Thanks [@RealKai42](https://github.com/RealKai42)! - Fix whitespace-only thinking content rendering as a blank bullet line in the transcript, both while streaming and when replaying session history.
- [#1809](https://github.com/MoonshotAI/kimi-code/pull/1809) [`56a321d`](https://github.com/MoonshotAI/kimi-code/commit/56a321d4d127c0b4cf7a3e15e2959ebf3eded192) Thanks [@sailist](https://github.com/sailist)! - web: Fix duplicate workspace groups on Windows when the same folder is opened with different path spellings, s

## Summary

uch as a different drive-letter casing; all of the folder's sessions now list under the single merged group.
- [#1847](https://github.com/MoonshotAI/kimi-code/pull/1847) [`56ba8e0`](https://github.com/MoonshotAI/kimi-code/commit/56ba8e0196a3053ad1115a7e8f8b8c4c0cd1b320) Thanks [@wbxl2000](https://github.com/wbxl2000)! - web: Fix LaTeX formulas rendering as garbled overlapping text when the web UI is accessed over the network; the server's content security policy now allows the inline styles that math and code highlighting rely on, while scripts remain strictly restricted.
- [#1816](https://github.com/MoonshotAI/kimi-code/pull/1816) [`44f3341`](https://github.com/MoonshotAI/kimi-code/commit/44f334191989183d21920f6867c405581347c748) Thanks [@sailist](https://github.com/sailist)! - Harden the embedded key-value engine's durability: WAL compaction now always terminates under sustained write storms instead of chasing the tail forever, a committed write can no longer slip through a compaction rotation undetected, torn WAL tails no longer misplace later disk-mode value pointers, read-only opens never create or modify database files or compact under a live writer, corrupt index-definition files no longer force a full rebuild, stale compaction temp files are cleaned on open, and the process lock can no longer be taken over by several processes at once.
- [#1816](https://github.com/MoonshotAI/kimi-code/pull/1816) [`44f3341`](https://github.com/MoonshotAI/kimi-code/commit/44f334191989183d21920f6867c405581347c748) Thanks [@sailist](https://github.com/sailist)! - Speed up the embedded key-value engine under stress: queries with skip/limit now stream candidates instead of decoding every match first, LRU eviction picks victims in O(1) instead of scanning every key, bursts of simultaneously expired TTL keys are drained within seconds, existence checks and size counting no longer read values when they only need metadata, and one oversized token can no longer poison the full-text index.
- [#1816](https://github.com/MoonshotAI/kimi-code/pull/1816) [`44f3341`](https://github.com/MoonshotAI/kimi-code/commit/44f334191989183d21920f6867c405581347c748) Thanks [@sailist](https://github.com/sailist)! - Cluster readers of the embedded key-value engine now catch up incrementally by replaying only newly appended WAL frames after another process writes, instead of fully reopening the shard on every read; cross-process read latency drops by orders of magnitude at larger shard sizes, and readers still fall back to a full reopen after WAL rotation or truncation.
- [#1816](https://github.com/MoonshotAI/kimi-code/pull/1816) [`44f3341`](https://github.com/MoonshotAI/kimi-code/commit/44f334191989183d21920f6867c405581347c748) Thanks [@sailist](https://github.com/sailist)! - Keep the embedded key-value engine writable when a WAL compaction rotation fails mid-way instead of wedging it until reopen, stop a rolled-back write from erasing a concurrently committed value for the same key, le

## Related Articles

- [[Release v0.86.0]]
- [[v3.13.0]]
- [[v0.26.1]]
- [[v3.14.0]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
