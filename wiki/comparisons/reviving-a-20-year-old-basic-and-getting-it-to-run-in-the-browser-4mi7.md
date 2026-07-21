---
title: "reviving a 20 year old basic and getting it to run in the browser 4mi7"
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
  - video-generation
  - web
---

# reviving a 20 year old basic and getting it to run in the browser 4mi7

> **Source:** reviving-a-20-year-old-basic---and-getting-it-to-run-in-the-browser-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/michel_vilain_f1f8e06dc47/reviving-a-20-year-old-basic-and-getting-it-to-run-in-the-browser-4mi7 ingested: 2026-07-18 sha256: 725749c62da23bcc15db9c7647f52317c32a66aab18...
> **Sources:**
>   - reviving-a-20-year-old-basic---and-getting-it-to-run-in-the-browser-2026-07-18.md
> **Links:**
- [[5 things i learned doing ai evaluation for 2 years 3kgh]]
- [[adding an ai chatbot to echostats 290m]]
- [[how we beat hotspot performance by cheating but not like that]]
- [[the gitbook migration trap 4gp2]]
- [[my insights on what working at big tech is actually like kgd]]

## Key Findings

---
source_url: https://dev.to/michel_vilain_f1f8e06dc47/reviving-a-20-year-old-basic-and-getting-it-to-run-in-the-browser-4mi7
ingested: 2026-07-18
sha256: 725749c62da23bcc15db9c7647f52317c32a66aab185625961a5a66fe20a7e81
blog_source: Dev Community
---
Reviving a 20-year-old BASIC — and getting it to run in the browser - DEV Community
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
![Cover image for Reviving a 20-year-old BASIC — and getting it to run in the browser](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fb4395u2o0z1pnd4uasoj.png)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fb4395u2o0z1pnd4uasoj.png)
[![michel vilain](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F4035368%2Fbff610af-85a9-4e71-bcf7-d49e3ed33f63.jpg)](/michel_vilain_f1f8e06dc47)
[michel vilain](/michel_vilain_f1f8e06dc47)
Posted on Jul 18
# 
Reviving a 20-year-old BASIC — and getting it to run in the browser
[#opensource](/t/opensource)
[#webassembly](/t/webassembly)
[#qt](/t/qt)
[#basic](/t/basic)
## 
First, go press a button
Before the story, the thing itself. Open this in a browser tab:
👉 **[https://uglymike17.github.io/basic256/](https://uglymike17.github.io/basic256/)**
That's the full BASIC

## Summary

256 editor and interpreter — running entirely in your browser, no install, no plugin, no account. Type `PRINT "hello"`, hit run. Or load a bundled example straight from the URL: [`?run=mandelbrot`](https://uglymike17.github.io/basic256/?run=mandelbrot).
If that feels unremarkable, hang on — a year ago this program didn't build on a modern machine at all.
## 
What BASIC256 is
BASIC256 (originally **KidBASIC**) is an easy, graphical dialect of BASIC built to teach absolute beginners how to program. Three panes: a code editor, a text output console, and a graphics canvas. You write a couple of lines and *immediately* see a circle, hear a beep, watch a sprite move. That instant feedback loop is the whole point — it's the on-ramp a lot of us had in the 80s and 90s, rebuilt for kids (and hobbyists) today.
It had a good run on SourceForge, reached version 2.0.0.11… and then stopped. Development stalled, apparently after a failed attempt to port it to Qt6. A few people tried to pick it up. The code drifted further from what modern toolchains expect every year.
I decided to have a go at bringing it back. I'll be honest about my qualifications up front, because it matters to the rest of this post: **I'm a hobbyist, not a C++ developer.** I'm comfortable with project direction, build configuration, and reading code, but I do not write production C++ from scratch. I've leaned heavily on AI tooling to get through the parts that are over my head. If that disqualifies me in your eyes, fair enough — but the thing runs, and I had a lot of fun.
## 
The revival, in layers
The one lesson I'd pass on to anyone resurrecting an old codebase: **do it in layers, and never try to modernize everything at once.** A giant "fix it all" branch becomes a multi-month swamp. Small, verifiable steps kept me sane.
Roughly the order it happened in:
**1. Get it onto modern infrastructure.** Migrated the original SVN history to GitHub, then set up continuous integration so *every* commit at least tries to build. You can't modernize what you can't build.
**2. qmake → CMake.** The old `.pro` files were replaced with CMake. I kept qmake working in parallel for a while so I always had a fallback, then removed it once CI was green.
**3. MinGW → MSVC on Windows.** The classic "missing `libstdc++-6.dll`" deployment pain went away once I moved to MSVC with `windeployqt`. Fewer DLL surprises, better tooling.
**4. One pipeline, four platforms.** A single GitHub Actions workflow now builds Windows, Linux x86-64, Raspberry Pi (ARM64) and macOS, each gated behind the TestSuite so a broken build can't ship. The Raspberry Pi build was a highlight: GitHub now offers native ARM64 runners, so I could throw out the old QEMU-emulation approach entirely. Linux ships as an AppImage (built with `linuxdeploy`), Windows as an NSIS installer.
**5. Qt5 → Qt6.** The big one. This is the migration that had killed the project before. `QRegExp` became `QRegularExpression`, the multimedia layer was rewritten, and I 

## Related Articles

- [[5 things i learned doing ai evaluation for 2 years 3kgh]]
- [[adding an ai chatbot to echostats 290m]]
- [[how we beat hotspot performance by cheating but not like that]]
- [[the gitbook migration trap 4gp2]]
- [[my insights on what working at big tech is actually like kgd]]
