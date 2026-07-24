---
title: "Weather Digest Automation Refactor Plan"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - architecture
  - automation
  - claude
  - data
  - design-pattern
  - edge
  - foundation-model
  - news
  - pipeline
  - prompt-tuning
  - use-case
  - workflow
---

# Weather Digest Automation Refactor Plan

> **Source:** local-weather-space-lunar-digestdocsautomation-refactor-planmd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/docs/automation-refactor-plan.md ingested: 2026-07-20 sha256: 9dd39031e459f1f05615db26126f481505bcc31d0d726006b621cb68194cabe3 blo...
> **Sources:**
>   - local-weather-space-lunar-digestdocsautomation-refactor-planmd-2026-07-20.md
> **Links:**
- [[local-llm-wiki-agent-contract]]
- [[local-llm-wiki-agent-contract-legacy]]
- [[local-llm-wiki-algorithm]]
- [[version]]
- [[manifest]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/docs/automation-refactor-plan.md
ingested: 2026-07-20
sha256: 9dd39031e459f1f05615db26126f481505bcc31d0d726006b621cb68194cabe3
blog_source: local:unknown
---
# Weather Digest Automation Refactor Plan
## Target Architecture
```text
skill/SKILL.md
↓ instructions, constraints, examples
scripts/scout.py
↓ collect raw data + location resolution
/output/scout_input.json
↓ payload contract
scripts/render_digest.py + digest-template.md
↓ template-first render
/output/digest_output.md
↓ Telegram/manual/cron delivery
validate_payload.py + tests/
↓ quality gate
```
## Standardized Automation Pattern
Every future business-process automation should ship with:
1. `SKILL.md` — trigger, workflow, pitfalls, verification.
2. `scripts/` — executable entrypoints.
3. `templates/` — user-facing output structure.
4. `references/` — APIs, contracts, debugging notes.
5. `tests/` — behavior tests for edge cases.
6. `validate_*` — schema/template consistency checks.
7. `AGENT_HANDOFF.md` or Claude-compatible section.
## Current Weather Digest Decisions
- Template-first remains the governing rendering model.
- `scout.py` owns location resolution and raw data capture.
- `render_digest.py` owns formatting and placeholder substitution only.
- `digest-pipeline.py` owns orchestration and CLI parameter forwarding.
- `validate_payload.py` owns unresolved placeholder detection.
## Next Development Phases
### Phase 1 — Stabilized Runtime
- Keep current Python scripts.
- Add behavior tests.
- Keep cron prompt simple: run pipeline, read `/output/digest_output.md`, deliver full content.
### Phase 2 — Package Boundary
- Move reusable logic to `weather_digest/` package.
- Keep CLI wrappers for backward compatibility.
- Add provider interfaces for weather, air raid, space, moon, news.
### Phase 3 — Automation Generator Pattern
- Generalize the structure into a reusable skill/app automation template.
- Use this digest as the reference implementation for future business-process pipelines.
## Risk Register
| Risk | Mitigation |
|---|---|
| Template/payload drift | `validate_payload.py` in every run/test |
| Location ambiguity | geocoder scoring + explicit coordinate fallback |
| Non-UA air raid confusion | `not_applicable`, never default to Chernihiv |
| Cron delivery truncation | Telegram chunking in future delivery wrapper |
| Duplicate root/scripts files | keep tests against both where practical |

## Summary

See Key Findings for full content.

## Related Articles

- [[local-llm-wiki-agent-contract]]
- [[local-llm-wiki-agent-contract-legacy]]
- [[local-llm-wiki-algorithm]]
- [[version]]
- [[manifest]]
