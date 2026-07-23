---
title: "Issue #2197: perf: reduce BPE tokenizer load-time memory"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - benchmark
  - cost
  - data
  - foundation-model
  - llama
  - open-source
  - parallel
  - real-time
  - streaming
---

# Issue #2197: perf: reduce BPE tokenizer load-time memory

> **Source:** gh-huggingfacetokenizers-issue-2197-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/tokenizers/issues/2197 ingested: 2026-07-14 sha256: eae095de872db771ac4b6f667bc86c2e7a812dcad0811b86683bdbce5e16ce9e blog_source: github:huggingface/toke...
> **Sources:**
>   - gh-huggingfacetokenizers-issue-2197-2026-07-14.md
> **Links:**
- [[Automating Ai Away]]
- [[Automating away]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [[sequoia ascent]]

## Key Findings

---
source_url: https://github.com/huggingface/tokenizers/issues/2197
ingested: 2026-07-14
sha256: eae095de872db771ac4b6f667bc86c2e7a812dcad0811b86683bdbce5e16ce9e
blog_source: github:huggingface/tokenizers
---
# Issue #2197: perf: reduce BPE tokenizer load-time memory
**State:** open | **Author:** xrl1 | **Created:** 2026-07-14T08:21:59Z
# Reduce BPE tokenizer load-time memory
## Motivation
We have a production low-memory environment where we want to move from WordPiece to BPE, but the load-time memory increase is too high for us to adopt as-is. This PR closes most of that gap.
## Context
Loading a large BPE `tokenizer.json` via `Tokenizer::from_file` allocates far more than the resulting model needs — a 128k-vocab BPE (llama-3) peaks at **172 MiB** to produce a model whose live footprint is ~44 MiB. Profiling traced this to two independent sources of transient allocation on the load path, neither of which touches the encode hot path.
## Changes
Three commits:
1. **`bench: add load_mem heap-allocation benchmark`** — a dhat-based bench measuring the *memory* cost of `from_file` (peak live bytes + churn), complementing the existing latency benches. Defaults to `data/llama-3-tokenizer.json` (fetched by `make data`), takes an optional path env.
2. **`perf(models): avoid serde_json::Value round-trip`** — `ModelWrapper::deserialize` used `#[serde(flatten)] rest: serde_json::Value` + `from_value`, parsing the entire model into an owned `Value` then reparsing it (allocating the whole vocab twice). Now captures the model as a borrowed `RawValue`, peeks the `type` tag, and `from_str`s once into the concrete type. Applies to **all** model types (BPE/WordPiece/WordLevel/Unigram). Also preserves on-disk field order (a `Value` map sorts keys), which enables change 3.
3. **`perf(bpe): resolve merges to ids while deserializing`** — instead of collecting every merge into an owned `Vec` and re-walking it in `build()`, `BPEVisitor` resolves each merge to ids as it is parsed (borrowing tokens via `Cow`), dropping strings immediately. Requires `vocab` before `merges` (guaranteed by change 2); falls back to buffer-then-resolve otherwise, so any valid `tokenizer.json` still loads.
### Details
The non-obvious parts of the diff:
- **`MergesResolver` (`serialization.rs`)** — a `DeserializeSeed` holding a reference to the already-parsed vocab, so it resolves merges to ids as the array is read rather than buffering them first.
- **`Cow` for merge tokens** — each merge token deserializes as `Cow`, borrowed from the input on the common path and only allocated when it contains JSON escapes. It's used to look up ids, then dropped.
- **`MergeInput` enum (`model.rs`)** — the builder now holds either `Raw` (strings to resolve later) or `Resolved` (already ids), so the two mutually exclusive states are type-enforced instead of tracked with parallel `Option`s.
- **Field-order fallback** — the fast path needs `vocab` (and `continuing_subword_prefix`) before `merges`. If `merges` com

## Summary

See Key Findings for full content.

## Related Articles

- [[Automating Ai Away]]
- [[Automating away]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [[sequoia ascent]]
