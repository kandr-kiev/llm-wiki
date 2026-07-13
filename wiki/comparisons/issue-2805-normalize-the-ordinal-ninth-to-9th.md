---
title: "Issue #2805: Normalize the ordinal "ninth" to "9th""
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - few-shot
  - open-source
  - real-time
  - whisper
---
# Issue #2805: Normalize the ordinal "ninth" to "9th"

> **Source:** gh-openaiwhisper-issue-2805-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/openai/whisper/issues/2805 ingested: 2026-07-11 sha256: b6eb29d521ea92143cdeca61bbf19983c1ce51543af15d80b72beac14ddf02c9 blog_source: github:openai/whisper --- # Iss...
> **Sources:**
>   - gh-openaiwhisper-issue-2805-2026-07-11.md
> **Links:**
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[Issue #47256: [serge] integration failure triage -]]
- [[issue-2797-feat-add-progress_callback-parameter-to-transcribe]]
- [[issue-3423-fix-ln-tuning-re-initializing-new-adapters-from-a-previously-merged-adapter]]

## Key Findings

---
source_url: https://github.com/openai/whisper/issues/2805
ingested: 2026-07-11
sha256: b6eb29d521ea92143cdeca61bbf19983c1ce51543af15d80b72beac14ddf02c9
blog_source: github:openai/whisper
---
# Issue #2805: Normalize the ordinal "ninth" to "9th"
**State:** open | **Author:** iammcoding | **Created:** 2026-07-02T14:26:03Z
The English number normalizer builds ordinal words by adding "th" to the cardinal word, with a few hardcoded exceptions (first, second, third, fifth, eighth, twelfth). "nine" was missing from those exceptions, so the rule produced "nineth", which nobody writes, and the real word "ninth" was never recognized.
As a result "ninth" was left as text instead of "9th", and compound ordinals broke: "twenty ninth" came out as "20 ninth" and "one hundred and ninth" as "100 and ninth".
Added "ninth" to the hardcoded ordinals and excluded 9 from the generated rule. Added tests for the simple and compound cases.

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[Issue #47256: [serge] integration failure triage -]]
- [[issue-2797-feat-add-progress_callback-parameter-to-transcribe]]
- [[issue-3423-fix-ln-tuning-re-initializing-new-adapters-from-a-previously-merged-adapter]]
