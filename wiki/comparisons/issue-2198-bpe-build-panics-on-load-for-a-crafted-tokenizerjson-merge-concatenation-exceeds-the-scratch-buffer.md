---
title: "Issue #2198: BPE `build()` panics on load for a crafted `tokenizer.json` (merge concatenation exceeds the scratch buffer)"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - foundation-model
  - open-source
---

# Issue #2198: BPE `build()` panics on load for a crafted `tokenizer.json` (merge concatenation exceeds the scratch buffer)

> **Source:** gh-huggingfacetokenizers-issue-2198-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/tokenizers/issues/2198 ingested: 2026-07-14 sha256: d127d4faf2df7277c93fd74ebcb8bef9466c246a0a2b6d3f6a834a95a1277974 blog_source: github:huggingface/toke...
> **Sources:**
>   - gh-huggingfacetokenizers-issue-2198-2026-07-14.md
> **Links:**
- [Issue #2197: perf: reduce BPE tokenizer load-time memory]
- [Issue #2450: Fix #2407: Fix get_wikitext2 tokenization bug causing sequence length warning]
- [Issue #8331: datasets-server.huggingface.co returning 503 on every endpoint (whole host down, not one route)]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]

## Key Findings

---
source_url: https://github.com/huggingface/tokenizers/issues/2198
ingested: 2026-07-14
sha256: d127d4faf2df7277c93fd74ebcb8bef9466c246a0a2b6d3f6a834a95a1277974
blog_source: github:huggingface/tokenizers
---
# Issue #2198: BPE `build()` panics on load for a crafted `tokenizer.json` (merge concatenation exceeds the scratch buffer)
**State:** open | **Author:** professor-moody | **Created:** 2026-07-14T18:59:36Z
**Summary.** A crafted `tokenizer.json` with a BPE model causes a panic during `Tokenizer::from_file` /
`from_str`, before any tokenization runs. The BPE builder writes a merge concatenation into a scratch buffer sized
for the longest *single* vocab token; a merge whose two tokens concatenate to something longer than any single vocab
entry overflows the slice and panics.
**Details.** In `tokenizers/src/models/bpe/model.rs`, `BpeBuilder::build`:
```rust
let mut buffer: Vec = vec![0; max_len]; // max_len = longest single vocab key (bytes)
...
buffer[0..a.len()].copy_from_slice(a.as_bytes());
let b_len = b.len() - prefix_len; // usize subtraction
let merge_len = a.len() + b_len;
buffer[a.len()..merge_len].copy_from_slice(&b.as_bytes()[prefix_len..]); // panics: merge_len can exceed max_len
```
Both `a` and `b` are individually in the vocab, so each is ` PanicException: range end index 4 out of range for slice of length 2 (at models/bpe/model.rs:267)
```
(A well-formed tokenizer never trips this because the merged token `"aabb"` is itself a vocab entry, so `max_len`
covers it; the crash requires a merge whose result is absent from / larger than the vocab.)
**Impact.** Loading an untrusted `tokenizer.json` (e.g. from a model repository) crashes the tokenizer load before
inference — a denial of service. Native (Rust) consumers abort the process; the Python binding raises a catchable
`PanicException`.
**Suggested fix.** Validate the pair length before the write (size the buffer to `2*max_len`, or check `merge_len b.len()`; ideally
move the write after the vocab-membership check so a malformed merge returns a `TokenizerBuilderError` instead of
panicking.
---
Reported by Halo Forge Labs.

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #2197: perf: reduce BPE tokenizer load-time memory]
- [Issue #2450: Fix #2407: Fix get_wikitext2 tokenization bug causing sequence length warning]
- [Issue #8331: datasets-server.huggingface.co returning 503 on every endpoint (whole host down, not one route)]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]
