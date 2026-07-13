---
title: "sampling"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - async
  - best-practice
  - edge
  - foundation-model
  - guide
  - image-generation
  - mlops
  - real-time
---# sampling

> **Source:** generation-configurations-temperature-top-k-top-p-and-test-time-compute-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** -  **Table of Contents** ** [Sampling](#sampling) - [Temperature](#temperature) - [Top-k](#top_k) - [Top-p](#top_p) - [Stopping condition](#stopping_condition) [Test Time Compute](#test_time_compute)...
> **Sources:**
>   - generation-configurations-temperature-top-k-top-p-and-test-time-compute-2026-07-10.md
> **Links:**
- [[animals-vs-ghosts]]
- [[how-to-engineer-prompts]]
- [[automating-ai-away-2026-07-07]]
- [[chemical-hygiene]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]

## Key Findings

- 
**Table of Contents**
**
[Sampling](#sampling)
- [Temperature](#temperature)
- [Top-k](#top_k)
- [Top-p](#top_p)
- [Stopping condition](#stopping_condition)
[Test Time Compute](#test_time_compute)
[Structured Outputs](#structured_outputs)
- [How to generate structured outputs](#how_to_generate_structured_outputs)
- [Constraint sampling](#constraint_sampling)
[Conclusion](#conclusion)
Table of Contents **
# Generation configurations: temperature, top-k, top-p, and test time compute
Jan 16, 2024
• Chip Huyen
ML models are probabilistic. Imagine that you want to know what’s the best cuisine in the world. If you ask someone this question twice, a minute apart, their answers both times should be the same. If you ask a model the same question twice, its answer can change. If the model thinks that Vietnamese cuisine has a 70% chance of being the best cuisine and Italian cuisine has a 30% chance, it’ll answer “Vietnamese” 70% of the time, and “Italian” 30%.
This probabilistic nature makes AI great for creative tasks. What is creativity but the ability to explore beyond the common possibilities, to think outside the box?
However, this probabilistic nature also causes inconsistency and hallucinations. It’s fatal for tasks that depend on factuality. Recently, I went over 3 months’ worth of customer support requests of an AI startup I advise and found that ⅕ of the questions are because users don’t understand or don’t know how to work with this probabilistic nature.
To understand why AI’s responses are probabilistic, we need to understand how models generate responses, a process known as sampling (or decoding). This post consists of 3 parts.
- **Sampling**: sampling strategies and sampling variables including temperature, top-k, and top-p.
- **Test time compute**: increasing the compute allocated to inference, e.g. sampling multiple outputs, to help improve a model’s performance.
- **Structured outputs**: how to get models to generate outputs in a certain format.
## Sampling
Given an input, a neural network produces an output by first computing the probabilities of all possible values. For a classifier, possible values are the available classes. For example, if a model is trained to classify whether an email is spam, there are only two possible values: spam and not spam. The model computes the probability of each of these two values, say being spam is 90% and not spam is 10%.
To generate the next token, a language model first computes the probability distribution over all tokens in the vocabulary.
![Sampling the next token based on token probabilities](/assets/pics/sampling/1-sampling-tokens.png)
For the spam email classification task, it’s okay to output the value with the highest probability. If the email has a 90% chance of being spam, you classify the email as spam. However, for a language model, always picking the most likely token, *greedy sampling*, creates boring outputs. Imagine a model that, for whichever question you ask, always responds with t

## Summary

he most common words.
Instead of always picking the next most likely token, we can sample the next token according to the probability distribution over all possible values. Given the context of `My favorite color is ...`, if `red` has a 30% chance of being the next token and `green` has a 50% chance, `red` will be picked 30% of the time, and “green” 50% of the time.
### Temperature
One problem with sampling the next token according to the probability distribution is that the model can be less creative. In the previous example, common words for colors like `red`, `green`, `purple`, etc. have the highest probabilities. The language model’s answer ends up sounding like that of a five-year-old: `My favorite color is green.` Because `the` has a low probability, the model has a low chance of generating a creative sentence such as `My favorite color is the color of a still lake on a spring morning.`
Temperature is a technique used to redistribute the probabilities of the possible values. Intuitively, it reduces the probabilities of common tokens, and as a result, increases the probabilities of rarer tokens. This enables models to create more creative responses.
To understand how temperature works, let’s take a step back to see how a model computes the probabilities. Given an input, a neural network processes this input and outputs a logit vector. Each logit corresponds to one possible. In the case of a language model, each logit corresponds to one token in the model’s vocabulary. The logit vector size is the size of the vocabulary.
![Sampling the next token based on token probabilities](/assets/pics/sampling/2-logits.png)
While larger logits correspond to higher probabilities, the logits don’t represent the probabilities. Logits don’t sum up to one. Logits can even be negative, while probabilities have to be non-negative. To convert logits to probabilities, a softmax layer is often used. Let’s say the model has a vocabulary of N and the logit vector is \([x_1, x_2, ..., x_N]\). The probability for the \(i^{th}\) token, \(p_i\), is computed as follows:
\[p_i = \text{softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}\]
Temperature is a constant used to adjust the logits before the softmax transformation. Logits are divided by temperature. For a given temperature of \(T\), the adjusted logit for the \(i^{th}\) token is \(\frac{x_i}{T}\). Softmax is then applied on this adjusted logit instead of on \(x_i\).
Let’s walk through a simple example to understand the effect of temperature on probabilities. Imagine that we have a model that has only two possible outputs: A and B. The logits computed from the last layer are `[1, 3]`. The logit for A is 1 and B is 3.
- Without using temperature, equivalent to temperature = 1, the softmax probabilities are `[0.12, 0.88]`. The model picks B 88% of the time.
- With temperature = 0.5, the probabilities are `[0.02, 0.98]`. The model picks B 98% of the time.
- With temperature = 2, the probabilities are `[0.27, 0.73]`. The mod

## Related Articles

- [[animals-vs-ghosts]]
- [[how-to-engineer-prompts]]
- [[automating-ai-away-2026-07-07]]
- [[chemical-hygiene]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
