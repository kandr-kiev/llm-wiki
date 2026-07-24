---
title: "wiki.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - data
  - llm
  - news
  - open-source
  - real-time
  - use-case
---

# wiki.py

> **Source:** local-weather-space-lunar-digestsrcadapterswikipy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/wiki.py ingested: 2026-07-20 sha256: 7fb529528fe5ca809c8d1ebc28dfd81cc0c4c31e2e786ed41c14913157097ac3 blog_source: lo...
> **Sources:**
>   - local-weather-space-lunar-digestsrcadapterswikipy-2026-07-20.md
> **Links:**
- [[news.py]]
- [[airraid.py]]
- [[local-llm-wiki-algorithm]]
- [[moon.py]]
- [[local-llm-wiki-agent-contract]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/wiki.py
ingested: 2026-07-20
sha256: 7fb529528fe5ca809c8d1ebc28dfd81cc0c4c31e2e786ed41c14913157097ac3
blog_source: local:unknown
---
"""Wiki adapter — reads from local llm-wiki instead of Wikipedia RSS."""
import os
import re
import sys
import datetime
from zoneinfo import ZoneInfo
def _get_wiki_path():
"""Get wiki path from env or default."""
return os.environ.get("WIKI_PATH", os.path.expanduser("~/wiki"))
def _parse_frontmatter(content):
"""Extract YAML frontmatter from markdown content (no yaml dependency)."""
if content.startswith("---"):
parts = content.split("---", 2)
if len(parts) >= 3:
fm = {}
body = parts[2].strip()
# Simple YAML parser for basic key: value pairs and lists
current_key = None
for line in parts[1].strip().split("\n"):
line_stripped = line.strip()
if not line_stripped:
continue
# List item
if line_stripped.startswith("- "):
if current_key:
val = line_stripped[2:].strip().strip('"').strip("'")
if current_key not in fm:
fm[current_key] = []
fm[current_key].append(val)
continue
# Key: value
if ":" in line_stripped:
key, _, value = line_stripped.partition(":")
key = key.strip()
value = value.strip().strip('"').strip("'")
if value:
current_key = key
fm[key] = value
else:
current_key = key
fm[key] = []
return fm, body
return {}, content.strip()
def _read_wiki_pages():
"""Read all wiki pages and return structured data."""
wiki_path = _get_wiki_path()
pages = []
if not os.path.exists(wiki_path):
return pages
# Scan all .md files in wiki directories
for root, dirs, files in os.walk(wiki_path):
# Skip _archive and raw directories
if "_archive" in root or "raw" in root:
continue
for fname in files:
if not fname.endswith(".md"):
continue
fpath = os.path.join(root, fname)
try:
with open(fpath, "r", encoding="utf-8") as f:
content = f.read()
fm, body = _parse_frontmatter(content)
fm["_body"] = body
fm["_path"] = fpath
fm["_filename"] = fname
pages.append(fm)
except Exception:
continue
return pages
def fetch_wiki_news(limit=5):
"""Fetch recent IT/AI news from wiki digests and concepts.
Returns list of (title, description, timestamp) tuples.
"""
pages = _read_wiki_pages()
news = []
tz_name = "Europe/Kiev"
try:
tz = ZoneInfo(tz_name)
except Exception:
tz = datetime.timezone(datetime.timedelta(hours=3))
now_local = datetime.datetime.now(tz)
prev_cutoff = (now_local - datetime.timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0)
for page in pages:
page_type = page.get("type", "")
timestamp = page.get("timestamp", "")
title = page.get("title", "")
desc = page.get("description", "")
body = page.get("_body", "")
# Skip non-relevant types
if page_type not in ("Digest", "Concept", "Entity", "Reference"):
continue
# Parse timestamp
pub_dt = None
if timestamp:
for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
try:
pub_dt = datetime.datetime.strptime(timestamp, fmt)
if pub_dt.tzinfo is None:
pub_dt = pub_dt.replace(tzinfo=tz)
break


## Summary

See Key Findings for full content.

## Related Articles

- [[news.py]]
- [[airraid.py]]
- [[local-llm-wiki-algorithm]]
- [[moon.py]]
- [[local-llm-wiki-agent-contract]]
