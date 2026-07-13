---
title: "vibe coding menugen"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - application
  - backend
  - claude
  - data
  - few-shot
  - foundation-model
  - frontend
  - image-generation
  - llm
  - machine-learning
  - open-source
  - real-time
  - streaming
  - use-case
  - web
---# vibe coding menugen

> **Source:** vibe-coding-menugen-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** [ #  karpathy ](/) Home Blog # Vibe coding MenuGen * 27 Apr, 2025 * Very often, I sit down at a restaurant, look through their menu, and feel... kind of stuck. What is Pâté again? What is a Tagine? Ca...
> **Sources:**
>   - vibe-coding-menugen-2026-07-10.md
> **Links:**
- [[finding-the-best-sleep-tracker]]
- [[auto-grade-hn]]
- [[chemical-hygiene]]
- [[automating-ai-away-2026-07-07]]
- [[animals-vs-ghosts]]

## Key Findings

[
# 
karpathy
](/)
Home Blog
# Vibe coding MenuGen
*
27 Apr, 2025
*
Very often, I sit down at a restaurant, look through their menu, and feel... kind of stuck. What is Pâté again? What is a Tagine? Cavatappi... that's a pasta right? Sweetbread sounds delicious (I have a huge sweet tooth). It can get really out of hand sometimes. *"Confit tubers folded with matured curd and finished with a beurre noisette infusion."* okay so... what is this exactly? I've spent so much of my life googling pictures of foods that when the time came to attend a recent vibe coding hackathon, I knew it was the perfect opportunity to finally build the app I always wanted, but could nowhere find. And here it is in flesh, I call it... 🥁🥁🥁 ... **MenuGen**:
![Screenshot 2025-04-26 at 1](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/02pm.webp)
MenuGen is super simple. You take a picture of a menu and it generates images for all the menu items. It visualizes the menu. Obviously it's not *exactly* what you will be served in that specific restaurant, but it gives you the basic idea: Some of these dishes are salads, this is a fish, this is a soup, etc. I found it so helpful in my personal use that after the hackathon (where I got the first version to work on localhost) I continued vibe coding a bit to deploy it, add authentication, payments, and generally make it real. So here it is, give it a shot the next time you go out :): menugen.app!
MenuGen is my first end-to-end vibe coded app, where I (someone who tinkers but has little to no actual web development experience) went from scratch all the way to a real product that people can sign up for, pay for, get utility out of, and where I pocket some good and honest 10% markup. It's pretty cool. But in addition to the utility of the app, MenuGen was interesting to me as an exploration of vibe coding apps and how feasible it is today. As such, I did not write any code directly; 100% of the code was written by Cursor+Claude and I basically don't really know how MenuGen works in the conventional sense that I am used to. So now that the project is "done" (as in the first version seems to work), I wanted to write up this quick post on my experience - what it looks like today for a non-webdev to vibe code a web app.
**First, local version**. In what is a relatively common experience in vibe coding, the very first prototype of the app running on my local machine took very little time. I took Cursor + Claude 3.7, I gave it the description of the app, and it wrote all the React frontend components very quickly, laying out a beautiful web page with smooth, multicolored fonts, little CSS animations, responsive design and all that, except for the actual backend functionality. Seeing a new website materialize so quickly is a strong hook. I felt like I was 80% done but (foreshadowing...) it was a bit closer to 20%.
**OpenAI API**. Around here is where some of the troubles started. I needed to call OpenAI APIs to OCR the menu items f

## Summary

rom the image. I had to get the OpenAI API keys. I had to navigate slightly convoluted menus asking me about "projects" and detailed permissions. Claude kept hallucinating deprecated APIs, model names, and input/output conventions that have all changed recently, which was confusing, but it resolved them after I copy pasted the docs back and forth for a while. Once the individual API calls were working, I immediately ran into some heavy rate limiting of the API calls, allowing me to only issue a few queries every 10 minutes.
**Replicate API**. Next, I needed to generate images given the descriptions. I signed up for a new Replicate API key and ran into similar issues relatively quickly. My queries didn't work because LLM knowledge was deprecated, but in addition, this time even the official docs were a little bit out of date due to recent changes in the API, which now don't return the JSON directly but instead some kind of a Streaming object that neither I or Claude understood. I then faced rate limiting on the API so it was difficult to debug the app. I was told later that these are common protection measures by these services to mitigate fraud, but they also make it harder to get started with new, legitimate accounts. I'm told Replicate is moving to a different approach where you pre-purchase credits, which might help going forward.
**Vercel deploy**. At this point at least, the app was working locally so I was quite happy. It was time to deploy the basic first version. Sign up for Vercel, add project, configure it, point it at my GitHub repo, push to master, watch a new Deployment build and... ERROR. The logs showed some linting errors due to unused variables and other basic things like that, but it was hard to understand or debug because everything worked fine on local and only broke on Vercel build, so I debugged the issues by pushing fake debugging commits to master to force redeploys. Once I fixed these issues, the site still refused to work. I asked Claude. I asked ChatGPT. I consulted docs. I googled around. 1 hour later I finally realized my silly mistake - My `.env.local` file stored the API keys to OpenAI and Replicate, but this file is (correctly!) part of `.gitignore` and doesn't get pushed to git, so you have to manually navigate to Vercel project settings, find the right place, and add your environment keys manually. I kind of understood the issue relatively quickly, but I could see an aspiring vibe coder get stuck on this for a while. Once the deployment finally succeeded, Vercel happily offered a URL. This surprised me again because my project was a private git repo that was not ready to see the light of day. I didn't realize that Vercel will take your *!private!* repo of an unfinished project and auto-deploy it on a totally public and easy to guess url just like that, hah.
**Clerk authentication**. Claude suggested that we use Clerk for authentication, so I went along with it. Signed up for Clerk, configured the project, got my 

## Related Articles

- [[finding-the-best-sleep-tracker]]
- [[auto-grade-hn]]
- [[chemical-hygiene]]
- [[automating-ai-away-2026-07-07]]
- [[animals-vs-ghosts]]
