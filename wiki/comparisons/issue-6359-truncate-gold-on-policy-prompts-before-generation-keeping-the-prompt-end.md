---
title: "Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - foundation-model
  - nlp
  - open-source
  - policy
  - prompt-tuning
  - real-time
  - self-supervised
  - system-design
  - training
  - use-case
---
# Issue #6359: Truncate GOLD on-policy prompts before generation, keeping the prompt end

> **Source:** gh-huggingfacetrl-issue-6359-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/trl/issues/6359 ingested: 2026-07-11 sha256: efe5107b445f1e281ee21c00b6f3a0e61769037cf6998f2e23473b9008dec3ee blog_source: github:huggingface/trl --- # I...
> **Sources:**
>   - gh-huggingfacetrl-issue-6359-2026-07-11.md
> **Links:**
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[animals-vs-ghosts]]
- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]

## Key Findings

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
prompt_ids = tok(text, return_tensors="pt")["input_ids"] # ends with the assistant marker
class RecordingVLLM:
prompts = None
def sync_weights(self): pass
def generate(self, prompts, images, num_generations):
self.prompts = prompts # what the model actually generates from
return None, [[arxiv260702542]], None, None
trainer = GOLDTrainer.__new__(GOLDTrainer)
trainer.accelerator = SimpleNamespace(device=torch.device("cpu"), is_main_process=True)
trainer.processing_class = tok
trainer.args = SimpleNamespace(max_length=10, report_to=[]) # budget = 10 - 4 = 6
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
print("trained on :", repr(trained_on))
print("same prompt for generation and training:", generated_on == trained_on)
print("training prompt keeps the assistant marker:", "assistant" in trained_on)
```
On `main`:
```
generated on: 'system\nYou are a helpful AI assistant named SmolLM, trained by Hugging Face\nuser\nWhat is 2 + 2? Answer with one number only.\nassistant\n'
trained on : 'system\nYou are a'
same prompt 

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[animals-vs-ghosts]]
- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]
