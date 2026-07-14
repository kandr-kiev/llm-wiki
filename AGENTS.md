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

