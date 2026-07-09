# Local LLM Wiki Architecture

## Purpose
Build a persistent, compounding knowledge base where raw sources are preserved, synthesized wiki pages are maintained by agents, and future automations can query or extend the knowledge without re-deriving everything from scratch.

## Design Inputs
- Karpathy LLM Wiki pattern: persistent interlinked markdown maintained by an LLM, not query-time-only RAG.
- Open Knowledge Format v0.1: markdown files with YAML frontmatter, portable, diffable, agent-readable.
- MCP architecture: optional final integration layer where the wiki can be exposed as resources/tools/prompts.

## Three-Layer Architecture

### Layer 1 — Raw Sources
Path: `raw/`

Responsibilities:
- Preserve external sources as immutable evidence.
- Store extraction date and body hash.
- Remain the source of truth when synthesized pages conflict.

Subfolders:
- `raw/articles/` — web pages, specs, articles, gists.
- `raw/papers/` — PDFs and academic papers.
- `raw/transcripts/` — meetings, videos, interviews.
- `raw/assets/` — images, diagrams, downloaded attachments.

### Layer 2 — Wiki Pages
Path: `wiki/`

Responsibilities:
- Convert raw material into concept pages, entity pages, comparisons, source notes, and filed answers.
- Maintain cross-links, confidence signals, citations, and index entries.
- Make knowledge navigable by humans and agents.

Subfolders:
- `wiki/concepts/` — reusable knowledge units (concepts, techniques, methods)
- `wiki/entities/` — specific things (hardware, tools, projects)
- `wiki/comparisons/` — side-by-side model/tool/method comparisons
- `wiki/playbooks/` — step-by-step operational runbooks
- `wiki/synthesis/` — multi-source integrated analysis
- `wiki/queries/` — filed Q&A from user interactions
- `wiki/references/` — static reference data (configs, schemas, templates)
- `wiki/templates/` — Markdown templates for new wiki pages

### Layer 3 — Schema and Operations
Files:
- `SCHEMA.md` — structural contract.
- `CLAUDE.md` — operational contract for coding agents.
- `ALGORITHM.md` — step-by-step workflows.
- `index.md` — navigation catalog.
- `log.md` — append-only action history.

## Directory Structure

```
llm-wiki/
├── SCHEMA.md              # Structural contract (types, tags, fields)
├── ARCHITECTURE.md        # This file — technical architecture
├── ALGORITHM.md           # Ingest/query/lint workflows
├── CLAUDE.md              # Agent operational contract
├── index.md               # Navigation catalog
├── log.md                 # Append-only action history
├── raw/                   # Layer 1: Immutable sources
│   ├── articles/          # Web pages, specs, guides
│   ├── papers/            # Academic papers (PDFs)
│   ├── transcripts/       # Meetings, videos, interviews
│   └── assets/            # Images, diagrams, attachments
├── wiki/                  # Layer 2: Synthesized knowledge
│   ├── concepts/          # Reusable knowledge units
│   ├── entities/          # Specific things (hardware, tools)
│   ├── comparisons/       # Side-by-side comparisons
│   ├── playbooks/         # Step-by-step runbooks
│   ├── synthesis/         # Multi-source integrated analysis
│   ├── queries/           # Filed Q&A
│   ├── references/        # Static reference data
│   ├── templates/         # Markdown templates for new pages
└── tools/                 # Layer 3: Operations
    └── wiki_lint.py       # Structural health checker
```

## Data Flow Diagram

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  External    │     │  Ingest      │     │  Raw         │
│  Sources     │────▶│  (curl,      │────▶│  (raw/)      │
│  (URL, PDF,  │     │   scrape)    │     │  Immutable   │
│   paste)     │     └──────────────┘     └──────┬───────┘
└──────────────┘                                 │ sha256 stored
                                                 │
                                                 ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Query       │     │  Lint        │     │  Synthesize  │
│  (index.md,  │◀────│  (wiki_      │◀────│  (agent      │
│  wikilinks)  │     │   lint.py)   │     │   reasoning) │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                  │
                                                  ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Index +     │     │  Log         │     │  Wiki Pages  │
│  Navigation  │◀────│  (log.md)    │◀────│  (wiki/)     │
│  (index.md)  │     │  (append-    │     │  Concepts,   │
│              │     │   only)      │     │  Entities,   │
└──────────────┘     └──────────────┘     │  Comparisons │
                                           └──────────────┘
