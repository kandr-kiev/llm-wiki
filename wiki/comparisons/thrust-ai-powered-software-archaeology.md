---
title: "thrust ai powered software archaeology"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - container
  - data
  - edge
  - image-generation
  - news
  - software
---# thrust ai powered software archaeology

> **Source:** ai-cant-recreate-the-thrust-game-but-it-can-help-you-understand-it-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-12
> **Updated:** 2026-07-12
> **Confidence:** high
> **Description:** AI Can't Recreate Thrust (But It Can Help You Understand It) ![Annhexation gameplay — a hex-based 4X strategy map](/annhex-gameplay-wide.jpg) ![Annhexation gameplay — a hex-based 4X strategy map](/ann...
> **Sources:**
>   - ai-cant-recreate-the-thrust-game-but-it-can-help-you-understand-it-2026-07-11.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[comparisons/ai]]
- [[animals-vs-ghosts]]
- [[away]]

## Key Findings

AI Can't Recreate Thrust (But It Can Help You Understand It)
![Annhexation gameplay — a hex-based 4X strategy map](/annhex-gameplay-wide.jpg)
![Annhexation gameplay — a hex-based 4X strategy map](/annhex-gameplay.jpg)
Annhexation
Early access
A turn-based 4X strategy game I built from scratch — custom WebGPU engine, eight civilisations, no install. Play it in your browser right now.
[
Play free in browser
](https://annhexation.com)
[
Wishlist on Steam
](https://store.steampowered.com/app/4663920/Annhexation/)
I asked Claude to recreate the classic 1986 game Thrust for me in the browser. It created slop but then things spiralled out of control.
Thrust was one of my favourite games on the BBC Micro — written by Jeremy C. Smith and published in 1986, it’s a deceptively deep game with amazing physics and gameplay. You pilot a ship through caverns, collecting fuel, avoiding turret fire, and retrieving a pod for bonus points while fighting gravity and momentum. Jeremy went on to create the even more impressive Exile with Peter Irvin before tragically dying in an accident in 1992. He was somewhere between 16 and 18 when he wrote Thrust. You can [play the original online](http://bbcmicro.co.uk/game.php?id=432).
I’ve got a BBC Master on the desk beside me and I still occasionally fire up Thrust on there along with some of the other classics. It’s one of those games I keep returning to along with Elite, Exile and Holed Out. I’ve now recreated three of these in different ways… the fourth is looking increasingly unavoidable.
## Starting with slop
Anyway. I guess I’d been thinking about Thrust as one morning recently I somewhat casually asked Claude Code to create it for me in the browser. I think I’d been reading the latest proclamations of capability from OpenAI and Anthropic and so I put together quite a comprehensive spec, gave it access to the original disassembled source code, screenshots, and said “go and recreate Thrust for me.”.
It created something for which the term slop would be too kind, it very vaguely resembled Thrust — it had the scanline stuff, sort of — but it was truly dreadful. It hadn’t even got gravity working right, the ship didn’t fall properly, the controls felt weird, and it was just… grim. In some ways its amazing that it created something that sort of worked and sort of looked like Thrust but it was not playable and nothing close to the elegance and beautfy of the real thing.
And that’s the thing about a game like Thrust. You could knock out something superficially similar pretty quickly — just run at the device frame rate, use standard delta-time physics, draw some caverns. But it would feel nothing like Thrust. The magic is in the specific timings, the weight of the ship, the way momentum builds. Particularly if you’ve played the original then those details are everything, and an AI working from a text description, and it turns out even the original source, can’t capture them.
## The archaeology
But it got me curious. How *did* t

## Summary

he original work? I find the tricks developers used to make this stuff work on the 8-bits fascinating, and it became a bit of an archaeology session. I quickly found [this brilliant commented disassembly](https://github.com/kieranhj/thrust-disassembly) of the original source by Kieran Connell and found myself feeding it into Claude and asking questions.
This is where things got interesting. Not because AI wrote the code — the code itself isn’t complicated, it’s a 1986 game that ran in 32K of RAM — but because Claude turned out to be an extraordinary tool for interrogating 6502 assembly. I could feed in a block of disassembled source and ask “how does the level data work?” or “what’s the physics model doing here?” and get detailed, accurate explanations of what the original code was doing.
Now to be fair I was working from some commented disassembled source code but even given that it was able to extract information from both the comments and the assembly and come up with detailed descriptions of how the game worked. My sense is without the comments helping to focus it at the right areas it would have been much less useful - but even so, it made the job an awful lot simpler and more enjoyable. And yes it seems likely I’ll strip the comments from the code and see how well Claude does then.
While doing this I realised I could use the answers as the basis to recreate the original game and started asking Claude to create specifications for the various subsystems. Most of the specifications I generated can be found in a [specs folder](https://github.com/JamesRandall/ts-thrust/tree/main/specs) in the source code. I might write them up properly at some point but for now they give a good insight into the nuances in the original — there’s quite a lot going on, more than I’d realised. For example I’d never noticed that the turrets stop firing for a time if you hit the generator, and there are subtleties in their firing angles that only become apparent when you read the actual code.
## The Physics
The physics was one of the most interesting areas to dig into. Thrust uses Q7.8 fixed-point arithmetic — a common technique on 8-bit machines where you don’t have floating point hardware. The rotation system uses 32 steps with lookup tables for the force components.
But the really tricky part was timing. My first implementation used the correct constants from the disassembly — the same gravity, the same thrust values, the same drag — but the ship was far too fast and too agile. It didn’t have the right weight. The constants were identical to the original so it had to be a timing problem.
And it was. The original doesn’t run its physics at the BBC Micro’s 50 Hz VSync rate. The tick loop waits at least 3 centiseconds per frame, giving an effective rate of about 33.33 Hz. But it goes further than that: within each tick, physics updates are gated to only 6 active slots per 16-tick window. The core of the physics step looks like this:
/** The 6 active physics slots per 

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[comparisons/ai]]
- [[animals-vs-ghosts]]
- [[away]]
