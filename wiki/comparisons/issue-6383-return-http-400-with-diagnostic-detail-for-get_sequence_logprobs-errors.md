---
title: "Issue #6383: Return HTTP 400 with diagnostic detail for get_sequence_logprobs errors"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - design-pattern
  - few-shot
  - foundation-model
  - gpu
  - multi-agent
  - open-source
  - real-time
  - review
  - training
---

# Issue #6383: Return HTTP 400 with diagnostic detail for get_sequence_logprobs errors

> **Source:** gh-huggingfacetrl-issue-6383-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/trl/issues/6383 ingested: 2026-07-14 sha256: 19bb597936c71e62f41fccc3450b7823ad435069487995062550a5f5089070fc blog_source: github:huggingface/trl --- # I...
> **Sources:**
>   - gh-huggingfacetrl-issue-6383-2026-07-14.md
> **Links:**
- [[Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]]
- [[Issue #2848: Implement multi-domain intake architecture and related specs]]
- [[Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]]
- [[Issue #3430: FIX HiRA ConvNd layers with groups > 1 crash on forward, not just merge]]
- [[Issue #14167: FlashPack support for transformers pipeline components]]

## Key Findings

---
source_url: https://github.com/huggingface/trl/issues/6383
ingested: 2026-07-14
sha256: 19bb597936c71e62f41fccc3450b7823ad435069487995062550a5f5089070fc
blog_source: github:huggingface/trl
---
# Issue #6383: Return HTTP 400 with diagnostic detail for get_sequence_logprobs errors
**State:** open | **Author:** DaoyuanLi2816 | **Created:** 2026-07-14T05:40:39Z
## What does this PR do?
`trl/scripts/vllm_serve.py`'s `/get_sequence_logprobs/` endpoint (`get_sequence_logprobs`, plus the `_format_logprob_response` helper it calls) raises intentional, diagnostic `ValueError`s for a few conditions:
- mismatched `sequences` / `prompt_lengths` lengths
- an out-of-range `prompt_length`
- a sequence longer than `--max-model-len`
- `prompt_logprobs is None` when formatting the vLLM output
None of these are ever caught. The file has no `HTTPException` usage and no exception handler, and the app runs without `debug=True`, so FastAPI's default handling turns every one of them into a content-free `500 Internal Server Error`. Training-time callers (`VLLMClient.get_sequence_logprobs()` — used by the SDFT/SDPO/Distillation live-teacher-server path) only ever see:
```
Exception: Request failed: 500, Internal Server Error
```
with none of the diagnostic detail the endpoint already computed, e.g. `"Sequence 0 has prompt_length=5 which is out of range [0, 3]. prompt_length must be between 0 and the sequence length inclusive."`.
This PR wraps `get_sequence_logprobs`'s body in a single `try/except ValueError`, re-raising as `HTTPException(status_code=400, detail=str(e))`. `_format_logprob_response` runs via `await loop.run_in_executor(...)`, and an exception raised in that executor thread propagates through the `await`, so this one wrapper at the endpoint boundary also covers the formatting helper's `ValueError`s — no need to repeat a `try/except` at every raise site. The `except` is scoped to `ValueError` only (not `Exception`), so unrelated failures (e.g. a DP worker crash surfaced through the batching queue) still propagate as a genuine 500.
Verified empirically, not just by inspection: constructed the real app via `vllm_serve.main()` (faking only the DP worker process/pipe and the uvicorn serve loop, since a live server needs a GPU) and hit `/get_sequence_logprobs/` with `TestClient(raise_server_exceptions=False)` for each condition above — 500 with no detail before the fix, 400 with the actual message after, reverting/reapplying to confirm both directions.
Added `TestGetSequenceLogprobsErrorHandling` to `tests/test_vllm_client_server.py` (and a small `require_fastapi` marker in `tests/testing_utils.py`, following the existing `require_vllm` pattern) covering 3 of the conditions above through that same real-app-construction approach, so this is regression-tested without needing a live multi-accelerator vLLM server.
## Before submitting
- [x] Did you read the [contributor guideline](https://github.com/huggingface/trl/blob/main/CONTRIBUTING.md#create-a-pull-request), 

## Summary

See Key Findings for full content.

## Related Articles

- [[Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]]
- [[Issue #2848: Implement multi-domain intake architecture and related specs]]
- [[Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]]
- [[Issue #3430: FIX HiRA ConvNd layers with groups > 1 crash on forward, not just merge]]
- [[Issue #14167: FlashPack support for transformers pipeline components]]
