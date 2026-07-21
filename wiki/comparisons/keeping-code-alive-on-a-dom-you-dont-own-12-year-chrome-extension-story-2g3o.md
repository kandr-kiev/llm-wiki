---
title: "keeping code alive on a dom you dont own 12 year chrome extension story 2g3o"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - image-generation
  - mobile
  - news
  - open-source
  - prompt-engineering
  - real-time
  - search
  - software
  - standards
  - video-generation
  - web
---

# keeping code alive on a dom you dont own 12 year chrome extension story 2g3o

> **Source:** keeping-code-alive-on-a-dom-you-dont-own-12-year-chrome-extension-story-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/svyatov/keeping-code-alive-on-a-dom-you-dont-own-12-year-chrome-extension-story-2g3o ingested: 2026-07-17 sha256: 8e4ef22f0e3733435cddb1cbc0a47e53db417d8ea8102b65e6ed587...
> **Sources:**
>   - keeping-code-alive-on-a-dom-you-dont-own-12-year-chrome-extension-story-2026-07-17.md
> **Links:**
- [[deadstop 2025 vs crossfit games 2024 1okg]]
- [[hackthebox void whispers writeup bh5]]
- [[stop prompting llms to do legal math its broken 27e0]]
- [[threads url analyzer gonggae deiteowa gyejeong seungin deiteoyi gyeonggye 2mid]]
- [[i gave my agent the right memory and it ignored it anyway li7]]

## Key Findings

---
source_url: https://dev.to/svyatov/keeping-code-alive-on-a-dom-you-dont-own-12-year-chrome-extension-story-2g3o
ingested: 2026-07-17
sha256: 8e4ef22f0e3733435cddb1cbc0a47e53db417d8ea8102b65e6ed58797e37412e
blog_source: Dev Community
---
Keeping code alive on a DOM you don't own: 12-year Chrome extension story - DEV Community
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
![Cover image for Keeping code alive on a DOM you don't own: 12-year Chrome extension story](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flm8wzz9xqyrni2crdjag.png)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flm8wzz9xqyrni2crdjag.png)
[![Leonid Svyatov](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F122709%2F4d89b6fb-d4ad-4af4-9c12-8cb53789179c.jpeg)](/svyatov)
[Leonid Svyatov](/svyatov)
Posted on Jul 17
# 
Keeping code alive on a DOM you don't own: 12-year Chrome extension story
[#javascript](/t/javascript)
[#showdev](/t/showdev)
[#sideprojects](/t/sideprojects)
[#webdev](/t/webdev)
In April 2014 I wanted to sort posts on the Hacker News front page by points, by time, or by comments. Nothing I found did it without cluttering the page, so I wrote a tiny Chrome extension over a couple of days, uploaded it to the Web

## Summary

 Store, and mostly stopped thinking about it for ten years.
I touched it exactly once in that decade, in 2019, to fix the selectors.
Then in March 2024 I rewrote it from scratch, with the old version still working fine: I wanted TypeScript, React, and tests, and Manifest v3 while I was in there. That's when I started actually maintaining it.
It's called [Hacker News Sorted](https://chromewebstore.google.com/detail/hacker-news-sorted/djkcnbncofmjekhlhemlkinfpkamlkaj), it's now at v2.6.1, and it has one dependency that never appears in package.json: the exact HTML structure of the Hacker News front page. HN can change that structure any day, without a changelog, and they owe me nothing.
Sorting 30 rows of a table is a weekend project. This post is about everything else: the selector that survived a layout change and the one that didn't, the badge that tells users it's my fault, the GitHub Action that checks HN's HTML every morning, and the timestamps HN quietly rewrites.
The obvious question first: HN has an official API, so why scrape the DOM at all? Because the extension doesn't need data, it needs to rearrange the page you're already looking at. Every number it sorts by is already sitting in the rows, true timestamps included.
Fetching the same 30 items over the network would only add latency, a wider permission surface, and a privacy story to explain.
## 
The selector war
HN's front page is one big `<table>`. Each story is three `<tr>`s, emitted in order: a title row, an info row (points, age, comments), and an empty spacer row. The natural way to grab them is `nth-child` arithmetic, and that part hasn't needed a single change since the 2024 rewrite:
```
// app/constants.ts (v2.6.1)
TITLE_ROWS: 'tr:nth-child(3n+1)',
INFO_ROWS: 'tr:nth-child(3n+2)',
SPACER_ROWS: 'tr:nth-child(3n+3)',
```
Enter fullscreen mode
Exit fullscreen mode
Each `3n+k` picks every third row from offset k: titles at 1, 4, 7, info rows at 2, 5, 8, spacers at 3, 6, 9. The pattern assumes nothing non-story slips between the rows. HN's one exception, the "More" link at the bottom, sits after all 30 stories, so it never shifts the count above it.
The trap is what those selectors run against. Until March 2026, my two outer anchors were absolute paths through HN's table soup:
```
// app/constants.ts, the anchors before March 2026 (v2.3.1)
CONTROL_PANEL_PARENT:
'body > center > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(3)',
TABLE_BODY:
'body > center > table > tbody > tr:nth-child(4) > td > table > tbody',
```
Enter fullscreen mode
Exit fullscreen mode
Every `nth-child(N)` in there is a bet that HN will never insert a row above row N. On March 11, 2026, HN added a logo row to its outer table and won the bet. Both anchors stopped matching, and the extension didn't crash or throw. It just silently did nothing, on every user's machine at once.
I committed a hotfix at 17:54 that day: bump the shifted indices by one. Committed, not delivered: an extension 

## Related Articles

- [[deadstop 2025 vs crossfit games 2024 1okg]]
- [[hackthebox void whispers writeup bh5]]
- [[stop prompting llms to do legal math its broken 27e0]]
- [[threads url analyzer gonggae deiteowa gyejeong seungin deiteoyi gyeonggye 2mid]]
- [[i gave my agent the right memory and it ignored it anyway li7]]
