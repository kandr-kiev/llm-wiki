---
source_url: https://github.com/huggingface/optimum/issues/2450
ingested: 2026-07-14
sha256: 626a53850e7c8be2069cf889ba3ffe29119f9f7021a823f81c18dc114524c875
blog_source: github:huggingface/optimum
---
# Issue #2450: Fix #2407: Fix get_wikitext2 tokenization bug causing sequence length warning

**State:** open | **Author:** nandanadileep | **Created:** 2026-06-12T09:08:12Z

Fixes #2407

Changed `get_wikitext2` from concatenating 1000 entries into a single string and tokenizing all at once (producing 73K+ token sequences that exceed the model's max length), to per-sample tokenization with a retry loop matching `get_c4`/`get_c4_new`.

Local test infra unavailable in CI sandbox.

---
This change was prepared with AI assistance under human direction and review.