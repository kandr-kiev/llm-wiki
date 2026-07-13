---
title: "year in review"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - architecture
  - data
  - deep-learning
  - foundation-model
  - gpt
  - image-generation
  - industry
  - llm
  - machine-learning
  - open-source
  - optimization
  - performance
  - real-time
  - reinforcement-learning
  - review
  - rlhf
  - sft
  - supervised
  - training
---# year in review

> **Source:** 2025-llm-year-in-review-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** [ #  karpathy ](/) Home Blog # 2025 LLM Year in Review * 19 Dec, 2025 * ![unnamed](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/unnamed.webp) 2025 has been a strong and eventful year o...
> **Sources:**
>   - 2025-llm-year-in-review-2026-07-10.md
> **Links:**
- [[automating-ai-away-2026-07-07]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[how-to-engineer-prompts]]

## Key Findings

[
# 
karpathy
](/)
Home Blog
# 2025 LLM Year in Review
*
19 Dec, 2025
*
![unnamed](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/unnamed.webp)
2025 has been a strong and eventful year of progress in LLMs. The following is a list of personally notable and mildly surprising "paradigm changes" - things that altered the landscape and stood out to me conceptually.
### 1. Reinforcement Learning from Verifiable Rewards (RLVR)
At the start of 2025, the LLM production stack in all labs looked something like this:
- Pretraining (GPT-2/3 of ~2020)
- Supervised Finetuning (InstructGPT ~2022) and
- Reinforcement Learning from Human Feedback (RLHF ~2022)
This was the stable and proven recipe for training a production-grade LLM for a while. In 2025, Reinforcement Learning from Verifiable Rewards (RLVR) emerged as the de facto new major stage to add to this mix. By training LLMs against automatically verifiable rewards across a number of environments (e.g. think math/code puzzles), the LLMs spontaneously develop strategies that look like "reasoning" to humans - they learn to break down problem solving into intermediate calculations and they learn a number of problem solving strategies for going back and forth to figure things out (see DeepSeek R1 paper for examples). These strategies would have been very difficult to achieve in the previous paradigms because it's not clear what the optimal reasoning traces and recoveries look like for the LLM - it has to find what works for it, via the optimization against rewards.
Unlike the SFT and RLHF stage, which are both relatively thin/short stages (minor finetunes computationally), RLVR involves training against objective (non-gameable) reward functions which allows for a lot longer optimization. Running RLVR turned out to offer high capability/$, which gobbled up the compute that was originally intended for pretraining. Therefore, most of the capability progress of 2025 was defined by the LLM labs chewing through the overhang of this new stage and overall we saw ~similar sized LLMs but a lot longer RL runs. Also unique to this new stage, we got a whole new knob (and and associated scaling law) to control capability as a function of test time compute by generating longer reasoning traces and increasing "thinking time". OpenAI o1 (late 2024) was the very first demonstration of an RLVR model, but the o3 release (early 2025) was the obvious point of inflection where you could intuitively feel the difference.
### 2. Ghosts vs. Animals / Jagged Intelligence
2025 is where I (and I think the rest of the industry also) first started to internalize the "shape" of LLM intelligence in a more intuitive sense. We're not "evolving/growing animals", we are "summoning ghosts". Everything about the LLM stack is different (neural architecture, training data, training algorithms, and especially optimization pressure) so it should be no surprise that we are getting very different entities in the intelligence space, which are 

## Summary

inappropriate to think about through an animal lens. Supervision bits-wise, human neural nets are optimized for survival of a tribe in the jungle but LLM neural nets are optimized for imitating humanity's text, collecting rewards in math puzzles, and getting that upvote from a human on the LM Arena. As verifiable domains allow for RLVR, LLMs "spike" in capability in the vicinity of these domains and overall display amusingly jagged performance characteristics - they are at the same time a genius polymath and a confused and cognitively challenged grade schooler, seconds away from getting tricked by a jailbreak to exfiltrate your data.
![G6zymj4a0AMNJkJ](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/g6zymj4a0amnjkj.webp)(human intelligence: blue, AI intelligence: red. I like this version of the meme (I'm sorry I lost the reference to its original post on X) for pointing out that human intelligence is also jagged in its own different way.)
Related to all this is my general apathy and loss of trust in benchmarks in 2025. The core issue is that benchmarks are almost by construction verifiable environments and are therefore immediately susceptible to RLVR and weaker forms of it via synthetic data generation. In the typical benchmaxxing process, teams in LLM labs inevitably construct environments adjacent to little pockets of the embedding space occupied by benchmarks and grow jaggies to cover them. Training on the test set is a new art form.
What does it look like to crush all the benchmarks but still not get AGI?
I have written a lot more on the topic of this section here:
- Animals vs. Ghosts
- Verifiability
- The Space of Minds
### 3. Cursor / new layer of LLM apps
What I find most notable about Cursor (other than its meteoric rise this year) is that it convincingly revealed a new layer of an "LLM app" - people started to talk about "Cursor for X". As I highlighted in my Y Combinator talk this year (transcript and video), LLM apps like Cursor bundle and orchestrate LLM calls for specific verticals:
- They do the "context engineering"
- They orchestrate multiple LLM calls under the hood strung into increasingly more complex DAGs, carefully balancing performance and cost tradeoffs.
- They provide an application-specific GUI for the human in the loop
- They offer an "autonomy slider"
A lot of chatter has been spent in 2025 on how "thick" this new app layer is. Will the LLM labs capture all applications or are there green pastures for LLM apps? Personally I suspect that LLM labs will trend to graduate the generally capable college student, but LLM apps will organize, finetune and actually animate teams of them into deployed professionals in specific verticals by supplying private data, sensors and actuators and feedback loops.
### 4. Claude Code / AI that lives on your computer
Claude Code (CC) emerged as the first convincing demonstration of what an LLM Agent looks like - something that in a loopy way strings together tool use and reason

## Related Articles

- [[automating-ai-away-2026-07-07]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[how-to-engineer-prompts]]
