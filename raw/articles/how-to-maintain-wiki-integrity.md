---
type: playbook
title: Wiki Integrity Maintenance — Tools & Workflow
description: Operational playbook for maintaining wiki integrity using automated tools: duplicate cleanup, fallback promotion, and wikilink fixing
created: 2026-07-09
updated: 2026-07-09
tags: [wiki-maintenance, integrity, duplicates, wikilinks, automation, tools]
sources: []
confidence: high
links: [wiki-lint, integrator, schema-conventions]
---

# Wiki Integrity Maintenance — Tools & Workflow

## Overview

This playbook covers the automated toolchain for maintaining wiki structural integrity. It addresses three critical operations:

1. **Duplicate cleanup** — removing `_1`/``_2`/`_3`/`_4` suffix duplicates created by the integrator
2. **Fallback promotion** — converting orphaned `_N` files to base versions when no canonical page exists
3. **Wikilink fixing** — repairing broken ````[base_1](wiki/base_1.md)```` → ````[base](wiki/base.md)```` references after promotion

**When to run:** After any batch ingest operation, or when `python3 tools/wiki_lint.py` reports broken wikilinks or missing pages.

---

## The Problem

The integrator (`integrator.py`) can create multiple suffixed versions (`_1`, `_2`, `_3`, `_4`) of the same page. This happens when:

- The integrator fails to check for an existing base version before writing
- Multiple source files map to the same conceptual page
- The integrator creates fallback versions as a safety net

Without intervention, the wiki accumulates:
- **Duplicate content** — same information scattered across `_1`, `_2`, `_3` files
- **Broken wikilinks** — other pages link to ```[page_1](wiki/page_1.md)``` which no longer exists after cleanup
- **Stale navigation** — `index.md` references suffixed names instead of clean base names

---

## Tool 1: `cleanup_duplicates.py`

### Purpose

Identifies and removes duplicate wiki pages created with `_N` suffixes.

### Logic

| Condition | Action |
|---|---|
| Base version (no suffix) EXISTS | Delete all `_N` versions — base is canonical |
| Base version does NOT exist | Keep first `_N` as fallback, delete rest |

### Usage

```bash
# Dry-run (default) — preview what would happen
python3 tools/cleanup_duplicates.py

# Apply — actually delete duplicate files
python3 tools/cleanup_duplicates.py --apply
```

### Output Format

```
Found 87 duplicate groups (231 total files)

Groups WITH base version: 74
Groups WITHOUT base version: 13

GROUPS WITHOUT BASE VERSION (need base creation or manual review):
  BASE: wiki/active-learning.md
    [DELETE] wiki/active-learning_07.md

GROUPS WITH BASE VERSION (delete _N versions):
  BASE: wiki/existential-risk.md (KEEP)
    -> wiki/existential-risk_1.md
    -> wiki/existential-risk_2.md

=== DRY RUN ===
Run with --apply to actually delete files.
Would delete: 157 files
```

### Key Details

- **Scans recursively** through all wiki subdirectories (`concepts/`, `entities/`, `comparisons/`, etc.)
- **Groups by base name** — strips `_N` suffix and groups files sharing the same stem
- **Preserves README.md** — never deletes README files in subdirectories
- **Dry-run first** — always preview with `--apply` off before committing changes

### When to Use

After a batch ingest where the integrator created multiple versions. Run `cleanup_duplicates.py` before `promote_fallback_to_base.py` to eliminate clean groups first.

---

## Tool 2: `promote_fallback_to_base.py`

### Purpose

Converts orphaned `_N` files (groups with NO base version) into canonical base versions. This is the **critical step** that the cleanup script alone cannot handle.

### Why This Exists

The cleanup script's logic for groups without a base was conservative: *"keep the first `_N` as fallback."* This is wrong — if no canonical page exists, the `_N` files ARE the only version of that content. They should be promoted to the base name.

### Logic

1. Find all files with `_N` suffixes (where N is a digit)
2. Group them by their base name (strip `_N`)
3. For groups where the base name file does NOT exist → rename highest `_N` to base
4. Report all promotions

### Usage

```bash
# Dry-run (default) — preview what would be promoted
python3 tools/promote_fallback_to_base.py

# Apply — actually rename files
python3 tools/promote_fallback_to_base.py --apply
```

### Output Format

```
Found 100 groups to promote:

[active-learning.md]
  [PROMOTED] active-learning_07.md -> active-learning.md

[advanced-prompt-engineering-techniques-in.md]
  [PROMOTED] advanced-prompt-engineering-techniques-in_2026.md -> advanced-prompt-engineering-techniques-in.md

[COMPLETE] Promoted 100 fallback files to base versions.
```

### Key Details

- **Promotes the highest `_N`** — if multiple `_1`, `_2`, `_3`, `_4` exist, the highest number is promoted (typically the most complete version)
- **Only promotes groups with NO base** — if a base version already exists, it is left untouched
- **Preserves directory structure** — files in `entities/`, `concepts/`, `playbooks/` are renamed in-place
- **100 files promoted in the 2026-07-09 cleanup** — demonstrates the scale of orphaned content

### When to Use

After `cleanup_duplicates.py` has removed clean groups. Run this to convert remaining orphaned `_N` files into clean base names.

---

## Tool 3: `fix_promoted_wikilinks.py`

### Purpose

Fixes broken wikilinks in all wiki files after `promote_fallback_to_base.py` has renamed files. After promotion, other pages still contain ```[base_1](wiki/base_1.md)``` links that now point to non-existent pages.

### The Problem

When `promote_fallback_to_base.py` renames `active-learning_07.md` → `active-learning.md`, every other page that contained ```[active-learning_07](wiki/active/learning_07.md)``` now has a **broken wikilink**. This causes `wiki_lint.py` to report `broken wikilink` errors.

### Logic

1. Build a set of all existing page slugs (filenames without `.md`)
2. Scan every wiki file for ```[...](wiki/....md)``` wikilinks
3. For each link matching `slug_N` pattern, check if `slug` (base) exists
4. If base exists, replace ```[slug_N](wiki/slug_N.md)``` with ```[slug](wiki/slug.md)```

### Usage

```bash
# Dry-run (default) — preview what would be fixed
python3 tools/fix_promoted_wikilinks.py

