---
title: "Release v5.14.1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - few-shot
  - foundation-model
---

# Release v5.14.1

> **Source:** gh-v5141-2026-07-16.md
> **Type:** comparison
> **Created:** 2026-07-16
> **Updated:** 2026-07-16
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/releases/tag/v5.14.1 ingested: 2026-07-16 sha256: 1ab6913c81ea1dd3b67bdb93a20645a17689c7fdd6243cfbaa731e7557004ee7 blog_source: github:huggi...
> **Sources:**
>   - gh-v5141-2026-07-16.md
> **Links:**
- [[Release v5.6.0]]
- [[v0.22.1]]
- [[Patch release v5.10.4]]
- [[Release v0.25.1]]
- [[Release v5.14.0]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/releases/tag/v5.14.1
ingested: 2026-07-16
sha256: 1ab6913c81ea1dd3b67bdb93a20645a17689c7fdd6243cfbaa731e7557004ee7
blog_source: github:huggingface/transformers
---
# Release v5.14.1
# Patch release v5.14.1
This patch solves a few issues which appeared when integrating Inkling model, most notably an issue affecting models using EncoderDecoderCache during assisted generation. It also fixes an issue that could appear during prefill with StaticCache and sdpa without padding for Inkling which uses a position_bias. 
It contains the following commits:
- Fix sdpa prefill with position_bias (#47359) by @Cyrilvallez
- Fix assisted decoding for models with EncoderDecoder cache & OlmoHybrid (#47361) by @Cyrilvallez
- [FP8] Bump kernels version (#47344) by @vasqu 
- Fix deepgemm on multiple devices (#47323) by @IlyasMoutawwakil

## Summary

See Key Findings for full content.

## Related Articles

- [[Release v5.6.0]]
- [[v0.22.1]]
- [[Patch release v5.10.4]]
- [[Release v0.25.1]]
- [[Release v5.14.0]]
