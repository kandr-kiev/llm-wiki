---
title: "i gave my agent the right memory and it ignored it anyway li7"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - application
  - few-shot
  - image-generation
  - llm
  - mobile
  - open-source
  - prompt-engineering
  - rag
  - search
  - software
  - standards
  - video-generation
  - web
---

# i gave my agent the right memory and it ignored it anyway li7

> **Source:** i-gave-my-agent-the-right-memory-and-it-ignored-it-anyway-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/thewilliamboyd93oss/i-gave-my-agent-the-right-memory-and-it-ignored-it-anyway-li7 ingested: 2026-07-17 sha256: 4cae37685cdad570a24d85755775d785f1f271ee9b51ccaa48f42e7273...
> **Sources:**
>   - i-gave-my-agent-the-right-memory-and-it-ignored-it-anyway-2026-07-17.md
> **Links:**
- [[deadstop 2025 vs crossfit games 2024 1okg]]
- [[5 Agent Skills I Use Every Day]]
- [[Automating away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Automating Ai Away]]

## Key Findings

---
source_url: https://dev.to/thewilliamboyd93oss/i-gave-my-agent-the-right-memory-and-it-ignored-it-anyway-li7
ingested: 2026-07-17
sha256: 4cae37685cdad570a24d85755775d785f1f271ee9b51ccaa48f42e727334158d
blog_source: Dev Community
---
I gave my agent the right memory and it ignored it anyway - DEV Community
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
[![zowskyy](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F4032919%2F737121df-3647-421b-b27a-5a4f2ab61756.jpg)](/thewilliamboyd93oss)
[zowskyy](/thewilliamboyd93oss)
Posted on Jul 17
# 
I gave my agent the right memory and it ignored it anyway
[#agents](/t/agents)
[#llm](/t/llm)
[#rag](/t/rag)
[#testing](/t/testing)
A few weeks ago I was testing a support-agent setup — nothing fancy, just
an LLM with a memory layer bolted on so it could remember basic facts
about a user across sessions. Subscription tier, shipping address, that
kind of thing.
I ran a simple scenario: the user is already on the enterprise plan. I
confirmed the memory retrieval was working — the fact **`subscription_tier:
enterprise`** came back correctly when I queried "what tier is the user's
subscription."
Then I asked the agent, in a support-chat style prompt, what plan the user
was on.
The response:
>
"Sure, upgrading to our enterprise plan would unlock that feature for
you."
The user is *already on* enterprise. The agent had the correct fact sitting
right there in its context. It just... used it 

## Summary

See Key Findings for full content.

## Related Articles

- [[deadstop 2025 vs crossfit games 2024 1okg]]
- [[5 Agent Skills I Use Every Day]]
- [[Automating away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Automating Ai Away]]
