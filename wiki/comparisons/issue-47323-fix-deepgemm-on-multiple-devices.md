---
title: "Issue #47323: Fix deepgemm on multiple devices"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - audio-generation
  - best-practice
  - ci-cd
  - closed-source
  - computer-vision
  - distributed
  - foundation-model
  - guide
  - library
  - llm
  - multimodal
  - nlp
  - open-source
  - policy
  - quantization
  - real-time
  - research
  - review
  - use-case
---

# Issue #47323: Fix deepgemm on multiple devices

> **Source:** gh-huggingfacetransformers-issue-47323-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/issues/47323 ingested: 2026-07-14 sha256: a5da383ffe3c1712a92c845d2ad994ef92c3ed9f8bd6b01cc3b59994dd3d9b99 blog_source: github:huggingface/t...
> **Sources:**
>   - gh-huggingfacetransformers-issue-47323-2026-07-14.md
> **Links:**
- [[Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]]
- [[Issue #47322: adding amd quark config class changes]]
- [[Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]]
- [[Issue #14185: ask to share self-review notes]]
- [[Issue #2848: Implement multi-domain intake architecture and related specs]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/issues/47323
ingested: 2026-07-14
sha256: a5da383ffe3c1712a92c845d2ad994ef92c3ed9f8bd6b01cc3b59994dd3d9b99
blog_source: github:huggingface/transformers
---
# Issue #47323: Fix deepgemm on multiple devices
**State:** open | **Author:** IlyasMoutawwakil | **Created:** 2026-07-14T15:35:31Z
[![CI](https://transformers-ci.lor-e.huggingface.cool/badge/pr?pr=47323)](https://transformers-ci.lor-e.huggingface.cool/d/pytest-observability-by-pr/pytest-observability-branch?var-pr=47323)
# What does this PR do?
Fixes # (issue)
## Code Agent Policy
The Transformers repo is currently being overwhelmed by a large number of PRs and issue comments written by
code agents. These often are low-quality, or fix extremely minor issues that occur rarely or never in practice.
As a result, we're instituting a rule that **first-time contributors should not use code agents to submit PRs or issues**.
We'd also ask autonomous "OpenClaw"-like agents not to open any PRs or issues.
Issues/PRs from first-time contributors that violate this rule will probably just be closed without review, and we
might block you, especially if you open more than one or appear to be deliberately ignoring this. We especially do not
want new contributors to jump in on random issues to contribute an agent-written fix. This creates lots of noise
for reviewers and other users and will almost certainly get you blocked.
For more information, please read [`CONTRIBUTING.md`](https://github.com/huggingface/transformers/blob/main/CONTRIBUTING.md).
- [ ] (First-time contributors only): I confirm that this PR description and code is not written by an LLM or code agent
## Before submitting
- [ ] This PR fixes a typo or improves the docs (you can dismiss the other checks if that's the case).
- [ ] Did you read the [contributor guideline](https://huggingface.co/docs/transformers/contributing) and the
[Pull Request](https://huggingface.co/docs/transformers/pr_checks) checks?
- [ ] Was this discussed/approved via a Github issue or the [forum](https://discuss.huggingface.co/)? Please add a link
to it if that's the case.
- [ ] Did you make sure to update the documentation with your changes according to the [guidelines](https://github.com/huggingface/transformers/tree/main/docs)?
- [ ] Did you write any new necessary [tests](https://huggingface.co/docs/transformers/testing)?
## Who can review?
Anyone in the community is free to review the PR once the tests have passed. Feel free to tag
members/contributors who may be interested in your PR.

## Summary

See Key Findings for full content.

## Related Articles

- [[Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]]
- [[Issue #47322: adding amd quark config class changes]]
- [[Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example]]
- [[Issue #14185: ask to share self-review notes]]
- [[Issue #2848: Implement multi-domain intake architecture and related specs]]
