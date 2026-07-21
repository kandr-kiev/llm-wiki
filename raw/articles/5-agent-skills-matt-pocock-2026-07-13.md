---
title: "5 Agent Skills I Use Every Day"
source_url: "https://www.aihero.dev/5-agent-skills-i-use-every-day"
blog_source: "aihero.dev"
author: "Matt Pocock"
ingested: "2026-07-13"
sha256: 082c76f06abd0ca8ce12e74ada1304a59533b5cc80e003c53301ba868e8e0526
---

# 5 Agent Skills I Use Every Day

Matt Pocock

Subscribe
Copy page Copy page Share

On this page
1.   `/grill-me`: Flesh Out an Idea

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

![Image 3: Claude asking clarifying questions about a feature](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_3840/f_auto/q_auto/v1773675112/ai-hero-images/p1coswbfzivaglbxkose?_a=BAVMn6DY0)

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

*   Ask the user for a detailed description
*   Explore the repo to verify assertions
*   Interview the user relentlessly (using the grill me skill)
*   Sketch out major modules needed
*   Write the PRD using a template and submit as a GitHub issue

The important part of any PRD is the user stories. These describe the desired behavior of your system in language, drawing from Agile methodology.

![Image 5: User stories section of a PRD](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_3840/f_auto/q_auto/v1773675114/ai-hero-images/mpombfwy8uz2rr1xy1yi?_a=BAVMn6DY0)

## [3. `/to-issues`: Breaking Down the Destination into a Journey](https://www.aihero.dev/5-agent-skills-i-use-every-day#3-to-issues-breaking-down-the-destination-into-a-journey)

