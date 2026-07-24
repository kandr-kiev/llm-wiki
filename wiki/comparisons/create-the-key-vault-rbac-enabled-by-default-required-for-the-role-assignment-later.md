---
title: "Create the Key Vault (RBAC enabled by default — required for the role assignment later)"
type: comparison
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

# Create the Key Vault (RBAC enabled by default — required for the role assignment later)

> **Source:** how-to-manage-secrets-securely-with-azure-key-vault-in-nodejs-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://www.freecodecamp.org/news/how-to-manage-secrets-securely-with-azure-key-vault-in-node-js/ ingested: 2026-07-20 sha256: f4118f79613e4ee988f8d6ffac8683a15fdf4bbd6bfce4e0cb593b4a2...
> **Sources:**
>   - how-to-manage-secrets-securely-with-azure-key-vault-in-nodejs-2026-07-20.md
> **Links:**
- [[master-full-stack-mobile-development-with-react-native]]
- [[windows-powershell]]
- [[how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging]]
- [[intro-to-shaders-javascript-and-p5-js-course-for-beginners]]
- [[understanding-dijkstra-s-algorithm]]

## Key Findings

---
source_url: https://www.freecodecamp.org/news/how-to-manage-secrets-securely-with-azure-key-vault-in-node-js/
ingested: 2026-07-20
sha256: f4118f79613e4ee988f8d6ffac8683a15fdf4bbd6bfce4e0cb593b4a2c84a0dd
blog_source: FreeCodeCamp Blog
---
How to Manage Secrets Securely with Azure Key Vault in Node.js
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
#JavaScript
# How to Manage Secrets Securely with Azure Key Vault in Node.js
![Zia Ullah](https://cdn.hashnode.com/uploads/avatars/6a32d4e8d06aa63cd556c4b9/9666ebc0-e7de-4f75-bd06-852d27c30919.jpg)
[
Zia Ullah
](/news/author/ziaullahzia/)
![How to Manage Secrets Securely with Azure Key Vault in Node.js](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/5491b408-9c6b-4d4d-a53e-215119fb2d97.png)
Last year a client called me about exactly this. Someone ran `git log -p` on a hunch and found a `.env` committed two years earlier, never caught. Database password, Stripe secret, JWT signing key — all still active. All still in production.
IBM's 2024 breach cost report put the average data breach at **$4.88 million** — and that's the average, not the worst cases.
Exposed credentials are consistently near the top of root causes. GitHub found over a million secrets leaked in public repos in 2023 alone, before you even count the private ones nobody ever discovered.
It's not a people problem. The developers I've worked with aren't careless — the architecture is just set up to fail them. A `.env` file gets committed once by accident. Credentials get copied and pasted into a Slack message to unblock a teammate. A Docker image gets published with secrets baked into a layer. A server gets shut down, and nobody rotates the credentials it was holding.
Azure Key Vault solves this differently. Your application fetches credentials at runtime from a centralized, encrypted service — the `.env` file stops being a liability because it stops holding anything worth stealing.
What you'll build is a Node.js Express API that fetches every secret from Azure Key Vault at startup. No passwords in the code. When someone quits, there's nothing in the repo to rotate. The `.env` ends up with one line — the vault name.
## Prerequisites
- Node.js 18+
- An Azure account (free tier works)
- Azure CLI installed and logged in (`az login`)
- Basic knowledge of Express.js
- Docker (optional — only needed for the local database test section)
## What We Will Build
A Node.js Express API that:
- Connects to PostgreSQL using credentials fetched from Key Vault at startup
- Uses Managed Identity for authentication — no client secrets or passwords anywhere
- Caches secrets in memory, so Key Vault isn't called on every request
- Works locally via Azure CLI aut

## Summary

h and in production via Managed Identity — same code, zero changes
## Table of Contents
- [How the Architecture Works](#heading-how-the-architecture-works)
- [What Is Azure Key Vault?](#heading-what-is-azure-key-vault)
- [Set Up the Key Vault](#heading-set-up-the-key-vault)
- [Create the Node.js Project](#heading-create-the-nodejs-project)
- [Connect to Key Vault with Managed Identity](#heading-connect-to-key-vault-with-managed-identity)
- [Cache Secrets at Startup](#heading-cache-secrets-at-startup)
- [Use Secrets in Your Express API](#heading-use-secrets-in-your-express-api)
- [Test Locally](#heading-test-locally)
- [Deploy to Azure App Service](#heading-deploy-to-azure-app-service)
- [Grant Key Vault Access to the App](#heading-grant-key-vault-access-to-the-app)
- [Rotate Secrets Without Redeploying](#heading-rotate-secrets-without-redeploying)
- [Troubleshooting](#heading-troubleshooting)
- [Wrapping Up](#heading-wrapping-up)
## How the Architecture Works
Before writing any code, it helps to see the full picture:
```
LOCAL DEVELOPMENT
.-------------------------------------------------------.
| |
| [Node.js App] |
| | |
| v |
| [DefaultAzureCredential] ---> az login session |
| | |
| v |
| [Azure Key Vault] ---> Returns secrets |
| | |
| v |
| [In-memory cache] ---> App uses secrets at runtime |
'-------------------------------------------------------'
PRODUCTION (Azure)
.-------------------------------------------------------.
| |
| [Azure App Service] |
| | |
| v |
| [DefaultAzureCredential] ---> Managed Identity |
| | |
| v |
| [Azure Key Vault] ---> Returns secrets |
| | |
| v |
| [In-memory cache] ---> App uses secrets at runtime |
'-------------------------------------------------------'
```
Both environments run the exact same code. `DefaultAzureCredential` figures out where it is — locally it picks up your `az login` session, on Azure it uses Managed Identity. You don't switch config files and you don't manage credentials. It just works.
## What Is Azure Key Vault?
Azure Key Vault is Microsoft's managed secret store — it handles secrets, keys, and certificates. For this tutorial, we're only using the secrets part: database passwords, API keys, JWT signing keys, anything your app needs to run but has no business being in your Git history.
Compared to `.env` files, the practical differences are worth understanding before you write any code.
Rotation is the one I notice most on real projects. Update a secret in Key Vault and every app picks it up on the next restart — no hunting down five different environment configs across staging and production.
Access control is the other big one. Each application only gets permission to read the secrets it actually needs. If one service gets compromised, it can't read credentials belonging to other services.
And every read gets logged. When something goes wrong — and eventually something will — you can see exactly which app accessed which secret, and when. That log is what auditors actually want to s

## Related Articles

- [[master-full-stack-mobile-development-with-react-native]]
- [[windows-powershell]]
- [[how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging]]
- [[intro-to-shaders-javascript-and-p5-js-course-for-beginners]]
- [[understanding-dijkstra-s-algorithm]]
