---
title: "less art more engineering it wasnt measurement"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - architecture
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - search
  - software
  - standards
  - video-generation
  - web
---

# less art more engineering it wasnt measurement

> **Source:** less-art-more-engineering-it-wasnt-measurement-2026-07-21.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/siy/less-art-more-engineering-it-wasnt-measurement-2916 ingested: 2026-07-21 sha256: 4ec754bec5d16f1e20bfb05046998655c27d0ec83ff8e8cc849e65ae1d2c8a06 blog_source: Dev Co...
> **Sources:**
>   - less-art-more-engineering-it-wasnt-measurement-2026-07-21.md
> **Links:**
- [[its ok to get lucky 1laf]]
- [[i tried kimi k3 for a week heres what happened]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[starting my developer journey bh8]]
- [[adding an ai chatbot to echostats 290m]]

## Key Findings

---
source_url: https://dev.to/siy/less-art-more-engineering-it-wasnt-measurement-2916
ingested: 2026-07-21
sha256: 4ec754bec5d16f1e20bfb05046998655c27d0ec83ff8e8cc849e65ae1d2c8a06
blog_source: Dev Community
---
Less Art, More Engineering: It Wasn't Measurement - DEV Community
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
[Skip to content](#main-content)
Navigation menu
[
![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)
](/)
Search
[
Powered by Algolia
Search
](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)
[
Log in
](https://dev.to/enter?signup_subforem=1)
[
Create account
](https://dev.to/enter?signup_subforem=1&state=new-user)
## DEV Community
Close
![](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)
Add reaction
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
Like
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
Unicorn
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
Exploding Head
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
Raised Hands
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
Fire
Jump to Comments
Save
Boost
More...
Copy link
Copy link
Copied to Clipboard
Share to X
Share to LinkedIn
Share to Facebook
Share to Mastodon
[Share Post via...](#)
[Report Abuse](/report-abuse)
[![Sergiy Yevtushenko](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F145374%2F6e93547b-45cc-430e-9659-3adea03266b5.jpeg)](/siy)
[Sergiy Yevtushenko](/siy)
Posted on Jul 21
# 
Less Art, More Engineering: It Wasn't Measurement
[#softwareengineering](/t/softwareengineering)
[#architecture](/t/architecture)
[#programming](/t/programming)
[#softwaredesign](/t/softwaredesign)
# 
Less Art, More Engineering: It Wasn't Measurement
Two and a half years ago I wrote an article called ["Less Art, More Engineering"](https://medium.com/@sergiy-yevtushenko/less-art-more-engineering-c01582feb7cb). The argument was simple: software development calls itself engineering but mostly isn't, because it runs on subjective criteria with no verifiable definitions. Readability with no metric. Best practices that contradict each other. Design methods that offer no way to check whether a design is correct. I ended on a promise: the next step is to convert what we know into a set of clearly defined, well grounded rules and criteria. "Ideally measurable," I wrote, "but in either case easily verifiable."
I want to report back on th

## Summary

at promise, because I got the diagnosis right and the cure wrong.
None of this began as a plan. The original goal was modest: organize code so its structure would be recognizable and its behavior predictable. I had nothing in mind beyond that. But the moment I asked what actually makes structure recognizable, the question refused to stay small. Answering it meant understanding low-level structure and the forces that shape it, and each answer uncovered the next one. That inquiry grew into Process-First Design, and Process-First Design in turn produced Architecture Synthesis. I set out to tidy functions and ended up deriving systems.
## 
What I tried
In 2025 I made the first real attempt, in an article called ["Beyond Best Practices"](https://medium.com/codex/beyond-best-practices-e36511c073e2). Instead of collecting an endless pile of best practices, I proposed five criteria to assess any coding decision: mental overhead, business/technical ratio, design impact, reliability, and complexity. Five stable criteria in place of countless ad-hoc rules. They work. You can hold two approaches against them and get a defensible comparison, and I still use them.
But look at what happened to the word "measurable" between the two articles. In 2023 I wanted measurement. By 2025 I was already writing that the criteria "could be either somehow measured or, at least, checked for presence/absence," and that "absolute numbers might not be that useful per se" as long as they "enable objective comparison." I had quietly retreated from measuring to comparing, and I had not noticed. That erosion, measurable to comparable to merely present-or-absent, was the whole story trying to surface. I just wasn't listening to it yet.
There was a second thing I glossed over. I called them "my own set of criteria." I chose those five, and I chose that they matter. The subjectivity I set out to remove had not left. It had gotten smaller and moved somewhere I could see it, but it was still mine.
## 
What surprised me
Here is the part I did not expect. The thing that actually removed subjective technical decisions was not measurement at all. It was determinism.
A measurement gives you a number. A derivation gives you an answer that two people, starting from the same inputs and following the same rules, both reach, without either of them exercising taste. That second property is what I had wanted the whole time. I had assumed the only road to it was to measure things, so I chased metrics for two years. But you do not need to measure anything to be objective in the way that matters. You need the decision to be derived by a fixed procedure rather than chosen by judgment. A derivation is reproducible even when nothing on the page is a number.
I had been treating "objective" and "measured" as the same word. Under contact with real work they came apart, and the one that did the job was not the one I had bet on.
The clearest case is architecture. I built a [procedure](https://pragmatica.dev/me

## Related Articles

- [[its ok to get lucky 1laf]]
- [[i tried kimi k3 for a week heres what happened]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[starting my developer journey bh8]]
- [[adding an ai chatbot to echostats 290m]]
