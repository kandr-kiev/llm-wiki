---
source_url: https://github.com/meta-llama/llama/issues/1452
ingested: 2026-07-11
sha256: be5a80533007d7c89ce075e052d5cab795061086e8dce9ab9bf5c53a055a80b4
blog_source: github:meta-llama/llama
---
# Issue #1452: Strengthen prompt injection protection in chat_completion

**State:** open | **Author:** tojixlugar | **Created:** 2026-06-30T04:44:19Z

## Summary

This PR strengthens the prompt injection protection in `chat_completion()` by addressing multiple bypass vectors:

1. **Unicode evasion** - Zero-width characters, full-width characters
2. **Role field injection** - Previously unvalidated
3. **Partial/modified tags** - Space insertion, character encoding

## Changes

- Add Unicode normalization function to catch evasion attempts
- Implement comprehensive message validation
- Add 20+ test cases covering all known bypass vectors
- Maintain backward compatibility (no API changes)

## Vulnerability Addresses

- Zero-width character bypass (U+200B, U+200C, U+200D)
- Role field manipulation (was not validated)
- Partial tag bypass ("[ INST]" with spaces)
- HTML entity encoding

## Testing

All 20+ tests pass:
- Unicode normalization tests
- Injection detection tests  
- Dialog validation tests
- Edge case handling
- Integration tests

## Security Impact

Fixes potential prompt injection vulnerabilities that could bypass the current safety check.

## Breaking Changes

None. This is a security hardening with no API changes.

## Checklist

- [x] Code follows project style
- [x] Tests added and passing
- [x] No breaking changes
- [x] Backward compatible
- [x] Security implications reviewed
- [x] Documentation updated with docstrings