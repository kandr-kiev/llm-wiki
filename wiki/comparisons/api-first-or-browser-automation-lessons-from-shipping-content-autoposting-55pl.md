---
title: "api first or browser automation lessons from shipping content autoposting 55pl"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - application
  - automation
  - cost
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - search
  - software
  - video-generation
  - web
---

# api first or browser automation lessons from shipping content autoposting 55pl

> **Source:** api-first-or-browser-automation-lessons-from-shipping-content-autoposting-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/content_ai/api-first-or-browser-automation-lessons-from-shipping-content-autoposting-55pl ingested: 2026-07-17 sha256: 84d619ab5eb52617420c3475797b3eca987722ae054951de6a...
> **Sources:**
>   - api-first-or-browser-automation-lessons-from-shipping-content-autoposting-2026-07-17.md
> **Links:**
- [[workers-cache]]
- [[sequoia-ascent]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[a-full-3d-live-weather-world-in-one-html-file-no-frameworks-no-build-step-4n83]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]

## Key Findings

---
source_url: https://dev.to/content_ai/api-first-or-browser-automation-lessons-from-shipping-content-autoposting-55pl
ingested: 2026-07-17
sha256: 84d619ab5eb52617420c3475797b3eca987722ae054951de6a0f15996b156bbe
blog_source: Dev Community
---
API-first or browser automation? Lessons from shipping content autoposting - DEV Community
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
[![Alex](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F4032911%2F62e877c8-e135-4b60-8a2c-f474328672e5.png)](/content_ai)
[Alex](/content_ai)
Posted on Jul 17
# 
API-first or browser automation? Lessons from shipping content autoposting
[#automation](/t/automation)
[#api](/t/api)
[#typescript](/t/typescript)
[#webdev](/t/webdev)
We built a pipeline that generates content and ships it to several platforms. Generation turned out to be the easy half. **Publishing** is where the real engineering was — and where I burned the most hours. Here is what I'd tell my past self.
## 
The rule I landed on: API when it exists, browser only when it doesn't
Not every platform exposes a publishing API. The tempting shortcut is to drive a headless browser everywhere. Don't. Two reasons:
- 
**Some platforms explicitly forbid it.** X's automation rules are blunt: *"Non-API-based forms of automation, such as scripting the X website, may result in permanent suspension."* If an API exists, scripting the site is not a clever workaround — it's a ban waiting to happen.

## Summary

See Key Findings for full content.

## Related Articles

- [[workers-cache]]
- [[sequoia-ascent]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[a-full-3d-live-weather-world-in-one-html-file-no-frameworks-no-build-step-4n83]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
