---
source_url: https://github.com/microsoft/DeepSpeed/issues/8140
ingested: 2026-07-14
sha256: c4de5c28f7f06f13cf8b646a7d194b456fbebcaf817f9a963bb95c385649badc
blog_source: github:microsoft/DeepSpeed
---
# Issue #8140: Add logging support for better observability

**State:** open | **Author:** goransh-buh | **Created:** 2026-07-14T05:21:34Z

## Feature Request

### Summary
The project would benefit from structured logging to make it easier to debug issues in production.

### Motivation
Currently it can be difficult to understand what the application is doing at runtime without adding print statements. Proper logging would:

- Allow users to control verbosity with log levels (DEBUG, INFO, WARNING, ERROR)
- Make it easier to integrate with log aggregation systems
- Help diagnose issues in production without code changes

### Proposed Implementation
```python
import logging

log = logging.getLogger(__name__)

def my_function():
    log.debug("Starting my_function")
    # ... 
    log.info("my_function completed successfully")
```

### Impact
Low risk change with high value for users running this in production environments.
