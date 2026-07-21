---
title: "digest.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ci-cd
  - data
  - gpt
  - llm
  - news
  - open-source
  - real-time
---

# digest.py

> **Source:** local-weather-space-lunar-digestsrcformattersdigestpy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/src/formatters/digest.py ingested: 2026-07-20 sha256: 041e4e51da3fa25f07ec16b18ff434a06f57f417f88b9818521461f70ebeb952 blog_source...
> **Sources:**
>   - local-weather-space-lunar-digestsrcformattersdigestpy-2026-07-20.md
> **Links:**
- [[Air raid comments]]
- [[── Translation helpers (moved from old adapters/noaa_swpc.py) ──]]
- [[airraid.py]]
- [[health advice.py]]
- [[Дайджест Аудит — Повний чек-лист помилок (2026-07-15)]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/formatters/digest.py
ingested: 2026-07-20
sha256: 041e4e51da3fa25f07ec16b18ff434a06f57f417f88b9818521461f70ebeb952
blog_source: local:unknown
---
"""Template-first renderer for weather-space-lunar-digest.
Maps scout.py JSON payload keys to digest-template.md placeholders.
All Monty comments are generated dynamically with thematic emojis.
"""
import json
import random
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo
def _format_time(iso_str):
"""Convert ISO time string to HH:MM format."""
if not iso_str:
return "--:--"
try:
# Handle "2026-07-13T04:50" format
return iso_str.split("T")[1][:5]
except (IndexError, AttributeError):
return str(iso_str)[:5]
def _wind_direction_to_text(deg):
"""Convert wind direction degrees to Ukrainian abbreviation."""
directions = ["Пн", "ПнСх", "Сх", "ПдСх", "Пд", "ПдЗх", "Зх", "ПнЗх"]
idx = int(deg / 45) % 8
return directions[idx]
def _wmo_code_to_text(code, is_night=False):
"""Convert WMO weather code to Ukrainian text with emoji.
User-approved condition names.
"""
codes = {
0: ("☀️", "Сонячно" if not is_night else "Ясне небо"),
1: ("🌤", "Мінлива хмарність"),
2: ("⛅", "Переважно хмарно"),
3: ("☁️", "Хмарно"),
45: ("🌫", "Туман"),
48: ("🌫", "Сильний туман"),
51: ("🌦", "Невеликий дощ"),
53: ("🌦", "Невеликий дощ"),
55: ("🌧", "Невеликий дощ"),
61: ("🌧", "Невеликий дощ"),
63: ("🌧", "Дощ"),
65: ("🌧", "Дощ"),
71: ("🌨", "Дощ зі снігом"),
73: ("❄️", "Сніг"),
75: ("❄️", "Снігопад"),
80: ("🌦", "Злива"),
81: ("🌧", "Злива"),
82: ("🌧", "Злива"),
95: ("⛈", "Гроза"),
96: ("⛈", "Гроза"),
99: ("⛈", "Гроза"),
}
emoji, text = codes.get(code, ("🌡️", f"Код {code}"))
return text
def _get_monty_comment(section, payload):
"""Generate context-aware Monty comment with thematic emoji."""
if section == "alert":
status = payload.get("air_raid_raw", {}).get("status", "stopped")
if status == "active":
return "Тривога активна, перевіряйте укриття! 🚨"
return "Тривоги зараз немає, працюємо спокійно. ✅"
if section == "weather":
cw = payload.get("weather_raw", {}).get("current_weather", {})
temp = cw.get("temperature", 20)
if temp > 25:
return "Спека сьогодні така, що навіть боти паряться. ☀️"
elif temp 10:
return "Графік температури стрибав, як акції на біржі. 📈"
elif wind_gust > 5.5:
return "Вітер сьогодні грає в піаніно на вікнах. 🌬️"
elif temp_range > 7:
return "Температура сьогодні як гарячий чай — то кипить, то остигає. 🌡️"
else:
return "Графік температури в нормі, без драми. 📈"
if section == "moon":
lunar_day = payload.get("moon_data", {}).get("lunar_day", 15)
phase = payload.get("moon_data", {}).get("phase", "")
zodiac = payload.get("moon_data", {}).get("zodiac", "")
symbol = payload.get("moon_data", {}).get("symbol_of_day", "")
if lunar_day = 5:
return "Космос сьогодні злий, як клієнт у понеділок. 🚀"
elif kp >= 3:
return "Сонце сьогодні дещо активне, але без паніки. ☄️"
return "Сонце сьогодні спокійне, працюємо. 🌌"
if section == 

## Summary

"news":
news = payload.get("news_raw", {})
if not isinstance(news, dict):
return "Новини спокійні, як реліз без багів. 📰"
news_count = sum(len(v) for v in news.values())
war_count = len(news.get("war", []))
geopol_count = len(news.get("geopol", []))
tech_count = len(news.get("tech", []))
llm_count = len(news.get("llm", []))
if war_count > 5:
return "Новин з фронту більше, ніж комітів за тиждень. 📰"
if llm_count > 2:
return "LLM-новин стільки, що GPT-5 сам не впорається. 🤖"
if tech_count > 2:
return "IT-новин стільки, що треба перекладати. 💾"
if geopol_count > 3:
return "Дипломатія кипить, як CI-піплайн у п'ятницю. 🌍"
if news_count > 10:
return "Новин сьогодні стільки, що не влізе в пам'ять. 📰"
elif news_count > 5:
return "Новинний фон гуде, як трансформатор біля дому. 📡"
return "Новини спокійні, як реліз без багів. 📰"
if section == "closing":
# Аналізуємо загальний стан дайджесту
air_status = payload.get("air_raid_raw", {}).get("status", "stopped")
space_kp = payload.get("space_raw", {}).get("kp", 2)
weather_temp = payload.get("weather_raw", {}).get("current_weather", {}).get("temperature", 20)
if air_status == "active":
return "Тривога активна — перевіряйте укриття, а не повідомлення. 🚨"
elif space_kp >= 5:
return "Космос сьогодні злий, але ви сильніші за магнітні бурі. 🚀"
elif weather_temp > 25:
return "Спека сьогодні така, що навіть боти паряться. ☀️"
elif weather_temp first_q:
# Deterioration: better → worse
suffix = _transition_suffix(last_cat)
if suffix:
return f"{_cat_name(first_cat)} {suffix}", has_storm
return _cat_name(last_cat), has_storm
else:
# Same quality level → mixed/back-and-forth
# Return dominant (most common)
most_common = Counter(codes_list).most_common(1)[0][0]
return _wmo_code_to_text(most_common, is_night), has_storm
def _get_condition_single(start_h, end_h, t_times, t_codes):
"""Get dominant weather code for a single time range."""
codes = []
for i, t in enumerate(t_times):
try:
hour = int(t.split("T")[1][:2])
if start_h 5:
folk_forecast = "🌿 Народний прогноз: \"Якщо зранку туман — буде дощ\""
else:
folk_forecast = "🌿 Народний прогноз: \"Якщо ввечері вітерець — завтра буде світло\""
# Try to use folk_forecasts.py pool if available (overwrite with random)
try:
from src.content.folk_forecasts import get_random as get_folk
# Folk forecasts in pool already start with "🌿", strip and re-wrap
folk_text = get_folk().strip()
if folk_text.startswith("🌿"):
folk_text = folk_text[1:].strip()
folk_forecast = f"🌿 Народний прогноз: \"{folk_text}\""
except ImportError:
pass
# ── 3. Parse air raid data ────────────────────────────────────────────
air_status = air_raid.get("status", "stopped")
air_raid_alert = "✅ Тривога закрита" if air_status != "active" else "🔴 ТРИВОГА АКТИВНА!"
air_raid_time = air_raid.get("raion_changed", "")
# Extract HH:MM from datetime string like "2026-07-13 04:55:52" or "2026-07-13T04:55:52"
air_raid_time_display = "—:—"
if air_raid_time:
s = str(air_raid_time).replace("T", " ")
parts = s.split(" ")
if len(parts) 

## Related Articles

- [[Air raid comments]]
- [[── Translation helpers (moved from old adapters/noaa_swpc.py) ──]]
- [[airraid.py]]
- [[health advice.py]]
- [[Дайджест Аудит — Повний чек-лист помилок (2026-07-15)]]
