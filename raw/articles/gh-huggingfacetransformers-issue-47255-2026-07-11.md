---
source_url: https://github.com/huggingface/transformers/issues/47255
ingested: 2026-07-11
sha256: 2f4399d06f6629738f2be5e9b0ad357d34a9ddbc91c2dc9b532441a5e2d179b9
blog_source: github:huggingface/transformers
---
# Issue #47255: Point to Gemma 4 model in Gemma4ForCausalLM docstring example

**State:** open | **Author:** lefft | **Created:** 2026-07-10T21:40:09Z

<!-- ci-dashboard-badge:start -->
[![CI](https://transformers-ci.lor-e.huggingface.cool/badge/pr?pr=47255)](https://transformers-ci.lor-e.huggingface.cool/d/pytest-observability-by-pr/pytest-observability-branch?var-pr=47255)
<!-- ci-dashboard-badge:end -->


# What does this PR do?

Point to a Gemma 4 model in Gemma4ForCausalLM docstring instead of a Gemma 2 model. 

## Code Agent Policy

- [x] (First-time contributors only): I confirm that this PR description and code is not written by an LLM or code agent

## Before submitting
- [x] This PR fixes a typo or improves the docs (you can dismiss the other checks if that's the case).
- [x] Did you read the [contributor guideline](https://huggingface.co/docs/transformers/contributing) and the
      [Pull Request](https://huggingface.co/docs/transformers/pr_checks) checks?
- [N/A] Was this discussed/approved via a Github issue or the [forum](https://discuss.huggingface.co/)? Please add a link
      to it if that's the case.
- [N/A] Did you make sure to update the documentation with your changes according to the [guidelines](https://github.com/huggingface/transformers/tree/main/docs)?
- [N/A] Did you write any new necessary [tests](https://huggingface.co/docs/transformers/testing)?


## Who can review?

@stevhliu for documentation, @ArthurZucker for text models (since this is the 4CausalLM class) 
