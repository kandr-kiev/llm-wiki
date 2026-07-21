---
title: "vision doc journeys to learning rust"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - computer-vision
  - evaluation
  - governance
  - image-generation
  - industry
  - machine-learning
  - nlp
  - prompt-engineering
  - real-time
  - research
  - self-supervised
  - software
  - streaming
  - system-design
  - tool
  - use-case
  - video-generation
  - zero-shot
---

# vision doc journeys to learning rust

> **Source:** the-many-journeys-of-learning-rust-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** [ ![](https://blog.rust-lang.org/images/rust-logo-blk.svg) Rust Blog ](https://blog.rust-lang.org/) - [Rust](https://www.rust-lang.org) - [Install](https://www.rust-lang.org/tools/install) - [Learn](h...
> **Sources:**
>   - the-many-journeys-of-learning-rust-2026-07-17.md
> **Links:**
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[Applying Massive Language Models In The Real World With Cohere]]
- [[Automating away]]
- [[ai]]

## Key Findings

[
![](https://blog.rust-lang.org/images/rust-logo-blk.svg)
Rust Blog
](https://blog.rust-lang.org/)
- [Rust](https://www.rust-lang.org)
- [Install](https://www.rust-lang.org/tools/install)
- [Learn](https://www.rust-lang.org/learn)
- [Tools](https://www.rust-lang.org/tools)
- [Governance](https://www.rust-lang.org/governance)
- [Community](https://www.rust-lang.org/community)
🖌
- Light
- Dark
- System
## The many journeys of learning Rust
June 25, 2026 · Pete LeVasseur
on behalf of [Vision Doc group](https://www.rust-lang.org/governance/teams/launching-pad#team-project-vision-doc-2025) 
*This is another post in our series covering what we learned through the Vision Doc process. We previously described the overall approach and what we learned about doing user research, we explored what people love about Rust, dug into what it takes to ship safety-crticial Rust, and described some of the major challenges that people face when using Rust.*
In this post we walk through what folks have found on their journey to learn the Rust programming language with ups and downs covered.
As a disclaimer, LLMs (Large Language Models) come up in this post because our interviewees brought them up. We're scoping discussion to their use as a learning tool, covering research and example generation, not broader questions about AI (Artificial Intelligence) in software development.
# [](#many-paths-to-needing-rust)
Many paths to needing Rust
The interviews surfaced several different paths into Rust: curiosity, embedded work, job-market pressure, organizational adoption, and reassignment after a team or company chose Rust. That last path matters because many learners are not evaluating Rust from a blank slate; they are trying to become productive after Rust has already arrived in their work.
>
"Funny enough, I've advocated for more niche languages than Rust in the past. Rust has pretty much stopped being as much of a niche language as it was, but it's not Java." -- Fractional CTO
# [](#rust-learning-resources)
Rust learning resources
Likely as expected, the folks that we talked to reach for a range of resources to learn Rust. Some reach for official documentation, such as The Rust Programming Language Book and find that sufficient to build on what the compiler was already showing them.
>
"I started with the official Rust documentation because there are a lot of great examples of how features like the borrow checker work." -- Software engineer at an Automotive supplier
Others needed more passes and more formats, sometimes reaching for resources the community maintains, such as Rustlings, The Little Book of Rust Macros, and Learn Rust With Entirely Too Many Linked Lists.
>
"The first time I went through the chapter in [The Rust Programming Language] on borrow checking, I was like, what is this? I read it again, then I watched a YouTube video of someone explaining the chapter." -- Rust freelance consultant
>
"Rust book, Rustlings, Zero to Production in Rust, Jon Gjengset tutori

## Summary

als. A bunch of books. It's not a one-pass reading. Can't say how many times I've gone through it." -- Software engineer working on video streaming and storage
These resources have brought up an entire generation of Rust programmers. But, to some, there is a perception that these resources have trouble keeping pace with the language.
>
"We'd like to use [The Rust Programming Language/'the book'], but we've found that it's out of date, unfortunately. We've looked at the GitHub repo and found it's got a lot of unresolved issues and unmerged PRs" -- Principal Software Engineering work on Rust adoption in a regulated industry
Whether or not this is factually true, Rust's growth has nonetheless put more scrutiny on these materials. Companies evaluating adoption and engineers getting reassigned to Rust teams are looking at them with fresh eyes and finding the gaps that affect their own evaluation.
# [](#beginner-stumblings-and-unlearning-habits)
Beginner stumblings and unlearning habits
It's pretty typical for Rust to be the 2nd, 3rd or Nth programming language that someone picks up. They'd end up writing their most familiar language in Rust, whether C++ patterns, Java patterns, or whatever they knew, for months or even years. Eventually they got comfortable enough to start writing idiomatic Rust.
>
"There's a bit of a drop in productivity compared to C if you're already familiar with it just because you're learning new rules, new syntax." -- Principal Firmware Engineer (mobile robotics)
>
"In the beginning it was more poking around the code and adding and removing some ampersands and asterisks to try to make sense of `mut` and not `mut` and whatever." -- Senior engineer with 20 years of Java experience in cloud and IoT
We also spoke with someone who found that not having much of a programming background seemed to benefit people picking up Rust. Not having worn-in grooves from other languages may play a role here, and it's worth investigating further.
>
"I had someone who had never programmed much before start working on the internals of [our Rust project]. She was just fine with getting into Rust. It's more of the senior people that struggle as they need to unlearn practices which may work in other languages, but it's not the 'Rust' way." -- Researcher, Automotive OEM R&D Lab
# [](#learning-to-work-with-the-borrow-checker)
Learning to work with the borrow checker
We heard a lot about learning to work with the borrow checker instead of against it. People get there through different paths, but a few patterns came up repeatedly.
## [](#the-compiler-as-teacher)
The compiler as teacher
Rust's diagnostics did the teaching on their own, especially around lifetimes.
>
"If you mess up the lifetimes in a piece of code that you've written by hand, I usually find that Rust's diagnostics are very helpful" -- Researcher working on static analysis of Rust programs
>
"Whatever's missing, the compiler usually fills in: it tells me 'you need to declare the lifetime of 

## Related Articles

- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[Applying Massive Language Models In The Real World With Cohere]]
- [[Automating away]]
- [[ai]]
