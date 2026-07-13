---
title: "Issue #2797: feat: add progress_callback parameter to transcribe()"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - audio-generation
  - foundation-model
  - open-source
  - use-case
  - whisper
---
# Issue #2797: feat: add progress_callback parameter to transcribe()

> **Source:** gh-openaiwhisper-issue-2797-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/openai/whisper/issues/2797 ingested: 2026-07-11 sha256: 9e5a3526eb275ef280f0314cfb8495c6fb9ee29102c1d2370c90a242371db44c blog_source: github:openai/whisper --- # Iss...
> **Sources:**
>   - gh-openaiwhisper-issue-2797-2026-07-11.md
> **Links:**
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]
- [[issue-2846-add-recipe-parse-any-document-with-the-unstructured-transform-mcp-server]]
- [[issue-2848-implement-multi-domain-intake-architecture-and-related-specs]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]

## Key Findings

---
source_url: https://github.com/openai/whisper/issues/2797
ingested: 2026-07-11
sha256: 9e5a3526eb275ef280f0314cfb8495c6fb9ee29102c1d2370c90a242371db44c
blog_source: github:openai/whisper
---
# Issue #2797: feat: add progress_callback parameter to transcribe()
**State:** open | **Author:** tahirkhan05 | **Created:** 2026-06-21T14:41:20Z
# feat: add progress_callback parameter to transcribe()
Adds an optional `progress_callback` parameter to `transcribe()` so callers
can track transcription progress without having to parse `tqdm` output or
redirect stdout.
This has been requested in PRs #2469 and #2625, both of which are open but
have no tests and don't handle the `None` case cleanly.
## API
```python
def transcribe(
model,
audio,
*,
progress_callback: Optional[Callable[[int, int], None]] = None,
...
):
```
The callback receives `(current_frame, total_frames)` on each seek update.
Callers can derive percentage as `current / total`.
Example:
```python
def on_progress(current, total):
print(f"{current / total:.0%}")
result = whisper.transcribe(model, "audio.mp3", progress_callback=on_progress)
```
The callback is purely optional — passing `None` (the default) leaves all
existing behaviour unchanged.
## Changes
- `whisper/transcribe.py`: add `progress_callback` parameter, call it inside
the seek loop after `pbar.update()`
- `tests/test_fixes.py`: 3 tests covering callback invocation count, `None`
safety, and correct fraction values
## Testing
```
pytest tests/test_fixes.py -v
```
Related to #2469, #2625.

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]
- [[issue-2846-add-recipe-parse-any-document-with-the-unstructured-transform-mcp-server]]
- [[issue-2848-implement-multi-domain-intake-architecture-and-related-specs]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
