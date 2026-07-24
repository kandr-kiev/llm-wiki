---
title: "you dont understand a system until youve rebuilt it 2e94"
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
  - system-design
  - video-generation
  - web
---
backlinks:
  - you-dont-understand-a-system-until-youve-rebuilt-it-2e94
---


# you dont understand a system until youve rebuilt it 2e94

> **Source:** you-dont-understand-a-system-until-youve-rebuilt-it-2026-07-22.md
> **Type:** comparison
> **Created:** 2026-07-23
> **Updated:** 2026-07-23
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/valentynkit/you-dont-understand-a-system-until-youve-rebuilt-it-2e94 ingested: 2026-07-22 sha256: 7c5116be3fb4a47a1d5695a16c5cc5dc35593d4225f4239c56489c39dc6a93f6 blog_s...
> **Sources:**
>   - you-dont-understand-a-system-until-youve-rebuilt-it-2026-07-22.md
> **Links:**
- [[its-ok-to-get-lucky-1laf]]
- [[the-part-of-this-year-i-dont-put-in-the-commit-messages-l6m]]
- [[i-tried-kimi-k3-for-a-week-heres-what-happened]]
- [[5-things-i-learned-doing-ai-evaluation-for-2-years-3kgh]]
- [[adding-an-ai-chatbot-to-echostats-290m]]

## Key Findings

---
source_url: https://dev.to/valentynkit/you-dont-understand-a-system-until-youve-rebuilt-it-2e94
ingested: 2026-07-22
sha256: 7c5116be3fb4a47a1d5695a16c5cc5dc35593d4225f4239c56489c39dc6a93f6
blog_source: Dev Community
---
You don't understand a system until you've rebuilt it - DEV Community
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
[![Valentyn Kit](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1466426%2Fcbad2b27-499a-43e4-a45f-01899556d6a1.jpg)](/valentynkit)
[Valentyn Kit](/valentynkit)
Posted on Jul 22
• Originally published at [valentynkit.com](https://valentynkit.com/blog/you-dont-understand-a-system-until-youve-rebuilt-it) 
# 
You don't understand a system until you've rebuilt it
[#programming](/t/programming)
[#systems](/t/systems)
[#rust](/t/rust)
[#c](/t/c)
"Build your own X to understand it" is advice so common it has stopped meaning anything. I repeated it for years without being able to say why it worked, which is the same as not understanding it. So I built the wrong things, learned less than I told myself I was learning, and kept the slogan anyway.
Then I rebuilt a TCP echo server seven times, and somewhere in the middle of it I finally understood a sentence I had read for six years and never once been able to derive. That is when the advice stopped being a slogan and turned into a method with rules.
The claim I actually believe now is narrower and stranger than the slogan. You don't understand a 

## Summary

system until you've rebuilt a worse version of it. Not read about it, not even read its source. Rebuilt it, badly, with your own hands. And it matters which parts you get wrong.
## 
Three ways to know a thing
We lump three different things together under the word "understand," and they are not the same thing at all.
You can use a system. You learn its interface: the calls you make, the arguments they take, the shape of what comes back. This is real knowledge and most of the time it is all you need. I have used Postgres for years and could not tell you how its query planner picks a join order, and that has cost me almost nothing.
You can read its source. Now you have trace knowledge. You can follow what it does, step by step, and point at the line where each thing happens. This feels like the deep version, and it is deeper, but it has a specific gap: you can trace every decision without understanding why any of them had to be made that way. You are reading answers to questions you never asked. The code tells you what was chosen. It is quiet about what the alternatives cost.
You can rebuild it. Now you are the one being asked the questions. You hit the wall the original was shaped to avoid, at the moment it stops you, with no answer key. The decision stops being a line to read and becomes a problem you have to solve. That is the whole difference.
## 
The theory is the thing you can't inherit
In 1985 Peter Naur wrote a short paper called "Programming as Theory Building." His argument was that the real product of programming is not the code. It is a theory that lives in the programmer's head: the mapping between the code and the world it models, the reason behind each decision, the sense of which changes are safe and which ones quietly break something three files away. The code is a partial record of that theory. The documentation is a worse one.
The part that stuck with me is his claim that the theory cannot be reconstructed from the code and the docs alone. When the people who hold it leave, it dies, even though every line they wrote is still sitting right there. He called that program death. The text survives; the understanding does not.
If that is true, then reading the source can only ever give you the text. The theory is the thing you have to build yourself, and rebuilding is how you build it for a system you did not design. You cannot inherit it by reading. You have to make the decisions, hit the walls, and pay for the wrong guesses, because that is the process that produced the theory in the first place.
I found this out concretely. I have written before about [rebuilding a TCP server seven times](https://valentynkit.com/blog/framework-knowledge-evaporates), from a blocking `accept` loop up through `select`, `poll`, `kqueue`, and `epoll`. Here is the kind of sentence I mean: a server that scales does not ask its connections "anything ready yet" in a loop, it sleeps until the kernel tells it one of them is. I had read that idea, in one form or

## Related Articles

- [[its-ok-to-get-lucky-1laf]]
- [[the-part-of-this-year-i-dont-put-in-the-commit-messages-l6m]]
- [[i-tried-kimi-k3-for-a-week-heres-what-happened]]
- [[5-things-i-learned-doing-ai-evaluation-for-2-years-3kgh]]
- [[adding-an-ai-chatbot-to-echostats-290m]]
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "you-dont-understand-a-system-until-youve-rebuilt-it-2e94")
```
