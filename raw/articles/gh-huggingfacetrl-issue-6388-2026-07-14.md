---
source_url: https://github.com/huggingface/trl/issues/6388
ingested: 2026-07-14
sha256: 198a4e683ef70ed7009bae975cf8767837024679b5648870ab07e679c4081dac
blog_source: github:huggingface/trl
---
# Issue #6388: [GOLD] Recommend LFM2.5 and Gemma 4 students

**State:** open | **Author:** kashif | **Created:** 2026-07-14T10:28:50Z

Updates the GOLD example to recommend LFM2.5-1.2B and Gemma 4 E4B students with a Qwen3-4B teacher. It uses the same Formal Logic dataset as the NeMo RL x-token recipe and converts its raw text into prompt/completion pairs.

This also enables positional ULD for SentencePiece tokenizers and fixes an MPS logging issue found during local testing.

Smoke tested one training step on an M5 Max:

- LFM2.5-1.2B → loss 0.3359
- Gemma 4 E4B with LoRA → loss 0.4245

The focused GOLD tests pass (`4 passed`).
