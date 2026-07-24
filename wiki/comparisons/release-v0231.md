---
title: "Release v0.23.1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - analysis
  - api
  - batch
  - benchmark
  - ci-cd
  - comparison
  - data
  - foundation-model
  - hardware
  - llama
  - machine-learning
  - multi-agent
  - parallel
  - performance
  - pipeline
  - real-time
  - security
  - workflow
---

# Release v0.23.1

> **Source:** gh-v0231-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/tokenizers/releases/tag/v0.23.1 ingested: 2026-07-14 sha256: 1c75c5f92c85e9f8bcdbb6b255db4942f80e480b82793130c8ddebefad59d48d blog_source: github:hugging...
> **Sources:**
>   - gh-v0231-2026-07-14.md
> **Links:**
- [Issue #2197: perf: reduce BPE tokenizer load-time memory](https://github.com/pytorch/pytorch/issues/2197)
- [[Release 5.0.0]]
- [[v0.22.1]]
- [[Sites That Block Ai Training Cr[Issue #6385: AsyncGRPO fork-independent epoch counting](https://github.com/pytorch/pytorch/issues/6385)5: AsyncGRPO fork-independent epoch counting]]

## Key Findings

---
source_url: https://github.com/huggingface/tokenizers/releases/tag/v0.23.1
ingested: 2026-07-14
sha256: 1c75c5f92c85e9f8bcdbb6b255db4942f80e480b82793130c8ddebefad59d48d
blog_source: github:huggingface/tokenizers
---
# Release v0.23.1
## TL;DR
`tokenizers 0.23.1` is the first proper stable release in the `0.23` line — `0.23.0` only ever shipped as `rc0` because the release pipeline itself was broken (Node side hadn't shipped multi-platform binaries since 2023, Python side was on `pyo3 0.27` without free-threaded support). `0.23.1` is the version where everything actually goes out the door together: full Node multi-platform wheels for the first time in years, Python 3.14 (regular **and** free-threaded `3.14t`), full type hints for every Python class, and a stack of measurable perf wins on the BPE / added-vocab hot paths.
There is no functional `0.23.0` published — we tag `0.23.1` directly so users don't accidentally pull a never-shipped version.
---
## 🚨 Breaking changes
- **Drop Python 3.9** (#1952) — `requires-python = ">=3.10"`; 3.9 users stay on `0.22.x`.
- **`add_tokens` normalizes `content` at insertion** (#1995) — re-saved `tokenizer.json` may differ in the `added_tokens` block. Existing files load unchanged.
- **Type stubs are precise** (#1928, #1997) — methods that returned `Any` now return real types; `mypy --strict` may surface previously-hidden errors. Stub layout also moved from `tokenizers//__init__.pyi` to `tokenizers/.pyi`. This breaks the surface of some of the processors like `RobertaProcessign`'s `__init__` . 
- **3.14t-only**: setters/getters return `PyResult` because of `Arc>`; a poisoned lock surfaces as `PyException` instead of a panic.
---
## ⚡ Performance — measured locally on this Mac, not lifted from PRs
Run with `cargo bench --bench -- --save-baseline v0_22_2` on `v0.22.2`, then `--baseline v0_22_2` on `v0.23.1`. Numbers are point-in-time wall clock on a single laptop; relative deltas are what matters, absolute numbers will differ on CI hardware.
### Added-vocabulary deserialize — the headline win (#1995, #1999)
`bench: improve added_vocab_deserialize to reflect real-world workloads` (#2000) is now representative of how transformers actually loads tokenizer.json files. The combined effect of `daachorse` for the matching automaton plus the normalize-on-insert refactor is enormous on this workload:
| benchmark | v0.22.2 | v0.23.1 | change |
|---|---:|---:|---:|
| 100k tokens, special, no norm | ~410 ms | 248 ms | **−40%** |
| 100k tokens, non-special, no norm| ~7.1 s | 273 ms | **−96%** |
| 100k tokens, special, NFKC | ~395 ms | 235 ms | **−40%** |
| 100k tokens, non-special, NFKC | ~7.4 s | 290 ms | **−96%** |
| 400k tokens, special, no norm | ~15 s | 980 ms | **−94%** |
Real-world impact: loading a Llama-3-style tokenizer with a large set of added tokens dropped from "noticeable pause" to "instant".
### BPE encode
| benchmark | v0.22.2 | v0.23.1 | change |
|---|---:|---:|---:|
| `BPE GPT2 encode batch, no cache` | 53

## Summary

0 ms | 446 ms | **−16%** |
| `BPE GPT2 encode batch` (cached) | 690 ms | 685 ms | noise |
| `BPE GPT2 encode` (single) | 1.95 s | 1.94 s | noise |
| `BPE Train (small)` | 32.6 ms| 31.5 ms| −3% |
| `BPE Train (big)` | 1.01 s | 988 ms | −2% |
The BPE per-thread cache PR (#2028) shows much larger wins on highly-parallel workloads (+47–62% at 88+ threads on a server box, per the PR's own measurements on Vera). Single-thread batch numbers above are flat or slightly improved because cache-hit overhead was already low without contention.
### Llama-3 encode
| benchmark | v0.22.2 | v0.23.1 | change |
|---|---:|---:|---:|
| `llama3-encode` (single) | 2.10 s | 2.02 s | −4% |
| `llama3-batch` | 438 ms | 408 ms | **−7%** |
| `llama3-offsets` | 410 ms | 395 ms | **−4%** |
### Truncation early exit (#1990)
Right-direction truncation no longer pre-tokenizes past `max_length`. The new `truncation_benchmark` doesn't exist on v0.22.2 so there's no apples-to-apples here, but the PR's own measurements on the same machine showed −20–28% across a range of `max_length` values for right-truncation; left-truncation unchanged.
### Other perf improvements (no direct comparable bench)
- `BPE::Builder::build` no longer formats strings in a hot loop (#2010) — ~45% faster `Tokenizer::from_file` on Llama-3 in the PR's profile.
- BPE per-thread cache (#2028) — see Vera numbers in PR description for parallel scale-out.
---
## 🔄 Serialization / deserialization
The `tokenizer.json` format is **forward-compatible**: existing files load on 0.23 unchanged. Two things to know if you re-save:
- `added_tokens` entries created via `add_tokens(..., normalized=True)` will have their `content` normalized at save time — see breaking-change note above.
- `tokenizer.train(...)` no longer keeps a redundant `added_tokens`/`special_tokens` `Vec` separate from the `added_tokens_map_r`. Public API surface unchanged; only the internal struct shape moved.
`bench: improve added_vocab_deserialize to reflect real-world workloads` (#2000) lands a more realistic micro-benchmark for this surface; if you're tracking deserialize perf in your own CI, the new bench is the one to compare against.
---
## 🐍 Python: free-threaded 3.14t support
Dedicated wheels for `python3.14t` (the free-threaded build introduced in PEP 703). The wheel:
- Declares `Py_MOD_GIL_NOT_USED`, so importing `tokenizers` does **not** force the GIL back on.
- Builds without the `abi3` cargo feature (free-threaded Python doesn't expose the limited API).
- Goes through `Arc>` for the inner state so concurrent setters and encoders don't race PyO3's per-pyclass borrow check.
A new stress-test module `tests/test_freethreaded.py` exercises N-encoder × M-setter races on a single `Tokenizer` and asserts no `RuntimeError: Already borrowed`, no `RwLock` poisoning, and that `sys._is_gil_enabled() is False` post-import.
For the regular CPython wheel everything is unchanged.
---
## 📦 Node.[Issue #2197: perf: reduce BPE tokenizer load-time memory](https://github.com/pytorch/pytorch/issues/2197)The npm

## Related Articles

- [[Issue #2197: perf: reduce BPE tokeni[Issue #6385: AsyncGRPO fork-independent epoch counting](https://github.com/pytorch/pytorch/issues/6385) [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [Issue #6385: AsyncGRPO fork-independent epoch counting](https://github.com/pytorch/pytorch/issues/6385)
