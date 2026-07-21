---
title: "openvm bugs"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - async
  - claude
  - container
  - image-generation
  - library
  - llm
  - news
  - open-source
  - parallel
  - pipeline
  - prompt-tuning
  - real-time
  - security
  - system-design
  - transfer-learning
  - use-case
---

# openvm bugs

> **Source:** ai-meets-cryptography-2-what-ai-found-in-openvms-zkvm-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** -  -  -  -  -  -  -  -  # [ZK/SEC Quarterly](../../index.html) [ Back to all posts ](../../index.html) # AI meets Cryptography 2: What AI Found in OpenVM's zkVM Stefanos Chaliasos, Hao Pham July 17, 2...
> **Sources:**
>   - ai-meets-cryptography-2-what-ai-found-in-openvms-zkvm-2026-07-17.md
> **Links:**
- [[Automating Ai Away]]
- [[ai music video arena claude vs gpt 5.6]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[ai]]
- [[Automating away]]

## Key Findings

- 
- 
- 
- 
- 
- 
- 
- 
# [ZK/SEC Quarterly](../../index.html)
[
Back to all posts
](../../index.html)
# AI meets Cryptography 2: What AI Found in OpenVM's zkVM
Stefanos Chaliasos, Hao Pham
July 17, 2026
13 min read
security
crypto
AI
zkao
audit
zkvm
![Thumbnail](./thumbnail.png)
This is the second post in the series.
In case you have not read the [first one on Cloudflare's CIRCL](../circl-bugs), it has more context on why we run these experiments and how our pipeline is set up.
In this post, we pointed [zkao](https://zkao.io/), our AI auditor, at [OpenVM's zkVM](https://github.com/openvm-org/openvm), and it found a critical soundness bug in its guest library `openvm-pairing` that lets a malicious prover forge any pairing equality.
Note that this is not a soundness bug in the zkVM's proving system itself; it only affects code that uses the vulnerable library.
The bug in this post was assigned [CVE-2026-46669](https://github.com/openvm-org/openvm/security/advisories/GHSA-76mq-v757-53gr) and fixed in OpenVM 1.6.0.
As far as we know, all partners building on OpenVM have since upgraded to that version.
Note
**Clarification**, same as in the first post: the AI produced a candidate finding, not a final report.
Humans on our team then validated the issue, confirmed exploitability, understood the full impact and affected projects, and handled disclosure.
In this case, a very quick manual triage was enough to decide it was worth sharing with the OpenVM team, thanks to the detailed report and a minimal PoC that zkao produced itself.
## How it happened
Four months ago, we scanned [OpenVM](https://github.com/openvm-org/openvm) as part of our AI experiment, the same way we scan everything at first: an LLM with a simple prompt, and then an LLM with our expert-maintained skills.
We ran it with Opus 4.6 and Codex 5.3.
As soon as Opus 4.7 and Codex 5.4 came out, we ran them again.
The candidate findings were all valid observations, and the models confidently labeled several of them as Critical or High, but none of them were actually exploitable.
Our hypothesis was that a zkVM is simply too complex for a naive LLM setup to handle with 300K tokens or even 1M tokens of context.
The dependencies between modules are far denser than in a typical library.
A cryptography library can often be audited in parallel by simply handing each subagent a folder that maps to a single cryptographic primitive.
Each subagent reads a small number of lines, applies only the relevant skills, writes its findings to a markdown file, and the main agent stitches those files together.
All of this happens out of the box with popular agentic coding tools such as Claude Code and Codex, with little human steering.
That approach does not transfer to a more complex codebase, like OpenVM.
There, except for the low-hanging fruit, a subagent's useful output is not a list of bugs.
You can have a provably secure module A and a provably secure module B whose composition is still not secure.
So, hunting f

## Summary

or bugs in that "isolated" mode cannot catch meaningful bugs.
Instead, a subagent's output should be *knowledge* about a module: what it assumes, what it delegates to its callers, and what invariant it is silently relying on.
However, representing that kind of output well is the hard part.
Too short and it skips the implementation detail that the bug actually sits on.
Too long and it overflows the main agent's context before it can be combined with anything else.
From what we have seen, at least at the time of writing, this problem is not solved efficiently by the agentic coding tools mentioned above.
With that hypothesis in mind, we decided to run [zkao](https://zkao.io/) on OpenVM, even though our original rule for these experiments was to run zkao only *after* the plain LLMs had already found a real bug.
We have spent a lot of time on context engineering for zkao, and we have encoded the working methods of our own experts into it as reusable flows for finding vulnerabilities, so it seemed like the right tool for exactly this situation.
After more than nine and a half hours of scanning, it returned many findings.
Similar to the prior experiment, we did not have time to go over every finding in depth. 
After a quick pass, one stood out immediately: a critical soundness bug in the pairing check in one of the guest libraries.
Our hypothesis held up, and months of effort had paid off!
Although there is only one bug to share, to stay consistent with the first post, here is the bug at a glance.
## Severities and fixes at a glance
#
Bug
AI severity
OpenVM severity
Fix commit
Found by
1
[`openvm-pairing` pairing check missing proper subfield check on scaling factor](#bug-1-openvm-pairing-pairing-check-missing-proper-subfield-check-on-scaling-factor)
Critical
Critical
[`a720e2c`](https://github.com/openvm-org/openvm/commit/a720e2c7ba529becd101dbad24c879bd5c1257f4)
[zkao](https://zkao.io/)
This time, the AI severity and the maintainer severity agree.
## Bug 1: `openvm-pairing` pairing check missing proper subfield check on scaling factor
### Background
Pairings are the engine under Groth16, PLONK with KZG, and BLS signatures.
In all of these protocols, the verifier is usually not asking for one pairing value.
It is asking whether a product of pairings is one:
$$ \prod_i e(P_i, Q_i) = 1. $$
From that one yes-or-no answer, a verifier concludes that a SNARK proof is valid, that a KZG opening is correct, or that a signature verifies.
So if a prover can make a false pairing product appear to be one, everything built on top of it is no longer sound.
A pairing is a bilinear map
$$
e : G_1 \times G_2 \to G_T,
$$
where $G_1, G_2, G_T$ are abelian groups. In our case, $G_1$ and $G_2$ are elliptic-curve groups and $G_T$ is a multiplicative subgroup of $\mathbb{F}_{p^{12}}^{*}$.
The most important property of pairing is bilinearity:
$$ e([a]P, [b]Q) = e(P, Q)^{ab}. $$
This is why pairings are useful, but we will not actually need this property to understand the bug.

## Related Articles

- [[Automating Ai Away]]
- [[ai music video arena claude vs gpt 5.6]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[ai]]
- [[Automating away]]
