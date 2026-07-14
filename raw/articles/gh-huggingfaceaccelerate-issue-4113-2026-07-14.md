---
source_url: https://github.com/huggingface/accelerate/issues/4113
ingested: 2026-07-14
sha256: 43bf96ae02803a3942f6ec4ee1ae72ae59f7df92372676adbb1ca20430b039de
blog_source: github:huggingface/accelerate
---
# Issue #4113: Fix typos in comments, docs, and examples

**State:** open | **Author:** maxtaran2010 | **Created:** 2026-07-09T20:58:19Z

Fix several spelling mistakes found across comments, documentation, and example files:

- `ore` -> `more` in CONTRIBUTING.md
- `indention` -> `indentation` in docs/README.md
- `relevent` -> `relevant` in three example files
- `perfrom` -> `perform` in automatic_gradient_accumulation.py
- `reproducable` -> `reproducible` in automatic_gradient_accumulation.py and three pippy inference examples
- `unecessary` -> `unnecessary` in gradient_accumulation_for_autoregressive_models.py
- `mannually` -> `manually` in megatron_lm_gpt_pretraining.py
- `inspite` -> `in spite` in megatron_lm_gpt_pretraining.py
- `annoted` -> `annotated` in examples/config_yaml_templates/README.md
- `parallism` -> `parallelism` in examples/inference/pippy/README.md
- `prioritzes` -> `prioritizes` in nd_parallel.py
- `undesireable` -> `undesirable` in manim_animations/dataloaders/stage_2.py

Found with `codespell`.