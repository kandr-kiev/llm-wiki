---
title: "── Translation helpers (moved from old adapters/noaa_swpc.py) ──"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
  ---

# ── Translation helpers (moved from old adapters/noaa_swpc.py) ──

> **Source:** local-weather-space-lunar-digestsrcadaptersnoaapy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/noaa.py ingested: 2026-07-20 sha256: 13677b2f76e710e740978e8959ba8087b382e3377122b7e84f3b33c68af44168 blog_source: lo...
> **Sources:**
>   - local-weather-space-lunar-digestsrcadaptersnoaapy-2026-07-20.md
> **Links:**
- [[airraid.py]]
- [[news.py]]
- [[moon.py]]
- [[дайджест-аудит-повний-чек-лист-помилок-2026-07-15]]
- [[phpunit]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/noaa.py
ingested: 2026-07-20
sha256: 13677b2f76e710e740978e8959ba8087b382e3377122b7e84f3b33c68af44168
blog_source: local:unknown
---
"""NOAA SWPC text forecast adapter."""
from .http import http_get
def fetch_forecast(url="https://services.swpc.noaa.gov/text/3-day-forecast.txt", timeout=15):
return http_get(url, timeout=timeout)
# ── Translation helpers (moved from old adapters/noaa_swpc.py) ──
_MONTHS = {
"Jan": "січня", "Feb": "лютого", "Mar": "березня", "Apr": "квітня",
"May": "травня", "Jun": "червня", "Jul": "липня", "Aug": "серпня",
"Sep": "вересня", "Oct": "жовтня", "Nov": "листопада", "Dec": "грудня",
}
def _translate_months(line: str) -> str:
for eng, uk in _MONTHS.items():
line = line.replace(eng, uk)
return line
_SOLAR_TERMS = {
"coronal mass ejection": "корональний викид маси (CME)",
"CME": "корональний викид маси (CME)",
"due to the anticipated arrival of a CME that left the Sun on": "через очікуване прибуття коронального викиду маси, що вийшов з Сонця",
"due to the anticipated arrival of a CME": "через очікуване прибуття коронального викиду маси (CME)",
"CME that left the Sun": "корональний викид маси, що вийшов з Сонця",
}
def _translate_solar_terms(text: str) -> str:
# Sort by length descending so longer phrases match first
for eng, uk in sorted(_SOLAR_TERMS.items(), key=lambda x: len(x[0]), reverse=True):
if eng in text:
text = text.replace(eng, uk)
return text
def _translate_forecast_line(line: str) -> str:
"""Translate a single forecast line (S-class or R-class probabilities)."""
line = _translate_months(line)
line = line.replace(
"Solar Radiation Storm Forecast for",
"Прогноз сонячної радіаційної штормової активності на"
)
for cls in ["S1", "S2", "S3", "S4", "S5", "R1", "R2", "R3", "R4", "R5"]:
line = line.replace(f"{cls} or higher", f"{cls} або вище")
return line

## Summary

See Key Findings for full content.

## Related Articles

- [[airraid.py]]
- [[news.py]]
- [[moon.py]]
- [[дайджест-аудит-повний-чек-лист-помилок-2026-07-15]]
- [[phpunit]]
