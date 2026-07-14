---
source_url: https://github.com/huggingface/tokenizers/issues/2196
ingested: 2026-07-14
sha256: ca2b5d28426fe962be125cf94826954e522b01e6f675657de92fc5b27bbdbc0c
blog_source: github:huggingface/tokenizers
---
# Issue #2196: Upgrade hf-hub to 1.0

**State:** open | **Author:** assafvayner | **Created:** 2026-07-14T01:08:55Z

Upgrades the `hf-hub` dependency from 0.4 to 1.0 and migrates `from_pretrained` to the new API: the `ureq` feature is replaced by `blocking`, and the old `ApiBuilder`/`Repo` flow is replaced with `HFClientSync` + the `download_file` builder. Behavior is unchanged (env token/endpoint fallback, bare identifiers, and revisions all work as before); verified with `cargo test --features http --test from_pretrained` against the live Hub. cc @mcpotato