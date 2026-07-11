---
source_url: https://github.com/huggingface/trl/issues/6359
ingested: 2026-07-11
sha256: efe5107b445f1e281ee21c00b6f3a0e61769037cf6998f2e23473b9008dec3ee
blog_source: github:huggingface/trl
---
# Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end

**State:** open | **Author:** roycho96 | **Created:** 2026-07-11T09:36:19Z

# What does this PR do?

GOLD generates on-policy completions from the full prompt, but then cuts the prompt from the **start** before saving the training example. So the model generates from one prompt and the student is trained on a different one.

When `max_length` is set and the prompt is longer than `max_length - max_new_tokens`, the part that is kept is the beginning of the prompt, which drops the actual question and the assistant marker at the end.

## Repro

vLLM is faked here since the cut happens in trl, not in vLLM.

```python
from types import SimpleNamespace
import torch
from transformers import AutoTokenizer
from trl.experimental.gold.gold_trainer import GOLDTrainer

tok = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-360M-Instruct")
text = tok.apply_chat_template(
    [{"role": "user", "content": "What is 2 + 2? Answer with one number only."}],
    tokenize=False, add_generation_prompt=True,
)
prompt_ids = tok(text, return_tensors="pt")["input_ids"]  # ends with the assistant marker

class RecordingVLLM:
    prompts = None
    def sync_weights(self): pass
    def generate(self, prompts, images, num_generations):
        self.prompts = prompts  # what the model actually generates from
        return None, [[42]], None, None

trainer = GOLDTrainer.__new__(GOLDTrainer)
trainer.accelerator = SimpleNamespace(device=torch.device("cpu"), is_main_process=True)
trainer.processing_class = tok
trainer.args = SimpleNamespace(max_length=10, report_to=[])  # budget = 10 - 4 = 6
trainer.use_vllm = True
trainer.use_uld_loss = False
trainer.teacher_tokenizer = None
trainer.uld_loss_fn = None
trainer.vllm_generation = RecordingVLLM()
trainer.vllm_sync_frequency = 1
trainer._last_vllm_sync_step = -1
trainer.state = SimpleNamespace(global_step=0)
trainer.num_generations = 1
trainer.generation_config = SimpleNamespace(max_new_tokens=4)
trainer._buffered_inputs = [None]
trainer._buffered_text_logs = [None]

slices = [{"prompts": prompt_ids, "prompt_attention_mask": torch.ones_like(prompt_ids)}]
GOLDTrainer._generate_on_policy_for_slices(trainer, slices, [0])

generated_on = tok.decode(trainer.vllm_generation.prompts[0])
trained_on = trainer._buffered_inputs[0]["original_prompt_text"][0]
print("generated on:", repr(generated_on))
print("trained on  :", repr(trained_on))
print("same prompt for generation and training:", generated_on == trained_on)
print("training prompt keeps the assistant marker:", "assistant" in trained_on)
```

On `main`:

```
generated on: '<|im_start|>system\nYou are a helpful AI assistant named SmolLM, trained by Hugging Face<|im_end|>\n<|im_start|>user\nWhat is 2 + 2? Answer with one number only.<|im_end|>\n<|im_start|>assistant\n'
trained on  : '<|im_start|>system\nYou are a'
same prompt for generation and training: False
training prompt keeps the assistant marker: False
```

The model sees the real question, but the student is trained on just the first 6 tokens of the system prompt, with no question and no marker.

With this PR:

```
generated on: '<|im_end|>\n<|im_start|>assistant\n'
trained on  : '<|im_end|>\n<|im_start|>assistant\n'
same prompt for generation and training: True
training prompt keeps the assistant marker: True
```

## Fix

Cut the prompt to `max_length - max_new_tokens` before generation, keeping the **end** (where the assistant marker is), in both the vLLM and non-vLLM paths. This way the model generates from and is trained on the same prompt. The old cut in `_process_completions_to_buffer` is removed, and the shortened `prompts` / `prompt_attention_mask` are written back so the padding width stays right.

## Before submitting

- [x] Did you read the [contributor guideline](https://github.com/huggingface/trl/blob/main/CONTRIBUTING.md#create-a-pull-request), Pull Request section?
- [x] Did you write any new necessary tests?

## AI writing disclosure

- [x] AI-assisted: some parts were suggested or improved by AI, but the PR was written and reviewed by a human.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Changes on-policy training inputs when `max_length` is set (correctness fix with behavior change for long prompts), but scope is limited to GOLD generation/buffering rather than auth or core infra.
> 
> **Overview**
> Fixes a **train/generate mismatch** in GOLD on-policy rollouts when `max_length` is set: the student used to generate from the full prompt but training examples were built from a **start-truncated** prompt, often dropping the user question and assistant marker.
> 
> **Before generation**, prompts are now capped to `max_length - max_new_tokens` using **keep-end** truncation (real tokens from `prompt_attention_mask`), on both the **vLLM** and **non-vLLM** paths. The post-buffer truncation in `_process_completions_to_buffer` (including `truncation_side`) is removed; buffered `original_prompt_text` matches what vLLM/`model.generate` saw.
> 
> The non-vLLM path only rebuilds left-padded `prompts` / masks when a row actually overflows the budget (so left-padded rows that already fit are not wrongly trimmed). After vLLM completion processing, **`prompts` and `prompt_attention_mask` are written back** so `prompt_length` stays aligned with the budgeted tensors.
> 
> Tests cover vLLM keep-end budgeting, non-vLLM parity, and the “fits budget with padding” case.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit d7ff3184212d3d448c8c1ea877f754d53a29b607. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->