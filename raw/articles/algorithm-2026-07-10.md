---

source_url: local:///workspace/llm-wiki/docs/ALGORITHM.md
ingested: 2026-07-10
sha256: e05de1b1aa51876e42f826030bb8b33c4dfe0ba796575764b3d224230437fc30
blog_source: local
---

# Local LLM Wiki Algorithm

## 0. Session Orientation
Before any operation:
1. Read `AGENT.md`.
2. Read `SCHEMA.md`.
3. Read `index.md`.
4. Read recent `log.md` entries.
5. Search existing wiki pages for the target topic.

Completion criterion: agent knows existing pages, taxonomy, and recent work.

## 1. Ingest Algorithm

Input: URL, file path, pasted text, or transcript.

1. Capture raw source.
   - URL: extract markdown/text and save under `raw/articles/` unless it is a paper/transcript.
   - File: copy/extract readable text into `raw/<type>/`.
   - Paste: save as timestamped raw note.
2. Add raw frontmatter: `source_url`, `ingested`, `sha256`.
3. Check existing pages by searching `index.md` and `wiki/**/*.md`.
4. Extract central concepts/entities.
5. For each central concept/entity:
   - create page if threshold is met;
   - otherwise update an existing page;
   - add sources and confidence.
6. Update cross-links.
7. Update `index.md` alphabetically inside sections.
8. Append one `log.md` entry listing all created/updated files.
9. Run lint and record findings.

## 2. Query Algorithm

Input: user question.

1. Read `index.md`.
2. Search relevant terms in `wiki/` and `raw/` if needed.
3. Read relevant wiki pages first.
4. If wiki pages are missing or low-confidence, inspect raw sources.
5. Answer with citations to wiki pages and raw sources.
6. If answer is reusable or analytical, save it under `wiki/queries/` or `wiki/comparisons/`.
7. Update `index.md` and `log.md` if a page was filed.

## 3. Lint Algorithm

1. Enumerate all markdown files under `wiki/` excluding README placeholders.
2. Validate frontmatter.
3. Validate required fields: `type`, `title`, `description`, `created`, `updated`, `tags`, `sources`, `confidence`, `links`.
4. Validate tags against `SCHEMA.md` taxonomy.
5. Extract `[[wikilinks]]`; flag links that do not resolve to a known page slug.
6. Check every wiki page appears in `index.md`.
7. Recompute raw body `sha256`; flag drift.
8. Flag pages over 200 lines.
9. Flag `confidence: low` and `contested: true` for review.
10. Write report to `outputs/lint-report.md`.
11. Append result to `log.md`.

## 4. Update Policy

When new information conflicts with old synthesis:
1. Prefer raw source over wiki synthesis.
2. Prefer newer source only if equally authoritative.
3. Preserve both claims if the conflict is unresolved.
4. Mark page `contested: true` and reduce confidence.
5. Log the conflict.

## 5. Naming Algorithm

1. Lowercase.
2. Transliterate only when needed; keep established English technical names.
3. Replace spaces and punctuation with hyphens.
4. Avoid duplicate slugs.
5. Use folder by type:
   - concepts → `wiki/concepts/<slug>.md`
   - entities → `wiki/entities/<slug>.md`
