---
title: "meerkat introduction"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - async
  - data
  - distributed
  - edge
  - image-generation
  - nlp
  - research
  - use-case
  - vector-database
---

# meerkat introduction

> **Source:** introducing-meerkat-an-experiment-in-global-consensus-2026-07-09.md
> **Type:** comparison
> **Created:** 2026-07-09

## Key Findings

---
source_url: https://blog.cloudflare.com/meerkat-introduction/
ingested: 2026-07-09
sha256: PLACEHOLDER
blog_source: Cloudflare Blog
---
Introducing Meerkat: an experiment in global consensus- - - - - - - - - 
- - <astro-island uid="ZKeGDo" component-url="/_astro/GoogleAnalytics.Buaiy_s2.js" component-export="GoogleAnalytics" renderer-url="/_astro/client.CpQ9otmg.js" props="{"title":[0,"Introducing Meerkat: an experiment in global consensus"],"canonical":[0,"https://blog.cloudflare.com/meerkat-introduction"],"info":[0,{"id":[0,"7zbgYCOZDfvIIsVrPpZ8xJ"],"title":[0,"Introducing Meerkat: an experiment in global consensus"],"slug":[0,"meerkat-introduction"],"excerpt":[0,"Cloudflare Research is building a global consensus service called Meerkat that uses a new consensus algorithm called QuePaxa. We plan to use Meerkat to build a strongly consistent, fault-tolerant key-value store, and other applications."],"featured":[0,false],"html":[0,"<p>Many internal services at Cloudflare need to read and modify the same control-plane state from across our 330+ global data centers. They need guarantees that different readers <i>never </i>see inconsistent state, and that the system remains available for writes even when some data centers or links fail. </p><p>But Cloudflareâs network runs across the entire Internet, and the Internet is an unpredictable place. Servers and data centers go down. Queues fill up. Links and cables get cut. These conditions make it difficult to run a globally available data system that guarantees strong consistency (e.g., that all readers are guaranteed to read all prior writes) because hostile conditions hinder distributed system replicasâ ability to reliably synchronize data with one another.</p><p>One way to synchronize data safely despite adverse network conditions is via a <i>consensus algorithm, </i>which<i> </i>allows a set of machines to agree on the same sequence of values, such as key-value store put and <code>get</code> operations, as long as a majority remains alive and able to communicate.Â </p><p>Unfortunately, commonly deployed consensus algorithms like <a href=\"https://raft.github.io/\" target=\"_blank\" rel=\"noopener noreferrer\"><u>Raft</u></a> suffer in wide-area networks like Cloudflareâs because they rely on <i>leaders </i>and<i> timeouts</i>. The <i>leader</i> is the only replica allowed to make writes, and if it fails due to a crash or network degradation, the system becomes unavailable until some other replica <i>times out</i> and a new leader is elected. And these timeout values are hard to configure in networks with unpredictable latencies.</p><p>We have experienced multiple incidents caused by unavailable leaders in consensus-driven systems.</p><p>And so, for the past year, Cloudflareâs Research <a href=\"https://research.cloudflare.com/\" target=\"_blank\" rel=\"noopener noreferrer\"><u>team</u></a> has been building a new distributed consensus service called <b>Meerkat</b> powered by a consensus 

## Summary

algorithm called <a href=\"https://bford.info/pub/os/quepaxa/quepaxa.pdf\" target=\"_blank\" rel=\"noopener noreferrer\"><u>QuePaxa</u></a>, published in 2023 by Tennage & BÄsescu et al. QuePaxa differs from Raft in that all replicas can perform writes at all times, and progress is never halted due to a timeout, which makes it well suited for Cloudflareâs network. We layer <i>applications</i>, like a transactional key-value store and leasing system, atop Meerkatâs consensus log. To our knowledge, this will be the first industrial deployment of QuePaxa at global scale.</p><p>Meerkat is an experimental consensus service that is still in development. Itâs being designed initially to manage small pieces of control plane state (e.g., leadership for replicated databases) and so it will be kept internal-only for the immediate future. This post introduces Meerkat and lays the groundwork for the Meerkat-related blog posts to come.Â </p>\n <div class=\"flex anchor relative\">\n <h2 id=\"what-we-need-from-a-global-control-plane-data-system\">What we need from a global control-plane data system</h2>\n <a href=\"#what-we-need-from-a-global-control-plane-data-system\" aria-hidden=\"true\" class=\"relative sm:absolute sm:-start-5\">\n <svg width=\"16\" height=\"16\" viewBox=\"0 0 24 24\"><path fill=\"currentcolor\" d=\"m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z\"></path></svg>\n </a>\n </div>\n <p>Many Cloudflare services read and write <i>control-plane data</i>, data that helps those services operate correctly, from multiple machines distributed all over the world. One example of control-plane data is <i>placement information</i>: where certain resources (like an AI model instance) are stored. Another example is <i>leadership information</i>: which machine is currently allowed to perform writes to a database.Â </p><p>Control-plane data must be both <i>strongly</i> <i>consistent</i> and<i> accessible despite particular kinds of faults.</i></p><p>In this section we precisely describe our consistency and fault tolerance requirements for a Cloudflare consensus service. We use a key-value store for a running example of an application running atop our consensus service, though other applications (e.g., distributed leases/locks) are possible.</p>\n <div class=\"flex anchor relative\">\n <h3 id=\"strong-consistency\">Strong consistency</h3>\n <a href=\"#strong-consistency\" aria-hidden=\"true\" class=\"relative sm:absolute sm:-start-5\">\n <svg width=\"16\" height=\"16\" viewBox=\"0 0 24 24\"><path fill=\"currentcolor\" d=\"m12.11 15.39-3.88 3.88a2.52 2.

## Related Articles

- [[workers cache]]
- [[rollbacks for workflows]]
- [[oauth for all]]
- [[robots txt 2023 war memorial]]
- [[applying large language models cohere]]
