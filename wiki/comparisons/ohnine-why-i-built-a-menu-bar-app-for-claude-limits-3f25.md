---
title: "ohnine why i built a menu bar app for claude limits 3f25"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - automation
  - claude
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

# ohnine why i built a menu bar app for claude limits 3f25

> **Source:** ohnine-why-i-built-a-menu-bar-app-for-claude-limits-2026-07-24.md
> **Type:** comparison
> **Created:** 2026-07-24
> **Updated:** 2026-07-24
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/raxxostudios/ohnine-why-i-built-a-menu-bar-app-for-claude-limits-3f25 ingested: 2026-07-24 sha256: 7f38b5628c0398104ede525fba7f5915ad6dee144bf8ee3da18ca52bf908f365 blog_...
> **Sources:**
>   - ohnine-why-i-built-a-menu-bar-app-for-claude-limits-2026-07-24.md
> **Links:**
- [[its ok to get lucky 1laf]]
- [[class vs object who is the big boss 32nj]]
- [[claude reflect i audited how i actually use ai 26g4]]
- [[5 things i learned doing ai evaluation for 2 years 3kgh]]
- [[hollowtest find tests that pass but prove nothing 2iii]]

## Key Findings

---
source_url: https://dev.to/raxxostudios/ohnine-why-i-built-a-menu-bar-app-for-claude-limits-3f25
ingested: 2026-07-24
sha256: 7f38b5628c0398104ede525fba7f5915ad6dee144bf8ee3da18ca52bf908f365
blog_source: Dev Community
---
OhNine: Why I Built a Menu Bar App for Claude Limits - DEV Community
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
[![RAXXO Studios](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3848289%2Ffd2912c9-5820-4993-8fdc-62ec1e778980.png)](/raxxostudios)
[RAXXO Studios](/raxxostudios)
Posted on Jul 24
• Originally published at [raxxo.shop](https://raxxo.shop/blogs/lab/ohnine-why-i-built-a-menu-bar-app-for-claude-limits) 
# 
OhNine: Why I Built a Menu Bar App for Claude Limits
[#ai](/t/ai)
[#productivity](/t/productivity)
[#claudecode](/t/claudecode)
[#automation](/t/automation)
- OhNine is a free menu bar app that tracks Claude session and weekly usage limits in real time
- It sends native alerts at 80%, 91%, and 100% so a session never ends without warning
- The hard problem was never reading a number, it was making the warning arrive before the cutoff instead of after
- Building a zero telemetry tool changed how I judge every product I ship after it
## 
The Problem: Hitting a Wall You Cannot See
For months, my Claude sessions ended the same frustrating way. I would be deep in a conversation, mid thought, actually making progress, and then the reply would just stop. No countdown. No yellow light. No wa

## Summary

rning that said "you have three messages left, wrap up." One second I was working, the next I was staring at a message telling me to wait for a reset I never saw coming.
The frustrating part was not the limit itself. Usage limits exist for a reason, and I understand why they are there. The frustrating part was the total lack of visibility into where I stood. Claude Code and claude.ai will occasionally mention you are close to a cap, sometimes at 97 percent, which is technically a warning and practically useless, because by then you are already mid-thought with no time left to land it cleanly.
It got worse once I noticed the layers. There is not one limit to track, there are several stacked on top of each other: a session limit, a rolling weekly cap, and separate caps depending on which model you are running. Switching models mid-session, thinking you had found a workaround, only to hit a wall from a different direction, was its own specific kind of frustrating. None of these layers showed up anywhere. There was no dashboard, no menu bar icon, nothing you could glance at the way you glance at your laptop's battery percentage before deciding whether to plug in.
So the wall kept arriving the same way: mid-flow, mid-sentence, with zero warning. Coding sessions got cut off between a question and its answer. Writing sessions lost momentum at the worst possible sentence. It is a small thing described out loud, and it was a genuinely disruptive thing to live with every day, because flow state does not survive a surprise stop.
I looked for something that already solved this before I considered building it myself, the way I usually do. General system monitors exist, and a few browser extensions promise usage tracking for various AI tools, but none of them understood the specific shape of Claude's limits: a session cap that resets on its own clock, a weekly cap that resets on a different one, and a model-specific cap layered on top of both. A generic tracker built for a different product could not show me any of that correctly, because it was never built with these specific rules in mind. Nothing existed that watched Claude specifically, showed the layered limits in one place, and warned early enough to actually be useful instead of decorative. That gap is the entire reason OhNine exists.
## 
What OhNine Actually Does
OhNine is a small app that lives in your menu bar and does one job well: it watches your Claude usage and tells you where you stand before you hit the wall, not after. It is not a browser dashboard you have to remember to open, and it is not a browser extension tied to one tab. It sits in the same place your clock and battery icon sit, always visible, never in the way.
The core of it is a live progress bar for your current session, showing percentage used and a countdown to reset. There is a small mascot that walks alongside the bar as you use up your session, and when you hit 100 percent it visibly gets tired and dims out before quietly walki

## Related Articles

- [[its ok to get lucky 1laf]]
- [[class vs object who is the big boss 32nj]]
- [[claude reflect i audited how i actually use ai 26g4]]
- [[5 things i learned doing ai evaluation for 2 years 3kgh]]
- [[hollowtest find tests that pass but prove nothing 2iii]]