[Read the guide](https://www.aihero.dev/skills-to-issues) · [GitHub](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues)

npx skills@latest add mattpocock/skills

The PRD describes your destination. But what you really need is the journey to get there.

That's what the PRD to Issues skill does. It takes a PRD and turns it into a Kanban board of independently grabbable issues.

The process:

1.   Locate the PRD (fetch it if needed)
2.   Explore the code base
3.   **Draft vertical slices** - break the PRD into tasks that flush out unknown unknowns quickly

The [tracer bullet](https://www.aihero.dev/tracer-bullets) analogy applies here. Each issue is a thin vertical slice cutting through all integration layers, not a horizontal slice of one layer.

The skill also establishes blocking relationships between tasks. For instance, one issue might not be blocked by anything, so it can be picked up independently. This is useful if you have parallel agent setups where multiple agents can work simultaneously.

![Image 6: Four GitHub issues created as vertical slices](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_3840/f_auto/q_auto/v1773675116/ai-hero-images/qaodyngpkcdpfwdvi1do?_a=BAVMn6DY0)

[![Image 7](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_384/f_auto/q_100/v1777381174/skills-newsletter-light?_a=BAVMn6DY0) AI Hero · Skill System ### There are more where these came from grill-with-docs, domain-model, and triage round out the kit — plus a changelog of updates as it evolves. See the skill set](https://www.aihero.dev/skills)
## [4. `/tdd`: Increasing Code Quality](https://www.aihero.dev/5-agent-skills-i-use-every-day#4-tdd-increasing-code-quality)

[Read the guide](https://www.aihero.dev/skills-tdd) · [GitHub](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)

npx skills@latest add mattpocock/skills

How do you execute on a skill? How do you make the implementation rock solid and increase code quality?

You use a TDD skill. TDD stands for Test-Driven Development, and it forces (or rather, encourages) the agent to follow a red-green-refactor loop.

This skill is substantial. It includes philosophy on refactoring, mocking, and what deep modules are. **Doing really good TDD has been the most consistent way to improve agent outputs.**

The workflow starts with confirming what interface changes are needed. When an AI looks at a bad codebase, it sees many tiny, undifferentiated modules. But if you restructure it into larger modules with thin interfaces on top, the AI can navigate it much more easily.

The skill then:

*   Confirm which behaviors to test
*   Design interfaces for testability
*   Write one test at a time (test first)
*   Implement code to make the test pass
*   Look for refactoring candidates

Red-green-refactor with agents is incredible. It creates a loop that continues until complete.

![Image 8: TDD workflow diagram showing the red-green-refactor cycle](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_3840/f_auto/q_auto/v1773675117/ai-hero-images/lz08tqnibbua15wpkq2n?_a=BAVMn6DY0)

## [5. `/improve-codebase-architecture`: Making Your Code Agent-Friendly](https://www.aihero.dev/5-agent-skills-i-use-every-day#5-improve-codebase-architecture-making-your-code-agent-friendly)

[View on GitHub](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)

npx skills@latest add mattpocock/skills

TDD demands a lot of your codebase. In a badly structured code base, test boundaries are unclear. Where should you test? At which layer?

When your code base has clear module boundaries, testing becomes much easier.

The `/improve-codebase-architecture` skill explores your codebase naturally, looking for confusions:

*   Where does understanding one concept require bouncing between many small files?
*   Where have pure functions been extracted just for testability, but real bugs hide in how they're called?
*   Where do tightly coupled modules create integration risk?

Then it presents candidates for deepening opportunities - chances to deepen shallow modules into deeper ones.

![Image 9: Three different interface designs presented side-by-side](https://res.cloudinary.com/total-typescript/image/upload/c_limit,w_3840/f_auto/q_auto/v1773675118/ai-hero-images/xcsyngiu3zdojvugipqz?_a=BAVMn6DY0)

Do this once a week or after a surge of development. As you keep refining your codebase, you'll notice the quality of the agent's output goes up.

**If you have a garbage code base, the AI will produce garbage within that code base.**

That's five of seven. The rest — grill-with-docs, domain-model, triage — and a changelog of updates live at [/skills](https://www.aihero.dev/skills).

## [Why This Matters: Treating AI Like Engineers](https://www.aihero.dev/5-agent-skills-i-use-every-day#why-this-matters-treating-ai-like-engineers)

The most successful way to get code quality up from agents is to treat them like humans. Humans with weird constraints, sure - humans with no memory who are cloned and go right to work. But humans nonetheless.

[Check out the skills repository](https://github.com/mattpocock/skills) to get started.

AI Hero · Skill System
### The kit keeps evolving
Get the next skill or guide the moment Matt ships it.

First Name 
Email*
Stay up to date
I respect your privacy. Unsubscribe at any time.

**Share**

[](https://x.com/intent/tweet?text=https%3A%2F%2Fwww.aihero.dev%2F5-agent-skills-i-use-every-day5%20Agent%20Skills%20I%20Use%20Every%20Day%20%20by%20%40mattpocockuk)[](https://bsky.app/intent/compose?text=5%20Agent%20Skills%20I%20Use%20Every%20Day%20%20by%20%40mattpocock.com%0A%0A%20%20%20%20%20%20%20%20https%3A%2F%2Fwww.aihero.dev%2F5-agent-skills-i-use-every-day)[](https://linkedin.com/share-article?mini=true&url=https%3A%2F%2Fwww.aihero.dev%2F5-agent-skills-i-use-every-day%3Fauthor%3DMatt%20Pocock)Copy URL

## Up Next

### My 'Grill Me' Skill Went Viral

[](https://www.aihero.dev/my-grill-me-skill-has-gone-viral)

[Log in](https://www.aihero.dev/login)to save progress.

### Learn

*   [AI SDK v6 Crash Course](https://www.aihero.dev/workshops/ai-sdk-v6-crash-course)
*   [LLM Fundamentals](https://www.aihero.dev/llm-fundamentals)
*   [AI Coding Dictionary](https://www.aihero.dev/ai-coding-dictionary)
*   [The AI Engineer Roadmap](https://www.aihero.dev/ai-engineer-roadmap)
*   [Vercel AI SDK Tutorial](https://www.aihero.dev/vercel-ai-sdk-tutorial)
*   [Model Context Protocol Tutorial](https://www.aihero.dev/model-context-protocol-tutorial)

### Live

*   [AI Coding for Real Engineers](https://www.aihero.dev/cohorts/ai-coding-for-real-engineers-m0k0w)

### Account

*   [Log in / Sign up](https://www.aihero.dev/login)

### Agents

*   [sitemap.md](https://www.aihero.dev/sitemap.md)
*   [llms.txt](https://www.aihero.dev/llms.txt)
*   [skills.md](https://www.aihero.dev/skills.md)
*   [rss.xml](https://www.aihero.dev/rss.xml)

[Browse All](https://www.aihero.dev/posts)·[Dictionary](https://www.aihero.dev/ai-coding-dictionary)·[Skills](https://www.aihero.dev/skills)·[Skills Newsletter](https://www.aihero.dev/skills/subscribe)·[FAQ](https://www.aihero.dev/faq)·[Terms](https://www.aihero.dev/privacy)system Theme