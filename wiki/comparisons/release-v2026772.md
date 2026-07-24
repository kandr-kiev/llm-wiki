---
title: "Release v2026.7.7.2"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - docker
  - image-generation
  - use-case
---

# Release v2026.7.7.2

> **Source:** gh-v2026772-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.7.2 ingested: 2026-07-17 sha256: 01bb9fbd5776a8fbd9d85fcebc13c0261af646381ed84c3b3afe38ba78767f41 blog_source: github:...
> **Sources:**
>   - gh-v2026772-2026-07-17.md
> **Links:**
- [[release-v0149-beta]]
- [[release-500]]
- [[release-v080]]
- [[v0.22.1]]
- [[release-v005]]

## Key Findings

---
source_url: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.7.2
ingested: 2026-07-17
sha256: 01bb9fbd5776a8fbd9d85fcebc13c0261af646381ed84c3b3afe38ba78767f41
blog_source: github:NousResearch/hermes-agent
---
# Release v2026.7.7.2
# Hermes Agent v0.18.2 (v2026.7.7.2)
**Release Date:** July 7, 2026
> Same-day patch on top of v0.18.1, picking up the WhatsApp Baileys dependency fix needed for tagged-release Docker builds.
---
## What's in this patch
- **fix(whatsapp): unpin Baileys from git commit, use published 7.0.0-rc13** ([#60643](https://github.com/NousResearch/hermes-agent/pull/60643)) — the WhatsApp bridge dependency now installs from the published npm release instead of a pinned git commit, making installs and Docker image builds reliable.
Full curated release notes for the entire post-v0.18.0 window ship with v0.19.0.
## Updating
```bash
hermes update # existing installs
pip install -U hermes-agent
```
**Full Changelog**: [v2026.7.7...v2026.7.7.2](https://github.com/NousResearch/hermes-agent/compare/v2026.7.7...v2026.7.7.2)

## Summary

See Key Findings for full content.

## Related Articles

- [[release-v0149-beta]]
- [[release-500]]
- [[release-v080]]
- [[v0.22.1]]
- [[release-v005]]
