---
title: "how to build a multi tenant saas api with nodejs rbac and audit logging"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - async
  - container
  - edge
  - gpt
  - multi-agent
  - news
  - search
---

# how to build a multi tenant saas api with nodejs rbac and audit logging

> **Source:** how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://www.freecodecamp.org/news/how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging/ ingested: 2026-07-20 sha256: 03e92323fe38e17276a4e8b7f528166ff5b74ccf651eb7bb...
> **Sources:**
>   - how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging-2026-07-20.md
> **Links:**
- [[Windows PowerShell]]
- [[master full stack mobile development with react native]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[openvm bugs]]
- [[understanding dijkstra s algorithm]]

## Key Findings

---
source_url: https://www.freecodecamp.org/news/how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging/
ingested: 2026-07-20
sha256: 03e92323fe38e17276a4e8b7f528166ff5b74ccf651eb7bb17d1401ecf16d47e
blog_source: FreeCodeCamp Blog
---
How to Build a Multi-Tenant SaaS API with Node.js, RBAC, and Audit Logging
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
#Node.js
# How to Build a Multi-Tenant SaaS API with Node.js, RBAC, and Audit Logging
![Zia Ullah](https://cdn.hashnode.com/uploads/avatars/6a32d4e8d06aa63cd556c4b9/9666ebc0-e7de-4f75-bd06-852d27c30919.jpg)
[
Zia Ullah
](/news/author/ziaullahzia/)
![How to Build a Multi-Tenant SaaS API with Node.js, RBAC, and Audit Logging](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/69793fe0-fe0e-4c9c-839d-12a134f65287.png)
A colleague asked me to help debug what looked like a permissions issue in their SaaS project management tool. Users were seeing resources they hadn't created.
I pulled up the query logs expecting something subtle. It was not. The list endpoint had no `tenant_id` filter at all. Every tenant in the database could read every other tenant's projects. The application never threw an error. It just returned whatever was there.
Missing tenant filters don't throw errors. They return the wrong data without any complaint, and nothing in your logs will flag it. I've seen this run in production for weeks before a support ticket pointed anyone at the query logs.
When it does surface, who finds it first matters a lot. A customer noticing it is bad. A compliance auditor noticing it during a SOC 2 review is a different kind of problem.
Isolation built in from the start is a day of work. The time I spent helping a team retrofit it after a compliance review was considerably longer than that, and involved more customer emails than anyone wanted to write.
The stack is Node.js with PostgreSQL. CRUD is the easy part. Tenant isolation, RBAC, and audit logging take more care, and where those checks run in the stack matters. I put all three in middleware, before any route handler fires. A handler that never calls the isolation logic directly can't accidentally skip it.
## Prerequisites
- Node.js 18+
- PostgreSQL 14+
- Basic knowledge of Express.js and JWT
## What We Will Build
A multi-tenant Express REST API that enforces:
- **Tenant isolation:** every database query scopes to the `tenant_id` from the verified JWT. The client can't influence which tenant the query runs against.
- **RBAC:** four roles, each with a numeric level (SuperAdmin is highest, Viewer lowest). Middleware checks the level before the handler runs.
- **Audit logging:** any write or sensitive read appends a row to the audit table. 

## Summary

The app can't modify those rows afterward. The database enforces this directly. If a bug in the app tries to UPDATE an audit row, the database refuses it. Application-level enforcement alone can't give you that guarantee.
- **Per-tenant rate limiting:** request counts in Redis, keyed to the tenant. I've seen IP-based limiting break an enterprise rollout when fifty users came through a single corporate proxy.
- **Tenant isolation tests:** a dedicated test file that proves cross-tenant data can't leak. Wire it into CI and it catches broken isolation before it ships.
## Table of Contents
- [How Multi-Tenancy Works](#heading-how-multi-tenancy-works)
- [Architecture Overview](#heading-architecture-overview)
- [Database Schema Design](#heading-database-schema-design)
- [Project Setup](#heading-project-setup)
- [JWT Design for Multi-Tenancy](#heading-jwt-design-for-multi-tenancy)
- [Auth and RBAC Middleware](#heading-auth-and-rbac-middleware)
- [The Tenant-Safe Repository Layer](#heading-the-tenant-safe-repository-layer)
- [Audit Logging Service](#heading-audit-logging-service)
- [Per-Tenant Rate Limiting](#heading-per-tenant-rate-limiting)
- [Building the Routes](#heading-building-the-routes)
- [Testing Tenant Isolation](#heading-testing-tenant-isolation)
- [Troubleshooting](#heading-troubleshooting)
- [Wrapping Up](#heading-wrapping-up)
## How Multi-Tenancy Works
This tutorial uses a **shared database with row-level isolation**: a `tenant_id` column on every table, a filter on every query. The database holds everyone's data together. The application decides what each tenant can see.
Two other approaches exist: schema-per-tenant and database-per-tenant. I've talked to teams on schema-per-tenant who ended up spending more engineering time on migration tooling than on their actual product. Database-per-tenant gives stronger guarantees but a connection pool that balloons with every new customer signup.
Neither scales cheaply. Row-level isolation scales further than most teams expect. The ones I know who moved off it did so years in, usually under specific regulatory pressure, not because the approach stopped working.
The one thing in this design that can't be optional: `tenant_id` **must always come from the verified JWT.** Not from the request body, not from the URL. Users control what they put in both of those. They don't control what gets signed into a JWT on your server.
## Architecture Overview
```
HTTP Request
│
▼
┌─────────────────────────────────────────┐
│ Express Middleware Stack │
│ │
│ 1. Rate Limiter (per tenant_id) │
│ 2. Auth Middleware (verify JWT) │
│ └─► Extracts: userId, tenantId, │
│ role, permissions │
│ 3. RBAC Middleware (check role) │
└──────────────┬──────────────────────────┘
│
▼
┌─────────────────────────────────────────┐
│ Route Handler │
│ │
│ 1. Call Repository (tenant-safe query) │
│ 2. Call Audit Service (fire & forget) │
│ 3. Return response │
└──────────────┬──────────────────────────┘
│
┌─────────┴──────────┐
▼ ▼
┌──────

## Related Articles

- [[Windows PowerShell]]
- [[master full stack mobile development with react native]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[openvm bugs]]
- [[understanding dijkstra s algorithm]]
