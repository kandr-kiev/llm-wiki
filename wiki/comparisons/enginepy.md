---
title: "engine.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - data
  - news
  - open-source
  - pipeline
---

# engine.py

> **Source:** local-weather-space-lunar-digestsrcpipelineenginepy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/src/pipeline/engine.py ingested: 2026-07-20 sha256: 3fae2e5c6b3990378850aa739f81a4130459d6bde775fa62cbbcd2bb06f31e2e blog_source:...
> **Sources:**
>   - local-weather-space-lunar-digestsrcpipelineenginepy-2026-07-20.md
> **Links:**
- [[news.py]]
- [[airraid.py]]
- [[digest.py]]
- [[wiki.py]]
- [[weather-digest-automation-refactor-plan]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/pipeline/engine.py
ingested: 2026-07-20
sha256: 3fae2e5c6b3990378850aa739f81a4130459d6bde775fa62cbbcd2bb06f31e2e
blog_source: local:unknown
---
"""Pipeline engine — runs scout.py, then formats and renders the digest."""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR)) # src/pipeline/ → src/ → корінь
TEMPLATE_PATH = os.path.join(ROOT_DIR, "templates", "digest-template.md")
HTML_TEMPLATE_PATH = os.path.join(ROOT_DIR, "src", "formatters", "html_template.html")
OUTPUT_MD_PATH = "/output/digest_output.md"
OUTPUT_HTML_PATH = "/output/digest_output.html"
def run_pipeline():
"""Run all services → format → write digest_output.md + digest_output.html."""
# ── 1. Collect data from services ────────────────────────────────────
from src.services.weather import get_weather_summary
from src.services.space import fetch_space
from src.services.news import fetch_news
from src.services.airraid import fetch_air_raid
from src.adapters.moon import get_moon_phase
from datetime import datetime
from zoneinfo import ZoneInfo
LATITUDE = 47.1
LONGITUDE = 31.5
TIMEZONE = "Europe/Kiev"
DEFAULT_LOCATION_TEXT = "с. Крехаїв, Чернігівська область, Чернігівський район"
try:
tz = ZoneInfo(TIMEZONE)
except Exception:
tz = datetime.timezone(datetime.timedelta(hours=3))
location = {
"query": DEFAULT_LOCATION_TEXT,
"name": "Крехаїв",
"display_name": DEFAULT_LOCATION_TEXT,
"latitude": LATITUDE,
"longitude": LONGITUDE,
"timezone": TIMEZONE,
"country": "Україна",
"country_code": "UA",
"admin1": "Чернігівська область",
"admin2": "Чернігівський район",
"admin3": "",
"source": "default_config",
"is_default": True,
}
weather_raw = get_weather_summary(LATITUDE, LONGITUDE)
air_raid_raw = fetch_air_raid(location.get("admin1", "Чернігівська область"))
space_raw = fetch_space()
moon_data = get_moon_phase()
news_raw = fetch_news()
payload = {
"timestamp": datetime.now(tz).isoformat(),
"location": location,
"weather_raw": weather_raw,
"air_raid_raw": air_raid_raw,
"space_raw": space_raw,
"moon_data": moon_data,
"news_raw": news_raw,
}
# ── 2. Load templates ────────────────────────────────────────────────
if not os.path.exists(TEMPLATE_PATH):
print(f"[ERROR] Template not found at {TEMPLATE_PATH}", file=sys.stderr)
sys.exit(1)
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
template = f.read()
html_template = ""
if os.path.exists(HTML_TEMPLATE_PATH):
with open(HTML_TEMPLATE_PATH, "r", encoding="utf-8") as f:
html_template = f.read()
# ── 3. Render ────────────────────────────────────────────────────────
from src.formatters.digest import render
md_rendered = render(payload, template)
html_rendered = ""
if html_template:
html_rendered = render(payload, html_template)
# ── 4. Write output ──────────────────────────────────────────────────
os.ma

## Summary

See Key Findings for full content.

## Related Articles

- [[news.py]]
- [[airraid.py]]
- [[digest.py]]
- [[wiki.py]]
- [[weather-digest-automation-refactor-plan]]