```

## Page Lifecycle

```
┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐
│  Raw Source │───▶│  Source    │───▶│  Concept/  │───▶│  Published │
│  Created    │    │  Note      │    │  Entity    │    │  (index.md │
│  (sha256)   │    │  (summary  │    │  (full     │    │  entry)    │
│             │    │   of raw)  │    │  content)  │    │            │
└────────────┘    └────────────┘    └────────────┘    └────────────┘
                       │                    │
                       ▼                    ▼
                ┌────────────┐    ┌────────────┐
                │  Comparison│    │  Synthesis │
                │  (multi-   │    │  (multi-   │
                │   source)  │    │   source)  │
                └────────────┘    └────────────┘
                       │                    │
                       ▼                    ▼
                ┌────────────┐    ┌────────────┐
                │  Playbook  │    │  Query/    │
                │  (step-by- │    │  Reference │
                │   step)    │    │  (filed)   │
                └────────────┘    └────────────┘
```

## Agent Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    Hermes Agent (Orchestrator)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. INGEST                                                      │
│     ├─ Detect new raw sources (cron every 30m)                 │
│     ├─ Compute SHA256 hash                                     │
│     ├─ Validate frontmatter (SCHEMA.md)                        │
│     └─ Update index.md                                          │
│                                                                 │
│  2. SYNTHESIZE                                                  │
│     ├─ Create concept/entity pages (wiki/concepts/, wiki/entities/)
│     ├─ Build comparisons (wiki/comparisons/)                  │
│     ├─ Create playbooks (wiki/playbooks/)                      │
│     └─ Produce synthesis (wiki/synthesis/)                     │
│                                                                 │
│  3. VALIDATE                                                    │
│     ├─ Run wiki_lint.py (structural health)                   │
│     ├─ Check SHA256 drift (raw sources)                        │
│     ├─ Verify wikilinks (broken references)                    │
│     └─ Audit tags (SCHEMA.md compliance)                       │
│                                                                 │
│  4. REPORT                                                      │
│     ├─ Update log.md (append-only)                             │
│     ├─ Report issues to user                                   │
│     └─ Suggest next actions                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
   ┌──────────┐            ┌──────────┐            ┌──────────┐
   │ Raw/     │            │ Wiki/    │            │ Tools/   │
   │ (source) │            │ (output) │            │ (lint)   │
   └──────────┘            └──────────┘            └──────────┘
```

## Operational Model

```text
Source URL/File/Paste
  ↓ ingest
raw/<type>/<source>.md + sha256
  ↓ synthesize
wiki/concepts/*.md, wiki/entities/*.md, wiki/comparisons/*.md
  ↓ navigation
index.md + log.md
  ↓ query/lint
answers + health reports + filed query pages
```

## Agent Roles

| Agent | Role |
|---|---|
| Hermes | Orchestrator, source inspection, validation, final reporting |
| Claude Code | Implementation agent for scripts/docs when explicitly delegated |
| Future MCP server | Expose wiki pages as resources and lint/query as tools |

## MCP Position
MCP is intentionally final-phase, not phase-one. The wiki must first be useful as plain files. Later, an MCP server can expose:
- Resources: pages, raw sources, index, log.
- Tools: `ingest_source`, `query_wiki`, `lint_wiki`.
- Prompts: `summarize_source`, `compare_concepts`, `audit_claims`.

## Architecture Decisions

| Decision | Rationale |
|---|---|
| Markdown first | Human-readable, diffable, works in Obsidian/VS Code/Git |
| Raw immutable | Prevents silent corruption of source evidence |
| Wiki mutable | Lets agent synthesis improve over time |
| Index + log mandatory | Prevents knowledge base decay |
| Schema local to repo | Any agent can resume without session memory |
| MCP later | Avoids premature protocol complexity |

## Acceptance Criteria
- A new agent can read `CLAUDE.md`, `SCHEMA.md`, `ALGORITHM.md`, `index.md`, `log.md` and know what to do.
- Every raw source has URL/date/hash frontmatter.
- Every wiki page has valid frontmatter and index entry.
- `tools/wiki_lint.py` reports structural health.
- The first ingest contains at least Karpathy LLM Wiki, OKF spec, and MCP intro/architecture source notes.
