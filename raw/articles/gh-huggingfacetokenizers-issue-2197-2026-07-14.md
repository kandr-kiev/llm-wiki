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

3. **`perf(bpe): resolve merges to ids while deserializing`** — instead of collecting every merge into an owned `Vec<(String,String)>` and re-walking it in `build()`, `BPEVisitor` resolves each merge to ids as it is parsed (borrowing tokens via `Cow`), dropping strings immediately. Requires `vocab` before `merges` (guaranteed by change 2); falls back to buffer-then-resolve otherwise, so any valid `tokenizer.json` still loads.

### Details

The non-obvious parts of the diff:

- **`MergesResolver` (`serialization.rs`)** — a `DeserializeSeed` holding a reference to the already-parsed vocab, so it resolves merges to ids as the array is read rather than buffering them first.

- **`Cow<str>` for merge tokens** — each merge token deserializes as `Cow`, borrowed from the input on the common path and only allocated when it contains JSON escapes. It's used to look up ids, then dropped.

- **`MergeInput` enum (`model.rs`)** — the builder now holds either `Raw` (strings to resolve later) or `Resolved` (already ids), so the two mutually exclusive states are type-enforced instead of tracked with parallel `Option`s.

- **Field-order fallback** — the fast path needs `vocab` (and `continuing_subword_prefix`) before `merges`. If `merges` comes first, it's buffered and resolved in `build()` as before. This crate always serializes vocab-first, so the fast path is what runs; the fallback just keeps arbitrary field order correct.

- **Shared helpers (`model.rs`)** — `resolve_merge` (one pair → ids) and `parse_legacy_merge` (one legacy `"a b"` line → pair) are reused by both the fast and fallback paths, keeping them behaviorally identical.

- **Reworded `Error::BadMerges`** — message changed from `"Merges text file invalid at line {N}"` to `"Invalid merge rule #{N}"` (variant name kept). For a `tokenizer.json` there is no merges file and `{N}` is an array index, not a line — so "line" was already wrong there, and it also collided with the position `serde_json` appends.

## Results

`cargo bench --bench load_mem` on `data/llama-3-tokenizer.json` (128k-vocab BPE):

| Stage | peak | churn |
|---|---|---|
| baseline | 172.4 MiB | 335.3 MiB |
| + RawValue (commit 2) | 94.5 MiB (−45%) | 160.6 MiB (−52%) |
| + streaming merges (commit 3) | **43.7 MiB (−75%)** | **97.6 MiB (−71%)** |

### Load time

Less allocation and no double-parse also make loading faster. `cargo bench --bench ci_benchmark -- serialization` (Criterion, sample-size 100), base vs this branch:

| Benchmark | before | after | change |
|---|---|---|---|
| `deserialize-llama3` (parse+build, no I/O) | 145.1 ms | 81.3 ms | **−44.0%** |
| `from-file-llama3` (full load) | 142.1 ms | 100.8 ms | **−29.0%** |
| `from-file-albert` | 16.7 ms | 13.6 ms | −18.4% |
| `deserialize-roberta` | 27.4 ms | 23.8 ms | −13.2% |
| `save-llama3` (control) | 38.4 ms | 39.0 ms | no change |

## Correctness

- Model unit tests pass (incl. serialization round-trip, model-type dispatch, OOV / bad-merges errors).
- Round-trip serialization + encode parity (ids **and** token strings) verified on real llama-3 over mixed ASCII/accented/CJK text.
- Field-order-independence test: deserialization yields the same model for every rotation of the JSON field order.

## Error messages

Model parsing now goes through `serde_json::from_str` over the extracted model slice, which changes deserialize-error text:

- **Improved:** an unknown model type now reports `Unknown model type \`X\`` instead of serde's `data did not match any variant of untagged enum ModelUntagged`.
- **Positions:** syntax errors keep correct file positions. Errors raised by our own visitors (OOV token, wrong field type, bad merge) now carry a *slice-relative* `at line L column C` — correct within the model object but offset by the lines preceding `"model"`. Previously these pointed at EOF, so this is no worse.


## Note on #2151

After preparing this PR I noticed that #2151 fixes an issue in the same code this PR touches (`resolve_merge` / `build`'s fixed merge scratch buffer, which can panic on a crafted oversized merge). This PR keeps that pre-existing behavior unchanged. Let me know if you'd like me to fold #2151's fix in here, or how you'd prefer to handle the potential conflict.
