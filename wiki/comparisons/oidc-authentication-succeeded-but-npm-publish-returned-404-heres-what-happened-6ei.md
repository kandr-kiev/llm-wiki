---
title: "oidc authentication succeeded but npm publish returned 404 heres what happened 6ei"
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
  - standards
  - video-generation
  - web
---

# oidc authentication succeeded but npm publish returned 404 heres what happened 6ei

> **Source:** oidc-authentication-succeeded-but-npm-publish-returned-404---heres-what-happened-2026-07-21.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/0xkoji/oidc-authentication-succeeded-but-npm-publish-returned-404-heres-what-happened-6ei ingested: 2026-07-21 sha256: a31279a2ef00ccbf7b23a51bf062d092586b1abb5c9a2fae61...
> **Sources:**
>   - oidc-authentication-succeeded-but-npm-publish-returned-404---heres-what-happened-2026-07-21.md
> **Links:**
- [[i-tried-kimi-k3-for-a-week-heres-what-happened]]
- [[class-vs-object-who-is-the-big-boss-32nj]]
- [[hollowtest-find-tests-that-pass-but-prove-nothing-2iii]]
- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[stop-hand-translating-between-sql-and-your-erd-4ohm]]

## Key Findings

---
source_url: https://dev.to/0xkoji/oidc-authentication-succeeded-but-npm-publish-returned-404-heres-what-happened-6ei
ingested: 2026-07-21
sha256: a31279a2ef00ccbf7b23a51bf062d092586b1abb5c9a2fae6163ec75c3a08c0d
blog_source: Dev Community
---
OIDC Authentication Succeeded, but npm Publish Returned 404 — Here’s What Happened - DEV Community
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
[![0xkoji](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F139970%2F4eca214c-1d8f-4ba2-9a36-aa79753aa186.png)](/0xkoji)
[0xkoji](/0xkoji)
Posted on Jul 21
# 
OIDC Authentication Succeeded, but npm Publish Returned 404 — Here’s What Happened
[#npm](/t/npm)
[#github](/t/github)
Last week I published a new npm package, `hakoniwa-term`.
[
npmjs.com
](https://www.npmjs.com/package/hakoniwa-term)
I did the first publish manually and set a GitHub Actions workflow to automate the publish process.
After adding a GitHub Actions workflow so that creating a release would automatically publish the latest package to npm, I registered my repository information on the npm side to use OIDC authentication. I had already done the same setup for another package called hyouji, so the configuration itself went smoothly. However, when I actually created a release, even though OIDC authentication worked fine, the npm publish step aborted with a 404 error.
What GitHub Actions showed me.
```
npm ERR! 404 Not Found - PUT https://registry.npmjs.org/hakoniwa-term


## Summary

See Key Findings for full content.

## Related Articles

- [[i-tried-kimi-k3-for-a-week-heres-what-happened]]
- [[class-vs-object-who-is-the-big-boss-32nj]]
- [[hollowtest-find-tests-that-pass-but-prove-nothing-2iii]]
- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[stop-hand-translating-between-sql-and-your-erd-4ohm]]
