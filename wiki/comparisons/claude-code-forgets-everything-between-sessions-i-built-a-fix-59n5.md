---
title: "claude code forgets everything between sessions i built a fix 59n5"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - claude
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - search
  - software
  - standards
  - use-case
  - video-generation
  - web
---

# claude code forgets everything between sessions i built a fix 59n5

> **Source:** claude-code-forgets-everything-between-sessions-i-built-a-fix-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/_548fe7f9c7fcd1125fd/claude-code-forgets-everything-between-sessions-i-built-a-fix-59n5 ingested: 2026-07-18 sha256: 452609b2b3e31d23f14b6aa23a36c08cd03a369007fd670bc7b4...
> **Sources:**
>   - claude-code-forgets-everything-between-sessions-i-built-a-fix-2026-07-18.md
> **Links:**
- [[17 none of it was for me a year of building with ai 32kf]]
- [[5 things i learned doing ai evaluation for 2 years 3kgh]]
- [[adding an ai chatbot to echostats 290m]]
- [[its a post 4hi8]]
- [[the gitbook migration trap 4gp2]]

## Key Findings

---
source_url: https://dev.to/_548fe7f9c7fcd1125fd/claude-code-forgets-everything-between-sessions-i-built-a-fix-59n5
ingested: 2026-07-18
sha256: 452609b2b3e31d23f14b6aa23a36c08cd03a369007fd670bc7b490516d0508e4
blog_source: Dev Community
---
Claude Code Forgets Everything Between Sessions. I Built a Fix. - DEV Community
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
[![nnyannya](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F4034880%2F82af7035-7094-40b9-8e64-07ef37af44ef.jpg)](/_548fe7f9c7fcd1125fd)
[nnyannya](/_548fe7f9c7fcd1125fd)
Posted on Jul 18
# 
Claude Code Forgets Everything Between Sessions. I Built a Fix.
[#ai](/t/ai)
[#claude](/t/claude)
[#agents](/t/agents)
[#opensource](/t/opensource)
## 
Claude Code Starts From Scratch Every Session
If you use Claude Code every day, you've probably found yourself repeating the same explanations over and over again.
- Why did we choose this architecture?
- Why did we reject that implementation?
- What parts are we planning to improve later?
Even when you're working on the same project, Claude Code forgets everything once a session ends.
The conversation logs are still there—they're stored as JSONL files under ~/.claude/projects/—but Claude doesn't use them in future sessions. In other words, the memory exists, but the agent can't access it.
Git can tell you what changed, but it can't tell you why. The design decisions, trade-offs, and discussions that happened during dev

## Summary

See Key Findings for full content.

## Related Articles

- [[17 none of it was for me a year of building with ai 32kf]]
- [[5 things i learned doing ai evaluation for 2 years 3kgh]]
- [[adding an ai chatbot to echostats 290m]]
- [[its a post 4hi8]]
- [[the gitbook migration trap 4gp2]]
