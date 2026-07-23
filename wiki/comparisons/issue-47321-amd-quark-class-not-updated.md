---
title: "Issue #47321: AMD quark class not updated"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - cuda
  - dataset
  - distributed
  - foundation-model
  - gpu
  - open-source
  - parallel
  - pipeline
  - pytorch
  - quantization
  - system-design
---

# Issue #47321: AMD quark class not updated

> **Source:** gh-huggingfacetransformers-issue-47321-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/issues/47321 ingested: 2026-07-14 sha256: 0d89ff82da6c4a70231de917787d1926ca3f12e2c3cd3f7e987fe7bf07998aeb blog_source: github:huggingface/t...
> **Sources:**
>   - gh-huggingfacetransformers-issue-47321-2026-07-14.md
> **Links:**
- [Issue #47254: `CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing]
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`]
- [Issue #8330: Dataset Studio and Viewer down]
- [[Release 5.0.0]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/issues/47321
ingested: 2026-07-14
sha256: 0d89ff82da6c4a70231de917787d1926ca3f12e2c3cd3f7e987fe7bf07998aeb
blog_source: github:huggingface/transformers
---
# Issue #47321: AMD quark class not updated
**State:** open | **Author:** debasisdwivedy | **Created:** 2026-07-14T15:29:30Z
### System Info
- `transformers` version: 5.13.1
- Platform: Linux-6.8.0-1058-gcp-x86_64-with-glibc2.39
- Python version: 3.13.13
- Huggingface_hub version: 1.23.0
- Safetensors version: 0.8.0
- Accelerate version: 1.14.0
- Accelerate config: not found
- DeepSpeed version: not installed
- PyTorch version (accelerator?): 2.12.1+cu130 (CUDA)
- Using distributed or parallel set-up in script?: 
- Using GPU in script?: 
- GPU type: Tesla T4
### Who can help?
Hi ,
The quantization config for AMD class points to an older release and needs to be updated.
File : `src/transformers/utils/quantization_config.py`
Previous versions of Quark had the config as `from quark.torch.quantization.config.config import Config`, which has been changed to `from quark.torch.quantization.config.config import QConfig`
Regards
### Information
- [x] The official example scripts
- [x] My own modified scripts
### Tasks
- [x] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [ ] My own task or dataset (give details below)
### Reproduction
def main():
evaluation_tracker = EvaluationTracker(
output_dir="./results",
save_details=True
)
pipeline_params = PipelineParameters(
launcher_type=ParallelismManager.ACCELERATE,
custom_tasks_directory=None, # Set to path if using custom tasks
# Remove the parameter below once your configuration is tested
# max_samples=10
)
model_config = TransformersModelConfig(
model_name="", #Quark quantized folder path
device="cuda"
)
task = ""
pipeline = Pipeline(
tasks=task,
pipeline_parameters=pipeline_params,
evaluation_tracker=evaluation_tracker,
model_config=model_config,
)
pipeline.evaluate()
pipeline.save_and_push_results()
pipeline.show_results()
### Expected behavior
Should load the quantized model, but we get error: "Unable to Import from quark.torch.quantization.config.config import Config"

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #47254: `CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing]
- [Issue #14166: Fix Hub download filtering for FlashPack pipelines]
- [Issue #6358: Add `trl.environments` submodule with `SandboxEnvironment`]
- [Issue #8330: Dataset Studio and Viewer down]
- [[Release 5.0.0]]
