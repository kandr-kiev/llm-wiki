---
source_url: https://github.com/huggingface/peft/issues/3420
ingested: 2026-07-11
sha256: a2167feccbd9c460dc70f0d9a8b3d649848bc462fd2c7b0a4bbb570fdc3e7f33
blog_source: github:huggingface/peft
---
# Issue #3420: Fix hotswapping for LoRA adapters targeting grouped Conv2d

**State:** open | **Author:** jayzuccarelli | **Created:** 2026-07-11T02:34:27Z

Fixes #3416

`prepare_model_for_compiled_hotswap` raises a shape mismatch for LoRA adapters that target a grouped `Conv2d`. For these layers, LoRA B is itself a grouped conv, so its weight stores `rank // groups` input channels, but `_get_padded_conv2d` treated that dimension as the full rank.

This PR:

- computes LoRA B's original rank as `in_channels * groups` and sizes its padded weight with `target_rank // groups` input channels
- lays out each group's LoRA A output channels at the start of that group's slice of the padded weight, so the grouped LoRA B multiplies the padding zeros with the right channels and the model output is unchanged
- rejects a target rank that is not divisible by the layer's groups

While testing the full flow, I found the same layout problem in `hotswap_adapter_from_state_dict`: when the incoming adapter has a smaller rank than the loaded (or padded) one, the contiguous copy of LoRA A silently produces wrong outputs for grouped convs (max abs diff vs. the adapter loaded directly was ~1.8 in my repro; this also reproduces on main without calling `prepare_model_for_compiled_hotswap`). The copy is now done per group block; with `groups == 1` it reduces to the previous single contiguous copy.

Tests run (CPU):

- new `test_prepare_model_for_compiled_hotswap_does_not_change_output_grouped_conv2d`: padding a grouped conv adapter preserves the output; without the fix it fails with the `ValueError` from the issue
- new `test_hotswap_works_different_ranks_grouped_conv2d`: pad to a larger target rank, hotswap in a smaller-rank adapter, output must match that adapter loaded directly; without the swap-path fix it fails (wrong output, no error)
- new `test_prepare_model_for_compiled_hotswap_grouped_conv2d_indivisible_target_rank_raises` for the new guard
- `pytest tests/test_initialization.py -k TestHotSwapping`: 35 passed
- `ruff check` and `ruff format --check` pass on the touched files

Coordination: reported in #3416, @BenjaminBossan gave the go-ahead in https://github.com/huggingface/peft/issues/3416#issuecomment-4934017022.

AI assistance was used for this PR (Claude Code). The change was reviewed and the tests were run before submitting.
