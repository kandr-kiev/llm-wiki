---
title: "Issue #3419: FIX Bug in forgetting metric in MetaMathQA"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - batch
  - benchmark
  - fine-tuning
  - foundation-model
  - lora
  - machine-learning
  - open-source
  - prompt-tuning
  - pytorch
  - real-time
  - training
---
# Issue #3419: FIX Bug in forgetting metric in MetaMathQA

> **Source:** gh-huggingfacepeft-issue-3419-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/peft/issues/3419 ingested: 2026-07-11 sha256: 6070ae0009442162a428bd1e6c3f60a86900517cc1ed498234cfbd836f09965d blog_source: github:huggingface/peft --- #...
> **Sources:**
>   - gh-huggingfacepeft-issue-3419-2026-07-11.md
> **Links:**
- [[finding-the-best-sleep-tracker]]
- [[animals-vs-ghosts]]
- [[away]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[automating-ai-away-2026-07-07]]

## Key Findings

---
source_url: https://github.com/huggingface/peft/issues/3419
ingested: 2026-07-11
sha256: 6070ae0009442162a428bd1e6c3f60a86900517cc1ed498234cfbd836f09965d
blog_source: github:huggingface/peft
---
# Issue #3419: FIX Bug in forgetting metric in MetaMathQA
**State:** open | **Author:** BenjaminBossan | **Created:** 2026-07-10T15:48:18Z
This PR fixes two bugs in how the forgetting metric in the MetaMathQA benchmark is determined.
## Background
I was revisiting the forgetting metric, which has some weird numbers on some of the MetaMathQA experiments. This revealed two bugs which are fixed in this PR:
1. Beforehand, we were comparing logits vs targets, but we should compare logits vs targets shifted by 1. This is done under the hood in the training loop when passing labels to the forward pass of the model, but when calculating the forgetting metric, we omitted it.
After I fixed that, I re-ran some tests, among others prompt tuning, which had a forgetting metric of 3.673, which is very high. To my surprise, after the fix the metric was -2.475. This prompted me to investigate further and I found the second issue:
2. We calculated the wiki text loss on the PEFT model before training. However, some PEFT methods are not identity transforms at the start of training. For instance, prompt tuning injects (by default) random virtual embeddings, which can severely reduce the loss before training. When, after training, the loss recovers, it appears as if forgetting is negative, when in reality the loss is just back to normal. I verified this by checking the loss before training and it was 3.63. For LoRA, which is an identity transform at the start, the loss was only 1.58.
The solution is to disable the PEFT contribution when calculating the initial wiki loss. Even better would be to calculate the loss before applying PEFT at all, but the way the code is structured, it's currently not possible. I also added a sanity check that the value is between 1 and 2. In theory, we could even hard-code the value, as it must be the same for each model, but then we would have to keep it up-to-date if there are changes.
## Results
With the fixed forgetting metric, I re-ran some experiments: LoRA as the default non-prompt learning PEFT method; adaption prompt, which had the lowest forgetting; and prompt tuning, which had the highest forgetting. The new numbers look much more reasonable:
```
LoRA r32: 0.417 -> 0.501
Adaption prompt lr 0.0005: -0.954 -> 0.221
Prompt tuning lr 0.001 3.673 -> 0.404
```
Of course, if we merge this PR, all forgetting metrics in our results are invalidated, so we would have to re-run all experiments. I think that would be overkill just for this change, but since we have several new PEFT methods, a new PyTorch version, and haven't run the full batch in some time, I would argue we should rerun everything for the upcoming PEFT v0.20.0 release.

## Summary

See Key Findings for full content.

## Related Articles

- [[finding-the-best-sleep-tracker]]
- [[animals-vs-ghosts]]
- [[away]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[automating-ai-away-2026-07-07]]
