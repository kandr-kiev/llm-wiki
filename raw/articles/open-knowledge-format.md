---
type: concept
title: Open Knowledge Format
description: Minimal markdown plus YAML-frontmatter convention for portable agent-readable knowledge bundles.
created: 2026-07-04
updated: 2026-07-04
tags: [okf, schema, knowledge-base]
sources: [raw/articles/google-open-knowledge-format-spec-0-1.md]
confidence: high
contested: false
links: [llm-wiki, model-context-protocol]
---

# Open Knowledge Format

Open Knowledge Format (OKF) is a draft specification for representing knowledge as a directory of markdown files with YAML frontmatter. It is designed to be human-readable, agent-parseable, diffable in Git, and portable across tools.

## Local Use

Local LLM Wiki borrows OKF's minimalism:
- markdown files as units of knowledge;
- YAML frontmatter for routing, filtering, and summaries;
- index/log files as navigation and history;
- permissive consumers that tolerate unknown fields.

The local schema is stricter than OKF because this wiki needs operational discipline for multiple agents.

Related: [[llm-wiki]], [[model-context-protocol]].

# Citations
[1] [OKF raw source](../../raw/google-open-knowledge-format-spec-0-1.md)
