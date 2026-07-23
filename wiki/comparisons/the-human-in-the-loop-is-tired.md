---
title: "the human in the loop is tired"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - async
  - container
  - data
  - image-generation
  - news
  - prompt-engineering
  - self-supervised
  - software
---

# the human in the loop is tired

> **Source:** the-human-in-the-loop-is-tired-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://pydantic.dev/articles/the-human-in-the-loop-is-tired ingested: 2026-07-17 sha256: 3d5ddc61583f420e4e2ec4ad089661f3233a09e749dfae5bf4b6f56294497980 blog_source: Hacker News ---...
> **Sources:**
>   - the-human-in-the-loop-is-tired-2026-07-17.md
> **Links:**
- [[Automating Ai Away]]
- [[Automating away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[5 Agent Skills I Use Every Day]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]

## Key Findings

---
source_url: https://pydantic.dev/articles/the-human-in-the-loop-is-tired
ingested: 2026-07-17
sha256: 3d5ddc61583f420e4e2ec4ad089661f3233a09e749dfae5bf4b6f56294497980
blog_source: Hacker News
---
The Human-in-the-Loop is Tired- - - - - - - - - - - - - - - - <astro-island uid="ZatWIX" prefix="r3" component-url="/_astro/ArticlePost.BMmrMWGB.js" component-export="default" renderer-url="/_astro/client.bNyakri2.js" props="{"post":[0,{"date":[0,"2026-02-18T09:00:00.000Z"],"title":[0,"The Human-in-the-Loop is Tired"],"description":[0,"On reward functions, dopamine, and what it actually feels like when the code starts writing itself"],"seoTitle":[0,"The Human-in-the-Loop is Tired"],"seoDescription":[0,"On reward functions, dopamine, and what it actually feels like when the code starts writing itself"],"seoKeywords":[0,"AI, LLMs, developer experience, human-in-the-loop, software engineering, AI-assisted programming"],"readtime":[0,"8 mins"],"authors":[1,[[0,{"name":[0,"Laura Summers"],"picture":[0,"https://avatars.githubusercontent.com/u/6570564"]}]],"categories":[1,[[0,"Pydantic AI"],[0,"Company"]],"slug":[0,"the-human-in-the-loop-is-tired"],"content":[0,"\nYet another thought piece about LLMs. I know. Bear with me.\n\nThis is an attempt to put words around something I think most developers are experiencing right now but haven't had time to make sense of. **Programming with LLMs is genuinely useful and genuinely destabilizing. These two things coexist. If we pretend the second one isn't happening, we will all burn out.**\n\nAt [Pydantic](https://pydantic.dev), we build tools that developers use to [validate data](https://pydantic.dev/docs/validation/latest/get-started/), [build AI agents](https://pydantic.dev/pydantic-ai), and [observe what their systems are doing](https://pydantic.dev/logfire) in production. We are, quite literally, in the business of making LLM-powered software more reliable. And we are _also_ having a weird time.\n\nThis isn't a thinkpiece about whether AI will replace programmers. It's not a doomer essay and it's not a hype piece. It's an honest account of what it feels like to be a developer right now, from someone inside it, and some thoughts on what might actually help.\n\n## Hands in the fabric\n\nWhen I was first learning to code in my early twenties, I remember having this distinct sensation that programming let me dip my hands into the fabric of the universe and shape it to my will. This was, of course, before I'd hit too many compile errors. But that feeling of touching some deep fundamental layer of abstraction, of being able to _make things_ from nothing but logic, has always stuck with me.\n\nI'm not a Computer Science graduate. I'm a designer and a programmer — formally trained in the first, self-taught in the second. I came to the formalisms of software engineering through painful experience rather than academic instruction. If anything, that made me take those principles _more_ seriously once I understood them. Wh

## Summary

en you've earned your opinions about architecture and code quality the hard way, they feel less like textbook rules and more like scar tissue.\n\nThat primal feeling of creation? It's the same promise that the low-code and no-code tools of the 2010s kept making but never quite delivered on. I'm old enough to remember building web pages in Dreamweaver, watching Adobe spruik zero-code design tools that generated absolute spaghetti under the hood. It was always _almost_ there, just good enough to hint at a future that was just around the corner (if only you were smart enough to grasp it).\n\nIf you're cynical about the current wave of AI tools, I get it. We've been promised this before. But this time the gap between promise and reality has actually, finally, narrowed to something meaningful. And that's exactly what makes it so unsettling.\n\n## What \"the code writes itself\" actually feels like\n\n![](/assets/blog/human-in-the-loop-is-tired/hero.png)\n\nYes the code (sorta) writes itself, but the human reviewing, directing, and course-correcting feels worse, not better.\n\nI recently had a conversation with my colleague [Douwe](https://github.com/DouweM), who maintains the Pydantic AI framework and has been one of the most thoughtful people I know about integrating LLMs into open source workflows. He described waking up to thirty PRs every morning, each one pulled overnight by someone's AI, and needing to make snap judgment calls on every single one. The temptation to delegate the review itself to an AI was enormous. But, as he put it: _\"at that point, what am I still doing here?\"_.\n\nThe honest truth is that in the last few months, there have been days when I have spent close to two full days writing a plan for an LLM to execute: obsessively clarifying, specifying, re-specifying, only to have it still do something inexplicably stupid. Port a React hook into a Storybook story file. Read from the wrong plan. Invent components that don't exist. And these aren't errors of capability; they're errors of coherence. The models are smart enough to produce plausible code, but not always smart enough to maintain a coherent intent across a complex change.\n\nThis creates a peculiar new kind of fatigue, the fatigue of _supervision_: of holding the intent in your head while the machine generates volumes of mostly-correct output that still needs your eyes, your judgment, and your taste. Douwe put it well: he used to get a dopamine hit from collaborating with a real person on a cool feature in open source. Helping someone become better at their craft. Now, he said, _\"everything I write goes into some AI black hole. There's no person on the other side actually learning anything.\"_ That loss is real and it's worth naming.\n\n## The intensity trap\n\n[Simon Willison](https://simonwillison.net/2026/Feb/9/ai-intensifies-work/) recently highlighted a [Berkeley Haas](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it) study which describes how AI usage

## Related Articles

- [[Automating Ai Away]]
- [[Automating away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[5 Agent Skills I Use Every Day]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
