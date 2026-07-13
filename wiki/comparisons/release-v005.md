---
title: "Release v0.0.5"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - best-practice
  - computer-vision
  - evaluation
  - few-shot
  - fine-tuning
  - foundation-model
  - llama
  - llm
  - multi-agent
  - nlp
  - open-source
  - policy
  - rag
  - tool
  - training
  - tutorial
  - use-case
---
# Release v0.0.5

> **Source:** gh-v005-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/facebookresearch/llama-recipes/releases/tag/v0.0.5 ingested: 2026-07-11 sha256: 2e1f0437e30531790fbe0e822cb4de265edabf2348e1b97b24508866db29145d blog_source: github:...
> **Sources:**
>   - gh-v005-2026-07-11.md
> **Links:**
- [[release-notes-ollama-vv0312]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]
- [[release-notes-langchain-vlangchain-openai135]]
- [[release-notes-llamacpp-vb9956]]

## Key Findings

---
source_url: https://github.com/facebookresearch/llama-recipes/releases/tag/v0.0.5
ingested: 2026-07-11
sha256: 2e1f0437e30531790fbe0e822cb4de265edabf2348e1b97b24508866db29145d
blog_source: github:facebookresearch/llama-recipes
---
# Release v0.0.5
## Llama-cookbook v0.0.5 Release Notes
This release changes the package name from `llama_recipes` to `llama_cookbook` and deprecates the `llama_recipes` package name.
## Highlighted Changes
---
- Name: `llama_cookbook` and `pip install llama-cookbook`
- Update instructions https://github.com/meta-llama/llama-cookbook/pull/852
- Update src package https://github.com/meta-llama/llama-cookbook/pull/861, https://github.com/meta-llama/llama-cookbook/pull/848
## What's Changed
* Improve discoverability of 3.2 recipes by @subramen in https://github.com/meta-llama/llama-cookbook/pull/684
* fix readme by @wukaixingxp in https://github.com/meta-llama/llama-cookbook/pull/679
* fix AutoModel and bump transformers version to 4.45 by @wukaixingxp in https://github.com/meta-llama/llama-cookbook/pull/686
* post1 release version bump by @mreso in https://github.com/meta-llama/llama-cookbook/pull/687
* Update multi_modal_infer.py by @init27 in https://github.com/meta-llama/llama-cookbook/pull/696
* Add recipe for Llama Triaging & Reporting Tool by @subramen in https://github.com/meta-llama/llama-cookbook/pull/651
* Updates to accommodate OpenLLM leaderboard v2 tasks and change Meta Llama 3.1 to Llama 3.1 by @wukaixingxp in https://github.com/meta-llama/llama-cookbook/pull/639
* Improve model checkpoint saving logic by @lucas-ventura in https://github.com/meta-llama/llama-cookbook/pull/691
* Delete cookie by @init27 in https://github.com/meta-llama/llama-cookbook/pull/700
* [Fixed] RuntimeError: probability tensor contains either inf, nan or element < 0 by @himanshushukla12 in https://github.com/meta-llama/llama-cookbook/pull/704
* chore: update train_utils.py by @eltociear in https://github.com/meta-llama/llama-cookbook/pull/690
* Update requirements.txt by @varunfb in https://github.com/meta-llama/llama-cookbook/pull/664
* added missing word and corrected spelling by @jnfinitym in https://github.com/meta-llama/llama-cookbook/pull/707
* Fix the bug when continue the peft. by @24kMengXin in https://github.com/meta-llama/llama-cookbook/pull/717
* Fix link to LLM finetuning overview by @vvolhejn in https://github.com/meta-llama/llama-cookbook/pull/719
* fix Colab link in quickstart_peft_finetuning.ipynb by @jgrivolla in https://github.com/meta-llama/llama-cookbook/pull/720
* Fix fine-tuning training loss accumulation by @celestinoalan in https://github.com/meta-llama/llama-cookbook/pull/725
* quick fix on readmes and deadlinks by @wukaixingxp in https://github.com/meta-llama/llama-cookbook/pull/729
* Initial Crusoe examples to 3p_integrations recipes by @ethxnp in https://github.com/meta-llama/llama-cookbook/pull/716
* Fix numpy seed in finetuning.py by @patrik-lambert in https://github.com/meta-llama/llama-cookbook/pul

