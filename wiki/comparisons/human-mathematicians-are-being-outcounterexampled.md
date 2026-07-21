---
title: "human mathematicians are being outcounterexampled"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - image-generation
  - library
  - news
  - reinforcement-learning
---

# human mathematicians are being outcounterexampled

> **Source:** human-mathematicians-are-being-outcounterexampled-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/ ingested: 2026-07-20 sha256: fd04298546f8bd29ff970a155b1dbe45d188fb2642add447999857004a5...
> **Sources:**
>   - human-mathematicians-are-being-outcounterexampled-2026-07-20.md
> **Links:**
- [[ai]]
- [[Automating away]]
- [[open source monopoly]]
- [[Automating Ai Away]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]

## Key Findings

---
source_url: https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/
ingested: 2026-07-20
sha256: fd04298546f8bd29ff970a155b1dbe45d188fb2642add447999857004a5f56b2
blog_source: Hacker News
---
Human mathematicians are being outcounterexampled | Xena
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
- 
- 
- - 
- 
- 
- 
- 
- 
[Xena](https://xenaproject.wordpress.com/)
Mathematicians learning Lean by doing.
[
![](https://xenaproject.wordpress.com/wp-content/uploads/2018/10/cropped-light2.png)
](https://xenaproject.wordpress.com/)
[Skip to content](#content)
- [Home](https://xenaproject.wordpress.com)
- [About Xena](https://xenaproject.wordpress.com/what-is-the-xena-project/)
- [Student projects](https://xenaproject.wordpress.com/student-projects/)
- Installing Lean and mathlib
- Bluesky
- [Useful links.](https://xenaproject.wordpress.com/useful-links/)
[← Formalizing Fermat workshop](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/)
## [Human mathematicians are being outcounterexampled](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/)
Posted on [July 20, 2026](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) by [xenaproject](https://xenaproject.wordpress.com/author/xenaproject/) 
It’s been an interesting few weeks for counterexamples. This post is basically my perspective of what has been going on in the world of formalization, AI tools and, in particular, counterexamples.
## Unit distance
Two months ago today (20th May 2026), ChatGPT disproved Erdős’ Unit Distance conjecture in discrete geometry. This is now old news but I had to start somewhere. The [announcement](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) was accompanied with testimonies by human mathematicians, many of whom I knew and a few of whom I trusted, saying that they believed the argument (they had been given early access to it and had checked it). The basic structure of the proof is that a profound theorem in number theory due to Golod and Shafarevich from the 1960s could be used to construct a counterexample to the conjecture.
It is now 9 years since I had a mid-life crisis, realised I no longer trusted many human mathematicians when it comes to technical details, discovered Lean, and started to argue that interactive theorem provers should play an important role in the future of mathematics. So of course my first question was “is the counterexample formalized in Lean”. The answer was “no”.
But under a week later (26th May 2026), I got an email from Fields Medallist Mike Freedman. Mike is now the Chief Science Officer for [Logical Intelligence](https://logicalintelligence.com/), a company cofounded by Turing Award winner and “godfather of AI” Yan LeCun. Mike informed me that their system had autoformalized the entire ChatGPT-generated paper in Lean and could I take a look. I looked, and my

## Summary

 post-doc Thomas Browning looked too. And indeed this was what Logical Intelligence had done: they had formalized precisely the statement that the profound theorem of number theory implied the Erdős counterexample. Breakthrough LLM-generated mathematics being formalized in real time. Interesting data point.
Of course there is an elephant in the room here though, the profound theorem of number theory which takes 100+ pages to prove (it needs huge chunks of global class field theory, a theory developed at the beginning of the 20th century and for which there are still no short proofs; it is proving difficult to compress). In 2025 I had run a [Clay Summer School](https://www.claymath.org/events/formalizing-class-field-theory/) with Richard Hill on the formalization of class field theory, and one year later we have nearly done the local case (it is the current PhD project of my student Edison Xie); the global case remained open, and indeed in 2025 formalizing global class field theory seemed like a fantasy.
One month later, on June 26th 2026, my perception of what was possible again changed. Boris Alexeev [announced on the Lean Zulip](https://leanprover.zulipchat.com/#narrow/channel/583339-AI-authored-projects/topic/Erd.C5.91s.20unit-distance.20counterexample.2C.20exponent.20above.201/near/606778508) that he had steered ChatGPT to a complete formalization of the Erdős counterexample, assuming nothing beyond the axioms of mathematics. Boris works at OpenAI and had used their new model Sol to do the autoformalization. Boris made the code public and it did not take long for me to realise that somewhere within all this AI-generated (and sometimes horrible, although sometimes decent) code was indeed a proof of some really hard theorems in global class field theory. Also of interest to me was that Sol had generated 1.2 million lines of Lean code in the three weeks that it had worked on the project. Lean’s fantastic (declaration of conflict of interest: I am a maintainer) mathematics library [mathlib](https://github.com/leanprover-community/mathlib4) is only 2.3 million lines of code, and took nine years to write. Perhaps it was at this point that the penny really dropped for me — large AI-generated developments of mathematics are inevitable. One cannot trust AI-generated code so I ran it in a sandbox on my machine (malicious Lean code can run arbitrary commands on your computer — Lean is a programming language, after all). Indeed, it was proving nontrivial theorems about the cohomology of number fields. Wow.
## Group schemes of order n
A week after Boris’ revelation, in early July, I was thinking hard about how to run my [Formalizing Fermat workshop](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/). This workshop was sponsored by [Logos Research](https://www.logosresearch.ai/), who, like Logical Intelligence (and Harmonic and Axiom AI and Moonshot AI and…) have a tool which can autoformalize mathematics — translating it from human

## Related Articles

- [[ai]]
- [[Automating away]]
- [[open source monopoly]]
- [[Automating Ai Away]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
