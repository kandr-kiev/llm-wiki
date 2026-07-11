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