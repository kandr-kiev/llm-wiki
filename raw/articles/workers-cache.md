---
title: "workers cache"
type: comparison
tags: [comparison]
description: Comparison page for workers cache

sources: []
links: []
description: Comparison page for workers cache

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
contested: false

---
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
- - <astro-island uid="1SUbyA" component-url="/_astro/GoogleAnalytics.Buaiy_s2.js" component-export="GoogleAnalytics" renderer-url="/_astro/client.CpQ9otmg.js" props="{"title":[0,"Your Worker can now have its own cache in front of it"],"canonical":[0,"https://blog.cloudflare.com/workers-cache"],"info":[0,{"id":[0,"1WYEYtVwQSo4H3jKHTcKmO"],"title":[0,"Your Worker can now have its own cache in front of it"],"slug":[0,"workers-cache"],"excerpt":[0,"We are launching Workers Cache, a regionally tiered cache that sits directly in front of your Worker entrypoints. Infinitely composable, configured via standard HTTP headers"],"featured":[0,false],"html":[0,"<p>Today we are launching <b>Workers Cache</b>: a <a href=\"https://developers.cloudflare.com/cache/how-to/tiered-cache/\" target=\"_blank\" rel=\"noopener noreferrer\"><u>tiered cache</u></a> that sits in front of your Worker, configured by a single line of Wrangler config and the same <code>Cache-Control</code> headers you already know.</p><p>When Workers Cache is enabled, every <a href=\"https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.3\" target=\"_blank\" rel=\"noopener noreferrer\"><u>cacheable</u></a> request to your Worker hits Cloudflare's cache first. If there's a fresh cached response, Cloudflare returns it directly â your Worker doesn't run, and you don't pay CPU time for it. On a miss, your Worker runs, and if your response is cacheable, Cloudflare stores it for the next request. The next request from anywhere on Earth can be served straight from cache.</p>\n <figure class=\"kg-card kg-image-card\">\n <Image src=\"https://cf-assets.www.cloudflare.com/zkvhlag99gkb/2Xyk1rkPl9p44y48mdoPk/2178d252281c0165e03e7cb9245a4c3a/BLOG-3262_image1.png\" alt=\"BLOG-3262 image1\" class=\"kg-image\" width=\"1999\" height=\"454\" loading=\"lazy\"/>\n </figure><p>The whole thing is one config block:</p>\n <pre class=\"language-Rust\"><code class=\"language-Rust\">{\n "name": "my-worker",\n "main": "src/index.ts",\n "compatibility_date": "2026-05-01",\n "cache": {\n "enabled": true\n }\n}</pre></code>\n <p>After that, you control caching the way HTTP has always wanted you to â by setting headers on your responses:</p>\n <pre class=\"language-TypeScript\"><code class=\"language-TypeScript\">return new Response(body, {\n headers: {\n "Cache-Control": "public, max-age=300, stale-while-revalidate=3600",\n "Cache-Tag": "products,product:123",\n },\n});</pre></code>\n <p>And when content changes, your Worker purges its own cache:</p>\n <pre class=\"language-TypeScript\"><code class=\"language-TypeScript\">await ctx.c

## Summary

ache.purge({ tags: ["product:123"] });</pre></code>\n <p>That's the whole API. There is no zone to configure, no rules engine to set up, no separate cache to provision, and no second product to log into. The Worker's code is the configuration surface, and the cache follows the Worker wherever it runs â on a custom domain, on <code>workers.dev</code>, behind a service binding, in a preview, in a <a href=\"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/\" target=\"_blank\" rel=\"noopener noreferrer\"><u>Workers for Platforms</u></a> tenant. One Worker, one cache, configured once.</p><p>That's the surface area. Thereâs a lot underneath: tiered caching across our entire network, full support for <a href=\"https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/\" target=\"_blank\" rel=\"noopener noreferrer\"><code><u>stale-while-revalidate</u></code></a> so stale responses never block a user, content negotiation via <a href=\"https://developers.cloudflare.com/workers/cache/#content-negotiation-with-vary\" target=\"_blank\" rel=\"noopener noreferrer\"><code><u>Vary</u></code></a>, multi-tenant-safe cache keys via <a href=\"https://developers.cloudflare.com/workers/runtime-apis/context/#props\" target=\"_blank\" rel=\"noopener noreferrer\"><code><u>ctx.props</u></code></a>, programmatic purges by tag or path prefix, and â the part we think is the biggest unlock â a cache that sits in front of every Worker entrypoint, not just the public one, with per-entrypoint control over which ones cache and which don't. That last piece means you can compose caching directly into the structure of your app: a chain of entrypoints with cache stages slotted in wherever you want them, configured by the code on either side. We'll walk through all of it below.</p><p>Workers Cache is available today to every Worker on any plan, enabled in Wrangler.</p><p>This is the caching API we've always wanted Workers to have. Here's why it took us this long, what becomes possible because of it, and what's coming next.</p>\n <div class=\"flex anchor relative\">\n <h2 id=\"why-server-rendered-apps-need-a-cache-in-front\">Why server-rendered apps need a cache in front</h2>\n <a href=\"#why-server-rendered-apps-need-a-cache-in-front\" aria-hidden=\"true\" class=\"relative sm:absolute sm:-start-5\">\n <svg width=\"16\" height=\"16\" viewBox=\"0 0 24 24\"><path fill=\"currentcolor\" d=\"m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z\"></path></svg>\n </a>\n </div>\n <p>When we

## Related Articles

- 
- 
- 
- 
- [[automating-ai-away-2026-07-07]]
