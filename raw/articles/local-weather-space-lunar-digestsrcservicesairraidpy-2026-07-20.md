---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/services/airraid.py
ingested: 2026-07-20
sha256: b10987b0de3310cf68ee5cba8b032a81cf157b31c2f7c22e34c8271fe80dd946
blog_source: local:unknown
---
"""Air raid service — fetches and parses air raid alerts."""
from src.adapters.airraid import fetch_air_raid as _fetch_air_raid


def fetch_air_raid(region: str = "Чернігівська область") -> dict | None:
    """Fetch air raid alerts for the given region.
    
    Returns dict with status, districts, previous_alerts, etc.
    Returns None on failure.
    """
    return _fetch_air_raid(region)
