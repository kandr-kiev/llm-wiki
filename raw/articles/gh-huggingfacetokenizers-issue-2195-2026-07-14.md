---
source_url: https://github.com/huggingface/tokenizers/issues/2195
ingested: 2026-07-14
sha256: bf30edbeb0d920cc1685cbe75b61bad1549d80e008f1c5b35a18892ae67f798d
blog_source: github:huggingface/tokenizers
---
# Issue #2195: Clarify byte-level pretokenizer behavior

**State:** open | **Author:** michaelalbada | **Created:** 2026-07-14T00:00:24Z

Clarifies the `ByteLevel` pre-tokenizer docs around raw byte input.

`ByteLevel` operates on Unicode strings and maps their UTF-8 bytes to visible byte-level characters. Passing arbitrary bytes decoded as Latin-1 can therefore re-encode bytes above 127 as UTF-8 and produce unexpected tokens.

  This PR:
  - documents that limitation in the `ByteLevel` docs
  - adds a short raw-byte encoding example using the GPT-2 byte-to-Unicode mapping
  - explains that already-mapped byte-level text should skip normalization and pre-tokenization

Designed to address [[https://github.com/huggingface/tokenizers/issues/1877]]