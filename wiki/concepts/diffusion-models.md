---
type: concept
title: Diffusion Models
description: Generative models that learn to reverse a gradual noising process, producing high-quality samples through iterative denoising.
created: 2026-07-07
updated: 2026-07-07
tags: [ml, diffusion, generative-models, image-generation, stable-diffusion]
sources: [raw/articles/diffusion-models-2026-07-07.md]
confidence: high
contested: false
links: [remaking-old-computer-graphics-with-ai-image-generation, the-illustrated-stable-diffusion]
---

# Diffusion Models

## Overview

Diffusion models are a class of generative models that learn to reverse a gradual noising process. They work by:
1. **Forward process:** Gradually add Gaussian noise to data until it becomes pure noise
2. **Reverse process:** Learn a neural network to denoise step-by-step, generating samples from noise

## Mathematical Foundation

### Forward Process
At each timestep t, noise is added: q(x_t | x_{t-1}) = N(x_t; √(1-β_t) · x_{t-1}, β_t · I)

The process can be sampled directly at any timestep:
x_t = √(ᾱ_t) · x_0 + √(1-ᾱ_t) · ε, where ε ~ N(0,I)

### Reverse Process
The model learns to predict the noise ε, and the reverse transition is:
p_θ(x_{t-1} | x_t) = N(x_{t-1}; μ_θ(x_t, t), σ_t² · I)

## Key Components

### Noise Schedule
The sequence of β_t values controls how quickly noise is added. Linear, cosine, and cosine schedules are common. The schedule affects sample quality and training stability.

### U-Net Architecture
The denoising network is typically a U-Net with:
- ResNet blocks for spatial processing
- Attention layers for global context
- Cross-attention for conditional generation (text-to-image)
- Skip connections for multi-scale information

### Training Objective
Simplified loss: L = E_{t,x_0,ε} [||ε - ε_θ(x_t, t)||²]
This predicts the noise added at each timestep.

## Types of Diffusion Models

| Type | Description | Use Case |
|---|---|---|
| DDPM | Denoising Diffusion Probabilistic Models | Base generative model |
| DDIM | Denoising Diffusion Implicit Models | Faster sampling (deterministic) |
| Score-Based | Directly learns score function ∇log p(x) | Theoretical analysis |
| Latent Diffusion | Diffusion in compressed latent space | Stable Diffusion, efficient |

## Stable Diffusion

Latent Diffusion Models (LDM) operate in a compressed latent space learned by a VAE:
1. Encode image to latent space with VAE encoder
2. Run diffusion process in latent space
3. Decode latent to image with VAE decoder

This reduces the diffusion dimensionality from pixels (e.g., 512×512×3) to latents (e.g., 64×64×4).

## Related Pages

- [[the-illustrated-stable-diffusion]] — Visual guide to Stable Diffusion architecture
- [[remaking-old-computer-graphics-with-ai-image-generation]] — Practical applications of AI image generation
