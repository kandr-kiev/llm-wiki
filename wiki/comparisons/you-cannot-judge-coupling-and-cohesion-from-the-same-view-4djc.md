---
title: "you cannot judge coupling and cohesion from the same view 4djc"
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
  - vector-database
  - video-generation
  - web
---

# you cannot judge coupling and cohesion from the same view 4djc

> **Source:** you-cannot-judge-coupling-and-cohesion-from-the-same-view-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/tbson87/you-cannot-judge-coupling-and-cohesion-from-the-same-view-4djc ingested: 2026-07-18 sha256: bfba69f71124073a6093099738e9a9ca950910ec6a6a8965d27663d287d6a0f1 blog...
> **Sources:**
>   - you-cannot-judge-coupling-and-cohesion-from-the-same-view-2026-07-18.md
> **Links:**
- [[stop hand translating between sql and your erd 4ohm]]
- [[adding an ai chatbot to echostats 290m]]
- [[my insights on what working at big tech is actually like kgd]]
- [[how we beat hotspot performance by cheating but not like that]]
- [[the gitbook migration trap 4gp2]]

## Key Findings

---
source_url: https://dev.to/tbson87/you-cannot-judge-coupling-and-cohesion-from-the-same-view-4djc
ingested: 2026-07-18
sha256: bfba69f71124073a6093099738e9a9ca950910ec6a6a8965d27663d287d6a0f1
blog_source: Dev Community
---
You Cannot Judge Coupling and Cohesion From the Same View - DEV Community
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
[
![Cover image for You Cannot Judge Coupling and Cohesion From the Same View](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fschemity.com%2Fimages%2Fblog%2Fyou-cannot-judge-coupling-and-cohesion-from-the-same-view%2Fbanner.webp)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fschemity.com%2Fimages%2Fblog%2Fyou-cannot-judge-coupling-and-cohesion-from-the-same-view%2Fbanner.webp)
[![Son Tran](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F79995%2F6de9d37a-5521-4b7a-a835-9787e74caf0c.jpg)](/tbson87)
[Son Tran](/tbson87)
Posted on Jul 18
• Originally published at [schemity.com](https://schemity.com/blog/you-cannot-judge-coupling-and-cohesion-from-the-same-view) 
# 
You Cannot Judge Coupling and Cohesion From the Same View
[#database](/t/database)
[#architecture](/t/architecture)
[#softwareengineering](/t/softwareengineering)
[#sql](/t/sql)
*Disclosure: I build [Schemity](https://schemity.com), a desktop ERD tool - this post is from our blog and uses it for the e

## Summary

xamples.*
>
**TL;DR:** Coupling and cohesion are questions at two different scales, and one diagram cannot answer both. Schemity's main view shows the cross-context edges that measure coupling; its context views isolate one domain to judge cohesion.
Every engineer can recite the goal: low coupling, high cohesion. Fewer dependencies between modules, more relatedness inside each one. We say it so often that it sounds like one rule. It is two, and they live at two different scopes. Judging coupling takes a whole-schema main view; judging cohesion takes an isolated context view - two questions, two diagrams.
Coupling is a property of the **boundaries**. It is about what crosses between modules. Cohesion is a property of the **interior**. It is about whether the things inside a module belong together. A diagram that is good at showing one is usually bad at showing the other, because the scope you need to see is different. To judge coupling you zoom out until the boundaries are visible. To judge cohesion you zoom in until a single module fills the frame and nothing else competes for attention.
This is why I gave Schemity two kinds of view, and why I keep using my own auth schema as the example.
## 
The main view is for reasoning about coupling
[![Main view: every context on one canvas, the cross-context relationships standing out as the coupling surface](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fimdvub9y56y4pkzslegz.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fimdvub9y56y4pkzslegz.png)
The main view shows every context at once: `auth`, `account`, `audit`, `localization`. You are not meant to read individual columns here. You are meant to read the **edges that cross context borders**.
Look at where lines leave the `auth` box. `roles.tenant_id` reaches into `account`. `sso_configs.tenant_id` does the same. `member_roles.member_id` points at `members`. `otps` carries both `tenant_id` and `member_id`. That bundle of crossing edges is the entire coupling surface between authentication and the account model. It is small, and it is all of the same shape: a tenant or a member identity flowing inward. That is what loose coupling looks like in practice. Not zero dependencies, but few dependencies, all pointing the same way, all explainable in one sentence.
If that surface were wide and tangled, no amount of clean code inside the contexts would save the design. You would feel it as the change that always spreads. The main view is where you catch that early, before it is written into a hundred files.
[The small markers on frontier tables](https://schemity.com/blog/a-view-owes-you-back-the-context-it-removes) are doing exactly this job. They flag the tables that participate in a cross-cont

## Related Articles

- [[stop hand translating between sql and your erd 4ohm]]
- [[adding an ai chatbot to echostats 290m]]
- [[my insights on what working at big tech is actually like kgd]]
- [[how we beat hotspot performance by cheating but not like that]]
- [[the gitbook migration trap 4gp2]]
