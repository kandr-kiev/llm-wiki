---
title: "genesis mission lawrence berkeley national laboratory segment anything dino"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - api
  - async
  - data
  - dataset
  - image-generation
  - news
  - video-generation
---
backlinks:
  - genesis-mission-lawrence-berkeley-national-laboratory-segment-anything-dino
---


# genesis mission lawrence berkeley national laboratory segment anything dino

> **Source:** metas-ai-models-are-powering-the-first-wave-of-genesis-mission-projects-2026-07-21.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://ai.meta.com/blog/genesis-mission-lawrence-berkeley-national-laboratory-segment-anything-dino/?_fb_noscript=1 ingested: 2026-07-21 sha256: 8fab188fc4371e62df16061e4e792ab0fce97f...
> **Sources:**
>   - metas-ai-models-are-powering-the-first-wave-of-genesis-mission-projects-2026-07-21.md
> **Links:**
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[Automating away]]
- [[kimi k3]]
- [[doom]]

## Key Findings

---
source_url: https://ai.meta.com/blog/genesis-mission-lawrence-berkeley-national-laboratory-segment-anything-dino/?_fb_noscript=1
ingested: 2026-07-21
sha256: 8fab188fc4371e62df16061e4e792ab0fce97fa62fa78f845633cb8a7e0476da
blog_source: Hacker News AI
---
How Meta’s AI Models are Powering the First Wave of Genesis Mission Projects- - - 
- 
- 
- 
- 
- 
- 
- 
- 
[![Meta](https://scontent-iev1-1.xx.fbcdn.net/v/t39.8562-6/252294889_575082167077436_6034106545912333281_n.svg/meta-logo-primary_standardsize.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=Ee8z1FcRjJ0Q7kNvwHA23ww&_nc_oc=AdpRaYTQ3n3EKAI0mC43kWYPTVi32TKFsQhuSzRSY2i61g-XlQ8AUponIc7Hig8XNcM&_nc_zt=14&_nc_ht=scontent-iev1-1.xx&_nc_gid=hyVsfaBU4uS_0OZynGtp8Q&_nc_ss=7b20f&oh=00_AQBEDYlVPUNlc4CdTZd58xEzFiHnxysIyq9jkAmShkjIVA&oe=6A6591B9)](#)- [Products](#)
- [AI Research](#)
- [Resources](#)
- [About](#)
- [Meta Model API](https://developer.meta.com/ai/)
- [Try Meta AI](https://applink.meta.ai/?pt=10684&pid=ai_meta_site&utm_source=ai_meta_site&utm_medium=web&utm_campaign=nav_try-meta-ai-palette_07072026&utm_content=nav_try-meta-ai-palette_07072026&ct=nav_try-meta-ai-palette_07072026&referrer=utm_source%3Dai_meta_site%26utm_medium%3Dweb%26utm_campaign%3Dnav_try-meta-ai-palette_07072026%26utm_content%3Dnav_try-meta-ai-palette_07072026)
- [](/)
Open Source# How Meta’s AI Models are Powering the First Wave of Genesis Mission Projects
July 21, 2026•**6 minute read![](https://scontent-iev1-1.xx.fbcdn.net/v/t39.2365-6/752631850_918439901272497_2117962010845605116_n.png?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=pryaHqlei_cQ7kNvwH1vi1d&_nc_oc=AdouyXEjoCdpWAOINj1RBFQwtMTfMUPZLe2n2NfY1axF-8utfjwlfrSEc0dqXIBJxO0&_nc_zt=14&_nc_ht=scontent-iev1-1.xx&_nc_gid=hyVsfaBU4uS_0OZynGtp8Q&_nc_ss=7b20f&oh=00_AQAWuRSPY43_8KzG19KcoU6cC3_w-IECX57O2RowXKnPeA&oe=6A79F03E)[Lawrence Berkeley National Laboratory ](https://www.lbl.gov/) — one of the [US Department of Energy's](https://www.energy.gov/) premier research laboratories, known for Nobel Prize-winning work in physics, chemistry, and materials science — operates some of the most advanced scientific facilities on the planet. Among them is the [Advanced Light Source](https://als.lbl.gov/) (ALS), a football field-sized facility that produces intensely bright beams of X-ray light, allowing researchers to study materials from the atomic and molecular scale all the way to plants. The ALS's instruments, known as beamlines, generate enormous quantities of data — and as recent facility upgrades have dramatically increased their resolution and speed, the volume of data has exploded beyond what scientists can keep up with.
The numbers are staggering: The DOE's light and neutron source facilities now produce tens of petabytes of data annually — that's millions of gigabytes, roughly equivalent to streaming 2 million hours of HD video. This backlog didn't always exist. Upgraded detectors, which have gone from capturing a single image every six seconds to 100,000 images per second, 

## Summary

mean these facilities now generate orders of magnitude more data than they did a decade ago, and traditional manual analysis simply can't keep pace.
The problem goes beyond volume: domain experts are scarce and overwhelmed, and modern in-situ experiments — where scientists observe dynamic processes like chemical reactions or material failures as they occur — demand real-time interpretation that no human team can deliver manually.
Much of the analysis challenge comes down to one task: segmentation — the process of identifying and drawing precise boundaries around distinct structures within an image. In computer vision, segmentation is what enables everything from medical scans that distinguish tumors from healthy tissue to autonomous vehicles that separate pedestrians from pavement. In scientific research, segmentation is what transforms a raw X-ray image from a wall of grayscale pixels into a labeled map of meaningful structures — cell walls, mineral grains, semiconductor layers — that researchers can quantify and compare across experiments.
## SYNAPS-I and the Genesis Mission
In late 2025, the White House launched [The Genesis Mission](https://www.energy.gov/undersecretaryforscience/genesis-mission/genesis-mission), a sweeping national initiative to accelerate scientific discovery and technological leadership using advanced artificial intelligence, led by DOE. SYNAPS-I (SYnergistic Neutron And Photon Science – Intelligence) in partnership with [Argonne](https://www.anl.gov/), [Brookhaven](https://www.bnl.gov/world/), [Oak Ridge](https://www.ornl.gov/), and other laboratories, aimed at transforming data analysis across X-ray and neutron science from a monthslong bottleneck into a real-time discovery engine, with scientific imaging as a major target. Nowhere is that bottleneck more acute than in image segmentation, where extracting meaningful structures from experimental data can consume weeks of expert effort per dataset.
At the heart of SYNAPS-I's segmentation pipeline are two open-source foundation models released by Meta: [Segment Anything Model 3](https://ai.meta.com/research/sam3/) (SAM 3) and [DINOv3](https://ai.meta.com/research/dinov3/).
## How SAM and DINO Transform Scientific Imaging
DINOv3 is a self-supervised vision model, meaning it learns visual patterns from raw images without requiring humans to label them first. It excels at understanding what different structures in an image represent and where they are located. SAM takes that understanding a step further, drawing precise boundaries around individual objects in an image — much like a scientist carefully outlining structures by hand, but in seconds rather than hours.
Together, the two models form a complementary pipeline: SAM delivers precise, pixel-level boundaries, while DINO provides global context to identify each structure and its place within the sample. The SYNAPS-I team fine-tuned both models on scientific imaging data collected at DOE beamlines, then deployed them across

## Related Articles

- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[Automating away]]
- [[kimi k3]]
- [[doom]]
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "genesis-mission-lawrence-berkeley-national-laboratory-segment-anything-dino")
```
