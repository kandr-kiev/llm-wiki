---
title: "ai can write code faster than i can responsibly review it 4ig4"
type: playbook
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - review
  - search
  - software
  - video-generation
  - web
confidence: medium
created: 2026-07-23
description: Auto-filled by Wiki Doctor
links: []
sources: []
updated: 2026-07-23
---
backlinks:
  - ai-can-write-code-faster-than-i-can-responsibly-review-it-4ig4
---


# ai can write code faster than i can responsibly review it 4ig4

> **Source:** ai-can-write-code-faster-than-i-can-responsibly-review-it-2026-07-22.md
> **Type:** playbook
> **Created:** 2026-07-23
> **Updated:** 2026-07-23
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/zenovay/ai-can-write-code-faster-than-i-can-responsibly-review-it-4ig4 ingested: 2026-07-22 sha256: 86d9e38e57290d2dc8d0e1b88eb7cb96b46e28d180c531cb5209d6725c0ce60e blog...
> **Sources:**
>   - ai-can-write-code-faster-than-i-can-responsibly-review-it-2026-07-22.md
> **Links:**
- [its ok to get lucky 1laf](https://dev.to/)
- [5 things i learned doing ai evaluation for 2 years 3kgh](https://dev.to/)
- [17 none of it was for me a year of building with ai 32kf](https://dev.to/)
- [adding an ai chatbot to echostats 290m](https://dev.to/)
- [class vs object who is the big boss 32nj](https://dev.to/)

## Key Findings

---
source_url: https://dev.to/zenovay/ai-can-write-code-faster-than-i-can-responsibly-review-it-4ig4
ingested: 2026-07-22
sha256: 86d9e38e57290d2dc8d0e1b88eb7cb96b46e28d180c531cb5209d6725c0ce60e
blog_source: Dev Community
---
AI Can Write Code Faster Than I Can Responsibly Review It - DEV Community
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
![Cover image for AI Can Write Code Faster Than I Can Responsibly Review It](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fxlucydmtr5kqfoatnc1y.png)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fxlucydmtr5kqfoatnc1y.png)
[![Zenovay](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3772909%2F8faf186c-8dcf-4cb1-bfcf-c5554bca55c8.webp)](/zenovay)
[Zenovay](/zenovay)
Posted on Jul 22
# 
AI Can Write Code Faster Than I Can Responsibly Review It
[#productivity](/t/productivity)
[#ai](/t/ai)
[#programming](/t/programming)
[#discuss](/t/discuss)
I use Claude Code almost every day while building Zenovay.
It can scaffold a feature, trace a bug across several files, write tests, refactor an old module, and explain an unfamiliar part of the codebase before I have finished my coffee.
That sounds like pure leverage.
But it created a problem I

## Summary

 did not expect:
**AI can produce code much faster than I can build a reliable mental model of it.**
The bottleneck is no longer writing code.
It is human attention.
## 
A large diff still feels like progress
There is something satisfying about watching an agent work through a task.
Files change. Tests appear. Type errors disappear. The terminal keeps moving.
Twenty minutes later, there is a 700-line diff and everything is green.
It feels like a productive session.
Then I open the diff and realize I cannot confidently explain every decision it made.
Why was this abstraction added?
Does this retry create duplicate events?
Is the permission check happening at the API boundary, or only in the interface?
What happens when the webhook arrives twice?
Did the code preserve the privacy rule I described three prompts ago?
The dangerous output is rarely code that obviously fails.
It is code that compiles, passes the happy-path test, and quietly implements the wrong assumption.
## 
Generation got cheap. Review did not.
Before coding agents, the effort required to write a feature naturally limited its size.
You had time to think while typing. You noticed awkward interfaces because you had to use them repeatedly. You remembered why a branch existed because you wrote it ten minutes earlier.
AI removes much of that friction.
That is useful, but the friction was also doing hidden work.
It slowed the amount of new code entering the system.
Now a solo developer can generate changes at something close to team velocity. The review capacity is still one person.
That creates a kind of review debt.
Every accepted line that I do not fully understand becomes a small future obligation. Maybe it is harmless. Maybe it becomes the function nobody wants to touch six months later because nobody remembers why it works.
The code was generated quickly.
The understanding was deferred.
## 
Some decisions should stay slow
While building an analytics product, small technical decisions can carry real consequences.
A mistake in attribution can show a customer the wrong acquisition channel.
A mistake in session replay can capture something that should have been masked.
A mistake in billing logic can affect real money.
A mistake in authorization can expose one customer's data to another.
I still use AI around all of these areas, but I do not let it silently decide the important boundaries.
There are a few things I now treat differently:
### 
Data and privacy boundaries
The agent can help implement the rule.
The rule itself has to come from me.
I want to know exactly what enters the system, where it is transformed, how long it stays, and what must never be stored.
### 
Authorization and billing
A plausible-looking permission check is not enough.
For auth, subscriptions, invoices, refunds, and webhooks, I review the full path instead of only the changed function.
### 
Database migrations
AI is very good at generating a migration that looks correct.
It is less aware of the strange data alre

## Related Articles

- [its ok to get lucky 1laf](https://dev.to/)
- [5 things i learned doing ai evaluation for 2 years 3kgh](https://dev.to/)
- [17 none of it was for me a year of building with ai 32kf](https://dev.to/)
- [adding an ai chatbot to echostats 290m](https://dev.to/)
- [class vs object who is the big boss 32nj](https://dev.to/)
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "ai-can-write-code-faster-than-i-can-responsibly-review-it-4ig4")
```
