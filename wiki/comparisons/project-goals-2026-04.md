---
title: "project goals 2026 04"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - application
  - backend
  - governance
  - image-generation
  - nlp
  - parallel
  - self-supervised
  - software
  - system-design
---

# project goals 2026 04

> **Source:** project-goals-update---april-2026-end-of-2025h2-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/ ingested: 2026-07-17 sha256: 3ed19b01b5f03eb605b0f9992536a9e93097ed4c0986dbd29399192810747324 blog_source: Rust Blog --- Pr...
> **Sources:**
>   - project-goals-update---april-2026-end-of-2025h2-2026-07-17.md
> **Links:**
- [[Automating Ai Away]]
- [[Rust 1.96.0]]
- [[Automating away]]
- [[Rust 1.97.0]]
- [[crates io development update]]

## Key Findings

---
source_url: https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/
ingested: 2026-07-17
sha256: 3ed19b01b5f03eb605b0f9992536a9e93097ed4c0986dbd29399192810747324
blog_source: Rust Blog
---
Project goals update — April 2026 (end of 2025H2) | Rust Blog
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
[
![](https://blog.rust-lang.org/images/rust-logo-blk.svg)
Rust Blog
](https://blog.rust-lang.org/)
- [Rust](https://www.rust-lang.org)
- [Install](https://www.rust-lang.org/tools/install)
- [Learn](https://www.rust-lang.org/learn)
- [Tools](https://www.rust-lang.org/tools)
- [Governance](https://www.rust-lang.org/governance)
- [Community](https://www.rust-lang.org/community)
🖌
- Light
- Dark
- System
## Project goals update — April 2026 (end of 2025H2)
May 18, 2026 · Nurzhan Saken
on behalf of [the Goals team](https://www.rust-lang.org/governance/teams/launching-pad#team-goals) 
The 2025H2 Project Goal period has now concluded. Over these months, the Rust Project pursued 41 Project Goals, 13 of which were designated as Flagship Goals. This post contains curated updates on our progress since the last post and the final status for each of the goals (many of which continue as part of the 2026 period). Full details for any particular goal are available in its tracking issue.
Thanks to everyone who contributed! <3
## [](#table-of-contents)
Table of contents
- [Flagship: Beyond the `&`](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#flagship-beyond-the)
- [Continue Experimentation with Pin Ergonomics](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#continue-experimentation-with-pin-ergonomics)
- [Design a language feature to solve Field Projections](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#design-a-language-feature-to-solve-field-projections)
- [Reborrow traits](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#reborrow-traits)
- [Flagship: Flexible, fast(er) compilation](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#flagship-flexible-fast-er-compilation)
- [build-std](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#build-std)
- [Production-ready cranelift backend](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#production-ready-cranelift-backend)
- [Promoting Parallel Front End](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#promoting-parallel-front-end)
- [Relink don't Rebuild](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#relink-don-t-rebuild)
- [Flagship: Higher-level Rust](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#flagship-higher-level-rust)
- [Ergonomic ref-counting: RFC decision and preview](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#ergonomic-ref-counting-rfc-decision-and-preview)
- [Stabilize cargo-script](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#stabilize-cargo-script)
- [Flagship: Unblocking dormant traits](https://blog.rust-lang.org/2026/05/18/project-goals-2

## Summary

026-04/#flagship-unblocking-dormant-traits)
- [Evolving trait hierarchies](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#evolving-trait-hierarchies)
- [In-place initialization](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#in-place-initialization)
- [Next-generation trait solver](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#next-generation-trait-solver)
- [Stabilizable Polonius support on nightly](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#stabilizable-polonius-support-on-nightly)
- [Other goal updates](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#other-goal-updates)
- [Add a team charter for rustdoc team](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#add-a-team-charter-for-rustdoc-team)
- [Borrow checking in a-mir-formality](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#borrow-checking-in-a-mir-formality)
- [C++/Rust Interop Problem Space Mapping](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#c-rust-interop-problem-space-mapping)
- [Comprehensive niche checks for Rust](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#comprehensive-niche-checks-for-rust)
- [Const Generics](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#const-generics)
- [Continue resolving `cargo-semver-checks` blockers for merging into cargo](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#continue-resolving-cargo-semver-checks-blockers-for-merging-into-cargo)
- [Develop the capabilities to keep the FLS up to date](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#develop-the-capabilities-to-keep-the-fls-up-to-date)
- [Emit Retags in Codegen](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#emit-retags-in-codegen)
- [Expand the Rust Reference to specify more aspects of the Rust language](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#expand-the-rust-reference-to-specify-more-aspects-of-the-rust-language)
- [Finish the libtest json output experiment](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#finish-the-libtest-json-output-experiment)
- [Finish the std::offload module](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#finish-the-std-offload-module)
- [Getting Rust for Linux into stable Rust: compiler features](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#getting-rust-for-linux-into-stable-rust-compiler-features)
- [Getting Rust for Linux into stable Rust: language features](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#getting-rust-for-linux-into-stable-rust-language-features)
- [Implement Open API Namespace Support](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#implement-open-api-namespace-support)
- [MIR move elimination](https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#mir-move-elimination)
- [Prototype a new set of Cargo "plumbing" commands](https://blog.rust-lang.org/2026/05/18/project-goals-

## Related Articles

- [[Automating Ai Away]]
- [[Rust 1.96.0]]
- [[Automating away]]
- [[Rust 1.97.0]]
- [[crates io development update]]
