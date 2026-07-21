---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/airraid.py
ingested: 2026-07-20
sha256: ae1cb289dfddcd1d349a78a1ef97f3f18f3a6f3275d9a90be119953e25dfda35
blog_source: local:unknown
---
"""Air raid alert adapter. Single job: fetch alerts from ubilling.net.ua raw API."""
from .http import http_get
import json


def fetch_air_raid(region: str = "Чернігівська область") -> dict | None:
    """Fetch air raid alerts from ubilling.net.ua raw mode.
    
    Returns dict with: status, cachedat, changed, districts, today_count, today_duration_min, previous_alerts, raion, region, source
    Returns None on failure.
    """
    url = "https://ubilling.net.ua/aerialalerts/?source=skog&raw"
    text = http_get(url, timeout=10)
    if not text:
        return None
    
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    
    raw = data.get("raw", {})
    
    # API тепер використовує числові ID замість назв областей
    # Мапінг: Чернігівська область = ID 24
    REGION_ID_MAP = {
        "Вінницька область": 1, "Волинська область": 2, "Дніпропетровська область": 3,
        "Донецька область": 4, "Житомирська область": 5, "Закарпатська область": 6,
        "Запорізька область": 7, "Івано-Франківська область": 8, "Київська область": 9,
        "Кіровоградська область": 10, "Луганська область": 11, "Львівська область": 12,
        "Миколаївська область": 13, "Одеська область": 14, "Полтавська область": 15,
        "Рівненська область": 16, "Сумська область": 17, "Тернопільська область": 18,
        "Харківська область": 19, "Херсонська область": 20, "Хмельницька область": 21,
        "Черкаська область": 22, "Чернівецька область": 23, "Чернігівська область": 24,
        "м. Київ": 25,
    }
    
    # Спочатку шукаємо за числовим ID
    target_id = REGION_ID_MAP.get(region)
    region_data = None
    if target_id is not None and str(target_id) in raw:
        region_data = raw[str(target_id)]
    
    # Якщо не знайшли — пробуємо зворотний пошук (ID → назва)
    if not region_data:
        for key, val in raw.items():
            if key.lstrip('-').isdigit():
                val_name = val.get("name", "")
                if region in val_name or val_name in region:
                    region_data = val
                    break
    
    # Якщо все ще не знайшли — пробуємо повне співпадіння з "область"
    if not region_data:
        for key, val in raw.items():
            if key.lstrip('-').isdigit():
                val_name = val.get("name", "")
                if val_name == region:
                    region_data = val
                    break
    
    if not region_data:
        return {
            "status": "not_applicable",
            "cachedat": None,
            "changed": None,
            "districts": [],
            "today_count": 0,
            "today_duration_min": 0,
            "previous_alerts": [],
            "raion": region,
            "region": region,
            "source": url,
        }
    
    # Normalize alert status
    raw_alert = region_data.get("alert", False)
    status = "active" if raw_alert in (True, 1, "yes", "так") else "stopped"
    
    # Normalize districts
    districts = []
    for d in region_data.get("districts", []):
        d_alert = d.get("alert", False)
        districts.append({
            "name": d.get("name", ""),
            "status": "active" if d_alert in (True, 1, "yes", "так") else "stopped",
            "changed": d.get("changed", ""),
        })
    
    # Previous alerts
    previous_alerts = []
    if region_data.get("previous_alerts"):
        for pa in region_data["previous_alerts"]:
            previous_alerts.append({
                "time": pa.get("time", ""),
                "district": pa.get("name", ""),
                "status": "active" if pa.get("alert", False) in (True, 1) else "stopped",
            })
    
    return {
        "status": status,
        "cachedat": region_data.get("changed", ""),
        "changed": region_data.get("changed", ""),
        "districts": districts,
        "today_count": region_data.get("today_count", 0),
        "today_duration_min": region_data.get("today_duration_min", 0),
        "previous_alerts": previous_alerts,
        # Шукаємо район з назвою "Чернігівський район", інакше — перший активний, інакше — перший
        "raion": _find_preferred_raion(districts, region),
        "raion_changed": _find_preferred_raion_changed(districts),
        "region": region_data.get("name", region),
        "source": url,
    }


def _find_preferred_raion(districts, fallback):
    """Вибрати район: спочатку 'Чернігівський район', потім перший активний, потім перший."""
    for d in districts:
        if "чернігівський" in d["name"].lower():
            return d["name"]
    for d in districts:
        if d["status"] == "active":
            return d["name"]
    return districts[0]["name"] if districts else fallback


def _find_preferred_raion_changed(districts):
    """Повернути час зміни для обраного району."""
    for d in districts:
        if "чернігівський" in d["name"].lower():
            return d.get("changed", "")
    for d in districts:
        if d["status"] == "active":
            return d.get("changed", "")
    return districts[0].get("changed", "") if districts else ""
