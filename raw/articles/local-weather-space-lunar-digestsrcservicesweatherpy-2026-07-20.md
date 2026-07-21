---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/services/weather.py
ingested: 2026-07-20
sha256: 9ae1fdfa357038368f548bd2307e1bf0ba98d9549ee3124e687909a4c387e3f6
blog_source: local:unknown
---
"""Weather service."""
from src.adapters.weather import fetch_weather
import json

def get_weather_summary(lat, lon):
    raw = fetch_weather(lat, lon)
    if not raw:
        return {
            "current_weather": {"temperature": 0, "weathercode": 0, "windspeed": 0, "winddirection": 0},
            "hourly": {},
            "daily": {}
        }
    try:
        data = json.loads(raw)
        current = data.get("current", {})
        hourly = data.get("hourly", {})
        daily = data.get("daily", {})
        return {
            "current_weather": current,
            "hourly": hourly,
            "daily": daily
        }
    except Exception as e:
        print(f"[WARN] Failed to parse weather data: {e}")
        return {
            "current_weather": {"temperature": 0, "weathercode": 0, "windspeed": 0, "winddirection": 0},
            "hourly": {},
            "daily": {}
        }
