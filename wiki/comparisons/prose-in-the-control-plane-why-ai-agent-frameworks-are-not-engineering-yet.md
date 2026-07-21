---
title: "prose in the control plane why ai agent frameworks are not engineering yet"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - image-generation
  - llm
  - mobile
  - open-source
  - prompt-engineering
  - search
  - software
  - video-generation
  - web
---

# prose in the control plane why ai agent frameworks are not engineering yet

> **Source:** prose-in-the-control-plane-why-ai-agent-frameworks-are-not-engineering-yet-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/jamilxt/prose-in-the-control-plane-why-ai-agent-frameworks-are-not-engineering-yet-1680 ingested: 2026-07-18 sha256: 77e5c5649914537487866a558efd4c86c2419a776cf1b63c4b9f...
> **Sources:**
>   - prose-in-the-control-plane-why-ai-agent-frameworks-are-not-engineering-yet-2026-07-18.md
> **Links:**
- [[the gitbook migration trap 4gp2]]
- [[its a post 4hi8]]
- [[introducing schemd a small text to svg compiler for circuits and uml 1i6p]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[deadstop 2025 vs crossfit games 2024 1okg]]

## Key Findings

---
source_url: https://dev.to/jamilxt/prose-in-the-control-plane-why-ai-agent-frameworks-are-not-engineering-yet-1680
ingested: 2026-07-18
sha256: 77e5c5649914537487866a558efd4c86c2419a776cf1b63c4b9f1b34ecee8ff1
blog_source: Dev Community
---
Prose in the Control Plane: Why AI Agent Frameworks Are Not Engineering (Yet) - DEV Community
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
![Cover image for Prose in the Control Plane: Why AI Agent Frameworks Are Not Engineering (Yet)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fk5ueu3kq0rdhrgtz808a.png)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fk5ueu3kq0rdhrgtz808a.png)
[![Md Jamilur Rahman](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F167939%2Fe9f79c11-0d2b-4558-89b3-4c0ff54e8821.jpg)](/jamilxt)
[Md Jamilur Rahman](/jamilxt)
Posted on Jul 18
# 
Prose in the Control Plane: Why AI Agent Frameworks Are Not Engineering (Yet)
[#ai](/t/ai)
[#llm](/t/llm)
[#agentskills](/t/agentskills)
[#programming](/t/programming)
Skill frameworks for AI coding agents are exploding in popularity. As of July 2026, Superpowers has roughly 256,000 GitHub stars, Matt Pocock's skills have roughly 176,000, and Agent Skills has roughly 79,000. A

## Summary

ll three promise to make AI agents write better code by feeding them structured Markdown instructions.
But there is a fundamental problem that deserves more attention than it gets: the behavioral control layer in these frameworks is **plain English written in Markdown files** (what literary types call "prose"). Not code. Not configuration. Not compiled rules. Just natural-language sentences that the agent reads and interprets. Ambiguous, probabilistically interpreted, context-sensitive sentences. And the industry is calling that engineering.
This article is about why that matters, what the real failure modes are, and what actual guardrails would look like.
## 
What Is the Control Plane?
In traditional software, the control plane is the layer that governs how a system behaves: configuration files, type systems, access control policies, deployment pipelines, CI/CD gates. These mechanisms share a common property. They are **deterministic**. A type checker either passes or fails. A CI pipeline either succeeds or errors. The behavior is reproducible and independently verifiable.
AI agent frameworks introduce a new kind of control plane. Instead of configuration files or type systems, they use prose instructions: SKILL.md files, system prompts, AGENTS.md files, CLAUDE.md files. The agent reads these instructions and decides what to do.
This is not a minor implementation detail. It is a fundamental shift in how behavioral control works. And it has consequences that the framework creators have not fully addressed.
## 
The Core Problem: Prose Is Probabilistic
When you write an instruction like `You MUST write tests before implementation` in a skill file (for example), the agent does not execute that instruction the way a compiler executes a type annotation. It **interprets** the instruction probabilistically. The same instruction might produce different behavior on different runs, in different contexts, or after the agent has read additional context that reframes its understanding of what "tests" means or what "implementation" means.
This is not speculation. Anthropic's own SWE-bench documentation acknowledges that agent performance "can vary significantly based on this scaffolding, even when using the same underlying AI model." The scaffolding is the prose. The variation is the probabilistic interpretation.
Three specific failure modes follow from this.
### 
1. Semantic Drift
Over a long-running session, the agent accumulates context. Earlier instructions get pushed further back. New context reframes old instructions. The agent's interpretation of "write tests first" in step 1 might differ from its interpretation in step 47, not because the instruction changed, but because the surrounding context changed.
No current framework addresses this at the instruction level. The instruction is prose. There is no mechanism that detects when the agent's interpretation has drifted from the original intent.
### 
2. Goal Reinterpretation
Agents expand scope. You ask f

## Related Articles

- [[the gitbook migration trap 4gp2]]
- [[its a post 4hi8]]
- [[introducing schemd a small text to svg compiler for circuits and uml 1i6p]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[deadstop 2025 vs crossfit games 2024 1okg]]
