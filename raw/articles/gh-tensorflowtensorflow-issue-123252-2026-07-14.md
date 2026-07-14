---
source_url: https://github.com/tensorflow/tensorflow/issues/123252
ingested: 2026-07-14
sha256: 2482efe9887cdf3d028d9b5bccf01887e6e6ecc8cd7c92f5740c247924afe97c
blog_source: github:tensorflow/tensorflow
---
# Issue #123252: [PjRt-IFRT] Use HighwayHash for array hashing

**State:** open | **Author:** copybara-service[bot] | **Created:** 2026-07-14T20:24:41Z

[PjRt-IFRT] Use HighwayHash for array hashing

This change replaces `tsl::Fingerprint64` with `HighwayHash` for IFRT array hashing.

`HighwayHash` is roughly 25.2% faster in a simple microbenchmark.
