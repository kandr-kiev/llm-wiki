---
title: "build a basic ai agent from scratch security ii 2m2c"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - search
  - security
  - software
  - standards
  - video-generation
  - web
---

# build a basic ai agent from scratch security ii 2m2c

> **Source:** build-a-basic-ai-agent-from-scratch-security-ii-2026-07-21.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/rogiia/build-a-basic-ai-agent-from-scratch-security-ii-2m2c ingested: 2026-07-21 sha256: 4443d4612dbb958f5f98631c8806ba30d168518954797263579eab483635136d blog_source: De...
> **Sources:**
>   - build-a-basic-ai-agent-from-scratch-security-ii-2026-07-21.md
> **Links:**
- [[the part of this year i dont put in the commit messages l6m]]
- [[hollowtest find tests that pass but prove nothing 2iii]]
- [[i tried kimi k3 for a week heres what happened]]
- [[starting my developer journey bh8]]
- [[class vs object who is the big boss 32nj]]

## Key Findings

---
source_url: https://dev.to/rogiia/build-a-basic-ai-agent-from-scratch-security-ii-2m2c
ingested: 2026-07-21
sha256: 4443d4612dbb958f5f98631c8806ba30d168518954797263579eab483635136d
blog_source: Dev Community
---
Build a Basic AI Agent From Scratch: Security II - DEV Community
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
[![Roger Oriol](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F905788%2F8cf647ea-956c-4ca9-aa00-2cd63540878f.png)](/rogiia)
[Roger Oriol](/rogiia)
Posted on Jul 21
# 
Build a Basic AI Agent From Scratch: Security II
[#agents](/t/agents)
[#ai](/t/ai)
[#security](/t/security)
Previous parts of *Build a Basic AI Agent From Scratch*:
- [Basic Agent](https://www.ruxu.dev/articles/ai/build-a-basic-ai-agent/)
- [Tools](https://www.ruxu.dev/articles/ai/build-an-ai-agent-with-tools/)
- [Long Task Planning](https://www.ruxu.dev/articles/ai/build-an-ai-agent-planning/)
- [Human in the Loop & Security](https://www.ruxu.dev/articles/ai/build-an-ai-agent-human-in-the-loop-security/)
>
You can find and clone this code in this blog series' [Github repo](https://github.com/rogiia/basic-agent-harness).
In the previous part we gave our agent a basic safety model: permission modes, an `acceptEdits` trust boundary, and an `ask_question` tool so the agent could stop and clarify before doing something risky. That was enough to keep the agent from running wild on your machine, but it was only the first layer of defense.


## Summary

These measures ultimately put the burden of security on the human instead of the machine, since the machine cannot be trusted. In many cases, this won't be enough. A human can be wrong, or they can glance over security issues because they are tired, or simply don't care. Once a tool call is approved by the human, the agent is free to run around and do all the damage its host allows it to do.
In this part we will start closing the security gaps we still have in our agent harness. We will move tool execution into a **Docker sandbox** so a runaway command can only touch the project directory, add **prompt-injection defenses** so the model stops trusting tool output as instructions, and validate every tool input against its **schema** before it runs.
## 
The Security Checklist
Before writing code, it helps to lay out everything a production-grade agent harness should defend against. The codebase ships a small checklist that captures the threat model in six sections:
- Prompt Injection Defense: delimit context, treat external data as data, re-validate intent
- Tool Permission Gating: least privilege, destructive-action confirmation, scoped params
- Input/Output Validation: validate input against schema, sanitize outputs
- Loop & Resource Controls: iteration caps, token budget, timeouts, cost circuit breakers
- Secret & Credential Management: no secrets in prompts, harness-level injection, per-session rotation
- Observability & Kill Switches: structured decision logs, human checkpoints, session-level abort
The previous part covered the user-facing slice of (2): permission modes and clarification. This part and the next cover the rest. Each control lands in its own module in the agent source code so the rules are easy to audit and extend:
- 
`prompt_safety.py`: Delimiters, trust-boundaries prompt, external-data wrapping, intent drift check.
- 
`tool_policy.py`: Path scoping, shell denylist, SSRF guard, always-confirm patterns.
- 
`tools/validators.py`: Dependency-free JSON-Schema validation + bounded output scope.
- 
`resource_limits.py`: Iteration caps, context trimming, cost tracker.
- 
`secret_management.py`: Env scan, system-prompt audit, container env scrub, session tokens.
- 
`session_control.py`: Abort controller, in-flight kill, file rollback.
- 
`tools/audit.py`: Append-only JSONL audit of every decision step.
- 
`tools/sandbox.py`: Docker container for action tools, per-call timeout, env injection.
- 
`agent.py`: Orchestration: wires every control into the agent loop.
## 
Sandbox: Execution Security
The goal of sandboxing is to isolate the agent from the host machine. Instead of having access to everything the host machine has to offer, we build a sandbox for the agent with just the files, programs and environment variables that it needs and nothing more. Ultimately, sandboxing limits the blast radius if something bad does get executed.
Even with perfect prompt-injection defense and tool gating, you still want sandboxing because the model migh

## Related Articles

- [[the part of this year i dont put in the commit messages l6m]]
- [[hollowtest find tests that pass but prove nothing 2iii]]
- [[i tried kimi k3 for a week heres what happened]]
- [[starting my developer journey bh8]]
- [[class vs object who is the big boss 32nj]]
