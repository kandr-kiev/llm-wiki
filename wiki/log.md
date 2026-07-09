# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete, cleanup

## [2026-07-09] cleanup | Wiki integrity maintenance — duplicate removal, fallback promotion, wikilink repair

### Tools Created

- `tools/cleanup_duplicates.py` — duplicate page removal (136 lines)
- `tools/promote_fallback_to_base.py` — orphaned `_N` → base version promotion (53 lines)
- `tools/fix_promoted_wikilinks.py` — broken `[[base_N]]` → `[[base]]` wikilink repair (70 lines)

### Actions

- **cleanup_duplicates.py --apply**: Deleted 157 duplicate files across 87 groups
- **promote_fallback_to_base.py --apply**: Promoted 100 orphaned `_N` files to base versions
- **fix_promoted_wikilinks.py --apply**: Fixed 179 broken wikilinks in 62 files
- **playbook created**: `wiki/playbooks/how-to-maintain-wiki-integrity.md` — documents the full toolchain and workflow

### Results

| Metric | Before | After |
|---|---|---|
| Total `.md` files | 207 | 222 |
| Files without suffixes | 133 | 233 |
| Files with `_N` suffixes | 74 | 0 |
| Broken wikilinks (lint) | ~200+ | 0 |
| Pages modified by wikilink fix | — | 62 |

### Lint Status

- **Before cleanup**: 250 issues (majority broken wikilinks)
- **After cleanup**: 121 issues (only `missing from index.md` — orphaned pages, not broken links)
- **Broken wikilinks**: 0 (fully resolved)

## [2026-07-09] lint | Post-cleanup verification

- 222 pages checked
- 0 broken wikilinks
- 121 pages missing from index.md (orphaned pages, not structural errors)
- All `_N` suffix files resolved (0 remaining)
