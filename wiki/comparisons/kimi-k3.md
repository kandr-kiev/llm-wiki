---
title: "kimi k3"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - analysis
  - api
  - application
  - benchmark
  - claude
  - cost
  - data
  - evaluation
  - few-shot
  - foundation-model
  - frontend
  - gemini
  - gpt
  - image-generation
  - llama
  - llm
  - machine-learning
  - mobile
  - news
  - open-source
  - prompt-engineering
  - prompt-tuning
  - self-supervised
  - software
  - tool
  - training
  - use-case
---

# kimi k3

> **Source:** kimi-k3-and-what-we-can-still-learn-from-the-pelican-benchmark-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** # [Simon Willison’s Weblog](/) Subscribe **Sponsored by:** Atlassian — Give your agents a plan. Not a prompt. New Jira capabilities unlock full-context for AI-native software development. Assign tasks...
> **Sources:**
>   - kimi-k3-and-what-we-can-still-learn-from-the-pelican-benchmark-2026-07-17.md
> **Links:**
- [[automating-ai-away-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
- [[away]]
- [[auto-grade-hn]]

## Key Findings

# [Simon Willison’s Weblog](/)
Subscribe
**Sponsored by:** Atlassian — Give your agents a plan. Not a prompt. New Jira capabilities unlock full-context for AI-native software development. Assign tasks to Claude, Cursor, or GitHub Copilot, now directly from Jira. [Learn more](https://fandf.co/4gCMW1I)
## Kimi K3, and what we can still learn from the pelican benchmark
16th July 2026
Chinese AI lab Moonshot AI [announced Kimi K3](https://www.kimi.com/blog/kimi-k3) this morning, describing it as their “most capable model to date, with 2.8 trillion parameters”. It’s currently available via their website and API, but an open weight release is promised “by July 27, 2026”.
Moonshot are calling this the first “open 3T-class model” (I guess they’re rounding 2.8 trillion up to 3 trillion), taking the crown from [DeepSeek’s 1.6T v4 Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro). Their [self-reported benchmarks](https://www.kimi.com/blog/kimi-k3#full-benchmark-table) have K3 mostly beating Claude Opus 4.8 max and GPT-5.5 high, while losing out to Claude Fable 5 and GPT-5.6 Sol.
A few highlights from the [Artificial Analysis report](https://twitter.com/ArtificialAnlys/status/2077832874183860404) on the model:
- “On our private long-horizon knowledge work evaluation, Kimi K3 reaches an overall Elo of 1547, +732 points from Kimi K2.6 and behind only Claude Fable 5.”
- “Cost per task ($0.94) is similar to GPT-5.6 Sol ($1.04), ~1/2 the price of Opus 4.8 ($1.80) and higher than open weights peers”
- “Kimi K3’s token usage on the Artificial Analysis Intelligence Index decreased significantly, using 21% fewer output tokens than K2.6.”
The model is also now the [leading model on Arena.ai’s Frontend Code arena](https://twitter.com/arena/status/2077824029126504525), surpassing even Claude Fable 5.
The new model is notable for the pricing: $3/million input tokens and $15/million output tokens, putting it at the same level as Anthropic’s Claude Sonnet series and making it the most expensive model released by a Chinese AI lab to date. This is a significant increase on their earlier models [such as Kimi K2.6](https://platform.kimi.ai/docs/pricing/chat-k26) at $0.95/$4. 2.8 trillion parameters is also more than twice the size of that 1T model.
#### But how does it pelican?
I used OpenRouter (to avoid signing up for a Moonshot API key) with the [llm-openrouter plugin](https://github.com/simonw/llm-openrouter) to generate an SVG of a pelican riding a bicycle:
```
llm -m openrouter/moonshotai/kimi-k3 'Generate an SVG of a pelican riding a bicycle'
```
Here’s [the transcript](https://gist.github.com/simonw/66a2699eb1594258904c7b5102840dd6). It looks like this:
![See description below](https://static.simonwillison.net/static/2026/kimi-3-pelican.jpg)
That pelican took 95 input tokens and 16,658 output tokens (13,241 were reasoning tokens), for a total cost of [25 cents](https://www.llm-prices.com/#it=95&ot=16658&ic=3&oc=15)!
Since K3 accepts image input I ran it against 

## Summary

that rendered SVG above (with my [alt text prompt](https://simonwillison.net/guides/agentic-engineering-patterns/prompts/#alt-text)) and [got back](https://gist.github.com/simonw/665dbf840701b421745f2cb891acdfd6) (for [0.6 cents](https://www.llm-prices.com/#it=822&ot=243&ic=3&oc=15)):
>
Cartoon illustration of a white pelican wearing a red scarf, riding a red bicycle along a gray road with white dashed lines; the pelican has a large orange beak and webbed orange feet pedaling, with white motion lines behind it; the background shows a light blue sky with white clouds, a yellow sun, two small black birds in flight, and green grass with tiny white flowers in the foreground
#### What can we learn from the pelican?
My [Generate an SVG of a pelican riding a bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle/) test is 21 months old now. It was never a particularly great benchmark. It started out as a joke on how absurdly difficult it is to compare these models, but then for the first year it turned out to have a [surprising correlation](https://simonwillison.net/2025/Jun/6/six-months-in-llms/) to how good the models actually were.
That connection has been mostly severed now. The [GPT-5.6](https://simonwillison.net/2026/Jul/9/gpt-5-6/) and [Claude Fable 5](https://simonwillison.net/2026/Jun/9/claude-fable-5/) pelicans are outclassed [by GLM-5.2](https://simonwillison.net/2026/Jun/17/glm-52/), and much as I love GLM I don’t think that’s a Fable-class model.
(I’m still not convinced that labs are [training for the benchmark](https://simonwillison.net/2025/Nov/13/training-for-pelicans-riding-bicycles/)—if they were, I’d expect much better results. There’s a chance that Gemini has optimized for [any combination of an animal on a vehicle](https://simonwillison.net/2026/Feb/19/gemini-31-pro/#jeff-dean) though!)
The biggest limitation of the pelican is that it doesn’t touch at all on the thing that matters most for today’s model: agentic tool calling and the ability to operate tools reliably as conversations grow in length.
So don’t go using pelicans to compare models!
All of that said, I still get a decent amount of value out of running the benchmark myself.
Firstly, it’s a forcing function for actually trying the model. If I show you a pelican, that means I’ve managed to run a prompt through it. If the model has an official API I’ll use that, if it’s open weight (and small enough to fit a 128GB M5 MacBook Pro) I’ll try running it on my own machine, usually via [llama.cpp](https://github.com/ggml-org/llama.cpp) or [LM Studio](https://lmstudio.ai) or [Ollama](https://ollama.com). I’ll frequently use [OpenRouter](https://openrouter.ai) since that usually provides a proxy to an official API without me needing a new API key.
Most of my pelicans are generated using [my LLM CLI tool](https://llm.datasette.io/), which helps encourage me to ensure the latest models are supported by that (via one of its plugins).
More importantly though, even the act of a

## Related Articles

- [[automating-ai-away-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
- [[away]]
- [[auto-grade-hn]]
