---
title: "Release v2.2.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - backend
  - ci-cd
  - data
  - dataset
  - efficiency
  - energy
  - gptq
  - guide
  - optimization
  - quantization
  - workflow
---
# Release v2.2.0

> **Source:** gh-v220-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/optimum/releases/tag/v2.2.0 ingested: 2026-07-11 sha256: 87b52ef4215bebaf6797696afa9178e198af1dab512cc7fb68018d3737ee566e blog_source: github:huggingface...
> **Sources:**
>   - gh-v220-2026-07-11.md
> **Links:**
- [[release-notes-ollama-vv0312]]
- [[release-v0192]]
- [[release-v160]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-notes-langchain-vlangchain-openai135]]

## Key Findings

---
source_url: https://github.com/huggingface/optimum/releases/tag/v2.2.0
ingested: 2026-07-11
sha256: 87b52ef4215bebaf6797696afa9178e198af1dab512cc7fb68018d3737ee566e
blog_source: github:huggingface/optimum
---
# Release v2.2.0
## What's Changed
* Make sure they run when releasing by @IlyasMoutawwakil in https://github.com/huggingface/optimum/pull/2395
* Remove deprecated INC and IPEX from documentation by @echarlaix in https://github.com/huggingface/optimum/pull/2396
* Handle single-device models without `hf_device_map` after Transformers optimization by @ZX-ModelCloud in https://github.com/huggingface/optimum/pull/2401
* docs: add empirical energy efficiency data to quantization concept guide by @hongping-zh in https://github.com/huggingface/optimum/pull/2410
* Remove optimum-amd from documentation by @echarlaix in https://github.com/huggingface/optimum/pull/2413
* Transformers v5 by @echarlaix in https://github.com/huggingface/optimum/pull/2408
* 🔒 Pin GitHub Actions to commit SHAs by @paulinebm in https://github.com/huggingface/optimum/pull/2418
* chore: bump doc-builder SHA for PR upload workflow by @rtrompier in https://github.com/huggingface/optimum/pull/2422
* Fix gptqmodel backend check by @jiqing-feng in https://github.com/huggingface/optimum/pull/2420
* fix gptq quantization condition by @jiqing-feng in https://github.com/huggingface/optimum/pull/2416
* [CI] Bump style-bot SHA + switch to GitHub App by @paulinebm in https://github.com/huggingface/optimum/pull/2435
* Remove deprecated IPEX pipelines by @echarlaix in https://github.com/huggingface/optimum/pull/2429
* chore: enable Dependabot weekly GitHub Actions bumps by @hf-dependantbot-rollout[bot] in https://github.com/huggingface/optimum/pull/2441
* bump to python 3.10 for workflows by @echarlaix in https://github.com/huggingface/optimum/pull/2443
* Bump the actions group with 7 updates by @dependabot[bot] in https://github.com/huggingface/optimum/pull/2442
* fix tests preprocessor loading by @echarlaix in https://github.com/huggingface/optimum/pull/2445
* Add namespace when loading wikitext dataset by @echarlaix in https://github.com/huggingface/optimum/pull/2446
* fix(exporters): handle read-only config in sentence-transformers >=5 by @SAY-5 in https://github.com/huggingface/optimum/pull/2439
## New Contributors
* @hongping-zh made their first contribution in https://github.com/huggingface/optimum/pull/2410
* @paulinebm made their first contribution in https://github.com/huggingface/optimum/pull/2418
* @rtrompier made their first contribution in https://github.com/huggingface/optimum/pull/2422
* @hf-dependantbot-rollout[bot] made their first contribution in https://github.com/huggingface/optimum/pull/2441
* @SAY-5 made their first contribution in https://github.com/huggingface/optimum/pull/2439
Full Changelog: https://github.com/huggingface/optimum/compare/v2.1.0...v2.2.0

## Summary

See Key Findings for full content.

## Related Articles

- [[release-notes-ollama-vv0312]]
- [[release-v0192]]
- [[release-v160]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-notes-langchain-vlangchain-openai135]]
