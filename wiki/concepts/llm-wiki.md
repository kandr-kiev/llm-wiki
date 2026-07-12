---
type: concept
title: LLM Wiki
description: Persistent markdown knowledge base maintained by agents as a compounding alternative to query-time-only RAG.
created: 2026-07-04
updated: 2026-07-04
tags: [llm-wiki, knowledge-base, agent-workflow]
sources: [raw/articles/karpathy-llm-wiki-2026.md, raw/articles/google-open-knowledge-format-spec-0-1.md]
confidence: high
contested: false
links: [open-knowledge-format, model-context-protocol, local-llm-hardware]
---# LLM Wiki

An LLM Wiki is a persistent, interlinked markdown knowledge base that an agent maintains over time. Unlike query-time RAG, the agent compiles knowledge into durable pages, updates them during ingest, and files valuable query results back into the wiki.

## Core Pattern

1. Human curates source material.
2. Agent captures source under `raw/`.
3. Agent updates source notes, concepts, entities, comparisons, index, and log.
4. Future queries read the already-compiled wiki first.

## Why It Matters

The value compounds because summaries, contradictions, and cross-links are preserved. The agent does not need to rediscover every relationship from raw chunks each time.

## Local Implementation

This repository implements the pattern with:
- immutable `raw/` sources;
- mutable `wiki/` synthesis;
- schema/algorithm contracts for agents;
- future MCP exposure as optional integration.

Related: [[open-knowledge-format]], [[model-context-protocol]], [[concepts/local-llm-hardware]].

# Citations
[1] [Karpathy LLM Wiki raw source](../../raw/karpathy-llm-wiki-2026.md)
[2] [OKF spec raw source](../../raw/google-open-knowledge-format-spec-0-1.md)
