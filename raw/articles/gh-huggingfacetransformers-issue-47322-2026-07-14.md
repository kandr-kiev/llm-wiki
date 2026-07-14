---
source_url: https://github.com/huggingface/transformers/issues/47322
ingested: 2026-07-14
sha256: d00f3231a1a226c17bc4cd4b247ba3a2d27d36b801e2f0ce844f9caf18489495
blog_source: github:huggingface/transformers
---
# Issue #47322: adding amd quark config class changes

**State:** open | **Author:** debasisdwivedy | **Created:** 2026-07-14T15:32:07Z

<!-- ci-dashboard-badge:start -->
[![CI](https://transformers-ci.lor-e.huggingface.cool/badge/pr?pr=47322)](https://transformers-ci.lor-e.huggingface.cool/d/pytest-observability-by-pr/pytest-observability-branch?var-pr=47322)
<!-- ci-dashboard-badge:end -->

# What does this PR do?



Fixes #47321

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
- [] This PR fixes a typo or improves the docs (you can dismiss the other checks if that's the case).
- [X] Did you read the [contributor guideline](https://huggingface.co/docs/transformers/contributing) and the
      [Pull Request](https://huggingface.co/docs/transformers/pr_checks) checks?
- [ ] Was this discussed/approved via a Github issue or the [forum](https://discuss.huggingface.co/)? Please add a link
      to it if that's the case.
- [ ] Did you make sure to update the documentation with your changes according to the [guidelines](https://github.com/huggingface/transformers/tree/main/docs)?
- [ ] Did you write any new necessary [tests](https://huggingface.co/docs/transformers/testing)?


## Who can review?

Anyone in the community is free to review the PR once the tests have passed. Feel free to tag
members/contributors who may be interested in your PR.

<!-- Your PR will be replied to more quickly if you can figure out the right person to tag with @

 If you know how to use git blame, that is the easiest way, otherwise, here is a rough guide of **who to tag**.
 Please tag fewer than 3 people.

Models:

- text models: @ArthurZucker @Cyrilvallez @vasqu
- vision models: @yonigozlan @molbap
- audio models: @eustlb @ebezzam @vasqu
- multimodal models: @zucchini-nlp
- graph models: @clefourrier

Library:

- generate: @zucchini-nlp (visual-language models) or @Cyrilvallez (all others)
- continuous batching: @remi-or @ArthurZucker @McPatate
- pipelines: @Rocketknight1
- tokenizers: @ArthurZucker and @itazap
- trainer: @SunMarc
- attention: @vasqu @ArthurZucker @CyrilVallez
- model loading (from pretrained, etc): @CyrilVallez
- distributed: @3outeille @ArthurZucker
- CIs: @ydshieh

Integrations:

- ray/raytune: @richardliaw, @amogkam
- Big Model Inference: @SunMarc
- quantization: @SunMarc
- kernels: @vasqu @drbh
- peft: @BenjaminBossan @githubnemo

Devices/Backends:

- AMD ROCm: @ivarflakstad
- Intel XPU: @IlyasMoutawwakil
- Ascend NPU: @ivarflakstad 

Documentation: @stevhliu

Research projects are not maintained and should be taken as is.

 -->