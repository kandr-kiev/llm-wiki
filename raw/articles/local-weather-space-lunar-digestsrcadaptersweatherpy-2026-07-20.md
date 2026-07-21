---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/weather.py
ingested: 2026-07-20
sha256: 987fda86c5e6614418ee2729c6a82b728d00c02fd4a3d135a67a610acb3d9c38
blog_source: local:unknown
---
"""Open-Meteo simplified adapter."""
from .http import http_get
import urllib.parse

def fetch_weather(lat, lon, tz="Europe/Kiev"):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
    url += f"&timezone={urllib.parse.quote(tz, safe='/')}"
    url += "&current_weather=true"
    url += "&daily=weather_code,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant,precipitation_sum,precipitation_probability_max,pressure_msl_max,pressure_msl_min,relative_humidity_2m_max,relative_humidity_2m_min,cloudcover_max"
    url += "&hourly=temperature_2m,relative_humidity_2m,pressure_msl,wind_speed_10m,wind_direction_10m,weather_code,cloudcover"
    url += "&forecast_days=3"
    return http_get(url)
