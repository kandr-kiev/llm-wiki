# Local LLM Wiki — Agent Contract

## Mission
Maintain `/workspace/llm-wiki` as a persistent, markdown-first, agent-readable knowledge base for LLM systems, automation patterns, and local business-process intelligence.

## Mandatory Orientation
Before writing or answering:
1. Read `SCHEMA.md`.
2. Read `index.md`.
3. Read recent `log.md`.
4. Search for existing relevant pages.

## Ground Truth
- `raw/` wins over `wiki/`.
- `wiki/` is synthesis and may be stale.
- Never edit raw sources after ingest.

## Operations

### ingest
Capture raw source, write to `raw/`, update concepts/entities/comparisons, update index, append log, run lint.

### query
Answer from `wiki/` first, then `raw/` if needed. File valuable synthesis into `wiki/queries/` or `wiki/comparisons/`.

### lint
Run `python3 tools/wiki_lint.py` from `/workspace/llm-wiki` or inspect manually if Python is unavailable. Fix structural problems only when explicitly asked.

## Page Rules
- Every wiki page has YAML frontmatter matching `SCHEMA.md`.
- Every wiki page appears in `index.md`.
- Every material action appends to `log.md`.
- Cross-link concepts with `[[slug]]`.
- Use approved tags from `SCHEMA.md` only.

## Claude Code Handoff
When asked to implement:
1. Treat `docs/ARCHITECTURE.md` and `docs/ALGORITHM.md` as the software requirements.
2. Modify only files inside `/workspace/llm-wiki` unless explicitly instructed.
3. Do not read secrets or config files outside the workspace.
4. Verify with lint before reporting success.

## Current Phase
Phase 1 Foundation Pack completed on 2026-07-04: structure, schema, architecture, algorithm, initial raw sources, initial concept pages, and lint tool.

Phase 2 Consolidation completed on 2026-07-06: removed `wiki/sources/`, `wiki/events/`, `wiki/digests/`; moved `templates/` to `wiki/templates/`; all wiki pages now reference raw sources directly via `sources: [raw/articles/filename.md]` frontmatter.

Phase 3 Batch Ingest completed on 2026-07-07: ingested 52 articles, generated 19 new wiki pages, updated index and log.

Phase 4 Architecture Documentation completed on 2026-07-09: created `docs/ARCHITECTURE.md` covering terminology glossary, three-layer architecture model, detailed algorithms for all 5 scripts, dependency graphs, implicit assumptions (12 items), architectural decisions (11 items), and current system statistics (313 files, 222 wiki pages, 91 raw sources).

Phase 5 Schema & Documentation completed on 2026-07-10: created `SCHEMA.md` (184 tags, 8 categories), consolidated documentation into `docs/` directory, renamed agent contract to `AGENT.md`, streamlined `CLAUDE.md` out of root.

Phase 6 Tag Sync completed on 2026-07-10: tag taxonomy synced across `SCHEMA.md` and `wiki_lint.py`, auto-tagged 101 pages, fixed `audit-report` frontmatter drift.
