---
source_url: https://github.com/tensorflow/tensorflow/issues/123250
ingested: 2026-07-14
sha256: ae45fdf3b581bad4d94bed07fc2e4e2d113fc912c6022b8ec9c539d7204d853e
blog_source: github:tensorflow/tensorflow
---
# Issue #123250: Disable GXL for cuda SM versions < 70.  It uses <cuda/barrier> which is not supported on older platforms.

**State:** open | **Author:** copybara-service[bot] | **Created:** 2026-07-14T19:09:47Z

Disable GXL for cuda SM versions < 70.  It uses <cuda/barrier> which is not supported on older platforms.
