---
title: "server state and client state why react apps need two libraries 144h"
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

# server state and client state why react apps need two libraries 144h

> **Source:** server-state-and-client-state-why-react-apps-need-two-libraries-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/warrendeleon/server-state-and-client-state-why-react-apps-need-two-libraries-144h ingested: 2026-07-20 sha256: a6b04f6f8516163b90fcb62a34e153687eca984bd460451534b78667ea...
> **Sources:**
>   - server-state-and-client-state-why-react-apps-need-two-libraries-2026-07-20.md
> **Links:**
- [[i tried kimi k3 for a week heres what happened]]
- [[adding an ai chatbot to echostats 290m]]
- [[the gitbook migration trap 4gp2]]
- [[hollowtest find tests that pass but prove nothing 2iii]]
- [[its a post 4hi8]]

## Key Findings

---
source_url: https://dev.to/warrendeleon/server-state-and-client-state-why-react-apps-need-two-libraries-144h
ingested: 2026-07-20
sha256: a6b04f6f8516163b90fcb62a34e153687eca984bd460451534b78667ea9dc16f
blog_source: Dev Community
---
Server state and client state: why React apps need two libraries - DEV Community
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
![Cover image for Server state and client state: why React apps need two libraries](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fwarrendeleon.com%2Fimages%2Fblog%2Fserver-vs-client-state.webp)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fwarrendeleon.com%2Fimages%2Fblog%2Fserver-vs-client-state.webp)
[![Warren de Leon](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3849498%2F78ff4b91-2b34-4678-85ae-19aaf1642e95.png)](/warrendeleon)
[Warren de Leon](/warrendeleon)
Posted on Jul 20
• Originally published at [warrendeleon.com](https://warrendeleon.com/blog/server-state-and-client-state-react-native/) 
# 
Server state and client state: why React apps need two libraries
[#reactnative](/t/reactnative)
[#statemanagement](/t/statemanagement)
[#redux](/t/redux)
[#reduxtoolkit](/t/reduxtoolkit)
>
📚 **State Management** series — [read it in full on warrendeleon.com](https://warrendeleon.com/blog/series/state-management/), where new parts land fi

## Summary

rst.
Almost every React Native app holds two kinds of state that behave nothing alike: server state and client state. Tell them apart and the choice of library mostly answers itself; blur them and you end up building by hand what a library would give you for free.
These two posts are a short break from the [Module Federation series](https://warrendeleon.com/blog/why-module-federation-react-native/?utm_source=devto&utm_medium=crosspost&utm_campaign=server-vs-client-state), because the federated work ahead leans on exactly this distinction. It is easier to get straight in one plain app first.
Two pairings hold up well as an app grows. With Redux Toolkit and RTK Query you keep one store, but server and client state are handled by two different tools inside it: RTK Query is a purpose-built server-state layer, caching machinery and all, and client state stays in plain `createSlice` slices. With TanStack Query and Zustand you split across two libraries instead, the server cache living in TanStack's own client, outside any store, and client state in a small Zustand store. Either way the two kinds get different handling and are never forced through one. The shortcut that undoes that is one general-purpose store, a thunk per request, and cache logic grown by hand. It is fine on a small app and turns into a second job as it grows.
## 
Two kinds of state
Server state is a local copy of something a server owns: a profile from `/users/me`, a product list, an order status. The copy is only ever a snapshot, and the original can change the instant after you read it. That one fact is where all the work comes from. A copy of remote data needs caching, so you are not refetching on every mount; deduplication, so two components asking for the same resource fire one request; background refetching, so the screen freshens quietly; retry, for the network that drops; invalidation, so a write can mark related data stale; and garbage collection, to drop what nothing is watching. None of that is peculiar to React. It is what any client owes data it does not own.
Client state is the other half: data the app owns outright. The selected account, a sort order, a form draft, whether a modal is open, the auth tokens you hold after login (where you keep them safely is [its own topic](https://warrendeleon.com/blog/tiered-secure-storage-react-native/?utm_source=devto&utm_medium=crosspost&utm_campaign=server-vs-client-state)), the user's theme and language. It has to be held, it has to be reactive, and once in a while it has to survive a restart. That is nearly the whole list. It cannot go stale, so it needs no caching; there is nothing to refetch, so it needs no background sync. The two are not degrees of the same thing. They have different jobs, and a library built for one is the wrong tool for the other.
## 
What each half asks for
Server state needs a library that already has the machinery. Build it by hand and every feature grows the same scaffolding: a request, a loading flag, a

## Related Articles

- [[i tried kimi k3 for a week heres what happened]]
- [[adding an ai chatbot to echostats 290m]]
- [[the gitbook migration trap 4gp2]]
- [[hollowtest find tests that pass but prove nothing 2iii]]
- [[its a post 4hi8]]
