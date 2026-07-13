---
title: "Issue #2803: Accept common CLI boolean values"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - cuda
  - foundation-model
  - machine-learning
  - open-source
  - pytorch
  - use-case
  - whisper
---
# Issue #2803: Accept common CLI boolean values

> **Source:** gh-openaiwhisper-issue-2803-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/openai/whisper/issues/2803 ingested: 2026-07-11 sha256: f9d633941c1980985e75ade03ad18280cf4406097244be3d998c420a549c7a9e blog_source: github:openai/whisper --- # Iss...
> **Sources:**
>   - gh-openaiwhisper-issue-2803-2026-07-11.md
> **Links:**
- [[issue-2797-feat-add-progress_callback-parameter-to-transcribe]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-14168-fix-batching-and-precomputed-embeddings-in-kandinsky-5-pipelines]]
- [[issue-2844-add-avian-magnetoreception-quantum-co-scientist-example]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]

## Key Findings

---
source_url: https://github.com/openai/whisper/issues/2803
ingested: 2026-07-11
sha256: f9d633941c1980985e75ade03ad18280cf4406097244be3d998c420a549c7a9e
blog_source: github:openai/whisper
---
# Issue #2803: Accept common CLI boolean values
**State:** open | **Author:** Jalendar10 | **Created:** 2026-06-28T03:05:48Z
## Summary
Accept common CLI boolean spellings in `str2bool` so command-line flags like `--fp16 false`, `--verbose false`, and `--word_timestamps true` work in addition to the current `True`/`False` values.
## Changes
- Normalize boolean arguments case-insensitively.
- Accept `true`/`false`, `1`/`0`, and `yes`/`no`.
- Add focused tests for accepted and rejected values.
## Validation
- `python3 -m pytest tests/test_utils.py tests/test_tokenizer.py tests/test_normalizer.py -q`
- `python3 -m pytest tests/test_utils.py tests/test_audio.py tests/test_tokenizer.py tests/test_normalizer.py tests/test_timing.py -q -m 'not requires_cuda'`
- `python3 -m pytest tests -q -m 'not requires_cuda' --ignore=tests/test_transcribe.py`
- `python3 -m black --check whisper/utils.py tests/test_utils.py`
- `python3 -m isort --check-only whisper/utils.py tests/test_utils.py`
- `python3 -m flake8 tests/test_utils.py`
Notes:
- I did not run `tests/test_transcribe.py` because it downloads/runs every model.
- Running timing tests without filtering `requires_cuda` fails on this machine because the installed PyTorch build has no CUDA support; the non-CUDA run passed with 28 passed and 8 deselected.

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-2797-feat-add-progress_callback-parameter-to-transcribe]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-14168-fix-batching-and-precomputed-embeddings-in-kandinsky-5-pipelines]]
- [[issue-2844-add-avian-magnetoreception-quantum-co-scientist-example]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
