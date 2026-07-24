---
title: "ArgoCD applies it, Crossplane reconciles it, AWS creates the bucket"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - async
  - container
  - edge
  - gpt
  - guide
  - news
  - search
---

# ArgoCD applies it, Crossplane reconciles it, AWS creates the bucket

> **Source:** how-to-build-an-internal-developer-platform-a-complete-guide-to-backstage-argocd-and-crossplane-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** --- source_url: https://www.freecodecamp.org/news/how-to-build-an-internal-developer-platform-a-complete-guide-to-backstage-argocd-and-crossplane/ ingested: 2026-07-18 sha256: af3c15e159d1c8ee45a87e54...
> **Sources:**
>   - how-to-build-an-internal-developer-platform-a-complete-guide-to-backstage-argocd-and-crossplane-2026-07-18.md
> **Links:**
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[5-agent-skills-i-use-every-day]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[intro-to-shaders-javascript-and-p5-js-course-for-beginners]]

## Key Findings

---
source_url: https://www.freecodecamp.org/news/how-to-build-an-internal-developer-platform-a-complete-guide-to-backstage-argocd-and-crossplane/
ingested: 2026-07-18
sha256: af3c15e159d1c8ee45a87e549a7303fea345bbc7bcba5e52c291685b9a329c6d
blog_source: FreeCodeCamp Blog
---
How to Build an Internal Developer Platform: A Complete Guide to Backstage, ArgoCD, and Crossplane
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
July 17, 2026
/
#Platform Engineering 
# How to Build an Internal Developer Platform: A Complete Guide to Backstage, ArgoCD, and Crossplane
![Ayobami Adejumo](https://lh3.googleusercontent.com/a/ACg8ocK7fWyBswxJ1N2BtJ9YSAKesdcHLSULl1nnWuKITGTqdWMgWQ=s96-c)
[
Ayobami Adejumo
](/news/author/aayostem/)
![How to Build an Internal Developer Platform: A Complete Guide to Backstage, ArgoCD, and Crossplane](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4e45df2a-5af9-4feb-84fa-f7eb1c04ee91.png)
Every fast-growing engineering team eventually hits the same wall.
A developer needs a new staging environment, so they file a ticket. The platform team queues it.
Two weeks later, the environment exists. It's configured slightly differently from the last one, with a naming convention that doesn't match the production setup, missing the observability stack the previous environment had. The developer deploys. Something breaks. Nobody knows why.
The problem isn't the ticket queue. The problem is the absence of a platform: a paved road where developers can self-serve infrastructure, deployments, and environments that are consistent, auditable, and safe without requiring a platform engineer for every request.
An Internal Developer Platform (IDP) solves this. Not by removing platform engineers from the picture, but by shifting their work from executing individual requests to building the systems that execute those requests automatically.
This handbook builds a production-grade IDP from the three CNCF tools that form its core in 2026: Backstage as the developer portal and software catalog, ArgoCD as the GitOps continuous delivery engine, and Crossplane as the Kubernetes-native infrastructure control plane.
By the end, developers on your platform will be able to provision a cloud database, deploy an application to staging, and register a new service in the catalog — all without filing a single ticket.
## Table of Contents
- [What You'll Learn](#heading-what-youll-learn)
- [Prerequisites](#heading-prerequisites)
- [Part 1: IDP Architecture — The Three-Layer Model](#heading-part-1-idp-architecture-the-three-layer-model)
- [Part 2: ArgoCD — The GitOps Foundation](#heading-part-2-argocd-the-gitops-foundation)
- [Part 3: Crossplane — Infrastructure as Kubernetes Resources](#headin

## Summary

g-part-3-crossplane-infrastructure-as-kubernetes-resources)
- [Part 4: Backstage — The Developer Portal](#heading-part-4-backstage-the-developer-portal)
- [Part 5: Wiring It Together — The Golden Path](#heading-part-5-wiring-it-together-the-golden-path)
- [Part 6: FinOps Integration — Cost Attribution on the IDP](#heading-part-6-finops-integration-cost-attribution-on-the-idp)
- [Part 7: The Platform Maturity Model — Measuring What You've Built](#heading-part-7-the-platform-maturity-model-measuring-what-youve-built)
- [Best Practices Summary](#heading-best-practices-summary)
- [Resources](#heading-resources)
## What You'll Learn
- The three-layer IDP architecture and why each layer must be implemented in a specific order
- How to install and configure ArgoCD with ApplicationSets for multi-environment GitOps delivery
- How to define cloud infrastructure as Kubernetes custom resources using Crossplane Compositions
- How to deploy and configure Backstage with a software catalog and Software Templates
- How to wire Backstage, ArgoCD, and Crossplane together into a single self-service golden path
- How to implement cost attribution on your IDP so every resource provisioned through it carries team and cost center metadata
- How to measure your IDP's maturity using the CNCF Platform Engineering Maturity Model
Let's build it.
## Prerequisites
Before following along, you should have:
**Knowledge:**
- Working familiarity with Kubernetes: you can deploy applications, write YAML manifests, and understand namespaces and RBAC
- Basic GitOps understanding: you know what "Git as source of truth" means in practice
- Comfort with Helm, Terraform HCL, and TypeScript at a reading level
- Understanding of AWS services: EKS, RDS, S3, IAM
**Tools and access:**
- An EKS cluster running Kubernetes 1.28 or later with at least 3 nodes (m5.xlarge or equivalent)
- `kubectl` configured and pointing at your cluster
- `helm` 3.12 or later installed
- AWS CLI v2 configured with admin-level permissions for the provisioning steps
- Node.js 18 or later and Yarn (for Backstage)
- A GitHub organisation you control (for the GitOps repositories and Backstage GitHub integration)
**Companion repository:**
```
git clone https://github.com/aayostem/platform-toolkit
cd platform-toolkit
```
The repository contains all manifests, Helm values files, Crossplane Compositions, and Backstage templates referenced in this guide. Each part maps to a directory in the repo.
**Estimated time:** The full implementation takes one to two days for an experienced platform engineer. Parts 1–3 can be completed in the morning and produce a working GitOps delivery layer.
## Part 1: IDP Architecture — The Three-Layer Model
### 1.1 What an IDP Actually Is
An Internal Developer Platform isn't a tool. It's a product: a collection of tools, workflows, and abstractions that platform teams build and maintain so that application developers can move fast without managing infrastructure directly.
The distinction matters be

## Related Articles

- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[5-agent-skills-i-use-every-day]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[intro-to-shaders-javascript-and-p5-js-course-for-beginners]]
