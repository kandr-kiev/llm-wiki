---
type: concept
title: Model Context Protocol
description: Client-server protocol for exposing tools, resources, prompts, and context to AI applications.
created: 2026-07-04
updated: 2026-07-04
tags: [mcp, automation, agent-workflow]
sources: [raw/articles/model-context-protocol-intro-architecture.md]
confidence: high
contested: false
links: [llm-wiki, open-knowledge-format, local-llm-hardware]
---

# Model Context Protocol

Model Context Protocol (MCP) standardizes how AI applications connect to external data sources, tools, prompts, and workflows. It uses a client-server architecture with hosts, clients, and servers.

## Role in Local LLM Wiki

MCP is not required for the first phase. The wiki should remain useful as plain markdown files. Later, an MCP server can expose:
- wiki pages as resources;
- `query_wiki`, `lint_wiki`, and `ingest_source` as tools;
- reusable prompts for source summarization and comparison.

Related: [[llm-wiki]], [[open-knowledge-format]], [[local-llm-hardware]].

# Citations
[1] [MCP raw source](../../raw/model-context-protocol-intro-architecture.md)
