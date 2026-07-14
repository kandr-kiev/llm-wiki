---
title: "5 Agent Skills I Use Every Day"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - architecture
  - claude
  - deep-learning
  - foundation-model
  - guide
  - image-generation
  - integration
  - llm
  - nlp
  - parallel
  - prompt-engineering
  - real-time
  - search
  - system-design
  - use-case
  - video-generation
  - workflow
---

# 5 Agent Skills I Use Every Day

> **Source:** 5-agent-skills-matt-pocock-2026-07-13.md
> **Type:** comparison
> **Created:** 2026-07-13
> **Updated:** 2026-07-13
> **Confidence:** high
> **Description:** --- title: "5 Agent Skills I Use Every Day" source_url: "https://www.aihero.dev/5-agent-skills-i-use-every-day" blog_source: "aihero.dev" author: "Matt Pocock" ingested: "2026-07-13" sha256: 5e8edab67...
> **Sources:**
>   - 5-agent-skills-matt-pocock-2026-07-13.md
> **Links:**
- [[Automating Ai Away]]
- [[The Illustrated Stable Diffusion]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Generative AI Strategy]]

## Key Findings

---
title: "5 Agent Skills I Use Every Day"
source_url: "https://www.aihero.dev/5-agent-skills-i-use-every-day"
blog_source: "aihero.dev"
author: "Matt Pocock"
ingested: "2026-07-13"
sha256: 5e8edab67b2f8c0dbb581d681e9cd402b0efdc3045ed3484a8cae6d3996e7a78
---
# 5 Agent Skills I Use Every Day
Matt Pocock
Subscribe
Copy page Copy page Share
On this page
1. `/grill-me`: Flesh Out an Idea
I've been an engineer for nearly a decade. Right now, process has never been more important.
You have access to a fleet of middling to good engineers that you can deploy at any time. But these engineers have a critical flaw: they have no memory. They don't remember things they've done before.
This means you need extremely strict and well-defined processes to get them to do useful work. As a developer, you're constantly steering your agents, keeping them on the right track.
My way of fixing this has been to create a LOT of agent skills. Each skill I've designed helps me encode my process so that AI has a strict path to follow every single time:
![Image 2: Repository of engineer skills and processes](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_3840/f_auto/q_auto/v1773675111/ai-hero-images/pgyy6kr82bhjliy774jx?_a=BAVMn6DY0)
The result? The code quality that AI produces has shot up dramatically.
**The kit:**[grill-me](https://www.aihero.dev/skills-grill-me) · [to-prd](https://www.aihero.dev/skills-to-prd) · [to-issues](https://www.aihero.dev/skills-to-issues) · [tdd](https://www.aihero.dev/skills-tdd) · improve-codebase-architecture · [see all skills →](https://www.aihero.dev/skills)
## [1. `/grill-me`: Flesh Out an Idea](https://www.aihero.dev/5-agent-skills-i-use-every-day#1-grill-me-flesh-out-an-idea)
[Read the guide](https://www.aihero.dev/skills-grill-me) · [GitHub](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)
npx skills@latest add mattpocock/skills
This is my favorite skill. It's only three sentences long, but it's incredibly impactful.
**The Grill Me Skill:**
> Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one. And finally, if a question can be answered by exploring the code base, explore the code base instead.
The concept of a "design tree" comes from _The Design of Design_ by Frederick P. Brooks. It's the idea that as you're designing something, you need to walk down all of the branches of a design tree.
For example, you might be designing a search page and need to decide between an advanced search interface or a simple text box. If you choose advanced search, you need to figure out all the filters and sorting methods. You keep walking down the tree until you've fully understood your design before committing to code.
![Image 3: Claude asking clarifying questions about a feature](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_3840/f_auto/q_auto/v1773

## Summary

675112/ai-hero-images/p1coswbfzivaglbxkose?_a=BAVMn6DY0)
When I invoke this skill, I want to reach a shared understanding with the LLM. Claude Code tends to spit out a plan really early when in plan mode, creating a document before we've truly understood each other. But the grill me skill forces that conversation.
In one conversation about adding a feature to my course video editor, Claude asked me 16 questions. And that was a relatively short grilling session. I've had sessions lasting nearly half an hour with 30, 40, or even 50 questions on really complex features.
![Image 4: 16 interview questions displayed in the conversation](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_3840/f_auto/q_auto/v1773675113/ai-hero-images/a0vvhui4lkubi5b2aqq9?_a=BAVMn6DY0)
**The key takeaway: Skills don't have to be long to be impactful. You just need to choose the right words at the right time.**
## [2. `/to-prd`: From Conversation to Document](https://www.aihero.dev/5-agent-skills-i-use-every-day#2-to-prd-from-conversation-to-document)
[Read the guide](https://www.aihero.dev/skills-to-prd) · [GitHub](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd)
npx skills@latest add mattpocock/skills
Once I've reached a shared understanding with the LLM, I invoke my next skill: `/write-a-prd`.
This skill asks the LLM to create a Product Requirements Document. It may skip steps if they're not necessary. For example, if you've already done a deep interview, it moves straight to step four.
The workflow includes:
* Ask the user for a detailed description
* Explore the repo to verify assertions
* Interview the user relentlessly (using the grill me skill)
* Sketch out major modules needed
* Write the PRD using a template and submit as a GitHub issue
The important part of any PRD is the user stories. These describe the desired behavior of your system in language, drawing from Agile methodology.
![Image 5: User stories section of a PRD](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_3840/f_auto/q_auto/v1773675114/ai-hero-images/mpombfwy8uz2rr1xy1yi?_a=BAVMn6DY0)
## [3. `/to-issues`: Breaking Down the Destination into a Journey](https://www.aihero.dev/5-agent-skills-i-use-every-day#3-to-issues-breaking-down-the-destination-into-a-journey)
[Read the guide](https://www.aihero.dev/skills-to-issues) · [GitHub](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues)
npx skills@latest add mattpocock/skills
The PRD describes your destination. But what you really need is the journey to get there.
That's what the PRD to Issues skill does. It takes a PRD and turns it into a Kanban board of independently grabbable issues.
The process:
1. Locate the PRD (fetch it if needed)
2. Explore the code base
3. **Draft vertical slices** - break the PRD into tasks that flush out unknown unknowns quickly
The [tracer bullet](https://www.aihero.dev/tracer-bullets) analogy applies here. Each issue is a thin vertical slice cu

## Related Articles

- [[Automating Ai Away]]
- [[The Illustrated Stable Diffusion]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Generative AI Strategy]]
