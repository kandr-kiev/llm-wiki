---
title: "test content.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - news
---

# test content.py

> **Source:** local-weather-space-lunar-digestteststest_contentpy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/tests/test_content.py ingested: 2026-07-20 sha256: 0c657368d53ebf9070b4570e303271791cc9679c58e02f7bb2906b791acbbd73 blog_source: l...
> **Sources:**
>   - local-weather-space-lunar-digestteststest_contentpy-2026-07-20.md
> **Links:**
- [[test adapters.py]]
- [[wiki.py]]
- [[health advice.py]]
- [[digest.py]]
- [[news.py]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/tests/test_content.py
ingested: 2026-07-20
sha256: 0c657368d53ebf9070b4570e303271791cc9679c58e02f7bb2906b791acbbd73
blog_source: local:unknown
---
"""Tests for content pools — verify random selection and diversity."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.content.monty_comments import get_random, AIR_RAID, WEATHER, MOON, SPACE, NEWS, FINAL
from src.content.anecdotes import ANECDOTES, get_random as get_anecdote
from src.content.folk_forecasts import FOLK_FORECASTS, get_random as get_folk
from src.content.health_advice import get_health_advice, get_tech_impact
def test_monty_comments_exist():
assert len(AIR_RAID) > 0
assert len(WEATHER) > 0
assert len(MOON) > 0
assert len(SPACE) > 0
assert len(NEWS) > 0
assert len(FINAL) > 0
print("✅ test_monty_comments_exist passed")
def test_monty_comments_themed_emoji():
"""Each Monty comment should end with a thematic emoji, not 🤖."""
# Base emoji characters (without variation selectors)
thematic_base = {"⚠", "☀", "📈", "🌿", "🌙", "🚀", "📰", "☕", "🤖"}
for comment in AIR_RAID + WEATHER + MOON + SPACE + NEWS + FINAL:
assert "🤖" not in comment or comment.count("🤖 Монті:") == 1, \
f"Comment should end with thematic emoji, not 🤖: {comment[-20:]}"
# Strip trailing variation selectors (U+FE0F = 0xFE0F)
stripped = comment.strip()
while stripped and ord(stripped[-1]) == 0xFE0F:
stripped = stripped[:-1]
last_char = stripped[-1] if stripped else ""
assert last_char in thematic_base, \
f"Comment doesn't end with thematic emoji (got '{last_char}'): {stripped[-30:]}"
print("✅ test_monty_comments_themed_emoji passed")
def test_monty_random_variety():
"""Random selection should return different values over many calls."""
results = set()
for _ in range(50):
results.add(get_random("weather"))
assert len(results) > 1, "Random selection should vary"
print("✅ test_monty_random_variety passed")
def test_anecdotes_exist_and_diverse():
assert len(ANECDOTES) > 5
results = set()
for _ in range(50):
results.add(get_anecdote())
assert len(results) > 1, "Anecdotes should vary"
print("✅ test_anecdotes_exist_and_diverse passed")
def test_folk_forecasts_exist_and_diverse():
assert len(FOLK_FORECASTS) > 3
results = set()
for _ in range(50):
results.add(get_folk())
assert len(results) > 1, "Folk forecasts should vary"
print("✅ test_folk_forecasts_exist_and_diverse passed")
def test_health_advice_by_kp():
# Low Kp
advice = get_health_advice(2.0)
assert "Спокійний" in advice or "мінімальний" in advice
# Medium Kp (5-6 = moderate impact)
advice = get_health_advice(5.5)
assert "контроль тиску" in advice
# High Kp
advice = get_health_advice(6.5)
assert "головний біль" in advice
assert "серцеві" in advice.lower() or "Серцеві" in advice
# Very high Kp
advice = get_health_advice(8.0)
assert "СИЛЬНА" in advice
assert "ОБОВ'ЯЗКОВИЙ" in advice
print("✅ test_health_advice_by_kp passed")
def test_tech_impact_by_kp():
# L

## Summary

See Key Findings for full content.

## Related Articles

- [[test adapters.py]]
- [[wiki.py]]
- [[health advice.py]]
- [[digest.py]]
- [[news.py]]
