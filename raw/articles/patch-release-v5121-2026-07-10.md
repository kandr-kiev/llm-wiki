---

source_url: https://github.com/huggingface/transformers/releases/tag/v5.12.1
ingested: 2026-07-10
sha256: b8b260adf28efa0a59fe216d0a8967149e098b836fb9c2536b2b757e8b985e13
blog_source: github
---

# Patch release v5.12.1

## Release Notes

# Patch release v5.12.1
Updated the lower bound for PEFT and a fix for auto tokenizer to properly resolve the mistral tokenizer (when `mistral-common` is installed). This is similar to v.5.10.3 minus the fixes that were already included in the main release - vLLM will first target 5.10.3 :hugs: 

* Fix `peft` lower bound #46605 by @hmellor (#46605)
* mistral common backend fix #46667 by @itazap (#46667)


**Full Changelog**: https://github.com/huggingface/transformers/compare/v5.12.0...v5.12.1

## Download

https://github.com/huggingface/transformers/releases/tag/v5.12.1