## Summary

l/728
* Fix/unit test 3.2 by @mreso in https://github.com/meta-llama/llama-cookbook/pull/726
* Tool Calling Tutorial and Example by @init27 in https://github.com/meta-llama/llama-cookbook/pull/697
* Update wordlist.txt by @init27 in https://github.com/meta-llama/llama-cookbook/pull/736
* Support converting fine-tuned llama 3.2 vision model to HF format and then local inference by @wukaixingxp in https://github.com/meta-llama/llama-cookbook/pull/737
* Save the `preprocessor_config.json` and `chat_template.json` for mllama model after conversion by @wukaixingxp in https://github.com/meta-llama/llama-cookbook/pull/741
* Append epoch rather than best val. loss to val_loss by @celestinoalan in https://github.com/meta-llama/llama-cookbook/pull/744
* Update wordlist.txt by @init27 in https://github.com/meta-llama/llama-cookbook/pull/745
* Notebook llama by @init27 in https://github.com/meta-llama/llama-cookbook/pull/739
* Small notes on next steps by @init27 in https://github.com/meta-llama/llama-cookbook/pull/746
* Fix minor grammatical errors by @terrchen in https://github.com/meta-llama/llama-cookbook/pull/748
* Update hello_llama_cloud.ipynb by @sharmax-vikas in https://github.com/meta-llama/llama-cookbook/pull/753
* Added a Gradio UI for multi-modal inferencing using Llama 3.2 Vision/ by @himanshushukla12 in https://github.com/meta-llama/llama-cookbook/pull/718
* Update hello_llama_cloud.ipynb by @sharmax-vikas in https://github.com/meta-llama/llama-cookbook/pull/754
* Quickstart docs: Fix path to location of dict for custom datasets by @j-klesen in https://github.com/meta-llama/llama-cookbook/pull/755
* Update Step-1 PDF-Pre-Processing-Logic.ipynb by @sharmax-vikas in https://github.com/meta-llama/llama-cookbook/pull/756
* added a notebook tutorial on llama 3.2 new capabilities by @Monireh2 in https://github.com/meta-llama/llama-cookbook/pull/764
* Updated QuickStart README by @Monireh2 in https://github.com/meta-llama/llama-cookbook/pull/767
* fix walkthrough.ipynb render by @subramen in https://github.com/meta-llama/llama-cookbook/pull/787
* colab links fix by @jeffxtang in https://github.com/meta-llama/llama-cookbook/pull/790
* add TogetherNotebookLM recipe by @zainhas in https://github.com/meta-llama/llama-cookbook/pull/766
* add freeze_LLM_only option for mllama finetuning by @JimChienTW in https://github.com/meta-llama/llama-cookbook/pull/791
* All functionality has been consolidated into a single file for CLI/UI/Checkpointing and Added fix for issue 702 and added code for that as well, added instructions in local_inference README.md by @himanshushukla12 in https://github.com/meta-llama/llama-cookbook/pull/757
* fix typo in auto wrap policy by @hiaoxui in https://github.com/meta-llama/llama-cookbook/pull/793
* [docs] small typo in eval readme by @jaysonfrancis in https://github.com/meta-llama/llama-cookbook/pull/796
* Add llama 3.2 mmlu, math, gpqa evals to meta_eval harness by @aidando73 in https://github.com/meta-llama/llama-cookbook/pull/

## Related Articles

- [[release-notes-ollama-vv0312]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-47255-point-to-gemma-4-model-in-gemma4forcausallm-docstring-example]]
- [[release-notes-langchain-vlangchain-openai135]]
- [[release-notes-llamacpp-vb9956]]
