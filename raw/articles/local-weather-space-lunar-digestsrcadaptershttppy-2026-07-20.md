---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/http.py
ingested: 2026-07-20
sha256: b0c2ce1b64f85896cf1df8cefb9d9eeb7c03b2b59915f63760e02006fc7ecb4c
blog_source: local:unknown
---
"""Shared HTTP client."""
import urllib.request
import sys


def http_get(url, timeout=15, user_agent="weather-space-lunar-digest/1.0"):
    """Generic HTTP GET with User-Agent."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": user_agent},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"[WARN] GET {url} failed: {e}", file=sys.stderr)
        return None
