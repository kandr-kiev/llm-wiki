---
title: "illustrated stable diffusion"
type: comparison
tags:
description: Comparison page for illustrated stable diffusion

sources: []
links: []
description: Comparison page for illustrated stable diffusion

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
---

# illustrated stable diffusion

> **Source:** the-illustrated-stable-diffusion-2026-07-07.md
> **Type:** comparison
> **Created:** 2026-07-08

## Key Findings

[![](https://avatars0.githubusercontent.com/u/1007956?s=460&v=4)](/)
# [Jay Alammar](/)
Visualizing machine learning one concept at a time.
Read our book, [Hands-On Large Language Models](https://www.LLM-book.com) and follow me on [LinkedIn](https://www.linkedin.com/in/jalammar/), [Bluesky](https://bsky.app/profile/jayalammar.bsky.social), [Substack](https://newsletter.languagemodels.co/), [X](https://x.com/JayAlammar),[YouTube ](https://www.youtube.com/channel/UCmOwsoHty5PrmE-3QhUBfPQ)
[Blog](/)
[About](/about)
# The Illustrated Stable Diffusion
Translations: [Chinese](https://blog.csdn.net/yujianmin1990/article/details/129143157), [Vietnamese](https://trituenhantao.io/kien-thuc/minh-hoa-stable-diffusion/).
(**V2 Nov 2022**: Updated images for more precise description of forward diffusion. A few more images in this version)
AI image generation is the most recent AI capability blowing people’s minds (mine included). The ability to create striking visuals from text descriptions has a magical quality to it and points clearly to a shift in how humans create art. The release of [Stable Diffusion](https://stability.ai/blog/stable-diffusion-public-release) is a clear milestone in this development because it made a high-performance model available to the masses (performance in terms of image quality, as well as speed and relatively low resource/memory requirements).
After experimenting with AI image generation, you may start to wonder how it works.
This is a gentle introduction to how Stable Diffusion works.
![](/images/stable-diffusion/stable-diffusion-text-to-image.png)
Stable Diffusion is versatile in that it can be used in a number of different ways. Let’s focus at first on image generation from text only (text2img). The image above shows an example text input and the resulting generated image (The actual complete prompt is here). Aside from text to image, another main way of using it is by making it alter images (so inputs are text + image).
![](/images/stable-diffusion/stable-diffusion-img2img-image-to-image.png)
Let’s start to look under the hood because that helps explain the components, how they interact, and what the image generation options/parameters mean.
## The Components of Stable Diffusion
Stable Diffusion is a system made up of several components and models. It is not one monolithic model.
As we look under the hood, the first observation we can make is that there’s a text-understanding component that translates the text information into a numeric representation that captures the ideas in the text.
![](/images/stable-diffusion/stable-diffusion-text-understanding-component-image-generation.png)
We’re starting with a high-level view and we’ll get into more machine learning details later in this article. However, we can say that this text encoder is a special Transformer language model (technically: the text encoder of a CLIP model). It takes the input text and outputs a list of numbers representing each word/token in the text (a vector per

## Summary

 token).
That information is then presented to the Image Generator, which is composed of a couple of components itself.
![](/images/stable-diffusion/Stable-diffusion-text-info-to-image-generator.png)
The image generator goes through two stages:
1- **Image information creator**
This component is the secret sauce of Stable Diffusion. It’s where a lot of the performance gain over previous models is achieved.
This component runs for multiple steps to generate image information. This is the *steps* parameter in Stable Diffusion interfaces and libraries which often defaults to 50 or 100.
The image information creator works completely in the *image information space* (or *latent* space). We’ll talk more about what that means later in the post. This property makes it faster than previous diffusion models that worked in pixel space. In technical terms, this component is made up of a UNet neural network and a scheduling algorithm.
The word “diffusion” describes what happens in this component. It is the step by step processing of information that leads to a high-quality image being generated in the end (by the next component, the image decoder).
![](/images/stable-diffusion/Stable-diffusion-image-generator-information-creator.png)
2- **Image Decoder**
The image decoder paints a picture from the information it got from the information creator. It runs only once at the end of the process to produce the final pixel image.
![](/images/stable-diffusion/stable-diffusion-cliptext-unet-autoencoder-decoder.png)
With this we come to see the three main components (each with its own neural network) that make up Stable Diffusion:
- 
**ClipText** for text encoding. 
Input: text. 
Output: 77 token embeddings vectors, each in 768 dimensions.
- 
**UNet + Scheduler** to gradually process/diffuse information in the information (latent) space. 
Input: text embeddings and a starting multi-dimensional array (structured lists of numbers, also called a *tensor*) made up of noise.
Output: A processed information array
- 
**Autoencoder Decoder** that paints the final image using the processed information array.
Input: The processed information array (dimensions: (4,64,64)) 
Output: The resulting image (dimensions: (3, 512, 512) which are (red/green/blue, width, height))
![](/images/stable-diffusion/stable-diffusion-components-and-tensors.png)
## What is Diffusion Anyway?
Diffusion is the process that takes place inside the pink “image information creator” component. Having the token embeddings that represent the input text, and a random starting *image information array* (these are also called *latents*), the process produces an information array that the image decoder uses to paint the final image.
![](/images/stable-diffusion/stable-diffusion-diffusion-process.png)
This process happens in a step-by-step fashion. Each step adds more relevant information. To get an intuition of the process, we can inspect the random latents array, and see that it translates to visual noise. Visual i

## Related Articles

- 
- 
- [[the-illustrated-stable-diffusion-2026-07-07]]
- 
- 
