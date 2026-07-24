---
title: "test pipeline.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - data
  - integration
  - news
  - open-source
  - pipeline
  - real-time
---

# test pipeline.py

> **Source:** local-weather-space-lunar-digestteststest_pipelinepy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/tests/test_pipeline.py ingested: 2026-07-20 sha256: c181617f6be6518fda3b510a6ae9ce86f059af6ca75be66c1d96e8dc76a61cb9 blog_source:...
> **Sources:**
>   - local-weather-space-lunar-digestteststest_pipelinepy-2026-07-20.md
> **Links:**
- [[test-contentpy]]
- [[test-adapterspy]]
- [[digest.py]]
- [[translation-helpers-moved-from-old-adaptersnoaa_swpcpy]]
- [[wiki.py]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/tests/test_pipeline.py
ingested: 2026-07-20
sha256: c181617f6be6518fda3b510a6ae9ce86f059af6ca75be66c1d96e8dc76a61cb9
blog_source: local:unknown
---
"""Integration test for the full pipeline — mocked data, verify output structure."""
import sys
import os
import re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def test_template_placeholders_match_replacements():
"""Verify all template {{placeholders}} have a corresponding replacement key."""
# Load template
template_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
"digest-template.md")
if not os.path.exists(template_path):
print(f"⚠️ Template not found at {template_path}, skipping")
return
with open(template_path, "r", encoding="utf-8") as f:
template = f.read()
# Extract all placeholders
placeholders = set(re.findall(r'\{\{(\w+)\}\}', template))
# Known replacements from src/formatters/digest.py render()
replacement_keys = {
"date_full", "scout_time", "location_text",
"air_raid_alert", "air_raid_time_display", "air_raid_raion",
"air_raid_previous", "air_raid_today_stats",
"weather_condition", "weather_temp_range", "weather_apparent_range",
"weather_wind_desc", "weather_wind_gust", "weather_pressure_range",
"weather_humidity_range", "weather_cloudiness", "weather_sunrise",
"weather_sunset", "weather_precip",
"weather_morning_block", "weather_day_block", "weather_evening_block", "weather_night_block",
"folk_forecast",
"moon_day", "moon_rise", "moon_planning",
"space_kp_index", "space_events_detail", "space_forecast",
"space_health_groups", "space_tech_detailed",
"news_sections",
"notes_drivers", "notes_military", "notes_satellite",
"monty_alert_comment", "monty_weather_comment",
"monty_chrono_comment", "monty_moon_comment",
"monty_space_comment", "monty_news_comment",
"monty_anecdote", "monty_final_closing",
}
# Check all template placeholders are covered
missing = placeholders - replacement_keys
if missing:
print(f"⚠️ Missing replacements for: {missing}")
# Check no extra replacements
extra = replacement_keys - placeholders
if extra:
print(f"⚠️ Extra replacements not in template: {extra}")
print(f"✅ test_template_placeholders_match_replacements passed ({len(placeholders)} placeholders)")
def test_content_pools_non_empty():
"""Verify all content pools have multiple options."""
from src.content.monty_comments import AIR_RAID, WEATHER, MOON, SPACE, NEWS, FINAL
from src.content.anecdotes import ANECDOTES
from src.content.folk_forecasts import FOLK_FORECASTS
assert len(AIR_RAID) >= 5, f"AIR_RAID has {len(AIR_RAID)} items"
assert len(WEATHER) >= 5, f"WEATHER has {len(WEATHER)} items"
assert len(MOON) >= 4, f"MOON has {len(MOON)} items"
assert len(SPACE) >= 4, f"SPACE has {len(SPACE)} items"
assert len(NEWS) >= 4, f"NEWS has {len(NEWS)} items"
assert len(FINAL) >= 4, f"FINAL has {len(FINAL)} items"
assert len(ANECDOTES) >= 10, f"ANECDOTES has {len(ANECDOTES)} items"
asse

## Summary

rt len(FOLK_FORECASTS) >= 5, f"FOLK_FORECASTS has {len(FOLK_FORECASTS)} items"
print("✅ test_content_pools_non_empty passed")
def test_no_english_in_space_translation():
"""Verify space translation removes English text."""
from src.adapters.noaa import _translate_solar_terms
english_text = "due to the anticipated arrival of a CME that left the Sun on Jul 9"
result = _translate_solar_terms(english_text)
# Should contain Ukrainian translation
assert "через" in result or "очікуване" in result, f"Expected Ukrainian translation, got: {result}"
# Should not contain "CME" without Ukrainian explanation
if "CME" in result:
assert "корональний" in result, f"CME should be explained in Ukrainian: {result}"
print("✅ test_no_english_in_space_translation passed")
def test_monty_no_emoji_ddd():
"""Verify Monty comments end with thematic emoji, not 🤖."""
from src.content.monty_comments import get_random
# Thematic emoji BASE characters (without variation selectors)
thematic_bases = {"⚠", "☀", "📈", "🌿", "🌙", "🚀", "📰", "☕"}
for section in ["air_raid", "weather", "chronology", "moon", "space", "news", "final"]:
for _ in range(10):
comment = get_random(section)
# Strip trailing variation selectors (U+FE0F = 0xFE0F) and ZWJ (U+200D)
stripped = comment.strip()
while stripped and ord(stripped[-1]) in (0xFE0F, 0x200D, 0x20E3):
stripped = stripped[:-1]
# Also strip combining diacriticals (U+0300–U+036F)
while stripped and 0x0300 <= ord(stripped[-1]) <= 0x036F:
stripped = stripped[:-1]
last_char = stripped[-1] if stripped else ""
assert last_char in thematic_bases, \
f"Section '{section}' comment ends with '{last_char}' (U+{ord(last_char):04X}) instead of thematic emoji: {stripped[-40:]}"
print("✅ test_monty_no_emoji_ddd passed")
def test_render_basic():
"""Test that render() fills all placeholders from a mock payload."""
from src.formatters.digest import render
payload = {
"location": {"display_name": "с. Крехаїв"},
"weather_raw": {
"current_weather": {"temperature": 20, "windspeed": 5, "winddirection": 180, "weathercode": 0},
"daily": {
"temperature_2m_max": [22], "temperature_2m_min": [12],
"apparent_temperature_max": [21], "apparent_temperature_min": [11],
"sunrise": ["2026-07-13T04:49"], "sunset": ["2026-07-13T21:00"],
"wind_gusts_10m_max": [15], "pressure_msl_max": [1013], "pressure_msl_min": [1011],
"precipitation_sum": [0], "precipitation_probability_max": [0],
"relative_humidity_2m_max": [70], "relative_humidity_2m_min": [50],
"cloudcover_max": [30],
},
"hourly": {
"time": [f"2026-07-13T{h:02d}:00" for h in range(24)],
"temperature_2m": [14] * 24,
"relative_humidity_2m": [70] * 24,
"pressure_msl": [1012] * 24,
"wind_speed_10m": [5] * 24,
"weather_code": [0] * 24,
"cloudcover": [30] * 24,
},
},
"air_raid_raw": {
"status": "stopped", "changed": "10:00",
"districts": [], "previous_alerts": [],
"today_count": 0, "today_duration_min": 0, "raion": "Чернігівський",
},
"space_raw": {
"kp": 2.0, "events": "Немає подій", "forecast": "Спокійно",
"solar_activity_level": "НИЗЬ

## Related Articles

- [[test-contentpy]]
- [[test-adapterspy]]
- [[digest.py]]
- [[translation-helpers-moved-from-old-adaptersnoaa_swpcpy]]
- [[wiki.py]]
