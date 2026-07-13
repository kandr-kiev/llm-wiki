---
title: "Issue #6360: Bump the actions group with 9 updates"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - analysis
  - best-practice
  - docker
  - gguf
  - nlp
  - open-source
  - performance
  - real-time
  - use-case
  - vector-database
---
# Issue #6360: Bump the actions group with 9 updates

> **Source:** gh-huggingfacetrl-issue-6360-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/trl/issues/6360 ingested: 2026-07-11 sha256: 3b9fe72b7130843d06d0adc3e23fd6ab6e5d6bf30142047c789e126703144c1d blog_source: github:huggingface/trl --- # I...
> **Sources:**
>   - gh-huggingfacetrl-issue-6360-2026-07-11.md
> **Links:**
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]
- [[Issue #47256: [serge] integration failure triage -]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[finding-the-best-sleep-tracker]]

## Key Findings

---
source_url: https://github.com/huggingface/trl/issues/6360
ingested: 2026-07-11
sha256: 3b9fe72b7130843d06d0adc3e23fd6ab6e5d6bf30142047c789e126703144c1d
blog_source: github:huggingface/trl
---
# Issue #6360: Bump the actions group with 9 updates
**State:** open | **Author:** dependabot[bot] | **Created:** 2026-07-11T09:37:34Z
Bumps the actions group with 9 updates:
| Package | From | To |
| --- | --- | --- |
| [huggingface/doc-builder/.github/workflows/build_main_documentation.yml](https://github.com/huggingface/doc-builder) | `4a384d0ccdeb8502a57f1003acee938b42a5592a` | `0f4784322c564503c4a4d67ccb7fba29e32f111a` |
| [huggingface/doc-builder/.github/workflows/build_pr_documentation.yml](https://github.com/huggingface/doc-builder) | `4a384d0ccdeb8502a57f1003acee938b42a5592a` | `0f4784322c564503c4a4d67ccb7fba29e32f111a` |
| [github/codeql-action/init](https://github.com/github/codeql-action) | `4.36.2` | `4.36.3` |
| [github/codeql-action/analyze](https://github.com/github/codeql-action) | `4.36.2` | `4.36.3` |
| [docker/setup-buildx-action](https://github.com/docker/setup-buildx-action) | `4.1.0` | `4.2.0` |
| [docker/login-action](https://github.com/docker/login-action) | `4.2.0` | `4.4.0` |
| [docker/build-push-action](https://github.com/docker/build-push-action) | `7.2.0` | `7.3.0` |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | `3.95.6` | `3.95.8` |
| [huggingface/doc-builder/.github/workflows/upload_pr_documentation.yml](https://github.com/huggingface/doc-builder) | `4a384d0ccdeb8502a57f1003acee938b42a5592a` | `0f4784322c564503c4a4d67ccb7fba29e32f111a` |
Updates `huggingface/doc-builder/.github/workflows/build_main_documentation.yml` from 4a384d0ccdeb8502a57f1003acee938b42a5592a to 0f4784322c564503c4a4d67ccb7fba29e32f111a
Commits
- [`0f47843`](https://github.com/huggingface/doc-builder/commit/0f4784322c564503c4a4d67ccb7fba29e32f111a) Mock optimum, torchao, gguf for diffusers docs ([#806](https://redirect.github.com/huggingface/doc-builder/issues/806))
- [`f8ab2e5`](https://github.com/huggingface/doc-builder/commit/f8ab2e5246a13eaa31c4b3760701856fc5ab98a6) Add bitsandbytes (mock) and sentencepiece (real) to diffusers doc deps ([#805](https://redirect.github.com/huggingface/doc-builder/issues/805))
- See full diff in [compare view](https://github.com/huggingface/doc-builder/compare/4a384d0ccdeb8502a57f1003acee938b42a5592a...0f4784322c564503c4a4d67ccb7fba29e32f111a)
Updates `huggingface/doc-builder/.github/workflows/build_pr_documentation.yml` from 4a384d0ccdeb8502a57f1003acee938b42a5592a to 0f4784322c564503c4a4d67ccb7fba29e32f111a
Commits
- [`0f47843`](https://github.com/huggingface/doc-builder/commit/0f4784322c564503c4a4d67ccb7fba29e32f111a) Mock optimum, torchao, gguf for diffusers docs ([#806](https://redirect.github.com/huggingface/doc-builder/issues/806))
- [`f8ab2e5`](https://github.com/huggingface/doc-builder/commit/f8ab2e5246a13eaa31c4b3760701856fc5ab98a6) Add bitsandbytes (mock) and sentencepiece (

## Summary

real) to diffusers doc deps ([#805](https://redirect.github.com/huggingface/doc-builder/issues/805))
- See full diff in [compare view](https://github.com/huggingface/doc-builder/compare/4a384d0ccdeb8502a57f1003acee938b42a5592a...0f4784322c564503c4a4d67ccb7fba29e32f111a)
Updates `github/codeql-action/init` from 4.36.2 to 4.36.3
Release notes
*Sourced from [github/codeql-action/init's releases](https://github.com/github/codeql-action/releases).*
>
## v4.36.3
No user facing changes.
Changelog
*Sourced from [github/codeql-action/init's changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md).*
>
# CodeQL Action Changelog
See the [releases page](https://github.com/github/codeql-action/releases) for the relevant changes to the CodeQL CLI and language packs.
## [UNRELEASED]
- *Upcoming breaking change*: Add a deprecation warning for customers using CodeQL version 2.20.6 and earlier. These versions of CodeQL were discontinued on 1 July 2026 alongside GitHub Enterprise Server 3.16, and will be unsupported by the next minor release of the CodeQL Action. [#3956](https://redirect.github.com/github/codeql-action/pull/3956)
## 4.37.0 - 08 Jul 2026
- Update default CodeQL bundle version to [2.26.0](https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.26.0). [#3995](https://redirect.github.com/github/codeql-action/pull/3995)
- In addition to the existing input format, the `config-file` input for the `codeql-action/init` step will soon support a new `[owner/]repo[@ref][:path]` format. All components except the repository name are optional. If omitted, `owner` defaults to the same owner as the repository the analysis is running for, `ref` to `main`, and `path` to `.github/codeql-action.yaml`. Support for this format ships in this version of the CodeQL Action, but will only be enabled over the coming weeks. [#3973](https://redirect.github.com/github/codeql-action/pull/3973)
## 4.36.3 - 01 Jul 2026
No user facing changes.
## 4.36.2 - 04 Jun 2026
- Cache CodeQL CLI version information across Actions steps. [#3943](https://redirect.github.com/github/codeql-action/pull/3943)
- Reduce requests while waiting for analysis processing by using exponential backoff when polling SARIF processing status. [#3937](https://redirect.github.com/github/codeql-action/pull/3937)
- Update default CodeQL bundle version to [2.25.6](https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.25.6). [#3948](https://redirect.github.com/github/codeql-action/pull/3948)
## 4.36.1 - 02 Jun 2026
No user facing changes.
## 4.36.0 - 22 May 2026
- *Breaking change*: Bump the minimum required CodeQL bundle version to 2.19.4. [#3894](https://redirect.github.com/github/codeql-action/pull/3894)
- Add support for SHA-256 Git object IDs. [#3893](https://redirect.github.com/github/codeql-action/pull/3893)
- Update default CodeQL bundle version to [2.25.5](https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.25.5). [#3926](https://redirect.github

## Related Articles

- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]
- [[Issue #47256: [serge] integration failure triage -]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[finding-the-best-sleep-tracker]]
