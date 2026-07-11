---
source_url: https://github.com/openai/openai-cookbook/issues/2847
ingested: 2026-07-11
sha256: 7edea7aa4ba2b86c41afb2790ee060ed3181b71728e4db8a828033c832ee3483
blog_source: github:openai/openai-cookbook
---
# Issue #2847: Update staging Dockerfile for laravel/passport compatibility

**State:** open | **Author:** alexanford | **Created:** 2026-07-11T02:29:23Z

## Summary

The staging Dockerfile needs to be updated to ensure full compatibility with `laravel/passport`. This is required for our Video Editing pipeline authentication flow.

## Context

- **Package:** `laravel/passport`
- **Environment:** Staging
- **Related work:** Product demo scheduled to discuss the Video Editing pipeline, which depends on OAuth2 token issuance via Passport.

## Proposed Changes

1. Update the base image to a version that supports the required PHP extensions for `laravel/passport`.
2. Ensure `ext-openssl`, `ext-pdo`, and `ext-mbstring` are installed and enabled.
3. Add a dedicated build stage for Passport keys generation.
4. Verify the `storage/oauth-*.key` paths are correctly volume-mounted in staging.

## Acceptance Criteria

- [ ] Staging Dockerfile builds successfully with `laravel/passport` installed.
- [ ] OAuth2 token issuance works end-to-end in staging.
- [ ] No regressions in existing CI/CD pipeline.