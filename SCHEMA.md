# Local LLM Wiki Schema

## Domain
Local LLM Wiki is a persistent, markdown-first knowledge base for AI/LLM systems, agent automation, RAG alternatives, MCP integration, OKF-compatible knowledge bundles, and business-process automation patterns.

## Operating Principles
- `raw/` is immutable ground truth. Agents read raw files but do not edit them after ingest.
- `wiki/` is agent-maintained synthesis: concept, entity, source-note, comparison, query, and synthesis pages.
- `SCHEMA.md` is the structural contract for all agents.
- `CLAUDE.md` is the operational contract for Claude Code and compatible coding agents.
- `index.md` is the navigation map. Every wiki page must be listed there.
- `log.md` is append-only. Every ingest/query/lint/design action must be recorded.
- If `raw/` and `wiki/` conflict, `raw/` wins and the wiki page is marked `contested: true` or `confidence: low`.

## Directory Contract

```text
/workspace/llm-wiki/
├── CLAUDE.md
├── SCHEMA.md
├── ARCHITECTURE.md
├── ALGORITHM.md
├── index.md
├── log.md
├── raw/
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── wiki/
│   ├── concepts/
│   ├── entities/
│   ├── comparisons/
│   ├── queries/
│   ├── references/
│   ├── playbooks/
│   ├── synthesis/
│   └── templates/
├── outputs/
├── docs/
└── tools/
```

## Type Taxonomy

|| Type | Folder | Purpose |
|---|---|---|
| `concept` | `wiki/concepts/` | Themes, ideas, theories, definitions |
| `entity` | `wiki/entities/` | People, organizations, products, systems |
| `comparison` | `wiki/comparisons/` | Comparisons, benchmarks, analytics |
| `query` | `wiki/queries/` | Valuable answers filed back into the wiki |
| `synthesis` | `wiki/synthesis/` | Multi-source conclusion |
| `reference` | `wiki/references/` | Static data: serials, passwords, configs, specs |
| `playbook` | `wiki/playbooks/` | Instructions, runbooks, procedures |

> **Note:** Source notes (`wiki/sources/`), events (`wiki/events/`), and digests (`wiki/digests/`) have been removed. Raw sources live in `raw/articles/` (or `raw/papers/`, `raw/transcripts/`). Wiki pages reference raw sources directly via `sources: [raw/articles/filename.md]` frontmatter.

New types must be added to this taxonomy before use. Unknown types → `wiki/misc/` or manual review.

## Frontmatter
Every wiki page must start with YAML frontmatter:

```yaml
---
type: concept | entity | source-note | comparison | query | synthesis
title: Human readable title
description: One sentence summary
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [llm-wiki, okf, mcp]
sources: [raw/articles/example.md]
confidence: high | medium | low
contested: false
links: [other-page-slug]
---
```

## Raw Source Frontmatter
Raw source files must include:

```yaml
---
source_url: https://example.com/source
ingested: YYYY-MM-DD
sha256: <sha256 of body below frontmatter>
---
```

## Tag Taxonomy
Approved tags:
- `llm-wiki`
- `knowledge-base`
- `rag`
- `okf`
- `mcp`
- `obsidian`
- `automation`
- `agent-workflow`
- `schema`
- `ingest`
- `query`
- `lint`
- `source-management`
- `business-process`
- `architecture`
- `comparison`
- `local-llm-hardware`
- `rtx-5070-ti`
- `playbook`
- `reference`
- `event`
- `digest`
- `hermes`
- `storage`
- `fine-tuning`
- `prompt-engineering`
- `open-source-llm`
- `llm-benchmarks`
- `evaluation`
- `helk`
- `mmlu`
- `mt-bench`
- `truthfulqa`
- `safety`
- `robustness`
- `fine-tuning`
- `lora`
- `qlora`
- `dpo`
- `peft`
- `sft`
- `rlhf`
- `prompt-engineering`
- `cot`
- `tot`
- `self-consistency`
- `in-context-learning`
- `zero-shot`
- `few-shot`
- `open-source-llm`
- `llama`
- `mistral`
- `qwen`
- `gemma`
- `glm`
- `deepseek`
- `synthesis`
- `benchmark`
- `cost-economics`
- `qa`
- `faq`
- `local`
- `deployment`
- `configuration`
- `health-check`
- `digest`
- `event`
- `meeting`
- `decision`
- `milestone`
- `company`
- `model`
- `data-engineering`
- `enterprise-ai`
- `ai-safety`
- `cloudflare`
- `serverless`
- `wiki`
- `indexer`
- `orchestration`
- `inference`
- `quantization`
- `serving`
- `toxicity-reduction`
- `constitutional-ai`

New tags must be added here before use.

## Page Thresholds
- Create a page when a concept is central to one source or appears in 2+ sources.
- Update an existing page instead of creating duplicates.
- Do not create pages for passing mentions.
- Split pages over ~200 lines.
- Every concept/comparison/query page should link to at least 2 other pages when possible.

## Link Policy
- Use Obsidian-style `[[wikilinks]]` in prose for conceptual links.
- Use markdown links for raw source paths and external URLs.
- Every new page must be listed in `index.md`.

## Quality Signals
- `confidence: high` — supported by multiple reliable sources or direct spec.
- `confidence: medium` — plausible synthesis from one strong source.
- `confidence: low` — weak, disputed, inferred, or needs review.
- `contested: true` — unresolved contradiction exists.

## Lint Requirements
A lint pass must check:
1. Missing frontmatter.
2. Missing required frontmatter fields.
3. Tags not in taxonomy.
4. Broken `[[wikilinks]]`.
5. Wiki pages absent from `index.md`.
6. Raw hash drift.
7. Pages over 200 lines.
8. Low-confidence or contested pages.

## Agent Handoff Rule
Any external agent, including Claude Code, starts by reading:
1. `CLAUDE.md`
2. `SCHEMA.md`
3. `index.md`
4. last entries of `log.md`

Then it performs only the requested operation and logs the result.
