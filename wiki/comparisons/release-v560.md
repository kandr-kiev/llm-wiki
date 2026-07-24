---
title: "Release v5.6.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - audio-generation
  - batch
  - computer-vision
  - cuda
  - data
  - dataset
  - distributed
  - edge
  - efficiency
  - embedding
  - foundation-model
  - gpu
  - hardware
  - image-generation
  - instruction-tuning
  - machine-learning
  - multi-agent
  - multimodal
  - onnx
  - parallel
  - prompt-tuning
  - pytorch
  - quantization
  - retrieval
  - search
  - self-supervised
  - training
  - transformers
  - use-case
  - video-generation
  - zero-shot
---

# Release v5.6.0

> **Source:** gh-v560-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/sentence-transformers/releases/tag/v5.6.0 ingested: 2026-07-14 sha256: 804b5e9c8a8cdd11a72654fa5d3ad59b3065541fe15a7cc8e687c0b0cee59066 blog_source: gith...
> **Sources:**
>   - gh-v560-2026-07-14.md
> **Links:**
- [[release-v0251]]
- [[release-500]]
- [Issue #6385: AsyncGRPO fork-independent epoch counting](https://github.com/pytorch[Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning](https://github.com/pytorch/pytorch/issues/2455)s>=5.0.0 and fix torch.load security warning]]

## Key Findings

---
source_url: https://github.com/huggingface/sentence-transformers/releases/tag/v5.6.0
ingested: 2026-07-14
sha256: 804b5e9c8a8cdd11a72654fa5d3ad59b3065541fe15a7cc8e687c0b0cee59066
blog_source: github:huggingface/sentence-transformers
---
# Release v5.6.0
This minor version is a correctness- and robustness-focused release. It fixes a silent scoring bug for causal-LM rerankers, corrects several hard-negative mining and GIST loss edge cases, restores TSDAE on `transformers` v5, and adds Apple Silicon (MPS) support for the cached losses.
The headline fix affects chat-template models that read the final token position, i.e. causal-LM rerankers (like `Qwen3-Reranker`) and last-token-pooling embedders: when an over-long input was truncated, the chat template's trailing suffix (e.g. the assistant prefill the model scores from) was silently dropped, producing wrong scores with no error. There's also a forward-looking deprecation: loading local custom code without `trust_remote_code=True` now warns, and will require it from v6.0.
Install this version with
```bash
# Training + Inference
pip install sentence-transformers[train]==5.6.0
# Inference only, use one of:
pip install sentence-transformers==5.6.0
pip install sentence-transformers[onnx-gpu]==5.6.0
pip install sentence-transformers[onnx]==5.6.0
pip install sentence-transformers[openvino]==5.6.0
# Multimodal dependencies (optional):
pip install sentence-transformers[image]==5.6.0
pip install sentence-transformers[audio]==5.6.0
pip install sentence-transformers[video]==5.6.0
# Or combine as needed:
pip install sentence-transformers[train,onnx,image]==5.6.0
```
## Fixed silently wrong scores when truncation drops chat-template suffixes (#3787)
Chat-template models render the full conversation to a flat string before tokenizing, so when the rendered input is longer than the tokenizer's `model_max_length`, the tokenizer truncates it from the right and drops the template's trailing suffix: the fixed tokens a template appends *after* the content, e.g. a prompt, instruction, `[/INST]`, or a trailing EOS. For models that read the final token position, this silently corrupted the result:
- causal-LM rerankers (e.g. `Qwen/Qwen3-Reranker-0.6B`) score a pair from the last token's `yes`/`no` logits, and
- last-token-pooling embedders read the final hidden state.
When the suffix was truncated away, that final position landed mid-document instead of after the prefill, so the score or embedding came from the wrong place.
`Transformer.preprocess` now detects when truncation drops the suffix and splices it back onto the tail of each truncated row. Because the fix lives in the shared base `Transformer`, it applies across `SentenceTransformer`, `CrossEncoder`, and `SparseEncoder`. It's enabled by default and saved to the model configuration. Pass `processing_kwargs={"chat_template": {"restore_suffix": False}}` to opt back into raw truncation.
## Hard-negative mining and GIST loss correctness (#3821, #3817, #3816)
A trio

## Summary

 of correctness and scalability fixes for hard-negative mining and the GIST losses:
- Sign-independent relative margin: `mine_hard_negatives(relative_margin=...)` and the `margin_strategy="relative"` branch of `GISTEmbedLoss` / `CachedGISTEmbedLoss` used a multiplicative threshold (`positive * (1 - margin)`) that only behaves correctly when the positive-pair similarity is positive. When that similarity was negative, the threshold moved the wrong way and let through false negatives: candidates *more* similar to the anchor than the true positive. The threshold is now `positive - |positive| * margin`, identical to before for positive scores but correct for negative ones.
- Distributed positive masking in the GIST losses: with `gather_across_devices=True` and a non-zero `margin`, the false-negative suppression mask protected the wrong columns on ranks beyond the first (it ignored the per-rank offset into the gathered batch), which set the true positive's logit to `-inf` and produced a `+inf` loss. The mask now accounts for the cross-rank offset, so multi-GPU GIST training stays finite.
- Memory-bounded mining without FAISS: `mine_hard_negatives(use_faiss=False)` (the default) materialized the full `(queries × corpus)` similarity matrix at once, which could OOM on large corpora. It now batches over the query axis (controlled by `faiss_batch_size`, default 16384), bounding peak memory while producing identical results.
## TSDAE weight tying restored on `transformers` v5 (#3781)
`transformers` v5 removed the private `PreTrainedModel._tie_encoder_decoder_weights` helper that `DenoisingAutoEncoderLoss` (TSDAE) used to tie its separate encoder and decoder. As a stopgap, v5.5 raised a `RuntimeError` for the default `tie_encoder_decoder=True` on `transformers >= 5.0.0`, effectively breaking TSDAE there unless you pinned an older `transformers` or disabled tying. TSDAE now ships its own tying routine that shares storage between encoder and decoder, so it works on both `transformers` =5 with the default settings.
## Deprecation: loading local custom code without `trust_remote_code` (#3807)
Sentence Transformers has historically treated any local model directory as implicitly trusted: local custom code (e.g. `modeling_*.py`) loaded even with `trust_remote_code=False`, unlike `transformers`. This discrepancy might be unexpected, so loading local custom code this way now emits a `FutureWarning`, and from **v6.0** it will require `trust_remote_code=True` like in `transformers`.
## Apple Silicon (MPS) support (#3812, #3818)
Two fixes for training on Apple Silicon:
- Cached losses on MPS: `CachedMultipleNegativesRankingLoss` and `CachedGISTEmbedLoss` crashed at construction on MPS because their `RandContext` used a CUDA-only RNG path. They now run on MPS with deterministic replay preserved.
- Legacy fit path and `SparseEncoder` sparsity on MPS: the legacy `model.fit(..., use_amp=True)` path hard-coded CUDA's AMP `GradScaler` / `autocast`, an[Issue #6385: AsyncGRPO fork-independent epoch counting](https://github.com/pytorch[Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning](https://github.com/pytorch/pytorch/issues/2455)ndent epoch counting]]
- [[release-v0231]]
- [Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning](https://github.com/pytorch/pytorch/issues/2455)
