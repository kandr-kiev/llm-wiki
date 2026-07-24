---
title: "my insights on what working at big tech is actually like kgd"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - search
  - software
  - video-generation
  - web
---

# my insights on what working at big tech is actually like kgd

> **Source:** my-insights-on-what-working-at-big-tech-is-actually-like-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/shayesta/my-insights-on-what-working-at-big-tech-is-actually-like-kgd ingested: 2026-07-18 sha256: d8463891e50a50f206576d3f96c2af8fd1632a6c4223265b89e9f7f61600c980 blog_...
> **Sources:**
>   - my-insights-on-what-working-at-big-tech-is-actually-like-2026-07-18.md
> **Links:**
- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[5-things-i-learned-doing-ai-evaluation-for-2-years-3kgh]]
- [[how-we-beat-hotspot-performance-by-cheating-but-not-like-that]]
- [[the-gitbook-migration-trap-4gp2]]

## Key Findings

---
source_url: https://dev.to/shayesta/my-insights-on-what-working-at-big-tech-is-actually-like-kgd
ingested: 2026-07-18
sha256: d8463891e50a50f206576d3f96c2af8fd1632a6c4223265b89e9f7f61600c980
blog_source: Dev Community
---
My insights on What Working at Big Tech Is Actually Like - DEV Community
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
[![shayesta](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F384148%2F6b3ec9ff-c989-41a5-b7ba-5232cf3faf3a.jpg)](/shayesta)
[shayesta](/shayesta)
Posted on Jul 18
# 
My insights on What Working at Big Tech Is Actually Like
[#career](/t/career)
[#discuss](/t/discuss)
[#watercooler](/t/watercooler)
[#softwareengineering](/t/softwareengineering)
When I was a student, I had a picture in my head of what working at a big tech company would be like. It came from the places any student's picture comes from: open-source projects, side projects, and coursework. That picture turned out to be accurate about some things and completely off about others.
None of that is a knock on the job. It's just that the day-to-day of large-scale engineering is genuinely different from what smaller-scale work prepares you for, and most people don't find that out until they're in it.
So if you're a student, a new grad, or someone eyeing the jump, here's the honest picture of what it's actually like. Not the recruiting version. The real texture of the work.
## 
Most of the design is already done
In school, alm

## Summary

ost every project starts from a blank page. Build a distributed system. Model this domain. Pick an architecture and defend it. The blank page is the whole point — you're being taught to make decisions.
At a large company, you're usually joining something that already exists, and it exists at a scale that took years and many people to build. The architecture is set. The service boundaries are drawn. The data model and deployment patterns are in place, and usually for good reasons that predate you.
So your work happens *inside* that structure. You still make design decisions, but they're smaller and more local — how to build your piece well, not what the whole system should look like. The big architectural questions were answered before you arrived.
This surprises a lot of new grads, and it's worth understanding early, because it reframes what "good work" means. It's less about inventing structure and more about working skillfully within it. Different muscle, and a genuinely valuable one.
## 
Your tools will be unfamiliar, even the familiar ones
I came in comfortable with the standard open-source stack — Maven, Gradle, the usual deployment tooling. I could build, test, and ship, and I'd done it enough to feel solid.
Then I learned that a company operating at this scale tends to build its own internal versions of almost everything. Its own build system, its own deployment tooling, its own monitoring and service frameworks, shaped around problems most open-source tools were never designed for.
The interesting part is that the concepts transfer even when the tools don't. It's all still builds, pipelines, and dependency graphs underneath. But knowing the open-source version doesn't mean you can skip learning the internal one — you learn it fresh, and lean on the concepts rather than the specifics. It's a humbling first few months, and then one day the internal tools stop feeling foreign and start feeling like tools.
A tip for anyone about to go through this: the discomfort of relearning familiar-feeling things is normal and temporary. It's not a sign you were underprepared.
## 
A lot of the job is understanding, not writing
Here's something school doesn't quite prepare you for: at scale, the systems are too large for any one person to hold in their head.
That changes the nature of the work. A big part of senior engineering turns out to be *holding context* — knowing why a service behaves the way it does, which team owns which piece, what was tried before and why it didn't work. Much of that knowledge isn't written down. It lives with people, and it moves through conversations.
Which means the job is more collaborative than the heads-down stereotype suggests. Not in a politics sense — just that the information you need often isn't in any document, and knowing how to find the right person and ask a good question becomes a real, everyday skill. Learning who knows what is part of learning the system.
## 
Debugging is more like detective work
When a project

## Related Articles

- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[5-things-i-learned-doing-ai-evaluation-for-2-years-3kgh]]
- [[how-we-beat-hotspot-performance-by-cheating-but-not-like-that]]
- [[the-gitbook-migration-trap-4gp2]]
