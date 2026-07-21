---
title: "building ai agents in php tool calling with laravel 4fji"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - search
  - software
  - standards
  - tool
  - video-generation
  - web
---

# building ai agents in php tool calling with laravel 4fji

> **Source:** building-ai-agents-in-php-tool-calling-with-laravel-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/adityakdevin/building-ai-agents-in-php-tool-calling-with-laravel-4fji ingested: 2026-07-17 sha256: 7c1041065369c1204be6227fe1575e9e8da4222553f5aa00cdcd9ff189852b61 blog_...
> **Sources:**
>   - building-ai-agents-in-php-tool-calling-with-laravel-2026-07-17.md
> **Links:**
- [[the gitbook migration trap 4gp2]]
- [[deadstop 2025 vs crossfit games 2024 1okg]]
- [[hackthebox void whispers writeup bh5]]
- [[threads url analyzer gonggae deiteowa gyejeong seungin deiteoyi gyeonggye 2mid]]
- [[using sqlite in go and its importance 3de1]]

## Key Findings

---
source_url: https://dev.to/adityakdevin/building-ai-agents-in-php-tool-calling-with-laravel-4fji
ingested: 2026-07-17
sha256: 7c1041065369c1204be6227fe1575e9e8da4222553f5aa00cdcd9ff189852b61
blog_source: Dev Community
---
Building AI Agents in PHP: Tool Calling with Laravel - DEV Community
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
[![Aditya Kumar](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F478841%2F67082e37-f826-4212-94dd-56933da5925c.jpeg)](/adityakdevin)
[Aditya Kumar](/adityakdevin)
Posted on Jul 17
• Originally published at [adityadev.in](https://adityadev.in/blog/building-ai-agents-in-php-tool-calling-with-laravel) 
# 
Building AI Agents in PHP: Tool Calling with Laravel
[#laravel](/t/laravel)
[#php](/t/php)
[#webdev](/t/webdev)
[#ai](/t/ai)
## 
The problem: chat that can only talk
The chatbot from earlier in this series can answer questions, but ask it "how many orders did we ship yesterday?" and it will confidently make something up. It has no hands — it can't query your database, call your services, or do anything except generate text.
Tool calling fixes that. You describe functions to the model; when a user's request needs one, the model responds with "call this function with these arguments" instead of prose. Your code runs the function, feeds the result back, and the model writes the final answer grounded in real data. That loop — model picks tool, you execute, model continues — is the whole tri

## Summary

See Key Findings for full content.

## Related Articles

- [[the gitbook migration trap 4gp2]]
- [[deadstop 2025 vs crossfit games 2024 1okg]]
- [[hackthebox void whispers writeup bh5]]
- [[threads url analyzer gonggae deiteowa gyejeong seungin deiteoyi gyeonggye 2mid]]
- [[using sqlite in go and its importance 3de1]]
