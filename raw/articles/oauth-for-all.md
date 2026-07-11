---
title: "oauth for all"
type: comparison
tags: [comparison]
description: Comparison page for oauth for all

sources: []
links: []
description: Comparison page for oauth for all

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
contested: false

---
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
- - <astro-island uid="ZFNHa7" component-url="/_astro/GoogleAnalytics.Buaiy_s2.js" component-export="GoogleAnalytics" renderer-url="/_astro/client.CpQ9otmg.js" props="{"title":[0,"Unlocking the Cloudflare app ecosystem with OAuth for all"],"canonical":[0,"https://blog.cloudflare.com/oauth-for-all"],"info":[0,{"id":[0,"77AgsHNNnpUDvP0Z6gqgp6"],"title":[0,"Unlocking the Cloudflare app ecosystem with OAuth for all"],"slug":[0,"oauth-for-all"],"excerpt":[0,"Self-Managed OAuth is now available to all developers on Cloudflare. Here's how we executed a zero-downtime migration of our core OAuth engine to make it happen."],"featured":[0,false],"html":[0,"<p>Cloudflare provides services that help run 20% of the web, but we donât do it alone. Developers on our platform use a myriad of tools and services from other companies too. Cloudflare provides a rich API for our platform that enables developers to create automations, CI/CD, and integrations that glue together the various parts of their infrastructure. Earlier this month, we announced <a href=\"https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/\" target=\"_blank\" rel=\"noopener noreferrer\"><u>self-managed OAuth</u></a>, making it easier for customers to create and manage their own OAuth clients for delegated access to the Cloudflare API.</p><p>Cloudflare isnât new to OAuth. If youâve used Wrangler, or used integrations from partners like PlanetScale, then youâve already used it. However, until now, third-party OAuth was only available through a small number of manually onboarded integrations, and was not available to developers more broadly. That meant developers building their own integrations had to rely on API tokens, which are harder to manage and a poor fit for many delegated application flows.Â </p><p>Over the last year, we onboarded a growing number of early partners while improving the consent, revocation, and security model behind Cloudflare OAuth. But as our Developer Platform grew and agentic tools drove demand for delegated access, it became clear that opening up OAuth to all customers was critical to the success of our platform.Â </p><p>With self-managed OAuth, developers can now offer a standard OAuth flow where customers grant scoped access directly, making it easier to build SaaS integrations, internal developer platforms, and agentic tools while giving users clearer consent, easier revocation, and more control over what an application can do.</p>\n <div class=\"flex anchor relative\">\n <h2 id=\"scaling-the-ecosystem-securely\">Scaling the ecosystem securely</h2>\n <a href=\"#scaling-the-ecosystem-securely\" aria-hidden=\"true\" class=\"relative sm:absolute sm:-start-5\">\n <svg wi

## Summary

dth=\"16\" height=\"16\" viewBox=\"0 0 24 24\"><path fill=\"currentcolor\" d=\"m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z\"></path></svg>\n </a>\n </div>\n <p>While our earlier OAuth solution was sufficient for a small number of carefully managed partners, we realized that our permissions model, our consent experience, and our ways of mitigating potential abuse vectors were not mature enough.Â </p><p>Earlier this year we <a href=\"https://blog.cloudflare.com/improved-developer-security/#improving-the-oauth-consent-experience\"><u>updated our consent experience</u></a> to make it clearer which application is requesting access, and what permissions it will receive. We also added revocation to the dashboard so developers can easily control which applications have access to their data, and made app ownership more visible to prevent OAuth phishing attacks.Â </p><p>Opening self-managed OAuth to all customers also required major upgrades to our underlying OAuth engine. This process required a large amount of planning to do with minimal user interruption, while also ensuring data stability and security.</p>\n <div class=\"flex anchor relative\">\n <h2 id=\"planning-the-upgrade-to-our-oauth-engine\">Planning the upgrade to our OAuth engine</h2>\n <a href=\"#planning-the-upgrade-to-our-oauth-engine\" aria-hidden=\"true\" class=\"relative sm:absolute sm:-start-5\">\n <svg width=\"16\" height=\"16\" viewBox=\"0 0 24 24\"><path fill=\"currentcolor\" d=\"m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z\"></path></svg>\n </a>\n </div>\n <p>Years ago, we deployed <a href=\"https://github.com/ory/hydra\" target=\"_blank\" rel=\"noopener noreferrer\"><u>Hydra</u></a>, an open-source OAuth engine, to power Cloudflare OAuth under the hood. That deployment served us well when usage was limited, but as the developer platform grew and agentic workflows became more common, it became clear that we needed a major upgrade to unlock new capabilities and improve performance.Â </p><p>As we planned the upgrade, we decided to do two smaller sequential upgrades rather than doing one large upgrade.Â  First, we would move to the latest 1.X release, evaluate any behavior or perform

## Related Articles

- 
- 
- 
- [[automating-ai-away-2026-07-07]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
