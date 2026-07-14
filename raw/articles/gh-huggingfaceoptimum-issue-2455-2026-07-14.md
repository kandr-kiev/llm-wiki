---
source_url: https://github.com/huggingface/optimum/issues/2455
ingested: 2026-07-14
sha256: 0412321f5ec85cf91d1448a25181d531d68e2eb713a087df84e6b37eeb7db073
blog_source: github:huggingface/optimum
---
# Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning

**State:** open | **Author:** vigneshkumar25 | **Created:** 2026-07-01T13:49:40Z

- Relax transformers upper bound to <6.0 to unblock v5 users
- Add weights_only=True to torch.load to fix CVE security warning

Fixes #2432

# What does this PR do?

<!--
Congratulations! You've made it this far! You're not quite done yet though.

Once merged, your PR is going to appear in the release notes with the title you set, so make sure it's a great title that fully reflects the extent of your awesome contribution.

Then, please replace this with a description of the change and which issue is fixed (if applicable). Please also include relevant motivation and context. List any dependencies (if any) that are required for this change.

Once you're done, someone will review your PR shortly (see the section "Who can review?" below to tag some potential reviewers). They may suggest changes to make the code even better. If no one reviewed your PR after a week has passed, don't hesitate to post a new comment @-mentioning the same persons---sometimes notifications get lost.
-->

<!-- Remove if not applicable -->

Fixes # (issue)


## Before submitting
- [ ] This PR fixes a typo or improves the docs (you can dismiss the other checks if that's the case).
- [ ] Did you make sure to update the documentation with your changes?
- [ ] Did you write any new necessary tests?

## Who can review?

<!--
For faster review, we strongly recommend you to ping the following people:
- Exporters (ONNX/OpenVINO) : @echarlaix, @JingyaHuang, @michaelbenayoun, @IlyasMoutawwakil
- GPTQ, quantization: @SunMarc, @IlyasMoutawwakil
-->
