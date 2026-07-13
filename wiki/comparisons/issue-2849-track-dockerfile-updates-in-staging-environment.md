---
title: "Issue #2849: Track Dockerfile updates in staging environment"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ci-cd
  - multi-agent
  - open-source
  - pipeline
  - security
  - workflow
---
# Issue #2849: Track Dockerfile updates in staging environment

> **Source:** gh-openaiopenai-cookbook-issue-2849-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/openai/openai-cookbook/issues/2849 ingested: 2026-07-11 sha256: 49554987a5173967831dbc0364b972482e3fc2256eec211c42ebb318483c0d3e blog_source: github:openai/openai-co...
> **Sources:**
>   - gh-openaiopenai-cookbook-issue-2849-2026-07-11.md
> **Links:**
- [[issue-2847-update-staging-dockerfile-for-laravelpassport-compatibility]]
- [[issue-2846-add-recipe-parse-any-document-with-the-unstructured-transform-mcp-server]]
- [[issue-2848-implement-multi-domain-intake-architecture-and-related-specs]]
- [[issue-6362-add-security-policy-to-the-repo]]
- [[issue-2844-add-avian-magnetoreception-quantum-co-scientist-example]]

## Key Findings

---
source_url: https://github.com/openai/openai-cookbook/issues/2849
ingested: 2026-07-11
sha256: 49554987a5173967831dbc0364b972482e3fc2256eec211c42ebb318483c0d3e
blog_source: github:openai/openai-cookbook
---
# Issue #2849: Track Dockerfile updates in staging environment
**State:** open | **Author:** alexanford | **Created:** 2026-07-11T06:42:14Z
## Summary
We need to track and manage Dockerfile updates in the staging environment to ensure consistency, reproducibility, and security across our containerized deployments.
## Context
- **Environment:** Staging
- **Component:** Dockerfile(s)
- **Goal:** Establish a clear process for reviewing, testing, and promoting Dockerfile changes from staging to production.
## Tasks
- [ ] Audit current Dockerfile(s) used in staging
- [ ] Identify outdated base images and dependencies
- [ ] Implement multi-stage build optimizations where applicable
- [ ] Add CI checks for Dockerfile linting (e.g., hadolint)
- [ ] Document the update and promotion workflow
## Acceptance Criteria
- All staging Dockerfiles are up to date with latest stable base images
- CI pipeline includes Dockerfile validation
- Documentation exists for the update/promotion process
---
*This issue was created to track ongoing Dockerfile maintenance in the staging environment.*

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-2847-update-staging-dockerfile-for-laravelpassport-compatibility]]
- [[issue-2846-add-recipe-parse-any-document-with-the-unstructured-transform-mcp-server]]
- [[issue-2848-implement-multi-domain-intake-architecture-and-related-specs]]
- [[issue-6362-add-security-policy-to-the-repo]]
- [[issue-2844-add-avian-magnetoreception-quantum-co-scientist-example]]
