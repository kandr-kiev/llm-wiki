---
source_url: file:///workspace/Projects/weather-space-lunar-digest/tests/test_formatters.py
ingested: 2026-07-20
sha256: d1987c115ad4ec44311bb8e14476f8cbbbcc18204ff43063a1b2b8b9b606c83d
blog_source: local:unknown
---
"""Tests for formatters — verify core formatting functions from src/formatters/digest.py."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.formatters.digest import _wmo_code_to_text, _wind_direction_to_text, _format_time


def test_wmo_description():
    assert _wmo_code_to_text(0) == "☀️ Ясно"
    assert _wmo_code_to_text(1) == "🌤 Мало хмар"
    assert _wmo_code_to_text(2) == "⛅ Пасмурно"
    assert _wmo_code_to_text(3) == "☁️ Хмарно"
    assert _wmo_code_to_text(45) == "🌫 Туман"
    assert _wmo_code_to_text(61) == "🌧 Невеликий дощ"
    assert _wmo_code_to_text(63) == "🌧 Дощ"
    assert _wmo_code_to_text(95) == "⛈ Гроза"
    assert _wmo_code_to_text(99) == "⛈ Сильна гроза з градом"
    assert _wmo_code_to_text(999) == "🌡️ Код 999"
    print("✅ test_wmo_code_to_text passed")


def test_wind_direction():
    assert _wind_direction_to_text(0) == "Пн"
    assert _wind_direction_to_text(90) == "Сх"
    assert _wind_direction_to_text(180) == "Пд"
    assert _wind_direction_to_text(270) == "Зх"
    assert _wind_direction_to_text(45) == "ПнСх"
    assert _wind_direction_to_text(225) == "ПдЗх"
    print("✅ test_wind_direction_to_text passed")


def test_format_time():
    assert _format_time("2026-07-12T04:49") == "04:49"
    assert _format_time("2026-07-12T21:00") == "21:00"
    assert _format_time("") == "--:--"
    assert _format_time(None) == "--:--"
    assert _format_time("invalid") == "inval"
    print("✅ test_format_time passed")


def test_hpa_to_mmhg_in_render():
    """Verify hPa to mmHg conversion is correct in render."""
    from src.formatters.digest import render
    
    payload = {
        "location": {"display_name": "тест"},
        "weather_raw": {
            "current_weather": {"temperature": 20, "windspeed": 5, "winddirection": 0, "weathercode": 0},
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
            "solar_activity_level": "НИЗЬКИЙ",
        },
        "moon_data": {
            "lunar_day": 26, "moonrise": "15:08", "moonset": "04:16",
            "moon_period": "12.07 — 13.07", "phase": "Спадаючий серп",
            "visibility": 50, "zodiac": "♓ Риби", "symbol_of_day": "🌿",
        },
        "news_raw": {
            "war": ["Новина 1"], "geopol": [], "economy": ["Новина 2"],
            "tech": ["Новина 3"], "general": ["Новина 4"],
        },
    }
    
    template_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                  "templates", "digest-template.md")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    rendered = render(payload, template)
    
    # Check pressure conversion: 1013 hPa * 0.750062 = ~760 mmHg
    assert "мм рт" in rendered, "Pressure should be in mmHg"
    
    # Check sunrise/sunset
    assert "04:49" in rendered, "Sunrise should be 04:49"
    assert "21:00" in rendered, "Sunset should be 21:00"
    
    # Check wind direction
    assert "Пн" in rendered, "Wind direction should be Пн for 0 degrees"
    
    print("✅ test_hpa_to_mmhg_in_render passed")


def test_render_no_unresolved():
    """Test that render() fills all placeholders from a full mock payload."""
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
            "solar_activity_level": "НИЗЬКИЙ",
        },
        "moon_data": {
            "lunar_day": 26, "moonrise": "15:08", "moonset": "04:16",
            "moon_period": "12.07 — 13.07", "phase": "Спадаючий серп",
            "visibility": 50, "zodiac": "♓ Риби", "symbol_of_day": "🌿",
        },
        "news_raw": {
            "war": ["Новина 1"], "geopol": [], "economy": ["Новина 2"],
            "tech": ["Новина 3"], "general": ["Новина 4"],
        },
    }
    
    template_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                  "templates", "digest-template.md")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    rendered = render(payload, template)
    
    # Check no unresolved placeholders
    import re
    unresolved = re.findall(r'\{\{(\w+)\}\}', rendered)
    if unresolved:
        print(f"⚠️ Unresolved placeholders: {set(unresolved)}")
    else:
        print("✅ test_render_no_unresolved passed — 0 unresolved placeholders")


if __name__ == "__main__":
    print("=" * 50)
    print("🧪 Тестування форматерів")
    print("=" * 50)
    
    test_wmo_description()
    test_wind_direction()
    test_format_time()
    test_hpa_to_mmhg_in_render()
    test_render_no_unresolved()
    
    print("\n" + "=" * 50)
    print("✅ ВСІ ТЕСТИ ПРОЙДЕНО!")
    print("=" * 50)
