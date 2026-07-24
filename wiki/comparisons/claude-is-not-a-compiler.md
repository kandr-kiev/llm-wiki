---
title: "claude is not a compiler"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - claude
  - image-generation
  - news
---
backlinks:
  - claude-is-not-a-compiler
---


# claude is not a compiler

> **Source:** claude-is-not-a-compiler-2026-07-21.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** [![exe.dev logo](/static/exy.webp)](https://exe.dev) [exe.dev](https://exe.dev) [docs](https://exe.dev/docs) [blog](/) [pricing](https://exe.dev/pricing) uses [SandboxDisposable VMs for AI agents, by...
> **Sources:**
>   - claude-is-not-a-compiler-2026-07-21.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[ai]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]

## Key Findings

[![exe.dev logo](/static/exy.webp)](https://exe.dev)
[exe.dev](https://exe.dev)
[docs](https://exe.dev/docs)
[blog](/)
[pricing](https://exe.dev/pricing)
uses
[SandboxDisposable VMs for AI agents, by the second.](https://exe.dev/sandbox)
[VPSPersistent Linux VMs with HTTPS and SSH.](https://exe.dev/vps)
[DevboxCloud dev environment for you and your agents.](https://exe.dev/devbox)
[Dashboard](https://exe.dev/auth)
# Claude Is Not a Compiler
2026-07-20
Josh Bleecher Snyder
In early 2025, I wrote [Is Claude a Compiler](https://commaok.xyz/ai/is-claude-a-compiler/)? At the time, my answer was: I don’t know.
I’m now pretty sure the answer is “no, that’s a category error, it’s *better* than a compiler.” But this requires a bit of unpacking.
Computer programs are notoriously intricate and finicky. A program operates at an extreme level of precision. There is no “wave hands” CPU instruction. High-level goals, meanwhile, are deeply underspecified.
In a highly stylized view of the world, software gets built in layers, each one adding specification and hiding “unnecessary” detail. Vision becomes strategy, product plans become coding plans, code becomes binaries. Each step is handled by a different role: executive, VP, PM, architect, engineer, compiler. 
Critically, every step involves making lots of decisions. That’s what it *means* to increase the level of specification. (This is why one of my two key metrics for hiring engineers is judgment. The other is comity.)
The bottom layer, from source code to binary, is what a compiler does. Compilers make lots of decisions! Inlining, register allocation, whether to emit warnings or reject a program outright. And these decisions matter: They drive performance, system stability, predictability, and failure modes. A compiler engineer’s job is to arrange for the compiler to make consistently good decisions.
A good, trusted compiler frees a software engineer from having to make these decisions. Most engineers have little idea how compilers work; they don’t need to in order to be effective. 
In 2025, we operated in a world where we used LLMs to generate smallish chunks of code. In this mental model, a coding agent might slot in as a new layer between a software engineer and a traditional compiler. It “compiles” natural language to code, making decisions so the engineer doesn’t have to. Its value is proportional to its reliability and the scale of the decisions it can make.
The thing is, this highly stylized view of the world is false. Abstractions leak and [layers rub](https://www.dbreunig.com/2026/07/03/ai-ecosytem-pace-layers.html). And even if they didn’t, we’d poke holes in them anyway.
Working across layers is extremely valuable; mechanical sympathy matters.
Part of how the [Empire State Building was constructed](https://www.construction-physics.com/p/building-fast-and-slow-the-empire) in under a year and under budget (!!) was by systematically working across layers. For example, when deciding about the exterior 

## Summary

chrome-nickel steel cladding:
>
Neither architects, builders nor subcontractors felt competent to deal with this complicated technical problem of construction without full consultation. Accordingly, after full preliminary discussion, an all-inclusive meeting was called which was attended by representatives of the owner, the architects and builders, the subcontractors rolling the material, the metal workers who were to fabricate and those who were to erect it, and the inspectors who were to test all sheets at the several stages of preparation.
This sounds really obvious when you say it out loud.
And yet we systematically fail at this in practice. I can only imagine the delight of the metal workers who had an opportunity to guide the design toward something that wasn’t slow and miserable to work on.
Part of the reason we fail is ignorance of what is even worth asking about. There’s a reason that [the best executives have deep knowledge of their industry](https://daringfireball.net/linked/2022/10/11/ceos-as-nerds). I also suspect that some of it is dismissiveness (“What could a line metalworker have to tell *me*?”). But a big chunk is also communication and organizational overhead. Layers exist for a reason—information hiding enables organizational scaling.
Claude is better than a compiler because it can work vertically across the stack. LLMs now talk strategy, product, architecture, code, and machine code. It can’t (yet?) do most individual tasks as well as an experienced, dedicated human, but it can do all of them, without having to schedule meetings or ask permission.
Here’s a concrete example.
[exe.dev](http://exe.dev) VMs have nice domain names: [vm-name.exe.xyz](http://vm-name.exe.xyz). When we start a new VM, we add a CNAME entry or three. Easy, right?
But our VMs start fast, so fast that even if we created the DNS entries before creating the VM, our users still had to sit around waiting for DNS to propagate, which occasionally took minutes, not seconds.
We did the obvious thing: We wrote our own DNS server, so that DNS always immediately matched the source of truth. And life was good.
But [latency matters](https://blog.exe.dev/regions), so we added regions. And just like that, DNS became the long pole again, because all DNS was served out of Oregon. Also, deployments caused tiny DNS outages. To fix this, all we needed now was a geographically distributed but fully consistent DNS server.
We did what a sensible engineer does when faced with a hard problem: cheat. We vibe-engineered a distributed DNS server tuned to our specific needs.
The goals were clear: Reduce latency for users far from Oregon and increase uptime resiliency. But the rest was not. We had to figure out everything from the exact behavior we wanted (particularly under various failure conditions), to how it fit into our overall company plans, to the architecture that could best achieve those goals, straight through down to the fine implementation details.
We hashed out the highe

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[ai]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "claude-is-not-a-compiler")
```
