---
title: "i built a cloudflare worker so you can give the public free ai without ever getting a surprise"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
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

# i built a cloudflare worker so you can give the public free ai without ever getting a surprise

> **Source:** i-built-a-cloudflare-worker-so-you-can-give-the-public-free-ai-without-ever-getting-a-surprise-bill-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/mister_buds_4874bbe643dda/i-built-a-cloudflare-worker-so-you-can-give-the-public-free-ai-without-ever-getting-a-surprise-1042 ingested: 2026-07-17 sha256: fa09a9f4b32f30...
> **Sources:**
>   - i-built-a-cloudflare-worker-so-you-can-give-the-public-free-ai-without-ever-getting-a-surprise-bill-2026-07-17.md
> **Links:**
- [[deadstop 2025 vs crossfit games 2024 1okg]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Automating Ai Away]]
- [[5 Agent Skills I Use Every Day]]
- [[Mesh LLM: distributed AI computing on iroh]]

## Key Findings

---
source_url: https://dev.to/mister_buds_4874bbe643dda/i-built-a-cloudflare-worker-so-you-can-give-the-public-free-ai-without-ever-getting-a-surprise-1042
ingested: 2026-07-17
sha256: fa09a9f4b32f30c2b343a88fe497df1e52f86f2be224a5a145f75d5fbf9880cc
blog_source: Dev Community
---
I built a Cloudflare Worker so you can give the public free AI, without ever getting a surprise bill - DEV Community
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
![Cover image for I built a Cloudflare Worker so you can give the public free AI, without ever getting a surprise bill](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fom30bvu95f1c4xwrkg9g.png)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fom30bvu95f1c4xwrkg9g.png)
[![Mister Buds](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F4032924%2F847fd74d-d5be-4cf3-bdfe-d27c56704461.png)](/mister_buds_4874bbe643dda)
[Mister Buds](/mister_buds_4874bbe643dda)
Posted on Jul 17
# 
I built a Cloudflare Worker so you can give the public free AI, without ever getting a surprise bill
[#cloudflare](/t/cloudflare)
[#ai](/t/ai)
[#webdev](/t/webdev)
[#indiehackers](/t/indiehackers)
I built a Cloudflare Worker so you can give the public free AI without ev

## Summary

er getting a surprise bill
Every time I wanted to add an AI feature to one of my apps and let anyone try it no login, no "enter your card," just here, use it the same thing stopped me: the bill.
The moment your API key is reachable by the public, you're one traffic spike, one bored person with a for loop, or one leaked key away from waking up to a four-figure invoice. So most of us do one of two things: bolt a login onto something that was supposed to be free, or just… never ship it.
I got tired of that trade-off, so I built the piece that was missing.
What it is
Free-Tier AI Relay is a ~20 KB Cloudflare Worker plus a zero-dependency browser client that sits between your app and the AI providers. You drop it in, drag it to Cloudflare's free plan, and you've got a public AI endpoint that can't run away with your money.
The whole design is built around one idea: ration a free allowance to anonymous strangers, and guarantee a spend ceiling.
How it actually works
Your key stays server-side. The browser only ever talks to your Worker — the provider key never touches the client.
Providers are tried in cost order, not reliability order. This is the part that's different from a normal gateway. It calls your cheapest option firs free tiers before anything paid. As shipped, that's Google Gemini's free tier, then free community models on OpenRouter. A paid model is only ever reached if you deliberately uncomment one. Out of the box, it calls only free tiers, so it costs $0 to run.
Free usage is capped three ways, every day, and a request has to pass all three:
per anonymous device (a UUID) soft fairness so one person can't hog it,
per network (a hashed IP, so you're not storing anyone's raw address) catches the easy device-reset abuse,
a hard global ceiling the one that actually protects your wallet. Once the whole app hits it for the day, the free tier closes until reset. You set that number from a budget you can live with.
It's one config file. Providers, cost order, caps, and endpoints all live in a single file. Adding a provider or a whole new AI feature needs zero code changes. There's also a one-toggle kill switch that pauses the entire free tier instantly, no redeploy.
"So do I ever actually pay?"
No not unless you choose to. The default state calls only free providers. The single paid-fallback line in the config is commented out; it does nothing until you uncomment it. And even if you do turn on a paid provider later (to get higher limits once you scale), the global daily cap becomes a hard ceiling on what you could possibly spend. Worst case is a number you picked in advance, not a surprise.
How it's different from LiteLLM / Portkey / other gateways
Those are great — at a different job. General LLM gateways make paid traffic from your own trusted backend reliable and observable, ordered by uptime. They assume you want to spend efficiently.
This solves the opposite problem: rationing a free allowance to an untrusted public, ordered by price, with a 

## Related Articles

- [[deadstop 2025 vs crossfit games 2024 1okg]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Automating Ai Away]]
- [[5 Agent Skills I Use Every Day]]
- [[Mesh LLM: distributed AI computing on iroh]]
