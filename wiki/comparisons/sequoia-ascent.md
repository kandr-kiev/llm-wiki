---
title: "sequoia ascent"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - data
  - image-generation
  - open-source
  - prompt-tuning
  - real-time
---
# sequoia ascent

> **Source:** sequoia-ascent-2026-summary-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://karpathy.bearblog.dev/sequoia-ascent-2026/ ingested: 2026-07-10 sha256: 05869abfd01af1d55a6637d5a80025f82b0da8e84d2e9b3a40a789a7af77f5e6 blog_source: Andrej Karpathy --- Sequoi...
> **Sources:**
>   - sequoia-ascent-2026-summary-2026-07-10.md
> **Links:**
- [[animals-vs-ghosts]]
- [[chemical-hygiene]]
- [[automating-ai-away-2026-07-07]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[finding-the-best-sleep-tracker]]

## Key Findings

---
source_url: https://karpathy.bearblog.dev/sequoia-ascent-2026/
ingested: 2026-07-10
sha256: 05869abfd01af1d55a6637d5a80025f82b0da8e84d2e9b3a40a789a7af77f5e6
blog_source: Andrej Karpathy
---
Sequoia Ascent 2026 summary – karpathy
- 
- 
- 
- 
[
# 
karpathy
](/)
Home Blog
# Sequoia Ascent 2026 summary
*
30 Apr, 2026
*
I did a fireside chat at Sequoia Ascent 2026. The YouTube video is here:
YouTube Video Link
As an experiment, I fed an LLM all of my recent blog posts and tweets, then I had it read this video's transcript and produce 1) a summary and 2) a cleaned up transcript (correcting all transcription mistakes, getting rid of fill words, etc). I am posting both of these below. These can be useful for both people who may want to just read the summary in text format, but also for LLMs so that my content is legible and available to them.
**AI generated content below for this talk follows.** I used a top capability model (in this case Codex 5.5) and read the content and it reads ok without glaring mistakes.
---
# Sequoia Ascent 2026: Software 3.0, Agentic Engineering, and Jagged Intelligence
I recently joined Stephanie Zhan for a fireside chat at Sequoia Ascent 2026, speaking with founders about the recent shift in AI agents, what it means for software, and how I think about the next wave of AI-native companies.
The transcript from the event is a bit noisy, so I wanted to write up the main intellectual content in a cleaner form. The short version is that I think we have crossed a new threshold. LLMs are no longer just chatbots or autocomplete. They are becoming a new programmable layer for digital work.
This is the compact version of the conversation.
## 1. December 2025 Was an Agentic Inflection Point
I said recently that I have never felt more behind as a programmer.
The reason is not that programming became harder in the old sense. It is that the default workflow changed. For much of 2025, tools like Claude Code, Codex, and Cursor-like agents were useful but still required frequent correction. Around December 2025, I felt a step change: the generated chunks got larger, more coherent, and more reliable. I started trusting the agents with more of the work.
The unit of programming changed from typing lines of code to delegating larger "macro actions":
- Implement this feature.
- Refactor this subsystem.
- Research this library.
- Set up this service.
- Write tests, run them, and fix failures.
- Compare approaches and propose a plan.
This is why I think the profession is being refactored. The programmer is increasingly not just a code writer, but an orchestrator of agents.
## 2. Software 3.0: The Context Window as the New Program
I think of this as the next step in a sequence:
- **Software 1.0:** humans write explicit code.
- **Software 2.0:** humans create datasets, objectives, and neural networks; the program is learned into weights.
- **Software 3.0:** humans program LLMs through prompts, context, tools, examples, memory, and instructions.
In S

## Summary

oftware 3.0, the context window becomes the main lever. The LLM is an interpreter over that context, performing computation over digital information.
One example is installation. In the old world, installing a complex tool across many environments required a brittle shell script full of conditionals. In the Software 3.0 world, the installer can be a block of instructions you paste into an agent. The agent reads the local environment, debugs errors, adapts to the machine, and completes the setup.
That is a different kind of program. It is less precise, but more adaptive.
## 3. MenuGen and the Moment Software Disappears
I used MenuGen as an example of a deeper shift.
MenuGen was a traditional web app: take a picture of a restaurant menu, OCR the dish names, generate images of the dishes, and render the result in a UI. It required frontend code, APIs, image generation, deployment, auth, payments, secrets, and infrastructure.
But later, I saw the Software 3.0 version: take a photo of the menu, give it to a multimodal model, and ask it to render dish images directly onto the menu image.
In that version, much of the app disappears. The neural network directly transforms input media into output media. The old software stack was scaffolding around a transformation the model can now perform directly.
This is one of the most important founder implications: AI is not just a faster way to build the old apps. Some apps should stop existing as apps.
## 4. The New Opportunity Is Not Just Faster Programming
The shift is broader than coding. LLMs automate forms of information processing that were not previously programmable.
My LLM Wiki pattern is the clearest example. Instead of using retrieval-augmented generation to answer questions from raw documents each time, an agent incrementally compiles raw sources into a persistent Markdown wiki: summaries, entity pages, concept pages, contradictions, cross-links, logs, and evolving synthesis.
No classical program could robustly maintain that kind of knowledge base across messy human documents. But an LLM can.
The lesson: do not only ask, "What existing workflow can AI speed up?" Also ask, "What information transformation was impossible before, but is now natural?"
## 5. Verifiability Explains Where AI Moves Fastest
My core automation framework is:
- Traditional software automates what you can **specify**.
- LLMs and reinforcement learning automate what you can **verify**.
If a task has an automatic reward or success signal, models can practice it. This is why math, coding, tests, benchmarks, games, and many engineering tasks improve so quickly. They are resettable, repeatable, and rewardable.
This also explains why coding agents feel dramatically better than many ordinary chatbot experiences. Coding gives the model feedback: tests pass or fail, programs run or crash, diffs can be inspected, benchmarks can be measured.
## 6. Jagged Intelligence Has Two Axes: Verifiability and Training Attention
The interview added an i

## Related Articles

- [[animals-vs-ghosts]]
- [[chemical-hygiene]]
- [[automating-ai-away-2026-07-07]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[finding-the-best-sleep-tracker]]
