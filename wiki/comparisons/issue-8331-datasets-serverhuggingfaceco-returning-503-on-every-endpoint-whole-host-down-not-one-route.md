---
title: "Issue #8331: datasets-server.huggingface.co returning 503 on every endpoint (whole host down, not one route)"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - backend
  - dataset
  - library
  - open-source
---

# Issue #8331: datasets-server.huggingface.co returning 503 on every endpoint (whole host down, not one route)

> **Source:** gh-huggingfacedatasets-issue-8331-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/datasets/issues/8331 ingested: 2026-07-14 sha256: 05d62ec27a31f2ba7d176864c14c1be67f361fac8a8bcc6fda153e690abe7cae blog_source: github:huggingface/datase...
> **Sources:**
>   - gh-huggingfacedatasets-issue-8331-2026-07-14.md
> **Links:**
- [[Issue #8330: Dataset Studio and Viewer down]]
- [[Release 5.0.0]]
- [[Issue #2848: Implement multi-domain intake architecture and related specs]]
- [[workers cache]]
- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]

## Key Findings

---
source_url: https://github.com/huggingface/datasets/issues/8331
ingested: 2026-07-14
sha256: 05d62ec27a31f2ba7d176864c14c1be67f361fac8a8bcc6fda153e690abe7cae
blog_source: github:huggingface/datasets
---
# Issue #8331: datasets-server.huggingface.co returning 503 on every endpoint (whole host down, not one route)
**State:** open | **Author:** ChristianDenniss | **Created:** 2026-07-14T13:59:29Z
### Describe the bug
The entire datasets-server.huggingface.co backend (the dataset-viewer API) is
returning 503 Service Temporarily Unavailable on every route I've tried, not
just one endpoint. It reproduces on public datasets with no auth token, so it
doesn't appear to be account- or dataset-specific. huggingface.co itself and
huggingface.co/api are unaffected, so this looks isolated to the dataset-viewer
service's backend/load balancer.
### Steps to reproduce the bug
Run any of the following (curl, no auth needed):
```bash
curl -i "https://datasets-server.huggingface.co/"
curl -i "https://datasets-server.huggingface.co/info?dataset=squad&config=plain_text"
curl -i "https://datasets-server.huggingface.co/splits?dataset=squad"
curl -i "https://datasets-server.huggingface.co/rows?dataset=squad&config=plain_text&split=validation&offset=0&length=1"
curl -i "https://datasets-server.huggingface.co/parquet?dataset=squad"
curl -i "https://datasets-server.huggingface.co/valid"
curl -i "https://datasets-server.huggingface.co/is-valid?dataset=squad"
curl -i "https://datasets-server.huggingface.co/size?dataset=squad"
curl -i "https://datasets-server.huggingface.co/statistics?dataset=squad&config=plain_text&split=validation"
```
All of the above return an identical response:
```
HTTP/1.1 503 Service Temporarily Unavailable
Content-Type: text/html
Content-Length: 162
Connection: keep-alive
Server: awselb/2.0
X-Cache: Error from cloudfront
Via: 1.1 d9d0b19761149aebd7234df3fac341aa.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: YUL62-P1
Run any of the following (curl, no auth needed):
```bash
curl -i "https://datasets-server.huggingface.co/"
curl -i "https://datasets-server.huggingface.co/info?dataset=squad&config=plain_text"
curl -i "https://datasets-server.huggingface.co/splits?dataset=squad"
curl -i "https://datasets-server.huggingface.co/rows?dataset=squad&config=plain_text&split=validation&offset=0&length=1"
curl -i "https://datasets-server.huggingface.co/parquet?dataset=squad"
curl -i "https://datasets-server.huggingface.co/valid"
curl -i "https://datasets-server.huggingface.co/is-valid?dataset=squad"
curl -i "https://datasets-server.huggingface.co/size?dataset=squad"
curl -i "https://datasets-server.huggingface.co/statistics?dataset=squad&config=plain_text&split=validation"
```
All of the above return an identical response
### Expected behavior
datasets-server.huggingface.co should respond normally (200, or an appropriate
4xx for a bad dataset/config/split) rather than a blanket 503 with an
awselb/cloudfront error page across every route.
### Environment info
N/A -

## Summary

See Key Findings for full content.

## Related Articles

- [[Issue #8330: Dataset Studio and Viewer down]]
- [[Release 5.0.0]]
- [[Issue #2848: Implement multi-domain intake architecture and related specs]]
- [[workers cache]]
- [[Issue #14166: Fix Hub download filtering for FlashPack pipelines]]