# Apply — actually fix wikilinks in files
python3 tools/fix_promoted_wikilinks.py --apply
```

### Output Format

```
Found 202 existing slugs.

[FIXED] 12-advanced-rag-techniques-beyond-naive-retrieval_2026.md: 2 fixes
[FIXED] active-learning_07.md: 5 fixes
[FIXED] architecture-overview_architecture.md: 2 fixes
[FIXED] entities/automated-data-readiness-for-scientific-ai-2026-07-07.md: 1 fixes

Total: 62 files, 179 wikilink fixes
[COMPLETE] Fixed 179 broken wikilinks in 62 files.
```

### Key Details

- **Regex-based matching** — uses `r'\[\[([^\]]+)\]\]'` to find all wikilinks
- **Safe replacement** — only replaces `slug_N` when `slug` actually exists
- **Preserves non-duplicate links** — ```[existing-page](wiki/existing/page.md)``` links are untouched
- **Handles nested directories** — scans `entities/`, `concepts/`, `playbooks/`, `synthesis/`, etc.
- **179 fixes in 62 files** (2026-07-09 run) — demonstrates the cascading effect of promotion

### When to Use

**Immediately after** `promote_fallback_to_base.py --apply`. This is a mandatory step — never skip it.

---

## Complete Workflow

The full integrity maintenance sequence:

```bash
cd /workspace/llm-wiki

# Step 1: Run lint to assess current state
python3 tools/wiki_lint.py
# Note: broken wikilinks, missing pages, orphans

# Step 2: Clean up groups where base version exists
python3 tools/cleanup_duplicates.py --apply
# Removes duplicates when canonical page is available

# Step 3: Promote orphaned _N files to base names
python3 tools/promote_fallback_to_base.py --apply
# Converts fallback versions to clean base names

# Step 4: Fix broken wikilinks in all other files
python3 tools/fix_promoted_wikilinks.py --apply
# Repairs  →  references

# Step 5: Run lint to verify
python3 tools/wiki_lint.py
# Should show 0 broken wikilinks, only remaining issues are:
# - Pages missing from index.md (add them manually)
# - Page size warnings (expected for playbooks/synthesis)
```

### Decision Flow

```
wiki_lint.py reports broken wikilinks?
  └─ Yes
     ├─ Are there _1/_2/_3/_4 duplicate files?
     │   ├─ Yes → cleanup_duplicates.py --apply
     │   └─ No → continue
     ├─ Are there orphaned _N files (no base)?
     │   ├─ Yes → promote_fallback_to_base.py --apply
     │   └─ No → continue
     └─ Broken wikilinks remain?
         ├─ Yes → fix_promoted_wikilinks.py --apply
         └─ No → lint should now pass
```

---

## Results — 2026-07-09 Cleanup Run

| Metric | Before | After | Change |
|---|---|---|---|
| Total `.md` files | 207 | 222 | +15 (renamed, not added) |
| Files without suffixes | 133 | 233 | +100 (promoted) |
| Files with `_N` suffixes | 74 | 0 | -74 (all resolved) |
| Broken wikilinks (lint) | 250 | 0 | -250 (all fixed) |
| Files modified by wikilink fix | — | 62 | 179 links repaired |

### Lint Comparison

| Issue Type | Before | After |
|---|---|---|
| Broken wikilinks | ~200+ | **0** |
| Missing from index.md | ~50 | ~50 (unchanged — these are orphaned pages, not broken links) |
| Page size warnings | ~20 | ~20 (expected for playbooks/synthesis) |

---

## Best Practices

1. **Always dry-run first** — never use `--apply` without previewing the output
2. **Run in sequence** — cleanup → promote → fix links → lint. Do not skip steps.
3. **Fix index.md manually** — these tools fix file names and wikilinks, but `index.md` entries must be updated manually
4. **Run lint after every step** — catch errors early before cascading issues
5. **Document in log.md** — record integrity maintenance actions in the wiki log
6. **Prevent duplicates at source** — the integrator bug (not checking base version before writing) should be fixed in `integrator.py` to prevent recurrence

---

## Related Tools

- `tools/wiki_lint.py` — structural validation of wiki pages
- `tools/integrator.py` — source ingestion engine (source of duplicate creation)
- `tools/verify_sha256.py` — SHA256 hash drift detection and correction
- `wiki-maintenance` skill — comprehensive wiki integrity operations

---

## See Also

- `tools/wiki_lint.py` — структурна валідація wiki-сторінок — linting and validation procedures
- `SCHEMA.md` — структура wiki та таксономія тегів — SCHEMA.md structure and tag taxonomy
- `tools/integrator.py` — інженерія інгісту джерел — source ingestion pipeline
