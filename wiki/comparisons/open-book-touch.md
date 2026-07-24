---
title: "open book touch"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - container
  - data
  - hardware
  - image-generation
  - mobile
  - news
  - nlp
  - online
  - open-source
  - real-time
  - search
  - software
  - web
---

# open book touch

> **Source:** open-book-touch-open-source-e-reader-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** [ Crowd Supply ](/) - [Browse](/browse) - [Apply](/apply) - [About](/about) -  [ ![Unknown Avatar](/_marvin/images/default-avatar.png) My Account ](/account) -  [ ** Cart ](/cart) ** [Oddly Specific O...
> **Sources:**
>   - open-book-touch-open-source-e-reader-2026-07-18.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[i-started-a-dirt-notebook]]
- [[the-great-software-regress-how-move-fast-and-break-things-broke-our-lives]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[the-illustrated-stable-diffusion-2026-07-07]]

## Key Findings

[
Crowd Supply
](/)
- [Browse](/browse)
- [Apply](/apply)
- [About](/about)
- 
[
![Unknown Avatar](/_marvin/images/default-avatar.png)
My Account
](/account)
- 
[
** Cart
](/cart)
**
[Oddly Specific Objects](/oddly-specific-objects)
**
[Books](/books)
**
[KiCad](/kicad)
# [Open Book Touch](/oddly-specific-objects/open-book-touch)
### 
A pocketable, front-lit, open source e-reader — for every book, in every language
[
![Open Book Touch](/img/7a19/ea41febb-029e-492e-bb3b-5953813c7a19_aa-md.jpg)
](/img/7a19/ea41febb-029e-492e-bb3b-5953813c7a19_gallery-lg.jpg)
$46,940 raised
of $45,000 goal
104% Funded!
[
2
updates
](/oddly-specific-objects/open-book-touch/updates)
33
days left
[
243
backers
](/oddly-specific-objects/open-book-touch/backers)
Back this project to help bring it into existence.
Funding ends on Aug 20, 2026 at 04:59 PM PDT.
#### 
$149 - $249
[
View Purchasing Options
](#products)
#### Recent Updates
- 
Jul 15, 2026
[Never a Loss for Words: Search, Highlights, and Dictionaries](/oddly-specific-objects/open-book-touch/updates/never-a-loss-for-words-search-highlights-and-dictionaries)
- 
Jul 09, 2026
[Six Years in the Making, Open Book Touch Is Here!](/oddly-specific-objects/open-book-touch/updates/six-years-in-the-making-open-book-touch-is-here)
Subscribe
Sign up to receive updates.
**Open Book Touch** is the device I’ve been trying to build for six years: a small, beautiful, completely open source e-book reader that does one thing and does it well. There are no physical buttons on the front; the device is a single, perfectly symmetrical 4.26-inch front-lit e-paper touchscreen, one centimeter thin in its enclosure. Open Book Touch slips into a pocket and disappears until you unlock it to read.
It’s taken a while to get here, but the TL;DR is this: *it’s real now*. Earlier Open Books could show you a wall of plain text. This one shows your book covers in a gorgeous, deeply designed interface, reads EPUB files (*finally!*), and renders dozens of writing systems. There’s Wi-Fi too, but mostly for getting books on, not for living online. And the whole thing is open source, both hardware and software, so you can hack it, fork it, tear it down, and build it back up.
It’s a liberated book for the people.
[
![](/img/756c/e8be06e7-c723-42cd-9591-a6cda9bc756c_md-xl.jpg)
](/img/756c/e8be06e7-c723-42cd-9591-a6cda9bc756c_gallery-lg.jpg)
Open Book Touch isn’t trying to be a tablet. Like all of the objects I design, it makes a deliberate set of tradeoffs to do its one job beautifully:
- **It's for reading, not for everything.** No notifications, no browser, no feed to scroll. The Wi-Fi is there to sync the time and download books, nothing more. There's a soft keyboard for simple tasks, but it's not meant for note-taking or vibe coding.
- **It's a microcontroller, not a Linux box.** As it turns out, less can be more: Open Book Touch boots straight into the book you're reading, sips power at under a milliampere, and runs readable C++ firmware (on ESP-IDF/F

## Summary

reeRTOS) that you can understand and hack on.
- **It's small, not big.** It's small enough to forget you're carrying it in a jacket pocket, and light enough to fit in an ultralight backpacker's kit. Open Book Touch is more "mass market paperback" than "leather-bound hardcover" — but it'll go places a 10-inch tablet won't.
## Spoilers: It’s a Book
The whole point of an e-reader is the reading, so that’s where most of the work has gone. Open Book Touch reads **EPUB** and **plain text** files straight off its microSD card: drop in your books, and they show up on the shelf.
[
![](/img/1bb6/834a7347-b835-4c6a-b975-af0797f11bb6_md-xl.jpg)
](/img/1bb6/834a7347-b835-4c6a-b975-af0797f11bb6_gallery-lg.jpg)
But "it shows text" is table stakes. Open Book Touch implements a real typesetting engine, alongside gorgeous fonts in multiple weights and sizes to truly up the ante:
- **Proper typography.** Lines are justified with even word spacing, words hyphenate at the right places, and pages break cleanly (hyphenation dictionaries available for English, Spanish, French, and Italian). Images embedded in a book render inline, 1-bit dithered to look crisp on e-paper.
- **Fonts that were actually drawn.** Your books are set in carefully drawn bitmap versions of **Lucida Bright** and **Lucida Sans**, in three sizes, each with true **bold** and *italic* letterforms drawn at every weight. (These were open-sourced in 1989 by Sun Microsystems; we are the inheritors of a proud legacy).
- **The stuff you reach for without thinking.** Tap and hold to highlight a passage or look up a word. Dog-ear a page. Sort your books onto shelves. Put the device down for a week, pick it up, and it opens right back to the page — and the spot on the page — where you left off.
[
![](/img/198d/15b3545a-e08d-4ff0-9043-064230ca198d_md-xl.jpg)
](/img/198d/15b3545a-e08d-4ff0-9043-064230ca198d_gallery-lg.jpg)
It’s a reader you’ll actually want to read on.
## Light Reading
Our e-paper panel packs the 480 × 800 pixels you’d normally find on a much larger 7.5-inch display into just 4.26 inches diagonal, so everything is remarkably sharp. It’s a 1-bit display at heart (crisp black on white), and it’s dense enough that even your book covers, dithered to pure black-and-white, look genuinely delightful on the home screen.
[
![](/img/f194/38422b6c-cec5-49c0-8750-0143958cf194_md-xl.jpg)
](/img/f194/38422b6c-cec5-49c0-8750-0143958cf194_gallery-lg.jpg)
The best part, though, is the frontlight. With **both warm and cool LEDs** in the frontlight module, you’re not stuck with one harsh color temperature: you can warm it all the way down for reading in bed, cool it for daylight, or dial in something in between, with fully adjustable brightness. You can read all night without wrecking your night vision (or keeping your partner awake with a reading light).
E-paper is still e-paper. The screen refreshes at a readerly pace; you’re not going to play DOOM on it. The fast 1-bit mode drives everything you touch, page tu

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[i-started-a-dirt-notebook]]
- [[the-great-software-regress-how-move-fast-and-break-things-broke-our-lives]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
