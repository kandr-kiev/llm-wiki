# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: ## [YYYY-MM-DD] action | subject
> Actions: ingest, update, query, lint, create, archive, delete, cleanup

## [2026-07-09] cleanup | Wiki integrity maintenance — duplicate removal, fallback promotion, wikilink repair

### Tools Created

- tools/cleanup_duplicates.py — duplicate page removal (136 lines)
- tools/promote_fallback_to_base.py — orphaned _N → base version promotion (53 lines)
- tools/fix_promoted_wikilinks.py — broken [[base_N]] → [[base]] wikilink repair (70 lines)

### Actions

- cleanup_duplicates.py --apply: Deleted 157 duplicate files across 87 groups
- promote_fallback_to_base.py --apply: Promoted 100 orphaned _N files to base versions
- fix_promoted_wikilinks.py --apply: Fixed 179 broken wikilinks in 62 files
- playbook created: wiki/playbooks/how-to-maintain-wiki-integrity.md — documents the full toolchain and workflow

### Results

| Metric | Before | After |
|---|---|---|
| Total .md files | 207 | 222 |
| Files without suffixes | 133 | 233 |
| Files with _N suffixes | 74 | 0 |
| Broken wikilinks (lint) | ~200+ | 0 |
| Pages modified by wikilink fix | — | 62 |

### Lint Status

- Before cleanup: 250 issues (majority broken wikilinks)
- After cleanup: 121 issues (only missing from index.md — orphaned pages, not broken links)
- Broken wikilinks: 0 (fully resolved)

## [2026-07-09] lint | Post-cleanup verification

- 222 pages checked
- 0 broken wikilinks
- 121 pages missing from index.md (orphaned pages, not structural errors)
- All _N suffix files resolved (0 remaining)

## [2026-07-09 16:47 UTC] rss_monitor | Scanned 1306 articles, ingested 20 new sources: raw/articles/ai-content-is-everywhere-on-social-media-especially-linkedin-2026-07-09.md, raw/articles/show-hn-fablecut--a-browser-video-editor-ai-agents-can-drive-zero-deps-2026-07-09.md, raw/articles/agentlens-production-assessed-trajectory-reviews-for-coding-agent-evaluation-2026-07-09.md, raw/articles/when-does-in-context-search-help-a-sampling-complexity-theory-of-reflection-driven-reasoning-2026-07-09.md, raw/articles/llm-powered-reasoning-in-agent-based-modeling-2026-07-09.md, raw/articles/qantis-hardware-calibrated-sequential-pomdp-belief-updates-on-ibm-heron-2026-07-09.md, raw/articles/cost-effective-agent-harnesses-for-abstract-reasoning-and-generalization-on-arc-agi-1-2026-07-09.md, raw/articles/evaluating-sagemath-augmented-llm-agents-for-computational-and-experimental-mathematics-2026-07-09.md, raw/articles/the-harness-effect-how-orchestration-design-sets-the-token-economics-of-enterprise-agentic-ai-2026-07-09.md, raw/articles/grounding-spatial-relations-in-a-compact-world-model-instruction-leakage-and-a-goal-free-dynamics-fi-2026-07-09.md, raw/articles/large-behavior-model-a-promptable-digital-twin-of-the-retail-customer-2026-07-09.md, raw/articles/learning-social-norms-enhances-compatibility-in-dynamic-human-ai-coordination-2026-07-09.md, raw/articles/why-we-cannot-wait-for-better-post-quantum-signature-algorithms-2026-07-09.md, raw/articles/introducing-meerkat-an-experiment-in-global-consensus-2026-07-09.md, raw/articles/our-approach-to-government-and-national-security-partnerships-2026-07-09.md, raw/articles/separating-signal-from-noise-in-coding-evaluations-2026-07-09.md, raw/articles/helping-k12-educators-build-practical-ai-skills-2026-07-09.md, raw/articles/introducing-gpt-live-2026-07-09.md, raw/articles/australian-payments-plus-moves-faster-with-chatgpt-and-codex-2026-07-09.md, raw/articles/mufg-aims-to-become-ai-native-with-openai-2026-07-09.md

## [2026-07-09 17:30 UTC] docs | Created comprehensive architecture documentation: docs/ARCHITECTURE.md (40,391 bytes). Covers: terminology glossary (14 terms), three-layer architecture model, detailed algorithms for all 5 scripts (integrator.py, rss_monitor.py, local_file_monitor.py, github_release_monitor.py, wiki_lint.py), dependency graphs, implicit assumptions (12 items with risk assessment), architectural decisions (11 items with rationale), and current system statistics (313 files total, 222 wiki pages, 91 raw sources).

## [2026-07-09 18:00 UTC] phase5 | Updated root files: CLAUDE.md (Phase 3/4 added), ALGORITHM.md (First Ingest Scope removed), SCHEMA.md (docs/ added to Directory Contract)
