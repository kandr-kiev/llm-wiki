---
title: "your clients schema doesnt belong in your cloud account e5g"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - cloud
  - image-generation
  - mobile
  - open-source
  - privacy
  - prompt-engineering
  - search
  - software
  - tool
  - vector-database
  - video-generation
  - web
---

# your clients schema doesnt belong in your cloud account e5g

> **Source:** your-clients-schema-doesnt-belong-in-your-cloud-account-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/tbson87/your-clients-schema-doesnt-belong-in-your-cloud-account-e5g ingested: 2026-07-18 sha256: 2fb135fa8256cd5e0170e87650b73ae86003d0ce0fa42d3aa42e7cb89ddce6dc blog_so...
> **Sources:**
>   - your-clients-schema-doesnt-belong-in-your-cloud-account-2026-07-18.md
> **Links:**
- [[stop-hand-translating-between-sql-and-your-erd-4ohm]]
- [[ai-help-with-your-database-design-without-the-cloud-32l4]]
- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[the-gitbook-migration-trap-4gp2]]
- [[17-none-of-it-was-for-me-a-year-of-building-with-ai-32kf]]

## Key Findings

---
source_url: https://dev.to/tbson87/your-clients-schema-doesnt-belong-in-your-cloud-account-e5g
ingested: 2026-07-18
sha256: 2fb135fa8256cd5e0170e87650b73ae86003d0ce0fa42d3aa42e7cb89ddce6dc
blog_source: Dev Community
---
Your Client's Schema Doesn't Belong in Your Cloud Account - DEV Community
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
![Cover image for Your Client's Schema Doesn't Belong in Your Cloud Account](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fschemity.com%2Fimages%2Fblog%2Fyour-clients-schema-doesnt-belong-in-your-cloud-account%2Fbanner.webp)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fschemity.com%2Fimages%2Fblog%2Fyour-clients-schema-doesnt-belong-in-your-cloud-account%2Fbanner.webp)
[![Son Tran](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F79995%2F6de9d37a-5521-4b7a-a835-9787e74caf0c.jpg)](/tbson87)
[Son Tran](/tbson87)
Posted on Jul 18
• Originally published at [schemity.com](https://schemity.com/blog/your-clients-schema-doesnt-belong-in-your-cloud-account) 
# 
Your Client's Schema Doesn't Belong in Your Cloud Account
[#database](/t/database)
[#freelance](/t/freelance)
[#privacy](/t/privacy)
[#career](/t/career)
*Disclosure: I build [Schemity](https://schemity.com), a desktop ERD tool - this post is from our blog and uses it for the examples.*
>
**TL;DR:** Consultant

## Summary

s juggling client engagements in one shared cloud account cannot guarantee NDA isolation or true deletion. Schemity keeps each client in a local workspace - a folder of JSON files - so isolation is physical and offboarding is a folder handover.
When several clients' schemas live side by side in one shared cloud diagram account, NDA isolation is a promise you cannot actually keep, and deletion at the end of an engagement is an act of faith in a vendor. Keeping one local workspace folder per client fixes both.
A consultant's Tuesday: in the morning you are in a fintech client's ledger schema, after lunch you are restructuring a logistics company's shipment tables, and at five someone from last year's engagement emails asking for "that diagram you made". Three clients, three NDAs, three completely unrelated data models.
And in most diagram tools: one account, one big list, everything side by side.
That list is the problem. The fintech schema sits one misclick away from the logistics one. Both [live on a vendor's server](https://schemity.com/blog/your-erd-shouldnt-be-able-to-just-disappear), under an account tied to you personally, governed by terms of service none of your clients ever signed. Somewhere in each of your contracts is a clause about where client material may be stored - and "my personal SaaS account" is almost never on the list.
## 
Every engagement ends - your account remembers
Client work has a lifecycle that cloud tools quietly ignore. An engagement ends, and two things are supposed to happen: the client receives everything you produced, and you stop holding their confidential material. Both are awkward when the diagrams live in someone else's cloud.
Handover becomes "let me export some PNGs" - flattened snapshots of living documents. Deletion becomes an act of faith: you click remove, and trust that the vendor's backups, caches, and audit copies eventually forget too. And if the client returns next year, you are either resurrecting archived projects in a tool you may no longer subscribe to, or starting from those PNGs.
None of this is hypothetical for consultants. It is the offboarding checklist of every project, and a cloud diagram account fails most of it.
## 
One client, one workspace, one folder
Schemity is a local ERD tool, and its unit of organization matches the consultant's unit of work: the workspace. Each workspace holds its own connections and diagrams, and each workspace is just a folder of [plain JSON files](https://schemity.com/doc/json-storage-format) on your machine. Nothing overlaps, nothing syncs anywhere, and the fintech schema cannot appear in the logistics client's window because they do not share so much as a directory.
[![Schemity's Connection Manager with a workspace list on the left and the selected workspace's own connections and diagrams on the right](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com

## Related Articles

- [[stop-hand-translating-between-sql-and-your-erd-4ohm]]
- [[ai-help-with-your-database-design-without-the-cloud-32l4]]
- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[the-gitbook-migration-trap-4gp2]]
- [[17-none-of-it-was-for-me-a-year-of-building-with-ai-32kf]]
