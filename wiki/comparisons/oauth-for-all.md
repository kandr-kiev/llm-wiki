---
title: "oauth for all"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - api
  - application
  - ci-cd
  - comparison
  - data
  - deployment
  - foundation-model
  - open-source
  - performance
  - real-time
  - security
  - self-supervised
  - standards
  - training
  - use-case
  - web
  - zero-shot
---
# oauth for all

> **Source:** oauth-for-all.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- title: "oauth for all" type: comparison tags: [comparison] description: Comparison page for oauth for all sources: [] links: [] description: Comparison page for oauth for all links: [] confidence:...
> **Sources:**
>   - oauth-for-all.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[animals-vs-ghosts]]
- [[away]]
- [[auto-grade-hn]]
- [[ml-dsa-will-have-to-do]]

## Key Findings


# oauth for all
> **Source:** unlocking-the-cloudflare-app-ecosystem-with-oauth-for-all-2026-07-07.md
> **Type:** comparison
> **Created:** 2026-07-08
## Key Findings
---
source_url: https://blog.cloudflare.com/oauth-for-all/
ingested: 2026-07-07
sha256: 4714e6d10b0167fe946ae68265fedf2e24f33546219d7d108bd08b17827175d6
blog_source: Cloudflare Blog
---
Unlocking the Cloudflare app ecosystem with OAuth for all- - - - - - - - - - - - - 
- - self-managed OAuth, making it easier for customers to create and manage their own OAuth clients for delegated access to the Cloudflare API.
Cloudflare isnât new to OAuth. If youâve used Wrangler, or used integrations from partners like PlanetScale, then youâve already used it. However, until now, third-party OAuth was only available through a small number of manually onboarded integrations, and was not available to developers more broadly. That meant developers building their own integrations had to rely on API tokens, which are harder to manage and a poor fit for many delegated application flows.Â 
Over the last year, we onboarded a growing number of early partners while improving the consent, revocation, and security model behind Cloudflare OAuth. But as our Developer Platform grew and agentic tools drove demand for delegated access, it became clear that opening up OAuth to all customers was critical to the success of our platform.Â 
With self-managed OAuth, developers can now offer a standard OAuth flow where customers grant scoped access directly, making it easier to build SaaS integrations, internal developer platforms, and agentic tools while giving users clearer consent, easier revocation, and more control over what an application can do.
\n \n ## Scaling the ecosystem securely
\n \n \n \n \n While our earlier OAuth solution was sufficient for a small number of carefully managed partners, we realized that our permissions model, our consent experience, and our ways of mitigating potential abuse vectors were not mature enough.Â 
Earlier this year we updated our consent experience to make it clearer which application is requesting access, and what permissions it will receive. We also added revocation to the dashboard so developers can easily control which applications have access to their data, and made app ownership more visible to prevent OAuth phishing attacks.Â 
Opening self-managed OAuth to all customers also required major upgrades to our underlying OAuth engine. This process required a large amount of planning to do with minimal user interruption, while also ensuring data stability and security.
\n \n ## Planning the upgrade to our OAuth engine
\n \n \n \n \n Years ago, we deployed Hydra, an open-source OAuth engine, to power Cloudfl

## Summary

See Key Findings for full content.

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[animals-vs-ghosts]]
- [[away]]
- [[auto-grade-hn]]
- [[ml-dsa-will-have-to-do]]
