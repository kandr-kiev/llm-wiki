---
title: "away"
type: comparison
tags: [comparison]
description: Comparison page for away

sources: []
links: []
description: Comparison page for away

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
contested: false

---
# away

> **Source:** automating-ai-away-2026-07-07.md
> **Type:** comparison
> **Created:** 2026-07-08

## Key Findings

[
![](/assets/img/tool.jpg)
Beagle SCM
](/)
# Automating away
![Escher: Stars](./img/stars.jpg#rightw40) A. Karpathy once said that OpenAI researchers are effectively "automating themselves away" by improving their AI. Right now I develop Beagle SCM with Anthropic's Fable and it is of course a brilliant model able to spot nits in a mountain of code, file tickets, make fixes. Still, yesterday it managed to commit the `build/` dir into a project, twice. It is brilliant, but clumsy. 
Due to the nature of LLMs, this issue is not going away as they progress further. They tend to be imprecise and non-deterministic. [Ragel](https://www.colm.net/open-source/ragel/) the parser generator can "code" a 10 KLoC **formally** correct parser in an instant, deterministically. What about Claude? Well, my instructions say in all caps: DO NOT PARSE ANYTHING MANUALLY, EVER. It would be torturous and it would be faulty, just don't. It tries anyway, so periodically I tell it to scan the codebase to find and remove any attempts at manual parsing. That mostly works.
It becomes ever more brilliant, no less clumsy.
The way to deal with an expensive, slow, clumsy but brilliant LLM is to give it fast, powerful and deterministic tools AND to build the entire thing into a deterministic formal workflow. Make it faster, make it see the relevant stuff at the right time, make it less clumsy, make it self-correct. Sandwich that brilliant but inconsistent non-determinism between powerful deterministic tools and equally formal processes.
This story becomes even more interesting if we make the tools and processes malleable. That way, if Claude does some sequence of actions too often, we automate it. If it fails at something repeatedly, we automate the verification step.
Essentially, we let the LLM automate itself away, in favor of simple reliable deterministic tools.
Beagle SCM lets LLMs [script their own routines](./js.html) in JavaScript. While all the [heavy lifting](https://github.com/gritzko/libdog) is implemented in C and rarely touched, the tooling layer (the lower part of the sandwich) and the workflow layer (the upper part) are [all JavaScript](https://github.com/gritzko/beagle-ext) and pick their code from the filesystem, `node_modules`-style. Imagine `git` hooks that can tokenize source files in almost any language, inspect file history and commit history, cross-check links, and basically reach any data `git` can reach internally. That is Beagle.

## Summary

See Key Findings for full content.

## Related Articles

- [[automating-ai-away-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- 
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
