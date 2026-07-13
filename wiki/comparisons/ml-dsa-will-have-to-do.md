---
title: "ml dsa will have to do"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - analysis
  - best-practice
  - comparison
  - data
  - open-source
  - real-time
  - search
  - standards
  - use-case
---
# ml dsa will have to do

> **Source:** ml-dsa-will-have-to-do.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- title: "ml dsa will have to do" type: comparison tags: [comparison] sources: [] description: Comparison analysis created: 2026-07-09 updated: 2026-07-09 confidence: medium contested: false links:...
> **Sources:**
>   - ml-dsa-will-have-to-do.md
> **Links:**
- [[finding-the-best-sleep-tracker]]
- [[chemical-hygiene]]
- [[automating-ai-away-2026-07-07]]
- [[animals-vs-ghosts]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]

## Key Findings


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
- - vulnerable to the attack of sufficiently advanced quantum computers. Such quantum computers do not exist yet, but they seem to be coming sooner than expected. Luckily, the solution is already available: migrate to ML-KEM encryption and ML-DSA signatures, which are designed to be resistant to quantum attack. They were standardized in 2024 by the U.S. National Institute of Standards and Technology (NIST) after an eight-year open international competition.
The migration to post-quantum cryptography is in full swing now. At the time of writing, the majority of traffic handled by Cloudflare is already using ML-KEM encryption, and is thus secured against the threat to data posed by harvest-now-decrypt-later attacks. But encryption is only one part of the equation: to be fully secure against quantum computers capable of breaking classical cryptography, we aim to deploy post-quantum signatures to protect authentication systems from unauthorized access. We are targeting 2029 for Cloudflare to be fully post-quantum secure.
ML-DSA, the best all-around post-quantum signature scheme standardized today, has its downsides: itâs much larger on the wire, and many tricks we were able to perform with RSA and ECC simply cannot be done with ML-DSA. There are better post-quantum si
## Summary
gnature schemes on the horizon: last month, NIST announced that it is advancing nine post-quantum signature schemes to the third round of the âsignatures on-rampâ. And a draft standard for FN-DSA (nÃ©e Falcon), which was picked from the previous competition, is expected imminently.
We have been very interested in advances in post-quantum signature algorithms, and wrote about the progress in 2021, 2022, 2024, and 2025. In this blog post weâll treat you to the latest developments in great detail.
But first we have to deal with the elephant in the room: These new signature algorithms will not be ready in time for the PQ transition â not even close, as we will see later on. The problem is arriving too soon for us to wait. ML-DSA is available today, and it will have to do for the first migration. As Eric Rescorla wrote in 2024:
>*You go to war with the algorithms you have, not the ones you wish you had.*
Nonetheless, the search for better post-quantum signature algorithms is crucial for several reasons, and we firmly be

## Summary

See Key Findings for full content.

## Related Articles

- [[finding-the-best-sleep-tracker]]
- [[chemical-hygiene]]
- [[automating-ai-away-2026-07-07]]
- [[animals-vs-ghosts]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
