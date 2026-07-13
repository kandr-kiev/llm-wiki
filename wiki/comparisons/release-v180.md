---
title: "Release v1.8.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - alignment
  - api
  - async
  - benchmark
  - computer-vision
  - data
  - dataset
  - dpo
  - foundation-model
  - gpu
  - llama
  - machine-learning
  - multi-agent
  - nlp
  - open-source
  - policy
  - prompt-tuning
  - qlora
  - reinforcement-learning
  - self-supervised
  - sft
  - tool
  - training
  - use-case
---
# Release v1.8.0

> **Source:** gh-v180-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/trl/releases/tag/v1.8.0 ingested: 2026-07-11 sha256: 153e2f7691f7d9a7b1a0e579fd19130f29f74b00ed60c2f7aa222054918699d7 blog_source: github:huggingface/trl...
> **Sources:**
>   - gh-v180-2026-07-11.md
> **Links:**
- [[release-v1140]]
- [[release-notes-ollama-vv0312]]
- [[llm-fine-tuning]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[train-large-neural-networks]]

## Key Findings

---
source_url: https://github.com/huggingface/trl/releases/tag/v1.8.0
ingested: 2026-07-11
sha256: 153e2f7691f7d9a7b1a0e579fd19130f29f74b00ed60c2f7aa222054918699d7
blog_source: github:huggingface/trl
---
# Release v1.8.0
## Features
### 🎓 KTO is now a stable trainer
After many cycles of `KTOTrainer` ↔ `DPOTrainer` alignment work, KTO graduates from `trl.experimental.kto` to the top-level `trl` package. Same API as DPO/GRPO/SFT — imports move from experimental, tests move to the main test tree, docs no longer flag it as experimental. The experimental path still works and emits a `FutureWarning` (removal in v2.0.0).
```python
# Before
from trl.experimental.kto import KTOConfig, KTOTrainer
# Now
from trl import KTOConfig, KTOTrainer
```
Per our telemetry, KTO is the 4th most used trainer in TRL — this graduation was overdue.
by @albertvillanova in https://github.com/huggingface/trl/pull/6175, https://github.com/huggingface/trl/pull/6287 and https://github.com/huggingface/trl/pull/6345
### Environment-owned rewards & multi-environment support
Three interrelated changes make agentic RL training with environments substantially more ergonomic.
**Environment-owned reward.** If your `environment_factory` env defines a reserved `get_reward()` method (no args → `float`), it's called once per completed rollout and treated as a reward source. `reward_funcs` becomes optional — no more leaking env state back out to trainer-owned reward funcs.
```python
class WordleEnv:
def reset(self, **kwargs):
self._target = sample(words); self._solved = False
def get_reward(self) -> float: # optional, reserved (not a tool)
return 1.0 if self._solved else 0.0
def guess(self, word: str) -> str: # exposed as a tool
self._solved = word == self._target; ...
trainer = GRPOTrainer(
model=model,
train_dataset=dataset,
environment_factory=WordleEnv, # no reward_funcs needed
)
```
**Multi-environment support.** `environment_factory` now accepts `dict[str, factory]` in addition to a single callable. Each dataset row selects its environment via an `environment` column, and **only that env's tools are exposed in that row's prompt** — so a coding task and a game can train together in one run without leaking each other's tool schemas. Single-callable usage is unchanged.
Same wiring lands in GRPO, AsyncGRPO, DPPO, and GRPO-with-replay-buffer.
Env-owned reward by @qgallouedec in https://github.com/huggingface/trl/pull/6238; multi-env in https://github.com/huggingface/trl/pull/6001 and https://github.com/huggingface/trl/pull/6002
### Entropy regularization for GRPO
`GRPOConfig` now supports both static and adaptive entropy regularization ([Skywork-OR1](https://huggingface.co/papers/2505.22617)). The bonus encourages exploration and helps prevent premature policy collapse.
```python
GRPOConfig(
entropy_coef=0.01, # static
# or:
use_adaptive_entropy=True, # adjust to target entropy
entropy_target=1.5,
entropy_coef_delta=0.01,
entropy_coef_min=0.0,
entropy_coef_max=0.1,
)
```
Adaptive mode adju

## Summary

sts the coefficient once per optimizer step from window-aggregated entropy (gradient accumulation-aware) and persists `entropy_coef` in the checkpoint for resume. Not compatible with the Liger kernel.
by @albertvillanova in https://github.com/huggingface/trl/pull/6140
### `quantization_config` trainer argument (streamlined QLoRA)
QLoRA no longer requires reaching into `model_init_kwargs` or pre-loading the model manually.
```python
SFTTrainer(
model="meta-llama/Llama-2-7b-hf",
quantization_config=BitsAndBytesConfig(load_in_4bit=True),
peft_config=LoraConfig(),
train_dataset=dataset,
)
```
Added to `SFTTrainer`, `DPOTrainer`, `GRPOTrainer`, `RLOOTrainer`, `RewardTrainer`, and `KTOTrainer`. Sits next to `peft_config` (the other non-serializable QLoRA ingredient), flows into `from_pretrained`, and raises if also set in `args.model_init_kwargs`. Also drops the redundant `get_kbit_device_map()` line — QLoRA trains identically without it across all tested configurations.
by @qgallouedec in https://github.com/huggingface/trl/pull/6157 and https://github.com/huggingface/trl/pull/6276
### MoE aux loss extends to DPO and KTO
v1.7 added the router load-balancing auxiliary loss to `GRPOTrainer` / `RLOOTrainer` / `AsyncGRPOTrainer`. It's now on `DPOTrainer` and `KTOTrainer` too, so post-training MoE models with preference data keeps experts balanced.
by @qgallouedec in https://github.com/huggingface/trl/pull/6208 and https://github.com/huggingface/trl/pull/6275
### Neuron-friendly `chunked_nll` via static-shape token packing
The chunked NLL path had data-dependent indexing that broke XLA/Neuron compilation. This PR reworks it to pack valid tokens to the front via a stable `argsort` on the validity mask, iterate over `ceil(n_valid / chunk_size) * chunk_size` whole chunks (a tensor, no Python-int sync), and use `ignore_index=-100` inside each chunk. GPU behavior is unchanged; Neuron now works too — same tiny memory footprint (~1.33 GiB vs the naive 5.94 GiB alternative) with no per-mask recompilation.
by @michaelbenayoun in https://github.com/huggingface/trl/pull/6314
### Packing-aware dynamic batching in AsyncGRPO
AsyncGRPO micro-batching becomes packing-aware and token-bounded on top of the padding-free path from v1.7:
- **Σ Lᵢ² row balancing** — a greedy longest-first assignment gives every DP row the same Σ Lᵢ² instead of the same token count (attention is O(L²), FFN is O(L), so equal token counts don't equalize wall-clock). **Cross-rank stragglers vanish; +19% MFU at 4B in the benchmark.**
- **Token-budget packing** (opt-in) — cap each row at `token_budget` tokens with a variable sample count, decoupling peak memory from `per_device_train_batch_size`. Useful in memory-bound regimes (no gradient checkpointing, long context, very large models).
Both ride HF Trainer's existing gradient accumulation — no training-loop surgery, FSDP/EP collectives stay in lockstep.
by @AmineDiro in https://github.com/huggingface/trl/pull/6092
### VLM support in `GOLDTrainer`
`G

## Related Articles

- [[release-v1140]]
- [[release-notes-ollama-vv0312]]
- [[llm-fine-tuning]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[train-large-neural-networks]]
