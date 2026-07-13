---
title: "Release v5.13.1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - use-case
---
# Release v5.13.1

> **Source:** gh-v5131-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/releases/tag/v5.13.1 ingested: 2026-07-11 sha256: 54ff6d08069301a47f9f252325e7c382e00d3413c70a46d38c879a3a85954b2d blog_source: github:huggi...
> **Sources:**
>   - gh-v5131-2026-07-11.md
> **Links:**
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[release-v0390]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-v1140]]
- [[release-notes-ollama-vv0312]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/releases/tag/v5.13.1
ingested: 2026-07-11
sha256: 54ff6d08069301a47f9f252325e7c382e00d3413c70a46d38c879a3a85954b2d
blog_source: github:huggingface/transformers
---
# Release v5.13.1
# Patch release v5.13.1 
This patch is focused on enabling `transformers` for the latest release of vllm! 
- Be more defensive with remap_legacy_layer_types for custom models (#47245) from @hmellor 
- Fix custom code which doesn't know about the new linear layer type names (#47174) from @hmellor 
- Fix case where _LazyAutoMapping.register is passed a str key (#47148) from @hmellor

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[release-v0390]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-v1140]]
- [[release-notes-ollama-vv0312]]
