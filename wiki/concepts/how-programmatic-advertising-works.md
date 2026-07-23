---
title: "how programmatic advertising works"
type: concept
tags:
  - llm-wiki
  - knowledge-base
    - async
  - container
  - edge
  - gpt
  - news
  - search
---

# how programmatic advertising works

> **Source:** how-programmatic-advertising-works-2026-07-23.md
> **Type:** concept
> **Created:** 2026-07-23
> **Updated:** 2026-07-23
> **Confidence:** high
> **Description:** July 22, 2026 / #Advertising # How Programmatic Advertising Works ![Manish Shivanandhan](https://cdn.hashnode.com/res/hashnode/image/upload/v1725238262566/37625c8b-4d87-4b8c-8fb7-b4fdcf34de9e.png?w=50...
> **Sources:**
>   - how-programmatic-advertising-works-2026-07-23.md
> **Links:**
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[i started a dirt notebook]]
- [[5 Agent Skills I Use Every Day]]

## Key Findings

July 22, 2026
/
#Advertising
# How Programmatic Advertising Works
![Manish Shivanandhan](https://cdn.hashnode.com/res/hashnode/image/upload/v1725238262566/37625c8b-4d87-4b8c-8fb7-b4fdcf34de9e.png?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp)
[
Manish Shivanandhan
](/news/author/manishshivanandhan/)
![How Programmatic Advertising Works](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/ead3788a-52c2-4821-b5c9-1c626c50d375.png)
Most tutorials on [programmatic advertising](https://advertising.amazon.com/blog/programmatic-advertising#1) stop at the web banner. That's a shame, because the idea gets far more interesting once you follow it off the screen and into the physical world.
If you've never worked in advertising, don't worry. You don't need any ad industry background to follow along. If you can read basic Python, you have everything you need.
The advertising part is just the setting. The real subject is a skill you'll use everywhere: taking a messy slice of the real world and turning it into data that software can act on.
In this article, you'll learn what programmatic advertising is and why it worked so well on the web. You'll see why bringing it to a billboard is really a data modeling problem, and you'll build small Python models for each step.
### What We'll Cover:
- [What Is Programmatic Advertising?](#heading-what-is-programmatic-advertising)
- [Why the Web Made Programmatic Easy](#heading-why-the-web-made-programmatic-easy)
- [The Billboard Problem](#heading-the-billboard-problem)
- [Step 1: Resolve Entities](#heading-step-1-resolve-entities)
- [Step 2: Model Location as Computed Context](#heading-step-2-model-location-as-computed-context)
- [Step 3: Represent Availability as a Schedule, Not a Boolean](#heading-step-3-represent-availability-as-a-schedule-not-a-boolean)
- [Step 4: Express Price as a Function, Not a Number](#heading-step-4-express-price-as-a-function-not-a-number)
- [Putting It Together](#heading-putting-it-together)
- [An Exercise to Build the Intuition](#heading-an-exercise-to-build-the-intuition)
- [The Takeaway](#heading-the-takeaway)
## What Is Programmatic Advertising?
Advertising has two sides. A publisher, such as a news site, has ad space to fill. And an advertiser, such as a shoe brand, wants to fill it. For decades, connecting the two meant phone calls, emails, and paperwork.
Programmatic advertising replaces that manual process with software. No human negotiates the placement. A system looks at an ad slot and decides, in milliseconds, whether to buy it and at what price.
Here's how it works when you open a web page. The page tells an ad exchange that a slot is open, along with some context about the page and the viewer. Advertisers' systems bid on the slot in a live auction. The winning ad appears before the page finishes loading. This process is called [real-time bidding](https://en.wikipedia.org/wiki/Real-time_bidding), and it happens billions of times a day.
Two quick term

## Summary

s will help. Inventory means the ad space a seller has to offer. An impression means one view of an ad by one person.
On the web, this model arrived fast and felt almost effortless. It's worth understanding why.
## Why the Web Made Programmatic Easy
The web made programmatic easy by accident. Every web ad slot came pre-structured. It had an address, meaning a URL and a position on the page. It sat inside a document with a known shape, the [Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model). And it could report back whether an ad had loaded and been seen.
The whole environment was machine-readable from birth, because machines were already serving it. When automated buying showed up, it had a clean surface to work against. The medium had already done the hard modeling work.
Keep that in mind. It's the key to the whole lesson.
## The Billboard Problem
Now point the same idea at a billboard. None of that convenient structure exists.
A physical sign doesn't announce where it is or which way it faces. It doesn't say what it costs this week or whether it's even available. For most of its history, that information lived in rate cards and salespeople's memories, not in anything a program could query.
Here's the insight. Out-of-home advertising, the industry term for billboards, transit posters, and public screens, didn't lag the web because it was a weaker medium. It lagged because it had no machine-readable interface. The audience was always there. The structured data was not.
So the real work of bringing programmatic to the physical world isn't clever bidding logic. It's data modeling.
Let's make that concrete. There are four steps. Each one maps to a pattern you'll see in many other engineering problems.
## Step 1: Resolve Entities
The same billboard often shows up in several vendors' datasets. Each vendor gives it a different name and slightly different coordinates. Before you can do anything else, one physical object has to become one record. This is known as [record linkage](https://en.wikipedia.org/wiki/Record_linkage), here with a geographic twist.
A simple approach: treat two records as the same panel if they sit close together and share a similar name. To measure the distance between two coordinates, you can use the [haversine formula](https://en.wikipedia.org/wiki/Haversine_formula).
```
from math import radians, sin, cos, asin, sqrt
def haversine_m(lat1, lon1, lat2, lon2):
"""Distance between two coordinates in meters."""
lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
a = sin((lat2 - lat1) / 2) ** 2 + \
cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2
return 6371000 * 2 * asin(sqrt(a))
def same_panel(a, b, max_distance_m=25):
close = haversine_m(a["lat"], a["lon"], b["lat"], b["lon"]) <= max_distance_m
similar_name = a["name"].lower().split()[0] == b["name"].lower().split()[0]
return close and similar_name
vendor_a = {"name": "I-95 North Bulletin", "lat": 25.7907, "lon": -80.1300}

## Related Articles

- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[i started a dirt notebook]]
- [[5 Agent Skills I Use Every Day]]
