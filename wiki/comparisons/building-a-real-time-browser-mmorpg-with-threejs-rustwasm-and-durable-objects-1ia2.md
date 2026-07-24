---
title: "building a real time browser mmorpg with threejs rustwasm and durable objects 1ia2"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - real-time
  - search
  - software
  - video-generation
  - web
---

# building a real time browser mmorpg with threejs rustwasm and durable objects 1ia2

> **Source:** building-a-real-time-browser-mmorpg-with-threejs-rustwasm-and-durable-objects-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/realmofechoes/building-a-real-time-browser-mmorpg-with-threejs-rustwasm-and-durable-objects-1ia2 ingested: 2026-07-18 sha256: c2c76b3c3768453b2668627c65a17f47b2cdf873bf1...
> **Sources:**
>   - building-a-real-time-browser-mmorpg-with-threejs-rustwasm-and-durable-objects-2026-07-18.md
> **Links:**
- [[the-gitbook-migration-trap-4gp2]]
- [[deadstop-2025-vs-crossfit-games-2024-1okg]]
- [[threads-url-analyzer-gonggae-deiteowa-gyejeong-seungin-deiteoyi-gyeonggye-2mid]]
- [[hackthebox-void-whispers-writeup-bh5]]
- [[privacy-by-design-at-the-binary-level-no-ghost-sdk-in-your-build-1bl0]]

## Key Findings

---
source_url: https://dev.to/realmofechoes/building-a-real-time-browser-mmorpg-with-threejs-rustwasm-and-durable-objects-1ia2
ingested: 2026-07-18
sha256: c2c76b3c3768453b2668627c65a17f47b2cdf873bf1e8b0e8f7ced3b2051cf91
blog_source: Dev Community
---
Building a real-time browser MMORPG with Three.js, Rust/Wasm, and Durable Objects - DEV Community
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
[![Realm of Echoes](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F4034586%2Fbd3d4cde-b3f8-4658-bd4d-015ba1ad4706.jpg)](/realmofechoes)
[Realm of Echoes](/realmofechoes)
Posted on Jul 18
# 
Building a real-time browser MMORPG with Three.js, Rust/Wasm, and Durable Objects
[#javascript](/t/javascript)
[#gamedev](/t/gamedev)
[#rust](/t/rust)
[#webassembly](/t/webassembly)
Realm of Echoes is a real-time 3D fantasy MMORPG that runs in a normal desktop browser tab. Players can choose a Warrior or Mage and enter as a guest, so testing the game does not begin with a download or account form.
You can [try the live build here](https://realm-of-echoes-auth.realmofechoes.workers.dev/).
This is less a launch announcement than an architecture field note: what is working, where the boundaries are, and what has been difficult about putting an authoritative shared world behind a Three.js client.
## 
Why make an MMORPG for the browser?
The browser removes the biggest source of friction for early playtesting. A link can take someone from curiosity

## Summary

 to movement and combat in seconds, and guest identity lets the game demonstrate value before asking the player to keep an account.
That convenience creates constraints too:
- the renderer, UI, networking, audio, and game loop all share one tab
- backgrounding and focus changes are normal
- integrated graphics and modest laptops need to remain viable
- controls must coexist with browser behavior
- a client that is easy to open is also easy to inspect, so it cannot be trusted as the authority
Those constraints shaped the architecture more than any individual framework choice.
## 
The current architecture
The system has three main boundaries:
```
Browser
Three.js 0.185.0 + TypeScript UI
|
| WebSocket
v
Cloudflare Durable Object
authoritative shared-world state
|
+-- Rust gameplay worker compiled to WebAssembly
+-- D1 account and recovery persistence
Separate TypeScript Worker
public client and authentication surface
```
Enter fullscreen mode
Exit fullscreen mode
The browser owns presentation, input, and immediate feedback. Three.js renders the world, characters, animation, spell effects, and combat presentation.
The gameplay worker is written in Rust and compiled to WebAssembly. A Cloudflare Durable Object owns the authoritative live-world state, while WebSockets keep connected players synchronized. A separate TypeScript Worker serves the public client and authentication surface, and D1 supports persisted account and recovery data.
The important rule is simple: the client can make the game feel responsive, but it does not decide the durable outcome of combat or progression.
## 
Keeping authority without making combat feel remote
A purely round-trip-driven combat interface feels sluggish. A purely client-authoritative one is not acceptable for a persistent multiplayer game.
The useful boundary is intent versus outcome. Input and local presentation can react immediately: targeting feedback, animation starts, cast indicators, and UI state should not wait for a network round trip. The authoritative world still decides whether the action is valid and what changed.
That makes reconciliation a product concern, not just a networking concern. When the server disagrees, the correction must be legible. Silent snapping or unexplained cooldown changes feel like bugs even when the server is technically correct.
The work is therefore split between:
- keeping identifiers and state transitions stable enough to reconcile;
- limiting how much speculative presentation can get ahead;
- making corrections understandable in the HUD and world;
- testing under imperfect latency rather than only on a local connection.
## 
Guest-first onboarding is an identity problem
Guest play looks like a UI feature, but it reaches deep into persistence.
The current flow lets a player name a hero and start immediately. Account linking is optional and can retain that guest hero. That means the system needs a clean transition from temporary identity to persisted identity without duplicating

## Related Articles

- [[the-gitbook-migration-trap-4gp2]]
- [[deadstop-2025-vs-crossfit-games-2024-1okg]]
- [[threads-url-analyzer-gonggae-deiteowa-gyejeong-seungin-deiteoyi-gyeonggye-2mid]]
- [[hackthebox-void-whispers-writeup-bh5]]
- [[privacy-by-design-at-the-binary-level-no-ghost-sdk-in-your-build-1bl0]]
