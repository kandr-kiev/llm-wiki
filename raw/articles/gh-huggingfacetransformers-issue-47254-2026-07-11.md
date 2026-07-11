---
source_url: https://github.com/huggingface/transformers/issues/47254
ingested: 2026-07-11
sha256: dcf5747340c1bd6734fdfad5431d10db7b4c62590cdaf0fd75989a6bdb91ff24
blog_source: github:huggingface/transformers
---
# Issue #47254: `CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing

**State:** open | **Author:** qgallouedec | **Created:** 2026-07-10T20:09:31Z

### System Info


- Platform: Linux-5.15.0-1048-aws-x86_64-with-glibc2.31
- Python version: 3.13.13
- PyTorch version: 2.11.0+cu128
- Transformers version: 5.13.0.dev0
- Accelerate version: 1.15.0.dev0
- DeepSpeed version: 0.19.2
- PEFT version: 0.19.1
- GPUs: 2x NVIDIA H100 80GB


### Who can help?

@SunMarc 

### Information

- [ ] The official example scripts
- [ ] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [ ] My own task or dataset (give details below)

### Reproduction

Training a PEFT (LoRA) model with `gradient_checkpointing=True` under DeepSpeed ZeRO-3 (≥2 processes) crashes in the backward pass with:

```
torch.utils.checkpoint.CheckpointError: Recomputed values for the following tensors
have different metadata than during the forward pass.
tensor at position 4: saved {'shape': [1024]} vs recomputed {'shape': [0]}
```

The `[0]`-shaped tensors are **frozen** parameters (RMSNorm weights: `hidden_size` and the per-head q/k norm `head_dim`). ZeRO-3 all-gathers them during the forward, but they are back in the partitioned state (empty) during the checkpoint recompute, so non-reentrant (now default) checkpointing's metadata check rejects them.

This is **not** specific to TRL / bitsandbytes / DoRA / VLMs: The original report (huggingface/trl#5217) used all of those, but the MRE below reproduces with none of them: plain `transformers.Trainer` + PEFT + ZeRO-3 + gradient checkpointing.

## Reproduction

`mre.py`

```python
from datasets import Dataset
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, Trainer, TrainingArguments

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B")
model = get_peft_model(model, LoraConfig())

dataset = Dataset.from_dict({"input_ids": [[1, 2, 3, 4]], "labels": [[1, 2, 3, 4]]})

trainer = Trainer(model, TrainingArguments(gradient_checkpointing=True), train_dataset=dataset)
trainer.train()
```

`ds_z3.yaml`

```yaml
distributed_type: DEEPSPEED
num_processes: 2
deepspeed_config:
  zero_stage: 3
```

```bash
accelerate launch --config_file ds_z3.yaml mre.py
```


## Workaround

Set `use_reentrant=True` for gradient checkpointing:

```python
TrainingArguments(gradient_checkpointing=True,
                  gradient_checkpointing_kwargs={"use_reentrant": True})
```

but it's old, and not recommended. in other words, not a good solution, because `use_reentrant=False` is the modern config for checkpointing.

## Full traceback

```
File ".../torch/utils/checkpoint.py", line 1177, in unpack_hook
    frame.check_recomputed_tensors_match(gid)
File ".../torch/utils/checkpoint.py", line 921, in check_recomputed_tensors_match
    raise CheckpointError(
torch.utils.checkpoint.CheckpointError: torch.utils.checkpoint: Recomputed values for
the following tensors have different metadata than during the forward pass.
tensor at position 4:
saved metadata:      {'shape': torch.Size([1024]), 'dtype': torch.bfloat16, 'device': cuda:0}
recomputed metadata: {'shape': torch.Size([0]),    'dtype': torch.bfloat16, 'device': cuda:0}
tensor at position 14:
saved metadata:      {'shape': torch.Size([128]),  'dtype': torch.bfloat16, 'device': cuda:0}
recomputed metadata: {'shape': torch.Size([0]),    'dtype': torch.bfloat16, 'device': cuda:0}
...
```

Related: huggingface/transformers#34928, huggingface/trl#5217, huggingface/trl#2514


### Expected behavior

To work