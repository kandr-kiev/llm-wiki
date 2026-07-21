---
title: "ai music video arena claude vs gpt 5.6"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - async
  - claude
  - comparison
  - data
  - gpt
  - image-generation
  - news
  - search
  - system-design
  - video-generation
  - web
---

# ai music video arena claude vs gpt 5.6

> **Source:** 100-ai-music-video-claude-fable-5-vs-gpt-56-sol-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** [ All posts](/blog)videocomparisonagents# $100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol We gave Claude Fable 5 and GPT-5.6 Sol the same song, a budget, web search, and local ffmpeg, then let eac...
> **Sources:**
>   - 100-ai-music-video-claude-fable-5-vs-gpt-56-sol-2026-07-17.md
> **Links:**
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[ai]]
- [[Automating Ai Away]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[sequoia ascent]]

## Key Findings

[ All posts](/blog)videocomparisonagents# $100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol
We gave Claude Fable 5 and GPT-5.6 Sol the same song, a budget, web search, and local ffmpeg, then let each autonomously direct a music video.
![TryAI](/_next/image?url=%2Flogo.png&w=48&q=75)TryAI·July 16, 2026· 8 min readWe built a small agentic harness with one job: hand a model a song, a hard dollar budget, and a set of tools, then get out of the way and let it produce a full music video on its own. The model researches which video models exist, generates clips, watches its own footage, edits with ffmpeg, and assembles a final cut.
A few readers of our last build-off said they wanted to see how tool use actually varies between models, so we gave frontier-level models an open-ended, long-horizon task where each model decides on its own what to research, what to generate, and how to edit. We log every tool call, so you can see exactly how each one worked (full transcripts below).
We ran two models, Claude Fable 5 and GPT-5.6 Sol, each at two budgets ($25 and $100), for four runs total. Every run got the same song (Bruno Mars and Mark Ronson's "Uptown Funk"), a short text description, and a time-stamped lyric transcript.
## The setup
Each model ran an autonomous tool-calling loop with six tools:
- **plan**: a tool for thinking (no cost, no action).
- **web_search**: to research generation models and their APIs and fetch information about music videos (if needed).
- **get_budget**: to check the remaining budget.
- **generate_image** and **generate_video**: the only tools that spend budget. The model can pick any FAL or Replicate model and pass its own parameters.
- **run_command**: a local shell with ffmpeg/ffprobe available, used to analyze audio, cut and concatenate clips, and mux the final video.
Once the budget hits zero, paid generation is refused, but the model can keep editing. Every model message, tool call, charge, and error was logged. The whole harness is open source at [github.com/hershalb/music-video-arena](https://github.com/hershalb/music-video-arena), so you can run it yourself.
## The four videos
Each clip below is the model's final, self-assembled output.mp4, full length with the original song muxed in.
Claude Fable 5 · $25GPT-5.6 Sol · $25
Claude Fable 5 · $100GPT-5.6 Sol · $100
## The numbers
All four runs finished on their own (none hit a step or time limit) and all four produced a valid, full-length video with the original song muxed in.
ModelBudget↕Wall-clock↕Steps↕Images↕Videos↕Failed calls↕Generation spend↕Output↕Claude Fable 5$2539m10s250541$24.301280x720GPT-5.6 Sol$2542m52s38614610$23.181280x720GPT-5.6 Sol$10049m39s340702$36.571280x720Claude Fable 5$10038m56s280800$48.601920x1080
"Generation spend" is the metered FAL cost, which is what the budget caps. At $25 both models nearly exhausted it. At $100 they spent $36.57 (Sol) and $48.60 (Fable), so more budget did translate into more footage. It does not include the cost of runnin

## Summary

g the model itself, which we add below.
## Time to finished video
![Wall-clock time per run in minutes](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/charts/time.svg)- - - 
## What each model built with
Left to choose their own tools, the models diverged. Three of the four runs went pure text-to-video. Only GPT-5.6 Sol at $25 used an image-to-video pipeline (generating stills first, then animating them). GPT-5.6 Sol at $100 mixed three different video models in a single run.
RunImage modelVideo model(s)ApproachFable 5 · $25noneWan 2.5 t2v ($0.05/s)Text-to-video onlySol · $25FLUX schnell ($0.003/img)Wan 2.2-5b i2v ($0.10/s)Keyframe, then image-to-videoSol · $100noneWan 2.5 ($0.05/s), Veo 3.1 Lite ($0.10/s), Hailuo 2.3 Standard ($0.28/video)Text-to-video, mixed modelsFable 5 · $100noneSeedance 1.0 Pro t2v (~$0.12/s at 1080p)Text-to-video only
Prices are FAL's listed rates, shown per second of output video unless noted. Hailuo 2.3 Standard is priced per video (about $0.28 per 6s clip), and Seedance 1.0 Pro is token-priced (~$0.62 per 5s 1080p clip, shown above as its effective per-second rate). Distinct clips generated per run ranged from 46 to 80.
![Number of images and videos successfully generated per run](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/charts/generations.svg)- - - 
## Tool usage
How each run spent its tool calls (this counts attempts, including failed generation calls).
Claude Fable 5 · $25GPT-5.6 Sol · $25![Tool-call distribution, Claude Fable 5 at $25](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/charts/tools-fable-25.svg)- - - ![Tool-call distribution, GPT-5.6 Sol at $25](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/charts/tools-sol-25.svg)- - - 
Claude Fable 5 · $100GPT-5.6 Sol · $100![Tool-call distribution, Claude Fable 5 at $100](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/charts/tools-fable-100.svg)- - - ![Tool-call distribution, GPT-5.6 Sol at $100](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/charts/tools-sol-100.svg)- - - 
Each run's full transcript, every plan, tool call, and command, is here: [Fable 5 · $25](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/transcripts/fable-25.txt), [Sol · $25](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/transcripts/sol-25.txt), [Sol · $100](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/transcripts/sol-100.txt), [Fable 5 · $100](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/transcripts/fable-100.txt).
## Errors along the way
"Failed calls" are generation requests that returned an error (mostly transient network failures to the provider). They were not charged, but the model spent steps retrying them.
![Failed generation calls per run](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/charts/errors.svg)- - - 
## Token usage
RunInput tokensOutput tokensReasoningCached inputFable 5 · $251,476,90044,341n/a0Sol · $252,956,27033

## Related Articles

- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[ai]]
- [[Automating Ai Away]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[sequoia ascent]]
