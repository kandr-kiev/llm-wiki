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

- [x] Did you read the [contributor guideline](https://github.com/huggingface/trl/blob/main/CONTRIBUTING.md#create-a-pull-request), Pull Request section?
- [ ] Was this discussed/approved via a GitHub issue? _(N/A — found via code review and empirical testing, not previously reported.)_
- [x] Did you make sure to update the documentation with your changes? _(N/A — no docs changes needed; the endpoint's docstring already describes these as error conditions, only the transport status code/body changes.)_
- [x] Did you write any new necessary tests?

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Narrow API error-handling change for client mistakes; non-ValueError failures are unchanged and still surface as 500.
> 
> **Overview**
> **`/get_sequence_logprobs/`** now maps intentional validation and formatting `ValueError`s to **HTTP 400** with the existing message in the response body, instead of an opaque **500**. That covers mismatched `sequences` / `prompt_lengths`, invalid `prompt_length`, sequences over `max_model_len`, and `prompt_logprobs is None` from `_format_logprob_response` (including errors raised in the executor). Only `ValueError` is caught so real server failures still return 500.
> 
> Regression coverage adds **`TestGetSequenceLogprobsErrorHandling`**, which builds the real FastAPI app via `vllm_serve.main()` with mocked vLLM workers and uvicorn, plus a **`require_fastapi`** pytest skip marker in `testing_utils.py`.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 079b8c57836f0a229b9000ebcfdcbf3077c8ba26. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->