---
title: "health advice.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
  ---

# health advice.py

> **Source:** local-weather-space-lunar-digestsrccontenthealth_advicepy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/src/content/health_advice.py ingested: 2026-07-20 sha256: 1ab55ef953e7a8168eb1bb5e84de3dfe948ae0ebf69c3d3e81ed01be3393f5e0 blog_so...
> **Sources:**
>   - local-weather-space-lunar-digestsrccontenthealth_advicepy-2026-07-20.md
> **Links:**
- [[airraid.py]]
- [[wiki.py]]
- [[moon.py]]
- [[anecdotes.py]]
- [[── Translation helpers (moved from old adapters/noaa_swpc.py) ──]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/content/health_advice.py
ingested: 2026-07-20
sha256: 1ab55ef953e7a8168eb1bb5e84de3dfe948ae0ebf69c3d3e81ed01be3393f5e0
blog_source: local:unknown
---
"""Health advice pool — randomized health recommendations based on Kp index."""
def get_health_advice(kp: float) -> str:
"""Get health advice based on Kp index.
Kp = 7: strong advice
"""
if kp str:
"""Get technical impact advice based on Kp index."""
if kp < 3:
return "🔧 **Технічний вплив:**\n 📡 Радіозв'язок: без перешкод\n 🛰 Супутники: стабільна робота\n 🛩 БПЛА/дрони: GPS стабільний"
if kp < 5:
return "🔧 **Технічний вплив:**\n 📡 Радіозв'язок: легкі перешкоди HF-діапазону\n 🛰 Супутники: можливі незначні збої\n 🛩 БПЛА/дрони: перевіряйте GPS"
return "🔧 **Технічний вплив:**\n 📡 Радіозв'язок: завади HF-діапазону\n 📻 HF: деградація на освітленій стороні\n 🛰 Супутники: зарядження поверхні, опір\n 🛩 БПЛА/дрони: збої навігації — перевіряйте GPS\n ⚡️ Енергосистеми: корективи напруги"

## Summary

See Key Findings for full content.

## Related Articles

- [[airraid.py]]
- [[wiki.py]]
- [[moon.py]]
- [[anecdotes.py]]
- [[── Translation helpers (moved from old adapters/noaa_swpc.py) ──]]
