---
title: "and nothing else</h-v>"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - data
  - fine-tuning
  - image-generation
  - news
  - real-time
  - use-case
  - video-generation
---

# and nothing else</h-v>

> **Source:** regressive-jpegs-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** Navigation: Homepage     Index     Yearly archives Fun Astrophotography     (catalog) About this site Real pages Dark Light TTY # *Regressive JPEGs:* 2026-07-17  One of the cool features of JPEG files...
> **Sources:**
>   - regressive-jpegs-2026-07-18.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[i-started-a-dirt-notebook]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
- [[open-source-monopoly]]

## Key Findings

Navigation:
Homepage
    Index
    Yearly archives
Fun
Astrophotography
    (catalog)
About this site
Real pages
Dark
Light
TTY
# *Regressive JPEGs:*
2026-07-17 
One of the cool features of JPEG files is that there's the option to save low frequency components first.
This means that a partially downloaded image will be displayed at low resolution instead of being cut off.
In the file, this works by breaking up the compressed data into multiple "scans", each prefixed with a header.
Here's the first scan of a representive image:
FF DA - "start of scan" marker
00 0C - Big endian length field (12 bytes) Includes itself
03 - Number of channels in scan (3)
01 - Global id of first included channel
00 - Huffman table index #1 (DC: 0, AC: 0)
02 - Global id of second included channel
10 - Huffman table index #2 (DC: 1, AC: 0)
03 - Global id of third included channel
10 - Huffman table index #2 (DC: 0, AC: 0)
00 - Starting DCT bin (DC)
00 - Ending DCT bin (also DC)
01 - Precision: half, no pre-existing data. 
f8ad 512d d3f1 cd96 - Huffman coded DCT coefficients
bcb0 58df 53d5 5d97
[...and a lot more]
... this one includes the lowest (DC) Fourier bin for all three color channels.
The three color channels are YCbCr instead of the usual RGB.
The luminance (Y) seperated because it must be high quality, but the color can be fudged quite a bit while looking fine.
Very roughly: Y = G, Cb = B - G, Cr = R - G
After it, the file contains eight more scans to fill in the rest of the data:
Scan numberChannelsDCT bin rangePrecision
0Y Cb Cr0 - 0Half (-1 bit)
1Y1 - 5Quarter (-2 bits)
2Cb1 - 63Half
3Cr1 - 63Half
4Y*6 - 63*Quarter
5Y1 - 63Half
6Y Cr Cb0 - 0Full
7Cr1 - 63Full
8Cb1 - 63Full
9Y1 - 63Full
Scan #0 contains a very low resolution preview of the image.
Scan #1 adds some details to the luminance.
Scans number two through five contain full low precision data.
Scan 4 has an unusual spectral range because it's filling in the gap left by #1.
That way, number 5 has full quarter precision data to build on.
Scans six through nine add the final missing bit to bring the image to full quality.
Given what I said about color being less important, it might seem weird that my example has the color data first:
This works because the the chrominance is saved at half resolution (quarter pixel count).
As a result, full chrominance data (Cr + Cb) only weighs half as much as luminance.
*Since each scan explicitly sets its spectral range*,
it should be possible to construct a JPEG file
where future scans overwrite already rendered image data.
Actually, it's very easy to do this:
Concatenate multiple images with the same resolution and filter out the start-of-image, start-of-frame and end-of-image markers.
This can be done in a hex editor, but I used a quick and dirty C program.
*When served over a slow network*, this concatenated file will switch between multiple images:
Click to open in new tab
*But, most decoders will give up after some number of scans*:
I think this is done to avoid 

## Summary

See Key Findings for full content.

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[i-started-a-dirt-notebook]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
- [[open-source-monopoly]]
