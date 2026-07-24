---
title: "adding an ai chatbot to echostats 290m"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - image-generation
  - llm
  - mobile
  - open-source
  - prompt-engineering
  - search
  - software
  - standards
  - streaming
  - video-generation
  - web
---

# adding an ai chatbot to echostats 290m

> **Source:** adding-an-ai-chatbot-to-echostats-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/chijioke_uzodinma_d6ae6ef/adding-an-ai-chatbot-to-echostats-290m ingested: 2026-07-18 sha256: 565185309ed9bff13f54313f6dd348de52717925340414424b23eac57d30bf64 blog_sourc...
> **Sources:**
>   - adding-an-ai-chatbot-to-echostats-2026-07-18.md
> **Links:**
- [[17-none-of-it-was-for-me-a-year-of-building-with-ai-32kf]]
- [[5-things-i-learned-doing-ai-evaluation-for-2-years-3kgh]]
- [[its-a-post-4hi8]]
- [[the-gitbook-migration-trap-4gp2]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]

## Key Findings

---
source_url: https://dev.to/chijioke_uzodinma_d6ae6ef/adding-an-ai-chatbot-to-echostats-290m
ingested: 2026-07-18
sha256: 565185309ed9bff13f54313f6dd348de52717925340414424b23eac57d30bf64
blog_source: Dev Community
---
Adding an AI Chatbot to Echostats - DEV Community
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
[![Chijioke Uzodinma](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3783088%2F7d2ff350-d029-43c6-a155-78a52aace111.webp)](/chijioke_uzodinma_d6ae6ef)
[Chijioke Uzodinma](/chijioke_uzodinma_d6ae6ef)
Posted on Jul 18
# 
Adding an AI Chatbot to Echostats
[#ai](/t/ai)
[#llm](/t/llm)
[#showdev](/t/showdev)
[#sideprojects](/t/sideprojects)
Echostats is a Spotify stats dashboard. You upload your extended streaming history, the app stores it, and from then on it syncs with your Spotify every time you open it, pulling in your listening history and turning it into stats: top artists, top songs, a song you've probably forgotten about, a "song of the day," and more.
Numbers on a dashboard only go so far, though. A user can see that an artist sits at the top of their list, but not necessarily *why* that matters or what it says about their taste. That's the gap I wanted the AI chatbot to fill — a chat interface inside Echostats that can explain the stats in plain language and give the user deeper, more personal insight into their own music taste, instead of just handing them a chart.
## 
Technical Decisions
The chatbot 

## Summary

runs on Google AI, specifically the `gemini-3.1-flash-lite` model, set as the default in `getGoogleConfig`. I didn't stick with my first choice the whole way through — the model got updated partway through the build as I iterated.
Streaming was the original plan. A chat interface almost always benefits from a typewriter-style response, where text appears as it's generated instead of arriving all at once, and that's how I initially built it. But Vercel's hosting environment introduced limitations that made streaming unreliable in production, and rather than chase a workaround, I made the call to switch to a normal, non-streaming response. The user still gets an answer, just not the typewriter effect.
## 
How I Approached the Integration
The build process had a fair amount of back-and-forth, and most of it centered on two problems.
**The blank message bug.** At one point, the backend was generating and sending the AI's response correctly — I could see it in storage — but the chat UI would render a blank message instead of the actual text. Tracing it back, the root cause was Vercel's Node.js serverless function limitations. Switching to the Edge runtime could have solved it, but Edge doesn't support Mongoose, which the backend depends on for MongoDB, so that fix wasn't available to me. I ended up refactoring how messages were structured and sent to the model several times (`toInteractionInput` went through a few iterations — first using a "parts" structure, then type/content, then constant type assertions) while working through this.
**The two-response problem.** Some questions can't be answered by the AI alone. If a user asks something like "what was my listening history for last week," the AI first replies with an acknowledgment — essentially "processing that now" — while the backend goes and fetches the actual data (in this case, the last seven days of listening history). Once that data comes back, the AI sends a second, real response. That means a single question can produce two responses. The loading indicator originally didn't account for that: it would stop after the first "processing" message came in, making it look like the app had frozen or broken while the second response was still on its way. I fixed this by adding a "delta" command that tells the loader a second response is still coming, so it now correctly reflects both stages instead of cutting out early.
## 
What I'd Do Differently
If I were building this again, I'd research the limitations of whatever framework or hosting environment I'm using — and confirm it fully supports what I'm trying to do — before writing the feature. I lost a full day debugging the streaming error, only to find out it came down to a Vercel limitation I hadn't checked for upfront. A bit of research at the start would have saved that time entirely.
## 
Top comments (0)
Subscribe
![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3

## Related Articles

- [[17-none-of-it-was-for-me-a-year-of-building-with-ai-32kf]]
- [[5-things-i-learned-doing-ai-evaluation-for-2-years-3kgh]]
- [[its-a-post-4hi8]]
- [[the-gitbook-migration-trap-4gp2]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
