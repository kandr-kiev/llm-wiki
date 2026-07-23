---
title: "Issue #6385: AsyncGRPO fork-independent epoch counting"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - batch
  - best-practice
  - data
  - dataset
  - foundation-model
  - framework
  - online
  - open-source
  - parallel
  - prompt-tuning
  - real-time
  - reinforcement-learning
  - sft
  - training
  - use-case
---

# Issue #6385: AsyncGRPO fork-independent epoch counting

> **Source:** gh-huggingfacetrl-issue-6385-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/trl/issues/6385 ingested: 2026-07-14 sha256: 0366e0e0977dd5f3eeb4fda325ddc6ea248cd995a0c758996b7e3dbf48b074b5 blog_source: github:huggingface/trl --- # I...
> **Sources:**
>   - gh-huggingfacetrl-issue-6385-2026-07-14.md
> **Links:**
- [[Release 5.0.0]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [Issue #2197: perf: reduce BPE tokenizer load-time memory]
- [[Release v1.8.0]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]

## Key Findings

---
source_url: https://github.com/huggingface/trl/issues/6385
ingested: 2026-07-14
sha256: 0366e0e0977dd5f3eeb4fda325ddc6ea248cd995a0c758996b7e3dbf48b074b5
blog_source: github:huggingface/trl
---
# Issue #6385: AsyncGRPO fork-independent epoch counting
**State:** open | **Author:** AmineDiro | **Created:** 2026-07-14T08:02:35Z
Under `num_train_epochs`, AsyncGRPO stops after only `~E/F` of the `E` requested epochs and `F` avg number of time we fork a message. The cause is **packing and forking**: message-mode forks make an epoch emit a variable `D*G*F` rows (`F` = rows per conversation, known only at runtime), and the trainer packs those rows into fixed-size steps, so the step count `= D*G*F/S` scales with `F`. So `max_steps` ends up undershooting the number of steps to pass through the data.
Some framework like `slime` packs one full rollout into one step (so variable batch size), so forks change batch width, not step count. This PR moves termination off `max_steps` and onto a fork-independent count of distinct prompts trained.
## What changed
Epochs are now counted in **distinct prompts trained**, not queue samples, so `num_train_epochs=N` always trains on N full passes over the prompt dataset regardless of how many rows message-mode forks produce.
Files:
- `async_rollout_worker.py`: add a `group_id` field to `RolloutGroup` + `RolloutSample`. The worker already assigns one id per prompt in `_repeat_iterator` (monotonic across the whole run, so unique per prompt even after the dataset cycles); we just thread it onto the emitted sample. All `G` generations of a prompt and all forked rows of a conversation share this id.
- `async_grpo_trainer.py`:
- `RolloutQueueDataset` carries `group_id` through the queue dict.
- `DataCollatorForRollout` gains a `groups_trained: set[int]` shared with the trainer and adds each batch's ids to it.
- `_EpochStopCallback`: on `on_step_end`, sets `should_training_stop` once the target is reached.
- `__init__`: replace the old `max_steps = num_train_epochs * D*G / S` formula with a target of `ceil(num_train_epochs * D)` groups, and set `max_steps` to a generous safety ceiling.
- `async_grpo_config.py`: `lr_scheduler_type` now defaults to `constant`, plus docs on how `num_train_epochs` / `max_steps` / `lr_scheduler_type` interact under forks.
## Choices and why
**Count in the collator, not the queue.** The token-budget batcher can drop oversized samples before they reach
the model. The collator runs on the main process right before the forward, so it sees exactly the prompts that get
trained. Counting anywhere upstream would overcount rows that never train.
**Reduce the stop decision across ranks.** Only the main process collates (`dispatch_batches=True`), so it alone
sees `_trained_groups`. The callback broadcasts "reached target?" with an all-reduce (sum) so every data-parallel
rank stops on the same step and stays in lockstep.
**Default to constant LR + drop the steps-per-group heuristic.** The LR-decay horizon is me

## Summary

asured in optimizer
steps, and the true step count `= N*D*G*F/S` is unknown at `__init__`. Rather than rebuild the scheduler online from an observed steps-per-group ratio, we default to `constant` (matching slime's RL practice). This makes `max_steps` a pure safety ceiling whose exact value is irrelevant. **Users who want decay set a decaying schedule together with an explicit `max_steps`.**
**`max_steps` stays a generous over-estimate.** When epoch-driven, it must never pre-empt the callback, so we size it
with a worst-case `max_rows_per_conv` (`max_tool_calling_iterations + 1`, else 32). Setting `max_steps` explicitly
(`> 0`) disables the epoch callback entirely and hands termination back to the step count (slime's SFT path).
## Empirical validation
- Validated end-to-end on H100s (Qwen3-0.6B, gsm8k). A forced-fork sweep (stub worker, only the fork rate K varies) gave K=1/3/6 → 31/94/189 optimizer steps but **2.000 / 2.000 / 2.000 epochs**.
- Epoch target scales linearly with `num_train_epochs` (2 epochs → 64 groups, 3 → 96), and an explicit `max_steps` correctly disables the callback. 
- Also confirmed the `max_steps` safety ceiling never pre-empts the callback (forks per conversation are bounded by turns ≤ `max_tool_calling_iterations + 1`, exactly the assumed `max_rows_per_conv`). 
Note: with a large `token_budget` the epoch stop is coarse (checked per step, each step spanning many groups) so it can overshoot by up to one step's worth of groups (e.g. 2.19 epochs); smaller `token_budget` / `FixedCountBatcher` gives near-exact epochs.
| scenario | batcher / stop | fork setting | steps | epochs @ stop | stop reason |
| ---------------- | ---------------------- | ------------------- | ----- | ------------- | -------------- |
| A_fixed_single | FixedCount, epochs=2 | no forks (F=1) | 31 | 2.000 | epoch-callback |
| C_budget_fork | TokenBudget32768, ep=2 | model (F≈1) | 8 | 2.19 (coarse) | epoch-callback |
| G_nofork | FixedCount, epochs=2 | threshold=∞ (F=1) | 31 | 2.000 | epoch-callback |
| H_maxfork | FixedCount, epochs=2 | threshold=1 (F≈1*) | 31 | 2.000 | epoch-callback |
| D_maxsteps | TokenBudget, max_steps=15 | n/a | 15 | 3.81 (untracked) | max_steps |
| K1_fork1 (stub) | FixedCount, epochs=2 | forced F=1 | 31 | 2.000 | epoch-callback |
| K3_fork3 (stub) | FixedCount, epochs=2 | forced F=3 | 94 | 2.000 | epoch-callback |
| K6_fork6 (stub) | FixedCount, epochs=2 | forced F=6 | 189 | 2.000 | epoch-callback |
| E_epochs3 | TokenBudget32768, ep=3 | model | 12 | 3.125 (target 96) | epoch-callback |
| F_small_budget | TokenBudget4096, ep=2 | model | 47 | 2.031 (finer) | epoch-callback |
| EP1/EP2/EP3 (stub) | FixedCount, ep=1/2/3 | forced K=3 | 46/94/142 | 1.000/2.000/3.000 | epoch-callback |
| fulltrain | TokenBudget4096, ep=1, N=128 | model | 96 | 1.000 (128/128) | epoch-callback |
---
> [!NOTE]
> **Medium Risk**
> Changes when training ends and default LR scheduling for epoch-driven runs; behavior is well-tested but misconfigured `max_steps` 

## Related Articles

- [[Release 5.0.0]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [Issue #2197: perf: reduce BPE tokenizer load-time memory]
- [[Release v1.8.0]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
