---
title: "pebble mega update july"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - async
  - batch
  - data
  - few-shot
  - image-generation
  - news
  - open-source
  - real-time
  - software
---

# pebble mega update july

> **Source:** pebble-mega-update--july-2026-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** [← Back to Blog](/blog)July 14, 2026# Pebble Mega Update - July 2026 TL:DR; - [Pebble Time 2 Shipping Status](/blog/pebble-mega-update-july-2026#pebble-time-2-shipping-status) - [Pebble Software Updat...
> **Sources:**
>   - pebble-mega-update--july-2026-2026-07-17.md
> **Links:**
- [[Mesh LLM: distributed AI computing on iroh]]
- [[Automating Ai Away]]
- [[Applying Massive Language Models In The Real World With Cohere]]
- [[the great software regress how move fast and break things broke our lives]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]

## Key Findings

[← Back to Blog](/blog)July 14, 2026# Pebble Mega Update - July 2026
TL:DR;
- [Pebble Time 2 Shipping Status](/blog/pebble-mega-update-july-2026#pebble-time-2-shipping-status)
- [Pebble Software Updates](/blog/pebble-mega-update-july-2026#pebble-software-progress-and-roadmap)
- [PT2 - Issues You’ve Reported](/blog/pebble-mega-update-july-2026#pebble-time-2-problems-you-ve-reported)
- [Pebble Round 2 Production Update](/blog/pebble-mega-update-july-2026#pebble-round-2-production-update-and-timeline)
- [Index 01 Production Update](/blog/pebble-mega-update-july-2026#index-01-production-update-and-shipping-timeline)
### [#Pebble Time 2 Shipping Status](#pebble-time-2-shipping-status)
![](/_next/image?url=%2Fassets%2Fpebble-mega-update-july-2026-0-cleanshot_2026-07-14_at_07.14.362x.png&w=3840&q=75)
Since we started mass production in late March, we’ve built over 23,000 Pebble Time 2 watches. We’re over 80% of the way through fulfilling all the pre-orders we’ve received! But that means there are still some ultra patient folks who haven’t received their watches yet. If you’ve placed an pre-order for PT2 and haven’t received it yet (including Batch 6 - August), here’s when we expect to ship your watch out:
- Pebble Time 2 - Black → July 31
- Pebble Time 2 - Red → July 31
- Pebble Time 2 - Grey → July 28
- Pebble Time 2 - Blue → July 28
Coincidentally, this means that we’ll be ‘in-stock’ with no wait very soon! If you’ve been holding off placing an order because you didn’t want to wait, now is the time to jump on it. This won’t last forever - first-come first serve. As soon as the current inventory is sold out, we’ll be back in pre-order mode waiting for the next shipment.
Order today on [rePebble.com/watch](/watch).
Major props to our three person customer support and logistics team! Claudio, Trevor and Colin have answered thousands of your questions and helped ship watches safely onto your wrist in 93 countries. Have a question? Please check out our [Help site](https://help.repebble.com/en/) first. If that doesn’t have an answer, please email us at [[email protected]](/cdn-cgi/l/email-protection#88e1e6eee7c8faedf8edeaeae4eda6ebe7e5).
Want an extra Pebble charger? [shop.repebble.com](http://shop.repebble.com/) now carries accessories - full selection of straps coming soon.
### [#Pebble Software - Progress and Roadmap](#pebble-software-progress-and-roadmap)
Over the last 6 months, the core four person Pebble software team built and shipped a metric ton of new Pebble open source software! Our improvements were centered around these areas:
**Battery life**
We’ve (well, mostly Gerard 🙂) worked extraordinarily hard over the last few months, optimizing and reducing power consumption in PebbleOS. As [predicted](https://ericmigi.com/blog/how-to-build-a-smartwatch-software-setting-expectations-and-roadmap/#near-term-software-r), we boosted the median battery life of Pebble 2 Duo from 17 days (last summer) to over 30 days. Pebble Time 2 median is currently around 

## Summary

21 days - more improvements in the works here too! The biggest consumers of power are backlight, watchfaces with a lot of animations and health tracking. If you want to ‘hypermile’ your Pebble, try switching to a low-animation watchface and the new *Battery Saver* backlight mode (Settings → Display → Backlight).
**Apps and SDK**
**T**ogether with the [Moddable](http://moddable.com/) team, we’ve published several Pebble SDK updates introducing new features like:
- [Touch Screen API](https://developer.repebble.com/guides/events-and-services/touch/) ([Calculator](https://apps.repebble.com/calculator_10966bb2d22145c4b428dfd7) on your wrist anyone?)
- [Speaker API](https://developer.repebble.com/guides/events-and-services/speaker/) (useful for [tuning your guitar](https://apps.repebble.com/guitar-pitch_6a19b41e81fae00009439e25), or feeding your [Tamagotchi](https://apps.repebble.com/tamagotchi-emulator_216a0f62c6e44aac8f725e68))
- [RGB Backlight API](https://developer.repebble.com/guides/events-and-services/light/#tinting-the-backlight-rgb-hardware-only) (try it in this wild little app [Chinese Toy Phone](https://apps.repebble.com/chinese-toy-phone_69f663b5ea28ba000ab50545))
- Apps can now determine [how they were quick launched](https://developer.repebble.com/docs/c/Foundation/Launch_Reason/#launch_button) (ie by single press, long press)
- [Alloy](https://developer.repebble.com/guides/alloy/) (native JS apps)
- FFI - run C code within Alloy JS apps (similar to Android NDK) and js debugger
- A [bunch of new ](https://developer.repebble.com/sdk/changelogs/4.17/)JS APIs
- `pebble build --debug` now defines PBL_DEBUG and launches XSBUG, a powerful JS debugger
Developers in the Pebble community have created [2,120 apps and watchfaces](https://apps.repebble.com/faces) for Pebble Time 2 and Pebble Round 2 already!
**Index 01**
The first version of all Index 01 functionality is up and running inside the Pebble mobile app. Don’t have an Index 01 yet? You can check out how it works and try the software interface in the Pebble app, just go to Settings → General → Enable Index feed.
All the main features are in, including syncing to iOS Reminders, Obsidian, Google Tasks, Calendar, Android music control, MCPs and sending recordings or transcriptions to your own server or app via Webhook. Optional encryption (you own the keys) protects optional cloud backup. And of course, it’s all open source ([github.com/coredevices/mobileapp](https://github.com/coredevices/mobileapp)). We even built a little webapp that you can use to access your Index information from anywhere → [index.rePebble.com](http://index.repebble.com/). Watch the [podcast](https://youtu.be/eF6hxEXwgso?t=406) or read the [blog post](/blog/how-i-use-my-index-01-production-update#how-do-i-use-my-index-01) to learn more.
**Stability**
Thanks to [helpful bug reports ](https://help.repebble.com/en/articles/15403206-get-help-contact-us-bug-reports)from y’all, we’ve made hundreds of small improvements to Pebb

## Related Articles

- [[Mesh LLM: distributed AI computing on iroh]]
- [[Automating Ai Away]]
- [[Applying Massive Language Models In The Real World With Cohere]]
- [[the great software regress how move fast and break things broke our lives]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
