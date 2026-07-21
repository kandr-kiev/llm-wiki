---
title: "how to use apple s foundation models in a web app with a macos companion"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - async
  - container
  - edge
  - foundation-model
  - gpt
  - news
  - search
  - use-case
  - web
---

# how to use apple s foundation models in a web app with a macos companion

> **Source:** how-to-use-apples-foundation-models-in-a-web-app-with-a-macos-companion-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://www.freecodecamp.org/news/how-to-use-apple-s-foundation-models-in-a-web-app-with-a-macos-companion/ ingested: 2026-07-20 sha256: 302880ac2cc595ff1e7609f7154e5d95f7ed06b59a5af7e...
> **Sources:**
>   - how-to-use-apples-foundation-models-in-a-web-app-with-a-macos-companion-2026-07-20.md
> **Links:**
- [[why it worked on my machine still happens]]
- [[build pdf signature tool javascript]]
- [[kimi k3]]
- [[ai music video arena claude vs gpt 5.6]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]

## Key Findings

---
source_url: https://www.freecodecamp.org/news/how-to-use-apple-s-foundation-models-in-a-web-app-with-a-macos-companion/
ingested: 2026-07-20
sha256: 302880ac2cc595ff1e7609f7154e5d95f7ed06b59a5af7e7e1ce4b97e6f6e63c
blog_source: FreeCodeCamp Blog
---
How to Use Apple’s Foundation Models in a Web App with a macOS Companion
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
- 
- 
- 
[![freeCodeCamp.org](https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg)](https://www.freecodecamp.org/news/)
- 
English
- 
Español
- 
中文（简体字）
- 
Italiano
- 
Português
- 
Українська
- 
日本語
- 
한국어
Menu
- 
- Forum
- Curriculum
- 
Night Mode
Donate
July 20, 2026
/
#software development
# How to Use Apple’s Foundation Models in a Web App with a macOS Companion
![Balogun Wahab](https://cdn.hashnode.com/res/hashnode/image/upload/v1763399420451/2a853a45-3f5a-4a93-ac27-717df966bb13.jpeg?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp)
[
Balogun Wahab
](/news/author/03balogun/)
![How to Use Apple’s Foundation Models in a Web App with a macOS Companion](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7f0e2343-7394-46b5-a4c8-3ef0fecfa57a.png)
Not every AI feature needs a cloud model, with its per-token bills, network round-trips, and private data leaving your machine. If you're on a modern Mac, a capable language model is already on your disk.
**Foundation Models** is Apple's Swift framework for working with large language models. It's the on-device model behind Apple Intelligence, Apple's Private Cloud Compute, or another provider's server model.
This tutorial targets the on-device model: you send it a prompt and it runs entirely on the Mac's own hardware locally, free-per-call, and offline-friendly.
Paired with Apple Vision for reading images on device, that's enough to build real AI features like summaries, classification, and structured extraction without the data ever leaving your machine.
## Table Of Contents
- [What You Will Build](#heading-what-you-will-build)
- [Prerequisites](#heading-prerequisites)
- [Why a macOS Companion App?](#heading-why-a-macos-companion-app)
- [Foundation Models Can't Read Images Directly](#heading-foundation-models-cant-read-images-directly)
- [Project Structure](#heading-project-structure)
- [Build the React App](#heading-build-the-react-app)
- [Check Companion Health](#heading-check-companion-health)
- [Convert the Image to Base64](#heading-convert-the-image-to-base64)
- [Analyze Immediately After Upload](#heading-analyze-immediately-after-upload)
- [Send the Image to the Companion](#heading-send-the-image-to-the-companion)
- [Render the JSON Output](#heading-render-the-json-output)
- [Build the macOS Companion App](#heading-build-the-macos-companion-app)
- [Check Foundation Models Availability](#heading-check-foundation-models-availability)
- [Extract Text with Apple Vision](#heading-extract-text-with-apple-vision)
- [Ask Foundation Models to Explain the Vision Output](#heading-ask-foundation-mod

## Summary

els-to-explain-the-vision-output)
- [Return JSON to the Browser](#heading-return-json-to-the-browser)
- [Run the App](#heading-run-the-app)
- [Conclusion](#heading-conclusion)
- [Resources](#heading-resources)
## What You Will Build
You'll build **Vision Bridge**, a web app that sends an image to a local macOS companion. The companion reads the image with Apple Vision, reasons about it with Foundation Models, and returns structured JSON to the browser: private, on-device AI behind a plain web interface.
You can find the complete source code in this GitHub repository: [github.com/03balogun/vision-bridge](http://github.com/03balogun/vision-bridge).
The goal isn't to build a giant product but rather to understand the architecture behind how this works.
![Screenshot of the Vision Bridge app, with image upload on the left and JSON output on the right](https://cdn.hashnode.com/uploads/covers/5db93b3da2342e8354088115/6d18db01-e921-4291-bb2e-26be2c02b304.png)
Vision Bridge has two parts:
- A React app with a split-screen interface.
- A macOS companion app that exposes a local API.
The React app has:
- An image upload area
- An image preview
- Automatic analysis after upload
- A JSON output viewer
- A companion health status indicator
The macOS companion app has:
- `GET /v1/health`
- `POST /v1/analyze-image`
- Apple Vision OCR
- Foundation Models availability checks
- Foundation Models reasoning over Vision output
The final response looks like this:
```
{
"support": {
"visionAvailable": true,
"foundationModelAvailable": true,
"foundationModelStatus": "available"
},
"image": {
"filename": "screenshot.png",
"contentType": "image/png",
"byteCount": 1048576,
"width": 1440,
"height": 900
},
"vision": {
"detectedText": [
{
"text": "Build failed",
"confidence": 0.96,
"boundingBox": {
"x": 0.12,
"y": 0.31,
"width": 0.45,
"height": 0.08
}
}
]
},
"model": {
"summary": "The image appears to show a software build failure.",
"description": "A developer tool window is showing an error state with diagnostic text.",
"suggestedTags": ["screenshot", "developer-tool", "error"],
"possibleUses": [
"Generate alt text",
"Summarize screenshots",
"Extract document data"
]
}
}
```
## Prerequisites
To follow along, you need:
- macOS 26 or newer
- Xcode with the macOS 26 SDK
- Node.js 20 or newer
- Basic React knowledge
- Basic Swift knowledge
- A Mac that supports Apple Intelligence
Foundation Models availability depends on the Mac, the OS version, and Apple Intelligence settings. The companion checks this at runtime, which we'll cover below.
## Why a macOS Companion App?
You can't write this in a regular React app:
```
import FoundationModels from "apple-frameworks";
```
That API doesn't exist in the browser. A native macOS app, however, can use any Apple framework, so the companion acts as a local bridge. The same pattern works for any native capability the web platform doesn't expose.
## Foundation Models Can't Read Images Directly
The public Foundation Models framework is a lan

## Related Articles

- [[why it worked on my machine still happens]]
- [[build pdf signature tool javascript]]
- [[kimi k3]]
- [[ai music video arena claude vs gpt 5.6]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
