---
title: "that s embarrassing why frontier ai still makes things up and what to do about it"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - async
  - container
  - edge
  - gpt
  - news
  - search
---

# that s embarrassing why frontier ai still makes things up and what to do about it

> **Source:** thats-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://www.freecodecamp.org/news/that-s-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it/ ingested: 2026-07-20 sha256: e05b7964a2340c3bed5e7114f0509fb8aefb8e...
> **Sources:**
>   - thats-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it-2026-07-20.md
> **Links:**
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Automating away]]
- [[Mesh LLM: distributed AI computing on iroh]]

## Key Findings

---
source_url: https://www.freecodecamp.org/news/that-s-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it/
ingested: 2026-07-20
sha256: e05b7964a2340c3bed5e7114f0509fb8aefb8ea119573d0eaa9add0b5b3b43f1
blog_source: FreeCodeCamp Blog
---
That's Embarrassing: Why Frontier AI Still Makes Things Up, and What to Do About It
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
[![freeCodeCamp.org](https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg)](https://www.freecodecamp.org/news/)
- 
English
- 
Español
- 
中文（简体字）
- 
Italiano
- 
Português
- 
Українська
- 
日本語
- 
한국어
Menu
- 
- Forum
- Curriculum
- 
Night Mode
Donate
July 20, 2026
/
#AI
# That's Embarrassing: Why Frontier AI Still Makes Things Up, and What to Do About It
![Omer Rosenbaum](https://cdn.hashnode.com/res/hashnode/image/upload/v1723363637693/639d28f7-9988-40dd-9e95-cb5fffbadb78.png)
[
Omer Rosenbaum
](/news/author/omerros/)
![That's Embarrassing: Why Frontier AI Still Makes Things Up, and What to Do About It](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8813b1ba-d75c-4c3d-90a1-504af66cce3b.png)
It's mid 2026, and the best frontier models out there still hallucinate. I want you to gain two things from reading this article: understanding that AI hallucinations are still real and possibly harmful, and an intuition as to why they might be so ubiquitous.
Before we get into AI at all, I want you to do something with me.
Listen to this clip of a football crowd chanting. What are they saying?
If you’re like most people, you have no idea. It’s a smear of sound. So let me help you: keep listening, and read along.
>
***Bart Simpson bouncing?***
Listen again.
>
***Baptism piracy?***
Again.
>
***Lobsters in motion?***
***Lactates in pharmacy?***
***Rotating pirate ship?***
The crowd is chanting the exact same phrase every single time. The audio never changes, but every time you read a different caption, your brain heard something different, and it heard it *confidently*. You didn’t experience doubt. You experienced *“oh, they’re clearly saying Bart Simpson bouncing.”*
What are they actually chanting? These are fans of Derby County, a UK football team, and they’re singing [1]:
>
***“That is embarrassing.”***
Play the clip one more time with that in mind, and you’ll hear it perfectly.
This article is based on my talk “Embarrassing AI.” If you prefer the video, you can [**watch it here**](https://www.youtube.com/watch?v=vneV9NIHs44&feature=youtu.be). All the stories below are real, all of them happened on frontier models, and most of them happened in the last month or two.
Every source, plus a few cases that didn’t make the cut, live on the [**companion resources page**](https://omerr.github.io/embarrassing-ai/resources.html). Inline citations below point to the [**References**](https://towardsdatascience.com/that-is-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it/#References) at the end.
### What We'll Cover:
- [You 

## Summary

Just Hallucinated](#heading-you-just-hallucinated)
- [Part 1: The Tales](#heading-part-1-the-tales)
- [Part 2: Why It Happens](#heading-part-2-why-it-happens)
- [So What Do You Actually Do About It?](#heading-so-what-do-you-actually-do-about-it)
- [Wrapping Up](#heading-wrapping-up)
- [References](#heading-references)
## **You Just Hallucinated**
What you just experienced has a name: **phonemic restoration** [2]. Your auditory system got an ambiguous input (the chant) and something to disambiguate it (the caption on the screen), so it filled the “gap”. It predicted the most plausible meaning given the context, and then it reported that prediction to you as if it were the thing you actually heard.
That move, where you meet an input you can’t fully resolve and fill the gap with something plausible and confident instead of reporting “I can’t tell,” is something that your brain experiences (as you’ve just seen), and also something that LLMs experience.
![Image 1: The same top-down move in a brain and a model: an ambiguous input, a gap filled by prediction, and a confident output that is never flagged as a guess. (Source: Brief)](https://contributor.insightmediagroup.io/wp-content/uploads/2026/07/phonemic_restoration.svg)
Image 1: The same top-down move in a brain and a model: an ambiguous input, a gap filled by prediction, and a confident output that is never flagged as a guess. (Source: [**Brief**](https://www.youtube.com/watch?v=vneV9NIHs44&feature=youtu.be))
(Note: all images in this post were created by me, and included in [**my talk**](https://www.youtube.com/watch?v=vneV9NIHs44&feature=youtu.be).)
So let me make a claim that should be uncontroversial by the end of this article: **no, we're not past the embarrassing AI tales.**
As of writing these words, it’s June 2026. The models are astonishing, honestly more capable than I predicted they’d be by now. And they still make things up, confidently, in production, in ways that range from funny to business-ending.
This article has two parts:
- **The tales**, a short parade of recent failures, in two acts: chatbots that *answer* wrong, then agents that *act* wrong.
- **Why it happens**: the intuition first, then an actual look inside the model, and finally what to do about it if you’re shipping AI yourself.
Watch the dates as we go. Some of these are a year old. Most are very, very recent.
## **Part 1: The Tales**
### Act I — Chatbots (when AI answers)
#### 1. Cursor, April 2025
Say you use Cursor, the agentic IDE. You switch laptops, log in on the new one, and Cursor logs you out of the old one. That’s pretty annoying 😒
So you ask support: *“I get logged out every time I switch laptops. Why?”*
The reply:
>
***“Cursor is designed to work with one device per subscription, as a core security feature.”***
Plausible! Except it’s completely false. There's no such policy. “Support” was an AI bot, and it had invented the policy on the spot, handing the same fabricated rule to multiple users, as if reading f

## Related Articles

- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Automating away]]
- [[Mesh LLM: distributed AI computing on iroh]]
