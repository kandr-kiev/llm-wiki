---
title: "news.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - news
  - search
---

# news.py

> **Source:** local-weather-space-lunar-digestsrcadaptersnewspy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/news.py ingested: 2026-07-20 sha256: 674af620b6834858869b7c6cf36df063c42b1d518fc950d8af16863d585de8c6 blog_source: lo...
> **Sources:**
>   - local-weather-space-lunar-digestsrcadaptersnewspy-2026-07-20.md
> **Links:**
- [[airraid.py]]
- [[moon.py]]
- [[дайджест-аудит-повний-чек-лист-помилок-2026-07-15]]
- [[app.js]]
- [[changelog]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/news.py
ingested: 2026-07-20
sha256: 674af620b6834858869b7c6cf36df063c42b1d518fc950d8af16863d585de8c6
blog_source: local:unknown
---
"""RSS news adapter."""
import urllib.request
import sys
import re
import json
RSS_SOURCES = [
"https://www.bbc.com/ukrainian/rss.xml",
"https://hromadske.radio/rss",
"https://dou.ua/feed/",
"https://www.unian.ua/rss/",
"https://www.epravda.com.ua/rss/",
]
def fetch_rss(url, timeout=10):
try:
req = urllib.request.Request(
url,
headers={"User-Agent": "weather-space-lunar-digest/1.0"},
)
with urllib.request.urlopen(req, timeout=timeout) as resp:
return resp.read().decode("utf-8", errors="replace")
except Exception as e:
print(f"[WARN] Failed to fetch {url}: {e}", file=sys.stderr)
return None
def parse_rss(content):
items = []
item_pattern = r"(.*?)"
matches = re.findall(item_pattern, content, re.DOTALL)
for match in matches:
title_m = re.search(r"(.*?)", match, re.DOTALL)
link_m = re.search(r"- (.*?)", match, re.DOTALL)
date_m = re.search(r"(.*?)", match, re.DOTALL)
desc_m = re.search(r"(.*?)", match, re.DOTALL)
item = {}
if title_m:
item["title"] = re.sub(r"", "", title_m.group(1)).strip()
if link_m:
item["link"] = re.sub(r"", "", link_m.group(1)).strip()
if date_m:
item["pubDate"] = re.sub(r"", "", date_m.group(1)).strip()
if desc_m:
item["description"] = re.sub(r"", "", desc_m.group(1)).strip()
if item.get("title"):
items.append(item)
return items
def fetch_news():
all_items = []
for url in RSS_SOURCES:
content = fetch_rss(url)
if content:
all_items.extend(parse_rss(content))
return all_items

## Summary

See Key Findings for full content.

## Related Articles

- [[airraid.py]]
- [[moon.py]]
- [[дайджест-аудит-повний-чек-лист-помилок-2026-07-15]]
- [[app.js]]
- [[changelog]]
