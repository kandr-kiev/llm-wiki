---
title: "ml dsa will have to do"
type: comparison
tags: [comparison]
sources: []
description: Comparison analysis
created: 2026-07-09
updated: 2026-07-09
confidence: medium
contested: false
links:
  - https://blog.cloudflare.com/ml-dsa-will-have-to-do/

---
# ml dsa will have to do

> **Source:** why-we-cannot-wait-for-better-post-quantum-signature-algorithms-2026-07-09.md
> **Type:** comparison
> **Created:** 2026-07-09

## Key Findings

---
source_url: https://blog.cloudflare.com/ml-dsa-will-have-to-do/
ingested: 2026-07-09
sha256: PLACEHOLDER
blog_source: Cloudflare Blog
---
Why we cannot wait for better post-quantum signature algorithms- - - - - - - - - 
- - <astro-island uid="Z1nLOAG" component-url="/_astro/GoogleAnalytics.Buaiy_s2.js" component-export="GoogleAnalytics" renderer-url="/_astro/client.CpQ9otmg.js" props="{"title":[0,"Why we cannot wait for better post-quantum signature algorithms"],"canonical":[0,"https://blog.cloudflare.com/ml-dsa-will-have-to-do"],"info":[0,{"id":[0,"5wMIF1Oa7DES2YNRpqiVB0"],"title":[0,"Why we cannot wait for better post-quantum signature algorithms"],"slug":[0,"ml-dsa-will-have-to-do"],"excerpt":[0,"NIST is advancing nine new post-quantum signature algorithms as potential candidates for future standardization. We take a closer look at all of them, and argue that while they are in the works and show great potential, we should use ML-DSA for now â the best one currently available. "],"featured":[0,false],"html":[0,"<p>RSA and ECC, cryptographic algorithms that weâve all relied on for decades, are <a href=\"https://blog.cloudflare.com/the-quantum-menace/\"><u>vulnerable</u></a> to the attack of sufficiently advanced quantum computers. Such quantum computers do not exist yet, but they seem to be coming <a href=\"https://scottaaronson.blog/?p=9718\" target=\"_blank\" rel=\"noopener noreferrer\"><u>sooner</u></a> than expected. Luckily, the solution is already available: migrate to ML-KEM encryption and ML-DSA signatures, which are designed to be resistant to quantum attack. They were standardized <a href=\"https://blog.cloudflare.com/nists-first-post-quantum-standards/\"><u>in 2024</u></a> by the U.S. National Institute of Standards and Technology (NIST) after an eight-year open international competition.</p><p>The migration to post-quantum cryptography is in full swing now. At the time of writing, the majority of traffic handled by Cloudflare is already using ML-KEM encryption, and is thus secured against the threat to data posed by <a href=\"https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later\" target=\"_blank\" rel=\"noopener noreferrer\"><u>harvest-now-decrypt-later</u></a> attacks. But encryption is only one part of the equation: to be fully secure against quantum computers capable of breaking classical cryptography, we aim to deploy post-quantum signatures to protect authentication systems from unauthorized access. We are <a href=\"https://blog.cloudflare.com/post-quantum-roadmap\"><u>targeting 2029</u></a> for Cloudflare to be fully post-quantum secure.</p><p>ML-DSA, the best all-around post-quantum signature scheme standardized today, has its downsides: itâs much larger on the wire, and many <a href=\"https://github.com/fancy-cryptography/fancy-cryptography\" target=\"_blank\" rel=\"noopener noreferrer\"><u>tricks</u></a> we were able to perform with RSA and ECC simply cannot be done with ML-DSA. There are better post-quantum si

## Summary

gnature schemes on the horizon: last month, NIST <a href=\"https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/LXoTAe5AN78/m/ZXgBCNlgDAAJ\" target=\"_blank\" rel=\"noopener noreferrer\"><u>announced</u></a> that it is advancing nine post-quantum signature schemes to the third round of the â<a href=\"https://csrc.nist.gov/projects/pqc-dig-sig\" target=\"_blank\" rel=\"noopener noreferrer\"><u>signatures on-ramp</u></a>â. And a draft standard for <a href=\"https://falcon-sign.info/\" target=\"_blank\" rel=\"noopener noreferrer\"><u>FN-DSA</u></a> (nÃ©e Falcon), which was picked from the previous competition, is expected imminently.</p><p>We have been very interested in advances in post-quantum signature algorithms, and wrote about the progress in <a href=\"https://blog.cloudflare.com/sizing-up-post-quantum-signatures/\"><u>2021</u></a>, <a href=\"https://blog.cloudflare.com/nist-post-quantum-surprise/\"><u>2022</u></a>, <a href=\"https://blog.cloudflare.com/another-look-at-pq-signatures/\"><u>2024</u></a>, and <a href=\"https://blog.cloudflare.com/pq-2025/#signatures-on-the-horizon\"><u>2025</u></a>. In this blog post weâll treat you to the latest developments in great detail.</p><p>But first we have to deal with the elephant in the room: These new signature algorithms will not be ready in time for the PQ transition â not even close, as we <a href=\"#timelines\"><u>will see later on</u></a>. The problem is arriving too soon for us to wait. ML-DSA is available today, and it will have to do for the first migration. As Eric Rescorla <a href=\"https://educatedguesswork.org/posts/pq-emergency/\" target=\"_blank\" rel=\"noopener noreferrer\"><u>wrote</u></a> in 2024:</p><blockquote><p><i>You go to war with the algorithms you have, not the ones you wish you had.</i></p></blockquote><p>Nonetheless, the search for better post-quantum signature algorithms is crucial for several reasons, and we firmly believe it is still the best use of NISTâs limited resources.</p><p>Letâs have a look at the signature algorithms in detail. After that weâll look at the timeline for their availability, and the reasons why we still need them.</p>\n <div class=\"flex anchor relative\">\n <h2 id=\"the-signature-algorithms\">The signature algorithms</h2>\n <a href=\"#the-signature-algorithms\" aria-hidden=\"true\" class=\"relative sm:absolute sm:-start-5\">\n <svg width=\"16\" height=\"16\" viewBox=\"0 0 24 24\"><path fill=\"currentcolor\" d=\"m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z\"></path></svg>\n </a>\n </div>\n <p>In the table below, we compare the can

## Related Articles

- [[meerkat introduction]]
- [[oauth for all]]
- [[post quantum eo]]
- [[workers cache]]
- [[content independence day ai options]]
