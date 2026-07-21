---
title: "theres no standard status page and other lessons from tracking 96 providers 56k6"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - cloud
  - devops
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

# theres no standard status page and other lessons from tracking 96 providers 56k6

> **Source:** theres-no-standard-status-page-and-other-lessons-from-tracking-96-providers-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/kerolos_atallah/theres-no-standard-status-page-and-other-lessons-from-tracking-96-providers-56k6 ingested: 2026-07-18 sha256: b695c2f8e006671b69c9289b06996c2792cf6d86d14...
> **Sources:**
>   - theres-no-standard-status-page-and-other-lessons-from-tracking-96-providers-2026-07-18.md
> **Links:**
- [[the gitbook migration trap 4gp2]]
- [[its a post 4hi8]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[hackthebox void whispers writeup bh5]]
- [[repeating tasks without repeating code 4fak]]

## Key Findings

---
source_url: https://dev.to/kerolos_atallah/theres-no-standard-status-page-and-other-lessons-from-tracking-96-providers-56k6
ingested: 2026-07-18
sha256: b695c2f8e006671b69c9289b06996c2792cf6d86d143b2e755230fc3d446d40c
blog_source: Dev Community
---
There's no standard status page, and other lessons from tracking 96 providers - DEV Community
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
![Cover image for There's no standard status page, and other lessons from tracking 96 providers](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F2r0y1917plql3eo0my8e.png)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F2r0y1917plql3eo0my8e.png)
[![Kerolos Atallah](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F4034583%2F2f750b6b-acd5-4eb2-a291-962e979b8e98.jpg)](/kerolos_atallah)
[Kerolos Atallah](/kerolos_atallah)
Posted on Jul 18
# 
There's no standard status page, and other lessons from tracking 96 providers
[#showdev](/t/showdev)
[#devops](/t/devops)
[#postgres](/t/postgres)
[#webdev](/t/webdev)
Your Slack won't load. Is it you, your VPN, the office wifi, or Slack? You open Slack's status page and it's green. It's often green while you're clearly down, because a company updates its

## Summary

 own status page *after* it confirms an incident — not the moment you feel it.
I spent the last few months building [OutageDeck](https://outagedeck.com), which reads the official status source of 96 cloud and SaaS providers and folds them into one place. I assumed the hard part would be the frontend. It wasn't. The hard part was that "official status" is a swamp. Here's what I found in it.
**The short version:**
- There is no standard status format. Statuspage is common, but the tail is bespoke — Google, Slack, Heroku, Azure over RSS, and AWS in UTF-16.
- Providers' own timestamps lag, sometimes by days, so you can't compute uptime from them.
- Some official feeds are stale fossils, or model thousands of instances, so "is it up?" has no single answer.
- Official status is authoritative but late — which is the whole reason crowd-sourced "is it down?" sites exist.
- All of this pushed me toward a deliberately tiny backend: one Next.js app and a Postgres database, no queue, about $55/month.
## 
There is no standard
Atlassian Statuspage is the closest thing to a common language. Around 89 of my 96 providers expose a Statuspage-style `summary.json` and `incidents.json`, and one adapter reads all of them. Some providers don't even run Statuspage but copy its shape anyway — incident.io serves a Statuspage-compatible endpoint on each customer's own domain, so Notion and Linear parse with the exact same code.
Then the long tail starts. Google publishes an `incidents.json` in its own format (shared across Cloud, Workspace, and Firebase). Slack has a bespoke API. Heroku is on the fourth version of its own. Azure only offers RSS. AWS ships an event feed encoded in **UTF-16 with a byte-order mark**, which silently breaks any parser that assumes UTF-8. "Just read the status page" turned into six adapters and a pile of encoding checks.
## 
The timestamps lie
My first uptime numbers were nonsense, and it took me a while to see why: I was computing them from each provider's own `captured_at` timestamp, and those lag. One provider's was **days** behind at one point. If a feed says a state was "captured three days ago," you can't tell whether the service was down for three days or the timestamp is just stale.
The fix was to stop trusting upstream time entirely. Every observation is stamped with *my* check time, and uptime is computed from when I saw a state, not when the provider says it happened. The corollary matters too: if my own poller has a gap — a deploy, say — I don't backfill it as "up." Any gap longer than 30 minutes is recorded as *no data*, because inventing green is worse than admitting I wasn't looking.
## 
Some official sources are fossils
A few providers technically have a machine-readable status endpoint that you still can't use. Stripe's legacy status JSON has been effectively frozen since 2024; it will cheerfully report that everything is fine, forever. Salesforce's status API models nearly 3,900 separate instances, so "is Salesforce up?" depends

## Related Articles

- [[the gitbook migration trap 4gp2]]
- [[its a post 4hi8]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[hackthebox void whispers writeup bh5]]
- [[repeating tasks without repeating code 4fak]]
