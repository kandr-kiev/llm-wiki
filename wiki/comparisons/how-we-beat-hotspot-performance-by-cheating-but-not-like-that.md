---
title: "how we beat hotspot performance by cheating but not like that"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - architecture
  - image-generation
  - mobile
  - open-source
  - performance
  - prompt-engineering
  - search
  - software
  - video-generation
  - web
---

# how we beat hotspot performance by cheating but not like that

> **Source:** how-we-beat-hotspot-performance-by-cheating-but-not-like-that-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/codenameone/how-we-beat-hotspot-performance-by-cheating-but-not-like-that-2187 ingested: 2026-07-18 sha256: 0d4c0b2bf9aba75be55e818f8e9efac3cea51254cebe2299b988e5d2fe4a0...
> **Sources:**
>   - how-we-beat-hotspot-performance-by-cheating-but-not-like-that-2026-07-18.md
> **Links:**
- [[the-gitbook-migration-trap-4gp2]]
- [[5-things-i-learned-doing-ai-evaluation-for-2-years-3kgh]]
- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[17-none-of-it-was-for-me-a-year-of-building-with-ai-32kf]]
- [[its-a-post-4hi8]]

## Key Findings

---
source_url: https://dev.to/codenameone/how-we-beat-hotspot-performance-by-cheating-but-not-like-that-2187
ingested: 2026-07-18
sha256: 0d4c0b2bf9aba75be55e818f8e9efac3cea51254cebe2299b988e5d2fe4a0251
blog_source: Dev Community
---
How We Beat HotSpot Performance (By Cheating, But Not Like That) - DEV Community
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
[Skip to content](#main-content)
Navigation menu
[
![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)
](/)
Search
[
Powered by Algolia
Search
](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)
[
Log in
](https://dev.to/enter?signup_subforem=1)
[
Create account
](https://dev.to/enter?signup_subforem=1&state=new-user)
## DEV Community
Close
![](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)
Add reaction
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
Like
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
Unicorn
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
Exploding Head
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
Raised Hands
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
Fire
Jump to Comments
Save
Boost
More...
Copy link
Copy link
Copied to Clipboard
Share to X
Share to LinkedIn
Share to Facebook
Share to Mastodon
[Share Post via...](#)
[Report Abuse](/report-abuse)
[
![Cover image for How We Beat HotSpot Performance (By Cheating, But Not Like That)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fwww.codenameone.com%2Fblog%2Fbeating-hotspot-performance.jpg)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fwww.codenameone.com%2Fblog%2Fbeating-hotspot-performance.jpg)
[![Shai Almog](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F417973%2Fa7b22dd9-5565-48f5-bfab-7e5035b3888f.png)](/codenameone)
[Shai Almog](/codenameone)
Posted on Jul 18
• Originally published at [codenameone.com](https://www.codenameone.com/blog/beating-hotspot-performance/) 
# 
How We Beat HotSpot Performance (By Cheating, But Not Like That)
[#java](/t/java)
[#mobile](/t/mobile)
[#android](/t/android)
[#ios](/t/ios)
[![How We Beat HotSpot Performance (By Cheating, But Not Like That)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2F

## Summary

uploads%2Farticles%2F7gd8xmtdwmpvcmjf6jzc.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F7gd8xmtdwmpvcmjf6jzc.jpg)
No, we didn't cheat in the benchmark. At least I hope we didn't. Every optimization in this story was gated on bit identical output checksums against HotSpot, and the harness refuses to print a ratio when a checksum differs. If anything, this post is about how good HotSpot actually is. We tilted the table in our favor in every way we could, we hand tuned C code, and we still only beat it on some benchmarks. Getting there was a genuine struggle. If you want to understand the nuts and bolts of what your Java code costs, and the tradeoffs each runtime picks, I hope this is a good read.
**What is Codename One?** Codename One is an open-source framework for building native iOS, Android, desktop, and web apps from a single Java or Kotlin codebase. Learn more at [codenameone.com](https://www.codenameone.com/).
The short version: [PR #5327](https://github.com/codenameone/CodenameOne/pull/5327) takes ParparVM, the AOT VM that compiles your Java bytecode to C for iOS and other targets, from 4.21x slower than warmed Java 25 to geomean 1.00x parity across a ten benchmark suite, with six of the ten at or below HotSpot. Along the way you'll meet a new page based heap, a poor man's Project Valhalla, code generation that finally lets clang do its job, and two places where HotSpot beat our hand written C anyway. The memory story ends even better than the speed story.
But before we get to that, a few announcements.
## 
Before You Update
The optimizations below landed this week. Performance was gated on bit identical output vs HotSpot on every commit. Correctness went further: 63 test pipelines ran across the ports, with torture suites for maps, string builders, threads, and GC stress, in both cooperative and forced signal stop modes, and we squashed every bug we found along the way, several of them in ports far from the VM. But this is a deep change to code generation, allocation, and collection. Like any change of this scale, there's risk.
If a build misbehaves, pin to the previous release with [versioned builds](https://www.codenameone.com/blog/versioned-builds-master/) and let us know through the usual channels. That's exactly the case versioned builds exist for.
There's a lot more shipping this week beyond the VM work; the bottom of this post links to the daily posts covering it.
## 
The Starting Point
Client VMs are a different beast. The joke around here is that I built ParparVM in two weeks and Steve spent the next three years fixing bugs. When I built it, throughput wasn't a priority at all. I was aiming for simplicity, reliability, and consistency. What actually matters for client performance is startup time, memory footprint, low latency, and fast native access. 90% of client code time should be spent in

## Related Articles

- [[the-gitbook-migration-trap-4gp2]]
- [[5-things-i-learned-doing-ai-evaluation-for-2-years-3kgh]]
- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[17-none-of-it-was-for-me-a-year-of-building-with-ai-32kf]]
- [[its-a-post-4hi8]]
