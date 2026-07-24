---
title: "https://stateofopensource.ai/"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - analysis
  - async
  - claude
  - closed-source
  - cloud
  - cost
  - data
  - fine-tuning
  - foundation-model
  - gpt
  - hardware
  - instruction-tuning
  - interoperability
  - news
  - nlp
  - offline
  - open-source
  - real-time
  - retrieval
  - speech-to-text
  - standards
  - training
  - use-case
  - web
---

# https://stateofopensource.ai/

> **Source:** the-state-of-open-source-ai-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** --- source_url: https://stateofopensource.ai/ ingested: 2026-07-17 sha256: 65e4a570cbcd5372ba2d6017fb3dbe9de3e02d8c26924f3820cccf72ce0e49a7 blog_source: Hacker News AI --- The State of Open Source AI...
> **Sources:**
>   - the-state-of-open-source-ai-2026-07-17.md
> **Links:**
- [[kimi-k3]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[robots-txt-2023-war-memorial]]

## Key Findings

---
source_url: https://stateofopensource.ai/
ingested: 2026-07-17
sha256: 65e4a570cbcd5372ba2d6017fb3dbe9de3e02d8c26924f3820cccf72ce0e49a7
blog_source: Hacker News AI
---
The State of Open Source AI — V1.0 · July 2026
- 
- 
- 
- 
[![Mozilla](assets/img/moz-logo.png)State of open source **AI**.](#top)
[Download full report](state-of-open-source-ai-2026.pdf)
[CTO's Letter](#letter)
![Mozilla](assets/img/moz-logo.png)
# The state of
open source AI.
V1.0 · Recurring · July 2026
A Letter From Our CTO, Raffi Krikorian
“
In New Zealand's far north, a Māori broadcaster trains speech models for te reo — a language too small for any market — under a license that keeps the data with its people. PwC, one of the largest accounting firms in the world, fine-tuned an open model on the language of finance and runs it today for hundreds of clients, on its own hardware, with no per-token meter running. Researchers in Lausanne built an open medical model with the Red Cross, tuned to its humanitarian guidelines, and are preparing clinical trials at home and in Tanzania. In East Africa, farmers diagnose cassava disease with a model that runs on the phone itself, offline, in fields the cloud has never reached. In Switzerland, a public consortium trained a national model on public supercomputers and released all of it: weights, data, training code. None of them asked permission, and none of them could have rented this. They own it — that is the whole idea.
We have been here before. Mozilla exists because one company tried to own the front door to the web, and an open community rose up to make sure it never could. Twenty-five years later, someone is running the same play. We bet on open the first time. Open won. Together, we can do it again.
Our belief is simple: the path forward is competition and interoperability. We believe in a world of many models, standard ways to plug them together, and the freedom to walk away from any vendor at any time. Open has a record here. It grew the pie and let more people own a slice of it.
Read what follows as a map: where open AI is winning — some numbers surprised even us — and where it is exposed. A case that hides its weak points is an advertisement.”
[Read Raffi's full letter here →](#letter)[Download the report here ↓](state-of-open-source-ai-2026.pdf)
Open weights closed the capability gap while the price of intelligence collapsed.
0%Capability gap to the top closed models — at parity on coding, behind on reasoning
0×Fall in GPT-4-class inference cost in 36 months: $20 → $0.40 per 1M tokens
01The current state of open-source AI
## Parity reached. The contest is one layer up.
Open weights are no longer a compromise. They are where the work happens: a majority of production tokens now route through them, and the five highest-volume models on OpenRouter are all open. Closed models still lead at the frontier, on reasoning and multimodality, but the frontier is not what most workloads need. Commodity inputs do not hold pricing power.

## Summary

 Value moves up, to the agentic harness.
The capability gap: 8.04% → 0.5% → 3.3%
Open-vs-closed gap on Chatbot Arena over 24 months. By August 2024, the gap had collapsed to 0.5%, and in February 2025 DeepSeek-R1 briefly matched the top US model. By March 2026 it had reopened to 3.3% as closed reasoning models pulled ahead. But 3.3% is an average over a jagged frontier: open is at or near parity on coding, instruction-following and general knowledge, while the gap concentrates in reasoning, long-context retrieval and agentic tasks. The question is no longer whether open models are good enough. It's what you need for your workload. Hover the points.
Source: Chatbot Arena, Jan 2024 – Mar 2026.
Inference fell 50× in 36 months
GPT-4-equivalent price per 1M tokens — faster than dotcom-era bandwidth or PC-compute price curves. Log scale.
Sources: Stanford HAI AI Index 2025 (280× GPT-3.5-class drop over 18 months); Epoch AI (9–900× annual decay); Nov 2025 MIT study (5–10×/yr at the frontier, hardware-adjusted).
Open weights win the tokens
The share of tokens routed on OpenRouter through open-weight models grew from a negligible base to a third by late 2025 to a majority by mid-2026.
Source: OpenRouter 100T-token study (Nov 2024–Nov 2025) and live leaderboard; intermediate points interpolated. By request count, closed US providers still lead — the open lead is a token-volume lead, concentrated in coding and agentic workloads.
OpenRouter live leaderboard — trailing month, tokens routed
The five highest-volume models are all open weights. Anthropic's closed Claude models are the next US-built entrants.
**Open weights**Closed
By mid-2026 the top nine models route roughly 18T weekly tokens for Chinese-built models against ~5.5T for US-built ones — more than 3:1 (FT analysis). Where developers route by cost, they route to open weights.
## Open ships easy.
Open deploys hard.
Data from the Mozilla / SlashData 2026 developer survey. Open models lead in adoption: 79% of developers adding AI functionality use them, against 71% for closed, and the two are largely complementary, with half of developers using both. But production is where teams stall: only 51% of open-model teams reach production versus 63% for closed. The gap is operational tooling and trust, not model capability.
Open models lead in adoption, and mostly coexist with closed
Share of developers adding AI functionality to their applications who currently use each model type, and how the two overlap.
Open models79%
Closed models71%
How they combine
29%OS only
50%Both
21%CS only
Source: Mozilla / SlashData 2026 developer survey. Open and closed aren't substitutes for most teams: 50% run both, 29% open only, 21% closed only.
Where open adoption peaks, and where closed still edges it
Open-model adoption by region. Greater China and East Asia lead at 89%; South America and Western Europe are the only two regions where closed adoption exceeds open.
Same survey, by developer region. In South America and West

## Related Articles

- [[kimi-k3]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[robots-txt-2023-war-memorial]]
