---
title: "Patch release v5.10.4"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - audio-generation
  - backend
  - few-shot
  - image-generation
  - mistral
  - nlp
  - video-generation
---
# Patch release v5.10.4

> **Source:** patch-release-v5104-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/releases/tag/v5.10.3 ingested: 2026-07-10 sha256: b137e201d9238f9f1a5567ead98ca0893de24a87262e6b3b35a474b293bb28f0 blog_source: github --- #...
> **Sources:**
>   - patch-release-v5104-2026-07-10.md
> **Links:**
- [[release-v0390]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-v5131]]
- [[langchain-openai134]]
- [[release-notes-ollama-vv0312]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/releases/tag/v5.10.3
ingested: 2026-07-10
sha256: b137e201d9238f9f1a5567ead98ca0893de24a87262e6b3b35a474b293bb28f0
blog_source: github
---
# Patch release v5.10.4
## Release Notes
# Patch release v5.10.4
Update: Note that on pypi `5.10.3` doesn't exist and this this saved under `5.10.4` (so essentially a minor version skipped). Sorry about that, that's on me. Just wanted to clarify to make this less confusing!
A few fixes needed for vLLM to sync with transformers :hugs: 
* [fix] regression introduced by #45534 #46456 by @eustlb (#46456)
* Fix {image/video/audio}_token_ids in ProcessorMixin #46500 by @hmellor (#46500)
* Fix InternVL models #46524 by @hmellor (#46524)
* Fix the offsets in processing #46525 by @zucchini-nlp (#46525)
* Fix `peft` lower bound #46605 by @hmellor (#46605)
* mistral common backend fix #46667 by @itazap (#46667)
**Full Changelog**: https://github.com/huggingface/transformers/compare/v5.10.2...v5.10.3
## Download
https://github.com/huggingface/transformers/releases/tag/v5.10.3

## Summary

See Key Findings for full content.

## Related Articles

- [[release-v0390]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-v5131]]
- [[langchain-openai134]]
- [[release-notes-ollama-vv0312]]
