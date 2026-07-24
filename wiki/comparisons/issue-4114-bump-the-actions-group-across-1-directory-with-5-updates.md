---
title: "Issue #4114: Bump the actions group across 1 directory with 5 updates"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - open-source
  - tool
---

# Issue #4114: Bump the actions group across 1 directory with 5 updates

> **Source:** gh-huggingfaceaccelerate-issue-4114-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/accelerate/issues/4114 ingested: 2026-07-14 sha256: 5409f17874470258501c4bdd6125cdac58caea5494349e04a210d4fcb7a8d96e blog_source: github:huggingface/acce...
> **Sources:**
>   - gh-huggingfaceaccelerate-issue-4114-2026-07-14.md
> **Links:**
- [[release-500]]
- [[release-v180]]
- [[v0.27.0]]
- [Issue #6360: Bump the actions group with 9 updates]
- [[Release Notes: Ollama vv0.31.2]]

## Key Findings

---
source_url: https://github.com/huggingface/accelerate/issues/4114
ingested: 2026-07-14
sha256: 5409f17874470258501c4bdd6125cdac58caea5494349e04a210d4fcb7a8d96e
blog_source: github:huggingface/accelerate
---
# Issue #4114: Bump the actions group across 1 directory with 5 updates
**State:** open | **Author:** dependabot[bot] | **Created:** 2026-07-13T07:56:54Z
Bumps the actions group with 5 updates in the / directory:
| Package | From | To |
| --- | --- | --- |
| [actions/checkout](https://github.com/actions/checkout) | `6` | `7` |
| [huggingface/doc-builder/.github/workflows/build_main_documentation.yml](https://github.com/huggingface/doc-builder) | `bcff59fca682130d2e7271ca8589911b7ac0b8bf` | `6108e850ae1cf2f71bb0815a600bcd50c39abfa7` |
| [huggingface/doc-builder/.github/workflows/build_pr_documentation.yml](https://github.com/huggingface/doc-builder) | `bcff59fca682130d2e7271ca8589911b7ac0b8bf` | `6108e850ae1cf2f71bb0815a600bcd50c39abfa7` |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | `3.95.5` | `3.95.8` |
| [huggingface/doc-builder/.github/workflows/upload_pr_documentation.yml](https://github.com/huggingface/doc-builder) | `bcff59fca682130d2e7271ca8589911b7ac0b8bf` | `6108e850ae1cf2f71bb0815a600bcd50c39abfa7` |
Updates `actions/checkout` from 6 to 7
Release notes
*Sourced from [actions/checkout's releases](https://github.com/actions/checkout/releases).*
>
## v7.0.0
## What's Changed
- block checking out fork pr for pull_request_target and workflow_run by [`@​aiqiaoy`](https://github.com/aiqiaoy) in [actions/checkout#2454](https://redirect.github.com/actions/checkout/pull/2454)
- Bump actions/publish-immutable-action from 0.0.3 to 0.0.4 in the minor-actions-dependencies group across 1 directory by [`@​dependabot`](https://github.com/dependabot)[bot] in [actions/checkout#2458](https://redirect.github.com/actions/checkout/pull/2458)
- Bump flatted from 3.3.1 to 3.4.2 by [`@​dependabot`](https://github.com/dependabot)[bot] in [actions/checkout#2460](https://redirect.github.com/actions/checkout/pull/2460)
- Bump js-yaml from 4.1.0 to 4.2.0 by [`@​dependabot`](https://github.com/dependabot)[bot] in [actions/checkout#2461](https://redirect.github.com/actions/checkout/pull/2461)
- Bump `@​actions/core` and `@​actions/tool-cache` and Remove uuid by [`@​dependabot`](https://github.com/dependabot)[bot] in [actions/checkout#2459](https://redirect.github.com/actions/checkout/pull/2459)
- upgrade module to esm and update dependencies by [`@​aiqiaoy`](https://github.com/aiqiaoy) in [actions/checkout#2463](https://redirect.github.com/actions/checkout/pull/2463)
- Bump the minor-npm-dependencies group across 1 directory with 3 updates by [`@​dependabot`](https://github.com/dependabot)[bot] in [actions/checkout#2462](https://redirect.github.com/actions/checkout/pull/2462)
- getting ready for checkout v7 release by [`@​aiqiaoy`](https://github.com/aiqiaoy) in [actions/checkout#2464](https://redirect.github.com/actions/checko

## Summary

ut/pull/2464)
- update error wording by [`@​aiqiaoy`](https://github.com/aiqiaoy) in [actions/checkout#2467](https://redirect.github.com/actions/checkout/pull/2467)
## New Contributors
- [`@​aiqiaoy`](https://github.com/aiqiaoy) made their first contribution in [actions/checkout#2454](https://redirect.github.com/actions/checkout/pull/2454)
**Full Changelog**: [https://github.com/actions/checkout/compare/v6.0.3...v7.0.0](https://github.com/actions/checkout/compare/v6.0.3...v7.0.0)
## v6.0.3
## What's Changed
- Update changelog by [`@​ericsciple`](https://github.com/ericsciple) in [actions/checkout#2357](https://redirect.github.com/actions/checkout/pull/2357)
- fix: expand merge commit SHA regex and add SHA-256 test cases by [`@​yaananth`](https://github.com/yaananth) in [actions/checkout#2414](https://redirect.github.com/actions/checkout/pull/2414)
- Fix checkout init for SHA-256 repositories by [`@​yaananth`](https://github.com/yaananth) in [actions/checkout#2439](https://redirect.github.com/actions/checkout/pull/2439)
- Update changelog for v6.0.3 by [`@​yaananth`](https://github.com/yaananth) in [actions/checkout#2446](https://redirect.github.com/actions/checkout/pull/2446)
## New Contributors
- [`@​yaananth`](https://github.com/yaananth) made their first contribution in [actions/checkout#2414](https://redirect.github.com/actions/checkout/pull/2414)
**Full Changelog**: [https://github.com/actions/checkout/compare/v6...v6.0.3](https://github.com/actions/checkout/compare/v6...v6.0.3)
## v6.0.2
## What's Changed
- Add orchestration_id to git user-agent when ACTIONS_ORCHESTRATION_ID is set by [`@​TingluoHuang`](https://github.com/TingluoHuang) in [actions/checkout#2355](https://redirect.github.com/actions/checkout/pull/2355)
- Fix tag handling: preserve annotations and explicit fetch-tags by [`@​ericsciple`](https://github.com/ericsciple) in [actions/checkout#2356](https://redirect.github.com/actions/checkout/pull/2356)
**Full Changelog**: [https://github.com/actions/checkout/compare/v6.0.1...v6.0.2](https://github.com/actions/checkout/compare/v6.0.1...v6.0.2)
## v6.0.1
## What's Changed
- Update all references from v5 and v4 to v6 by [`@​ericsciple`](https://github.com/ericsciple) in [actions/checkout#2314](https://redirect.github.com/actions/checkout/pull/2314)
- Add worktree support for persist-credentials includeIf by [`@​ericsciple`](https://github.com/ericsciple) in [actions/checkout#2327](https://redirect.github.com/actions/checkout/pull/2327)
- Clarify v6 README by [`@​ericsciple`](https://github.com/ericsciple) in [actions/checkout#2328](https://redirect.github.com/actions/checkout/pull/2328)
**Full Changelog**: [https://github.com/actions/checkout/compare/v6...v6.0.1](https://github.com/actions/checkout/compare/v6...v6.0.1)
Commits
- [`9c091bb`](https://github.com/actions/checkout/commit/9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0) update error wording ([#2467](https://redirect.github.com/actions/checkout/issues/2467))
- [`1044a6d`](https://

## Related Articles

- [[release-500]]
- [[release-v180]]
- [[v0.27.0]]
- [Issue #6360: Bump the actions group with 9 updates]
- [[Release Notes: Ollama vv0.31.2]]
