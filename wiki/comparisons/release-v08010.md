---
title: "Release v0.80.10"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - foundation-model
  - use-case
---

# Release v0.80.10

> **Source:** gh-v08010-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://github.com/earendil-works/pi/releases/tag/v0.80.10 ingested: 2026-07-17 sha256: 8948753b60b6f409424cfdb0e9ab9f1c8eb37dd828233334e8115ba3c3f2236b blog_source: github:earendil-wo...
> **Sources:**
>   - gh-v08010-2026-07-17.md
> **Links:**
- [[v0.23.0]]
- [[v0.22.1]]
- [[Release v0.1.49-beta]]
- [[v3.13.0]]
- [[v3.14.0]]

## Key Findings

---
source_url: https://github.com/earendil-works/pi/releases/tag/v0.80.10
ingested: 2026-07-17
sha256: 8948753b60b6f409424cfdb0e9ab9f1c8eb37dd828233334e8115ba3c3f2236b
blog_source: github:earendil-works/pi
---
# Release v0.80.10
### New Features
- **Kimi Coding thinking compatibility** — Kimi Coding models now use adaptive thinking correctly; K3 exposes its supported `max` level and supports replaying empty-signature thinking blocks. See [Kimi For Coding setup](https://github.com/earendil-works/pi/blob/v0.80.10/packages/coding-agent/docs/providers.md#api-keys) and [Model Options](https://github.com/earendil-works/pi/blob/v0.80.10/packages/coding-agent/docs/usage.md#model-options).
### Fixed
- Fixed inherited Kimi Coding requests to use Anthropic adaptive thinking effort without token budgets, and enabled empty thinking signatures for K3 and `kimi-for-coding`.
- Fixed inherited Kimi K3 pricing metadata for Moonshot AI and Moonshot AI China.
- Fixed inherited Kimi Coding K3 thinking-level metadata to expose only the supported `max` level ([#6737](https://github.com/earendil-works/pi/issues/6737)).
- Fixed inherited catalog generation restoring xAI models removed in 0.80.9 ([#6736](https://github.com/earendil-works/pi/issues/6736)).

## Summary

See Key Findings for full content.

## Related Articles

- [[v0.23.0]]
- [[v0.22.1]]
- [[Release v0.1.49-beta]]
- [[v3.13.0]]
- [[v3.14.0]]
