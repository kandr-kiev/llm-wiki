---
title: "test adapters.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - data
  - real-time
---

# test adapters.py

> **Source:** local-weather-space-lunar-digestteststest_adapterspy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/tests/test_adapters.py ingested: 2026-07-20 sha256: f091084ad446220775d60a9c108c9a6ebd240c80cae37aac19236ca8f090ec79 blog_source:...
> **Sources:**
>   - local-weather-space-lunar-digestteststest_adapterspy-2026-07-20.md
> **Links:**
- [[translation-helpers-moved-from-old-adaptersnoaa_swpcpy]]
- [[airraid.py]]
- [[news.py]]
- [[digest.py]]
- [[moon.py]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/tests/test_adapters.py
ingested: 2026-07-20
sha256: f091084ad446220775d60a9c108c9a6ebd240c80cae37aac19236ca8f090ec79
blog_source: local:unknown
---
"""Tests for adapters — mock HTTP responses, verify data structure."""
import sys
import os
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.adapters.http import http_get
from src.adapters.airraid import fetch_air_raid
from src.adapters.moon import get_moon_phase
from src.adapters.noaa import _translate_months, _translate_solar_terms, _translate_forecast_line
def test_http_get():
"""Test HTTP client with a real URL."""
result = http_get("https://httpbin.org/get", timeout=5)
# httpbin.org may return 503 — acceptable in test env
if result is not None:
assert "httpbin" in result.lower()
print("✅ test_http_get passed")
def test_translate_months():
assert "липня" in _translate_months("Jul 12")
assert "січня" in _translate_months("Jan 1")
assert "грудня" in _translate_months("Dec 25")
assert "червня" in _translate_months("Jun 15")
print("✅ test_translate_months passed")
def test_translate_solar_terms():
text = "due to the anticipated arrival of a CME that left the Sun on Jul 9"
result = _translate_solar_terms(text)
assert "коронального викиду маси" in result
assert "через очікуване прибуття" in result
print("✅ test_translate_solar_terms passed")
def test_translate_forecast_line():
text = "Solar Radiation Storm Forecast for Jul 12-14"
result = _translate_forecast_line(text)
assert "Прогноз сонячної радіаційної" in result
assert "липня" in result
print("✅ test_translate_forecast_line passed")
def test_moon_phase_structure():
"""Test that moon phase returns all required keys."""
result = get_moon_phase()
required_keys = ["age", "phase", "visibility", "lunar_day", "zodiac", "symbol_of_day"]
for key in required_keys:
assert key in result, f"Missing key: {key}"
# Values should make sense
assert 0 <= result["age"] < 30
assert 0 <= result["visibility"] <= 100
assert 1 <= result["lunar_day"] <= 29
print("✅ test_moon_phase_structure passed")
def test_air_raid_returns_dict():
"""Test air raid adapter returns dict (may be empty if API down)."""
result = fetch_air_raid("Чернігівська область")
if result is not None:
assert isinstance(result, dict)
assert "status" in result
assert "districts" in result
assert "region" in result
if result["status"] == "not_applicable":
# Non-UA location
assert result["status"] in ("not_applicable", "active", "stopped")
else:
# API down — acceptable
print("⚠️ Air raid API unavailable (expected in test env)")
print("✅ test_air_raid_returns_dict passed")
if __name__ == "__main__":
print("=" * 50)
print("🧪 Тестування адаптерів")
print("=" * 50)
test_translate_months()
test_translate_solar_terms()
test_translate_forecast_line()
test_moon_phase_structure()
test_air_raid_returns_dict()
# HTTP test may fail in restricted env
try:
test_http_get()
except Exception as e:
print(f"⚠

## Summary

See Key Findings for full content.

## Related Articles

- [[translation-helpers-moved-from-old-adaptersnoaa_swpcpy]]
- [[airraid.py]]
- [[news.py]]
- [[digest.py]]
- [[moon.py]]
