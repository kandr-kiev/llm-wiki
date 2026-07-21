---
title: "crates io development update"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - api
  - application
  - architecture
  - frontend
  - governance
  - image-generation
  - integration
  - library
  - open-source
  - review
  - search
  - security
  - self-supervised
  - software
  - standards
  - system-design
  - vector-database
---

# crates io development update

> **Source:** cratesio-development-update-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** [ ![](https://blog.rust-lang.org/images/rust-logo-blk.svg) Rust Blog ](https://blog.rust-lang.org/) - [Rust](https://www.rust-lang.org) - [Install](https://www.rust-lang.org/tools/install) - [Learn](h...
> **Sources:**
>   - cratesio-development-update-2026-07-17.md
> **Links:**
- [[Rust 1.96.0]]
- [[Rust 1.97.0]]
- [[Rust 1.97.1]]
- [[The Illustrated Stable Diffusion]]
- [[Rust 1.96.1]]

## Key Findings

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
## crates.io: development update
July 13, 2026 · Tobias Bieniek
on behalf of [the crates.io team](https://www.rust-lang.org/governance/teams/crates-io) 
Another six months have passed since our last development update, and the crates.io team has been busy. Here's a summary of the most notable changes and improvements made to crates.io since then.
## [](#source-code-viewer)
Source Code Viewer
Crate pages now have a "Code" tab that lets you browse the contents of published crate versions directly on crates.io. This shows you the exact files that `cargo` downloads when you add a crate as a dependency, which might differ from the linked repository. This makes it much easier to audit your dependencies, including files that never appear in the repository, like the normalized `Cargo.toml` files that `cargo` generates.
![Source code viewer showing the "Code" tab of the serde crate](https://blog.rust-lang.org/2026/07/13/crates-io-development-update/code-tab.png)
The viewer comes with a file tree sidebar with search functionality, syntax highlighting, and GitHub-style line selection, where clicking or dragging line numbers produces shareable `#L10-L20` URLs.
Under the hood, the server now builds a zip file for every published version. Since the `.crate` files that `cargo` consumes are gzipped tarballs without random access support, a background job re-packs each of them into a seekable zip archive plus a JSON manifest describing the contained files. Both are served from our static CDN. The frontend then fetches only the manifest and loads each file on demand with an HTTP range request. Because of this architecture, browsing crate sources essentially adds no load on the crates.io API servers. Existing crate versions have been backfilled, so this works for old releases too.
The rendering library behind the code viewer is a diff renderer at heart, and that's no accident: a version-to-version diff viewer built on the same infrastructure is currently in the works. This will allow you to review exactly what changed between two published versions, right on crates.io. Stay tuned!
## [](#untangling-crates-io-accounts-from-github)
Untangling crates.io Accounts from GitHub
At the end of May, the crates.io team accepted RFC #3946. Crates.io accounts always have been tightly coupled to GitHub: signing in means "Log in with GitHub", and your crates.io identity is your GitHub username. The RFC changes that. It introduces usernames that are native to crates.io and independent of linked GitHub accounts, as a prerequisite for eventually supporting login via other identity prov

## Summary

iders.
The implementation of crates.io usernames has started, but there is still a lot left to do, most visibly the ability to change your crates.io username. After that is complete, there will be future RFCs and implementation for signing in with identity providers other than GitHub. Since all of this touches authentication and account security, we are deliberately taking it slow and rolling these changes out in small, carefully reviewed steps.
## [](#advisories-and-suggestions)
Advisories and Suggestions
In our January update we introduced the "Security" tab, which shows security advisories from the RustSec database. We have since taken this integration one step further: crates that RustSec has flagged as unmaintained now show a warning banner directly on their crate pages, linking to the corresponding advisory for details and possible alternatives. Thanks to Dirkjan Ochtman for implementing this feature!
![Unmaintained warning banner on the ansi_term crate page](https://blog.rust-lang.org/2026/07/13/crates-io-development-update/unmaintained-banner.png)
Related to this, some popular crates have been largely absorbed into the Rust standard library over the years, like `lazy_static`, which has been superseded by `std::sync::LazyLock` since Rust 1.80. Crate pages of such crates now show a friendly "You might not need this dependency" banner describing the standard library replacement, and superseded crates in dependency lists get a small light bulb icon with a similar hint.
!["You might not need this dependency" banner on the lazy_static crate page](https://blog.rust-lang.org/2026/07/13/crates-io-development-update/std-replacement-banner.png)
The dataset behind this feature lives in the new rust-lang/std-replacement-data repository, together with a documented inclusion policy: standard library replacements only, every entry must cite the stable `std`, `core`, or `alloc` API and Rust version, and crate maintainers get a notice-and-comment window before an entry is added. New entries can be proposed upstream and can benefit other tools too.
## [](#ferris)
Ferris
The most delightful change of this cycle: the Ferris on our error pages now follows your mouse cursor with its eyes:
![Ferris' eyes following the mouse cursor on the error page](https://blog.rust-lang.org/2026/07/13/crates-io-development-update/ferris.gif)
Getting a 404 error on crates.io is now slightly less sad.
## [](#svelte-frontend-migration-completed)
Svelte Frontend Migration Completed
In our January update, we announced that we were experimenting with porting the crates.io frontend from Ember.js to Svelte. This experiment has concluded successfully: the new frontend reached feature parity, went through a public testing phase in April, became the default at the beginning of May, and the Ember.js app has been removed from our repository.
We designed this change to be invisible for our users, since the new frontend is a 1:1 port of the previous design and functionality. For the team and

## Related Articles

- [[Rust 1.96.0]]
- [[Rust 1.97.0]]
- [[Rust 1.97.1]]
- [[The Illustrated Stable Diffusion]]
- [[Rust 1.96.1]]
