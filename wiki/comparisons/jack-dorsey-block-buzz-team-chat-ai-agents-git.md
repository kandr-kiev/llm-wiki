---
title: "jack dorsey block buzz team chat ai agents git"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - architecture
  - deployment
  - foundation-model
  - image-generation
  - news
  - open-source
  - real-time
  - self-supervised
  - video-generation
---
backlinks:
  - jack-dorsey-block-buzz-team-chat-ai-agents-git
---


# jack dorsey block buzz team chat ai agents git

> **Source:** jack-dorsey-launches-buzz-to-combine-team-chat-ai-agents-and-git-hosting-2026-07-21.md
> **Type:** comparison
> **Created:** 2026-07-22
> **Updated:** 2026-07-22
> **Confidence:** high
> **Description:** [RuntimeWire](/) [AI](/category/ai) [Startups](/category/startups) [Venture](/category/venture) [Products](/category/products) [Funding](/category/funding) [Exits](/category/exits) [Models](/models) [...
> **Sources:**
>   - jack-dorsey-launches-buzz-to-combine-team-chat-ai-agents-and-git-hosting-2026-07-21.md
> **Links:**
- [[ai music video arena claude vs gpt 5.6]]
- [[v3.13.0]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[kimi k3]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]

## Key Findings

[RuntimeWire](/)
[AI](/category/ai)
[Startups](/category/startups)
[Venture](/category/venture)
[Products](/category/products)
[Funding](/category/funding)
[Exits](/category/exits)
[Models](/models)
[Head-to-Head](/head-to-head)
[About](/about)
You're browsing RuntimeWire with JavaScript disabled. Articles and
navigation work fully. Interactive features — search, comments,
and newsletter signup — require JavaScript.
[ai](/category/ai)
# Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting
**Block's self-hostable workspace uses signed Nostr events, while its current relay architecture remains centralized within each deployment.**
By [Ryan Merket](/author/ryan-merket)
· Published Jul 21, 2026, 12:13pm CT
## Why it matters
Buzz turns Dorsey's agent-centered operating thesis into an open-source product. Its key bet is that shared identity and signed events can make agents accountable participants in software work.
![Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting — Block's self-hostable workspace uses signed Nostr events, while its current relay architecture remains centralized within each deployment.](https://runtimewire.com/api/storage/uploads/source-images/jack-dorsey-block-buzz-team-chat-ai-agents-git-f562a21f.jpg)
Jack Dorsey (@jack) said in an announcement on X on July 21st that Block is launching Buzz, an open-source workspace designed to put employees, AI agents, conversations and software repositories behind one identity system.
Dorsey, Block's cofounder and Block Head, is pitching Buzz as a way to reduce Block's dependence on Slack and GitHub. The move takes his preference for open protocols into the daily machinery of software development, where teams typically spread discussions, source code, automated workflows and agent activity across several vendors.
Buzz also fits the operating model Dorsey has been building inside Block. In an essay with Sequoia Capital's Roelof Botha, Dorsey argued that AI should change how organizations coordinate rather than serve only as a productivity add-on. Buzz supplies an infrastructure layer for that thesis: Block's public repository documents a separate internal build configured for Block's relay and agent provider.
### One workspace for humans and agents
Buzz is built around a self-hostable Nostr relay. Every message, reaction, workflow step, code event and approval is stored as a cryptographically signed event. Human employees and agents receive the same basic identity structure, including their own key pairs, channel memberships and audit trails.
That design lets agents participate as members rather than conventional chat bots. According to Block's documentation, agents can search prior discussions, open repositories, submit patches, review code, run workflows, edit shared canvases and create channels. Buzz includes an agent-oriented command-line interface and harnesses for Goose, Codex and Claude Code, keeping the underlying model choice separate from the

## Summary

 workspace.
Buzz's Git ambitions go well beyond posting repository notifications into chat. The project specification describes a built-in software forge using standard Git Smart HTTP. A feature branch can become its own channel, with patches, continuous-integration results, review comments and the merge decision preserved in the same record. Repositories, discussions and workflow history then share one search index.
The currently working feature set includes channels, threads, direct messages, shared canvases, media, search, an audit log, a desktop application and YAML-based workflows. Packaged builds are available for macOS, Windows and Linux. The repository is licensed under Apache 2.0.
### Decentralized control, centralized relays
Dorsey described Buzz as decentralized and self-sovereign, but Block's architecture document draws a more specific boundary. Buzz currently has no peer-to-peer event exchange, gossip layer or replication between relays. All reads and writes in a workspace pass through a single relay, which authenticates users, verifies signatures, stores events and distributes updates.
Buzz's decentralization therefore comes from deployment and ownership. An organization can run its own relay, retain its domain and data, and use portable Nostr key pairs instead of depending on a single hosted service. A hosted operator can also run multiple isolated communities on shared infrastructure. Within each community, however, the relay remains the authoritative server.
That distinction matters for teams evaluating Buzz as a Slack or GitHub substitute. Self-hosting gives an operator control over infrastructure and data location, but it also transfers responsibility for availability, backups, security and upgrades. The signed event model provides attribution and an audit trail; it does not remove the operational risks attached to the server hosting the workspace.
### An early product with a wide scope
Buzz is available for testing and development, though Block's own documentation repeatedly labels it unfinished. Mobile clients remain in development, push notifications are pending, and workflow approval gates have database, API and interface components without a completed execution path. The latest desktop release, version 0.4.21, shipped on July 21st with fixes and additions covering agent controls, authentication and workspace onboarding.
Block has given Buzz a broad assignment: replace portions of chat, code hosting, workflow automation, project search and agent orchestration with one event system. Combining those surfaces may reduce the integration work required to give agents useful context and tightly scoped access. It also puts Buzz against mature products whose separate roles let customers replace one tool without migrating the rest of their development stack.
Dorsey's launch makes Block the first customer reference embedded in Buzz's documentation, but Block has not published adoption, pricing or external customer figures. For now, Bu

## Related Articles

- [[ai music video arena claude vs gpt 5.6]]
- [[v3.13.0]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[kimi k3]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "jack-dorsey-block-buzz-team-chat-ai-agents-git")
```
