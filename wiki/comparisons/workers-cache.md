---
title: "workers cache"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - api
  - async
  - comparison
  - image-generation
  - multi-agent
  - nlp
  - open-source
  - real-time
  - standards
---
# workers cache

> **Source:** workers-cache.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- title: "workers cache" type: comparison tags: [comparison] description: Comparison page for workers cache sources: [] links: [] description: Comparison page for workers cache links: [] confidence:...
> **Sources:**
>   - workers-cache.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[oauth-for-all]]
- [[chemical-hygiene]]
- [[sequoia-ascent]]

## Key Findings


# workers cache
> **Source:** your-worker-can-now-have-its-own-cache-in-front-of-it-2026-07-07.md
> **Type:** comparison
> **Created:** 2026-07-08
## Key Findings
---
source_url: https://blog.cloudflare.com/workers-cache/
ingested: 2026-07-07
sha256: 0e1a4ca5496719936540a527b170b95df7d5d91d90eaa713ba05ab52d008e3fd
blog_source: Cloudflare Blog
---
Your Worker can now have its own cache in front of it- - - - - - - - - 
- - tiered cache that sits in front of your Worker, configured by a single line of Wrangler config and the same `Cache-Control` headers you already know.
When Workers Cache is enabled, every cacheable request to your Worker hits Cloudflare's cache first. If there's a fresh cached response, Cloudflare returns it directly â your Worker doesn't run, and you don't pay CPU time for it. On a miss, your Worker runs, and if your response is cacheable, Cloudflare stores it for the next request. The next request from anywhere on Earth can be served straight from cache.
\n \n \n The whole thing is one config block:
\n {\n "name": "my-worker",\n "main": "src/index.ts",\n "compatibility_date": "2026-05-01",\n "cache": {\n "enabled": true\n }\n}\n After that, you control caching the way HTTP has always wanted you to â by setting headers on your responses:
\n return new Response(body, {\n headers: {\n "Cache-Control": "public, max-age=300, stale-while-revalidate=3600",\n "Cache-Tag": "products,product:123",\n },\n});\n And when content changes, your Worker purges its own cache:
\n await ctx.c
## Summary
ache.purge({ tags: ["product:123"] });\n That's the whole API. There is no zone to configure, no rules engine to set up, no separate cache to provision, and no second product to log into. The Worker's code is the configuration surface, and the cache follows the Worker wherever it runs â on a custom domain, on `workers.dev`, behind a service binding, in a preview, in a Workers for Platforms tenant. One Worker, one cache, configured once.
That's the surface area. Thereâs a lot underneath: tiered caching across our entire network, full support for `stale-while-revalidate` so stale responses never block a user, content negotiation via `Vary`, multi-tenant-safe cache keys via `ctx.props`, programmatic purges by tag or path prefix, and â the part we think is the biggest unlock â a cache that sits in front of every Worker entrypoint, not just the public one, with per-entrypoint control over which ones cache and which don't. That last piece means you can compose caching directly into the structure of your app: a chain of entrypoints with cache stages slotted in wherever you want them, configured by the code on either side. We'll walk through all of it below.
Workers Cache is availa

## Summary

See Key Findings for full content.

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[oauth-for-all]]
- [[chemical-hygiene]]
- [[sequoia-ascent]]
