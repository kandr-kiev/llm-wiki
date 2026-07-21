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
        elif temp < 10:
            return "Мороз такий, що навіть чайник мерзне. Не виходьте без шапки. ❄️"
        return "Погода під контролем, працюємо в штатному режимі. 🌤"
    
    if section == "chrono":
        # Аналізуємо дані хронології
        temp_morning = payload.get("weather_raw", {}).get("hourly", {}).get("temperature_2m", [])
        temp_day = payload.get("weather_raw", {}).get("daily", {}).get("temperature_2m_max", [20])[0]
        temp_min = payload.get("weather_raw", {}).get("daily", {}).get("temperature_2m_min", [10])[0]
        wind_gust = payload.get("weather_raw", {}).get("daily", {}).get("wind_gusts_10m_max", [5])[0]
        
        temp_range = temp_day - temp_min
        if temp_range > 10:
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
        
        if lunar_day <= 7:
            return "Місяць сьогодні як новий стартап — з ентузіазмом, але ще без досвіду. 🌙"
        elif lunar_day <= 14:
            return "Місяць сьогодні повний сил, як Java-розробник після кофеїну. 🌕"
        elif lunar_day <= 21:
            return "Місяць сьогодні як старий код — повільно, але з гідністю. 🌗"
        else:
            return "Місяць сьогодні як clean up — прибирає зайве, готує новий цикл. 🌑"
    
    if section == "space":
        kp = payload.get("space_raw", {}).get("kp", 2)
        if kp >= 5:
            return "Космос сьогодні злий, як клієнт у понеділок. 🚀"
        elif kp >= 3:
            return "Сонце сьогодні дещо активне, але без паніки. ☄️"
        return "Сонце сьогодні спокійне, працюємо. 🌌"
    
    if section == "news":
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
        elif weather_temp < 10:
            return "Мороз такий, що навіть чайник мерзне. ❄️"
        else:
            return "Добрий день! Нехай код компілюється з першого разу. ☕"
    
    return "Система працює стабільно."


def render(payload, template):
    """Main rendering function mapping payload keys to template placeholders."""
    
    # ── 1. Extract data safely ────────────────────────────────────────────
    weather = payload.get("weather_raw", {})
    air_raid = payload.get("air_raid_raw", {})
    space = payload.get("space_raw", {})
    news = payload.get("news_raw", {})
    moon = payload.get("moon_data", {})
    loc = payload.get("location", {})

    # ── 2. Parse weather data ─────────────────────────────────────────────
    cw = weather.get("current_weather", {})
    daily = weather.get("daily", {})
    hourly = weather.get("hourly", {})

    # Current weather
    current_temp = cw.get("temperature", 15)
    # Open-Meteo returns wind speed in km/h → convert to m/s (÷ 3.6)
    current_wind_speed_kmh = cw.get("windspeed", 0)
    current_wind_speed = current_wind_speed_kmh / 3.6 if current_wind_speed_kmh else 0
    current_wind_dir = cw.get("winddirection", 0)
    current_wind_dir_text = _wind_direction_to_text(current_wind_dir)
    current_condition = _wmo_code_to_text(cw.get("weathercode", 3))
    
    # Wind description — avoid "0.0 м/с" when wind is calm
    if current_wind_speed < 0.5:
        current_wind_desc = "Слабкий вітер"
    else:
        current_wind_desc = f"{current_wind_dir_text} {current_wind_speed:.1f} м/с"
    
    current_humidity = "—"
    current_pressure = "—"
    if hourly and "relative_humidity_2m" in hourly:
        idx = 0
        current_humidity = f"{hourly['relative_humidity_2m'][idx]}%"
    if daily and "pressure_msl_min" in daily and "pressure_msl_max" in daily:
        p_min = daily["pressure_msl_min"][0]
        p_max = daily["pressure_msl_max"][0]
        # hPa to mmHg: 1 hPa = 0.750062 mmHg
        p_min_mmhg = p_min * 0.750062
        p_max_mmhg = p_max * 0.750062
        current_pressure = f"{p_min_mmhg:.0f}–{p_max_mmhg:.0f} мм рт. ст."

    # Daily ranges
    temp_max = daily.get("temperature_2m_max", [20])[0] if daily.get("temperature_2m_max") else 20
    temp_min = daily.get("temperature_2m_min", [10])[0] if daily.get("temperature_2m_min") else 10
    app_max = daily.get("apparent_temperature_max", [20])[0] if daily.get("apparent_temperature_max") else 20
    app_min = daily.get("apparent_temperature_min", [10])[0] if daily.get("apparent_temperature_min") else 10
    # Open-Meteo wind_gusts_10m_max is in km/h → convert to m/s
    wind_gust_kmh = daily.get("wind_gusts_10m_max", [5])[0] if daily.get("wind_gusts_10m_max") else 5
    wind_gust = wind_gust_kmh / 3.6 if wind_gust_kmh else 0
    precip = daily.get("precipitation_sum", [0])[0] if daily.get("precipitation_sum") else 0
    precip_prob = daily.get("precipitation_probability_max", [0])[0] if daily.get("precipitation_probability_max") else 0
    humidity_max = daily.get("relative_humidity_2m_max", [60])[0] if daily.get("relative_humidity_2m_max") else 60
    humidity_min = daily.get("relative_humidity_2m_min", [40])[0] if daily.get("relative_humidity_2m_min") else 40
    cloudiness = daily.get("cloudcover_max", [50])[0] if daily.get("cloudcover_max") else 50
    sunrise = _format_time(daily.get("sunrise", [""])[0]) if daily.get("sunrise") else "--:--"
    sunset = _format_time(daily.get("sunset", [""])[0]) if daily.get("sunset") else "--:--"

    # Chronology blocks — use ONLY first day (24h) for morning/day/evening
    # For night (22-6): use 22-23 from day 1 + 0-6 from day 2
    all_times = hourly.get("time", [])
    all_temps = hourly.get("temperature_2m", [])
    all_codes = hourly.get("weather_code", [])
    all_hums = hourly.get("relative_humidity_2m", [])
    all_winds = hourly.get("wind_speed_10m", [])
    all_wind_dirs = hourly.get("wind_direction_10m", [])
    
    # Day 1: hours 0-23
    today_times = all_times[:24]
    today_temps = all_temps[:24]
    today_codes = all_codes[:24]
    today_hums = all_hums[:24]
    today_winds = all_winds[:24]
    today_wind_dirs = all_wind_dirs[:24]
    
    # Day 2: first 7 hours (00-06) for night block
    tomorrow_times = all_times[24:31]
    tomorrow_temps = all_temps[24:31]
    tomorrow_codes = all_codes[24:31]
    tomorrow_hums = all_hums[24:31]
    tomorrow_winds = all_winds[24:31]
    tomorrow_wind_dirs = all_wind_dirs[24:31]

    def _get_temp_range_single(start_h, end_h, t_times, t_temps):
        """Get min/max temp for a single time range."""
        temps = []
        for i, t in enumerate(t_times):
            try:
                hour = int(t.split("T")[1][:2])
                if start_h <= hour < end_h and i < len(t_temps):
                    temps.append(t_temps[i])
            except (IndexError, ValueError):
                pass
        if temps:
            return f"+{min(temps):.0f}° / +{max(temps):.0f}°"
        return f"+{temp_min:.0f}° / +{temp_max:.0f}°"

    def _get_temp_range_night():
        """Get min/max temp for night (22-6): 22-23 day1 + 0-6 day2."""
        t1 = _get_temp_range_single(22, 24, today_times, today_temps)
        t2 = _get_temp_range_single(0, 7, tomorrow_times, tomorrow_temps)
        all_temps = []
        for p in (t1, t2):
            nums = [float(x) for x in p.replace("°", "").split("/") if x.strip().lstrip("+-").replace(".", "").isdigit()]
            all_temps.extend(nums)
        if all_temps:
            return f"+{min(all_temps):.0f}° / +{max(all_temps):.0f}°"
        return f"+{temp_min:.0f}° / +{temp_max:.0f}°"

    # Category groups for transition detection
    CLEAR_CODES = {0, 1}        # Сонячно/Мінлива хмарність
    CLOUDY_CODES = {2, 3}       # Переважно хмарно, Хмарно
    RAIN_CODES = {51, 53, 55, 61, 63, 65}  # Невеликий дощ, Дощ
    STORM_CODES = {95, 96, 99}  # Гроза
    FOG_CODES = {45, 48}        # Туман, Сильний туман
    SNOW_CODES = {71, 73, 75}   # Дощ зі снігом, Сніг, Снігопад
    DRIZZLE_CODES = {51, 53, 55, 61}  # Невеликий дощ
    HEAVY_RAIN_CODES = {63, 65}  # Дощ
    DOWNPOUR_CODES = {80, 81, 82}  # Злива

    def _detect_transition(codes_list, is_night=False):
        """Detect weather transitions in a time-ordered list of codes.
        Returns (text, has_storm).
        
        Rules:
        - Single category → dominant name, no suffix
        - Improvement (worse→better):
            - rain→clear: "Невеликий дощ"
            - clear/cloudy→clear: "Початкова + з проясненнями"
            - anything→cloudy: "Хмарно" / "Хмарно з дощем" / "Хмарно зі снігом"
        - Deterioration (better→worse):
            - anything→snow: "Початкова + зі снігом"
            - anything→rain/downpour: "Початкова + з дощем"
            - anything→storm: "Початкова + з грозою"
            - anything→fog: "Початкова + з туманом"
            - anything→clear/cloudy: "Кінцева" напряму
        - Mixed (same quality level) → dominant name, no suffix
        """
        if not codes_list:
            return "—", False

        has_storm = any(c in STORM_CODES for c in codes_list)

        # Categorize all codes
        categories = set()
        for c in codes_list:
            if c in CLEAR_CODES:
                categories.add("clear")
            elif c in CLOUDY_CODES:
                categories.add("cloudy")
            elif c in RAIN_CODES:
                categories.add("rain")
            elif c in STORM_CODES:
                categories.add("storm")
            elif c in FOG_CODES:
                categories.add("fog")
            elif c in SNOW_CODES:
                categories.add("snow")
            elif c in DOWNPOUR_CODES:
                categories.add("downpour")
            else:
                categories.add("other")

        # Single category = no transition
        if len(categories) <= 1:
            most_common = Counter(codes_list).most_common(1)[0][0]
            return _wmo_code_to_text(most_common, is_night), has_storm

        # Quality order (low = good, high = bad)
        quality = {
            "clear": 0,
            "cloudy": 1,
            "fog": 2,
            "rain": 3,
            "downpour": 4,
            "snow": 5,
            "storm": 6,
        }

        first = codes_list[0]
        last = codes_list[-1]

        # Determine first/last category
        def _cat(code):
            if code in CLEAR_CODES: return "clear"
            if code in CLOUDY_CODES: return "cloudy"
            if code in RAIN_CODES: return "rain"
            if code in STORM_CODES: return "storm"
            if code in FOG_CODES: return "fog"
            if code in SNOW_CODES: return "snow"
            if code in DOWNPOUR_CODES: return "downpour"
            return "other"

        first_cat = _cat(first)
        last_cat = _cat(last)
        first_q = quality.get(first_cat, 99)
        last_q = quality.get(last_cat, 99)

        # Helper: get the name of a category (canonical name)
        def _cat_name(cat):
            if cat == "clear": return "Сонячно"
            if cat == "cloudy": return "Хмарно"
            if cat == "rain": return "Дощ"
            if cat == "storm": return "Гроза"
            if cat == "fog": return "Туман"
            if cat == "snow": return "Сніг"
            if cat == "downpour": return "Злива"
            return "—"

        # Helper: suffix for a category (used in transitions)
        def _transition_suffix(cat):
            if cat == "snow": return "зі снігом"
            if cat in ("rain", "downpour"): return "з дощем"
            if cat == "storm": return "з грозою"
            if cat == "fog": return "з туманом"
            return ""

        # Determine if improvement or deterioration
        if last_q < first_q:
            # Improvement: worse → better
            if last_cat == "clear":
                # Special: rain → clear → "Невеликий дощ"
                if first_cat == "rain":
                    return "Невеликий дощ", has_storm
                # For clear→clear: use first code's name + "з проясненнями"
                if first_cat == "clear":
                    base = _wmo_code_to_text(first, is_night)
                    return f"{base} з проясненнями", has_storm
                # Otherwise: canonical name + "з проясненнями"
                return f"{_cat_name(first_cat)} з проясненнями", has_storm
            elif last_cat == "cloudy":
                # "Кінцева + суфікс початкової" (напр. "Хмарно з дощем")
                suffix = _transition_suffix(first_cat)
                if suffix:
                    return f"{_cat_name(last_cat)} {suffix}", has_storm
                return _cat_name(last_cat), has_storm
            else:
                # Fallback: "Початкова + з проясненнями"
                return f"{_cat_name(first_cat)} з проясненнями", has_storm

        elif last_q > first_q:
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
                if start_h <= hour < end_h and i < len(t_codes):
                    codes.append(t_codes[i])
            except (IndexError, ValueError):
                pass
        if codes:
            text, _ = _detect_transition(codes)
            return text
        return "—"

    def _get_condition_night():
        """Get dominant weather code for night (22-6): 22-23 day1 + 0-6 day2."""
        all_night_codes = []
        for i, t in enumerate(today_times):
            try:
                hour = int(t.split("T")[1][:2])
                if 22 <= hour < 24 and i < len(today_codes):
                    all_night_codes.append(today_codes[i])
            except:
                pass
        for i, t in enumerate(tomorrow_times):
            try:
                hour = int(t.split("T")[1][:2])
                if 0 <= hour < 7 and i < len(tomorrow_codes):
                    all_night_codes.append(tomorrow_codes[i])
            except:
                pass
        if all_night_codes:
            text, _ = _detect_transition(all_night_codes, is_night=True)
            return text
        return "—"

    def _get_has_storm(start_h, end_h, t_times, t_codes):
        """Check if thunderstorm occurs in a time range."""
        for i, t in enumerate(t_times):
            try:
                hour = int(t.split("T")[1][:2])
                if start_h <= hour < end_h and i < len(t_codes):
                    if t_codes[i] in STORM_CODES:
                        return True
            except:
                pass
        return False

    def _get_wind_single(start_h, end_h, t_times, t_speeds):
        """Get wind speed range for a single time range. km/h → m/s (÷ 3.6)."""
        speeds = []
        for i, t in enumerate(t_times):
            try:
                hour = int(t.split("T")[1][:2])
                if start_h <= hour < end_h and i < len(t_speeds):
                    speeds.append(t_speeds[i] / 3.6)
            except (IndexError, ValueError):
                pass
        if speeds:
            return f"{min(speeds):.1f}–{max(speeds):.1f} м/с"
        return "—"

    def _get_wind_night():
        """Get wind speed range for night (22-6): 22-23 day1 + 0-6 day2."""
        w1 = _get_wind_single(22, 24, today_times, today_winds)
        w2 = _get_wind_single(0, 7, tomorrow_times, tomorrow_winds)
        return w1 if w1 != "—" else w2

    def _get_humidity_single(start_h, end_h, t_times, t_hums):
        """Get humidity range for a single time range."""
        hums = []
        for i, t in enumerate(t_times):
            try:
                hour = int(t.split("T")[1][:2])
                if start_h <= hour < end_h and i < len(t_hums):
                    hums.append(t_hums[i])
            except (IndexError, ValueError):
                pass
        if hums:
            return f"{min(hums)}–{max(hums)}%"
        return "—"

    def _get_humidity_night():
        """Get humidity range for night (22-6): 22-23 day1 + 0-6 day2."""
        h1 = _get_humidity_single(22, 24, today_times, today_hums)
        h2 = _get_humidity_single(0, 7, tomorrow_times, tomorrow_hums)
        return h1 if h1 != "—" else h2

    def _get_wind_dir_single(start_h, end_h, t_times, t_dirs):
        """Get dominant wind direction for a single time range."""
        dirs = []
        for i, t in enumerate(t_times):
            try:
                hour = int(t.split("T")[1][:2])
                if start_h <= hour < end_h and i < len(t_dirs):
                    dirs.append(t_dirs[i])
            except (IndexError, ValueError):
                pass
        if dirs:
            from collections import Counter
            most_common = Counter(dirs).most_common(1)[0][0]
            return _wind_direction_to_text(most_common)
        return current_wind_dir_text

    def _get_wind_dir_night():
        """Get dominant wind direction for night (22-6): 22-23 day1 + 0-6 day2."""
        d1 = _get_wind_dir_single(22, 24, today_times, today_wind_dirs)
        d2 = _get_wind_dir_single(0, 7, tomorrow_times, tomorrow_wind_dirs)
        return d1 if d1 != current_wind_dir_text else d2

    morning_block = f"{_get_temp_range_single(5, 9, today_times, today_temps)}, {_get_condition_single(5, 9, today_times, today_codes)}, вітер {_get_wind_dir_single(5, 9, today_times, today_wind_dirs)} {_get_wind_single(5, 9, today_times, today_winds)}, вологість {_get_humidity_single(5, 9, today_times, today_hums)}"
    day_block = f"{_get_temp_range_single(10, 17, today_times, today_temps)}, {_get_condition_single(10, 17, today_times, today_codes)}, вітер {_get_wind_dir_single(10, 17, today_times, today_wind_dirs)} {_get_wind_single(10, 17, today_times, today_winds)}, вологість {_get_humidity_single(10, 17, today_times, today_hums)}"
    evening_block = f"{_get_temp_range_single(17, 21, today_times, today_temps)}, {_get_condition_single(17, 21, today_times, today_codes)}, вітер {_get_wind_dir_single(17, 21, today_times, today_wind_dirs)} {_get_wind_single(17, 21, today_times, today_winds)}, вологість {_get_humidity_single(17, 21, today_times, today_hums)}"
    night_block = f"{_get_temp_range_night()}, {_get_condition_night()}, вітер {_get_wind_dir_night()} {_get_wind_night()}, вологість {_get_humidity_night()}"

    # Thunderstorm warnings
    storm_morning = _get_has_storm(5, 9, today_times, today_codes)
    storm_day = _get_has_storm(10, 17, today_times, today_codes)
    storm_evening = _get_has_storm(17, 21, today_times, today_codes)
    storm_night = _get_has_storm(22, 24, today_times, today_codes) or _get_has_storm(0, 7, tomorrow_times, tomorrow_codes)
    storm_any = storm_morning or storm_day or storm_evening or storm_night
    storm_warning = "⚠️ ⚡️ **Грозова небезпека!** Очікується гроза протягом доби. Уникайте відкритих просторів, дерев, металевих конструкцій." if storm_any else ""

    # Folk forecast (simple rule-based, elif chain)
    if cloudiness < 30:
        folk_forecast = "🌿 Народний прогноз: \"Ясно вранці — весь день буде добре\""
    elif precip > 5:
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
        if len(parts) >= 2:
            time_part = parts[1][:5]  # "04:55:52" → "04:55"
            air_raid_time_display = time_part
        else:
            air_raid_time_display = s[:5]
    air_raid_raion = air_raid.get("raion", "Чернігівський район")
    air_raid_previous = ""
    prev_alerts = air_raid.get("previous_alerts", [])
    if prev_alerts:
        for pa in prev_alerts[:3]:
            air_raid_previous += f"🔹 {pa.get('time', '—')} — {pa.get('district', '—')} ({pa.get('status', '—')})\n"
    air_raid_today_stats = f"{air_raid.get('today_count', 0)} тривог, сумарно ~{air_raid.get('today_duration_min', 0)} хв."
    # Use "Немає" if previous alerts are empty
    air_raid_previous_display = air_raid_previous.strip() if air_raid_previous.strip() else "Немає попередніх сповіщень"

    # Air raid HTML helpers
    air_raid_color = "#f85149" if air_status == "active" else "#3fb950"
    air_raid_previous_html = ""
    if air_raid_previous.strip():
        air_raid_previous_html = f'    <div style="margin-top: 6px; font-size: 12px; color: #6e7681;">📊 Попередні: {air_raid_previous.strip().replace(chr(10), "<br>")}</div>\n'
    else:
        air_raid_previous_html = '    <div style="margin-top: 6px; font-size: 12px; color: #6e7681;">📊 Попередні: Немає попередніх сповіщень</div>\n'

    # ── 4. Parse space data ───────────────────────────────────────────────
    space_kp = space.get("kp", 2)
    # Space events - translate English fragments
    space_events_text = space.get("events", "🔺 Немає значних подій")
    # Replace common English phrases with Ukrainian
    space_events_text = space_events_text.replace("to the arrival of a CME that left the Sun on", "Прибуття CME, що вийшла з Сонця")
    space_events_text = space_events_text.replace("to the arrival of a CME", "Прибуття CME (короткохвильової бурі)")
    space_events_text = space_events_text.replace("CME that left the Sun", "CME, що вийшла з Сонця")
    space_events_text = space_events_text.replace("💥", "☄️")
    if not any(c in space_events_text for c in "абвгдежзийклмнопрстуфхцчшщъыьєіїґ"):
        space_events_text = "🔺 Немає значних подій"

    space_forecast = space.get("forecast", "🔮 Прогноз: стабільно.")
    space_solar_level = space.get("solar_activity_level", "Нормальний")

    # Space events_detail - strip leading whitespace
    space_events_detail = space.get("events_detail", "🔺 Немає значних подій")
    if space_events_detail:
        space_events_detail = space_events_detail.strip()
    else:
        space_events_detail = "🔺 Немає значних подій"

    # Space forecast — translate English rationale, strip any "Прогноз:" prefix
    space_forecast_raw = space.get("forecast", "стабільно.")
    space_forecast = space_forecast_raw.replace("🔮 Прогноз: ", "").replace("Прогноз: ", "")
    space_solar_level = space.get("solar_activity_level", "Невідомо")

    # Space health impact — детальний список категорій
    if space_kp >= 5:
        space_health = (
            "🔹 Загальний стан: ⚠️ Магнітна буря — головний біль, тиск, безсоння\n"
            "🔹 Серцеві хворі: моніторинг тиску, уникати навантажень\n"
            "🔹 Люди з мігренями: можливі сильні симптоми\n"
            "🔹 Вагітні: уникати перевантажень, більше відпочивати\n"
            "🔹 Діти та літні: обмежити час біля електроніки"
        )
    elif space_kp >= 3:
        space_health = (
            "🔹 Загальний стан: чутливі особи можуть відчувати легку втому\n"
            "🔹 Серцеві хворі: моніторинг тиску\n"
            "🔹 Люди з мігренями: можливі симптоми\n"
            "🔹 Вагітні: уникати перевантажень\n"
            "🔹 Діти та літні: обмежити час біля електроніки"
        )
    else:
        space_health = (
            "🔹 Загальний стан: норма\n"
            "🔹 Серцеві хворі: без змін\n"
            "🔹 Люди з мігренями: без змін\n"
            "🔹 Вагітні: без змін\n"
            "🔹 Діти та літні: без змін"
        )

    # Space tech impact — динамічний на основі Kp
    if space_kp >= 5:
        space_tech = (
            "📡 Радіозв'язок: переривчасті завади HF\n"
            "📻 HF: деградація сигналу\n"
            "🛰 Супутники: підвищене зарядження\n"
            "🛩 БПЛА/дрони: можливі збої GPS\n"
            "⚡️ Енергосистеми: можливі корективи"
        )
    elif space_kp >= 3:
        space_tech = (
            "📡 Радіозв'язок: можливі мікроперерви\n"
            "📻 HF: незначна деградація\n"
            "🛰 Супутники: стабільні\n"
            "🛩 БПЛА/дрони: без збоїв\n"
            "⚡️ Енергосистеми: стабільні"
        )
    else:
        space_tech = (
            "📡 Радіозв'язок: стабільний\n"
            "📻 HF: норма\n"
            "🛰 Супутники: стабільні\n"
            "🛩 БПЛА/дрони: без збоїв\n"
            "⚡️ Енергосистеми: стабільні"
        )

    # ── 5. Parse moon data ────────────────────────────────────────────────
    moon_day = moon.get("lunar_day", 26)
    moon_rise = moon.get("moonrise", "15:08")
    moon_set = moon.get("moonset", "04:16")
    moon_period = moon.get("moon_period", "—")
    moon_phase = moon.get("phase", "—")
    moon_visibility = moon.get("visibility", 50)
    moon_zodiac = moon.get("zodiac", "—")
    moon_symbol = moon.get("symbol_of_day", "—")
    moon_energy = moon.get("energy_of_day", "—")
    moon_advice = moon.get("advice_of_day", "—")

    # Moon planning — НЕ включає "Період" (шаблон вже має {{moon_period}})
    moon_planning = f"🌗 Фаза: {moon_phase} ({moon_visibility}% видимості)\n🌟 Зодіак: {moon_zodiac}\n🔮 Символ дня: {moon_symbol}\n⚡ Енергетика: {moon_energy}\n\n💡 Порада на добу: {moon_advice}\n\n📋 Рекомендації\n"
    if moon_day >= 22:
        moon_planning += "🌿 Сад і город: ⚠️ Період спокою — обрізання, прополка\n"
        moon_planning += "🎨 Творчість: ⚠️ Спостереження та аналіз\n"
        moon_planning += "💻 Технічні справи: ⚠️ Рефакторинг, тестування, налаштування\n"
        moon_planning += "⛔ Зайві зобов'язання\n"
    elif moon_day >= 14:
        moon_planning += "🌿 Сад і город: ✅ Посадка коренеплодів, збирання врожаю\n"
        moon_planning += "🎨 Творчість: ✅ Активна робота\n"
        moon_planning += "💻 Технічні справи: ✅ Впровадження змін\n"
    elif moon_day >= 7:
        moon_planning += "🌿 Сад і город: ✅ Посадка листяних культур, полив\n"
        moon_planning += "🎨 Творчість: ✅ Генерация ідей\n"
        moon_planning += "💻 Технічні справи: ✅ Розробка, планування\n"
    else:
        moon_planning += "🌿 Сад і город: ✅ Посадка насіння, коренеплодів\n"
        moon_planning += "🎨 Творчість: ✅ Планування, підготовка\n"
        moon_planning += "💻 Технічні справи: ✅ Аналіз, рефакторинг\n"

    # ── 6. Format news data ────────────────────────────────────────────────
    from src.services.news import format_news_sections as _format_news_sections
    news_sections = _format_news_sections(news)

    # ── 7. Generate Monty comments ────────────────────────────────────────
    monty_alert = _get_monty_comment("alert", payload)
    monty_weather = _get_monty_comment("weather", payload)
    monty_chrono = _get_monty_comment("chrono", payload)
    monty_moon = _get_monty_comment("moon", payload)
    monty_space = _get_monty_comment("space", payload)
    monty_news = _get_monty_comment("news", payload)
    monty_closing = _get_monty_comment("closing", payload)

    # Anecdote — случайний з пулу
    from src.content.anecdotes import get_random as get_anecdote
    anecdote = f"{get_anecdote()} 🤖"

    # ── 8. Build replacement dictionary ───────────────────────────────────
    loc_text = loc.get("display_name", "с. Крехаїв, Чернігівська область, Чернігівський район")
    now = datetime.now(ZoneInfo("Europe/Kiev"))
    days_uk = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
    months_uk = ["січня", "лютого", "березня", "квітня", "травня", "червня",
                 "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"]
    full_date = f"{now.day} {months_uk[now.month - 1]} {now.year}, {days_uk[now.weekday()]}"
    time_str = now.strftime("%H:%M")

    # Notes — динамічні дані з API
    # Водії: залежно від погоди (дощ, туман, сніг, вітер)
    if precip > 5:
        notes_drivers = "Дороги слизькі через дощ. Знизь швидкість і збільш дистанцію."
    elif cloudiness > 80 and current_condition == "Туман":
        notes_drivers = "Туман — видимість погана. Увімкни протитуманні фари."
    elif wind_gust > 15:
        notes_drivers = f"Сильний вітер ({wind_gust:.0f} м/с). Обережно з високими транспортними засобами."
    else:
        notes_drivers = "Дороги у штатному стані. Увага — завжди."
    
    # Військові: залежно від статусу тривоги
    if air_status == "active":
        notes_military = "ТРИВОГА АКТИВНА! Перевірте укриття, евакуаційні маршрути, зв'язок."
    elif air_raid.get("today_count", 0) > 5:
        notes_military = f"Сьогодні {air_raid.get('today_count', 0)} тривог — будьте пильні."
    else:
        notes_military = "Статус спокійний. Але тримайте вухо вострі."
    
    # Супутниковий зв'язок: залежно від Kp-індексу
    if space_kp >= 5:
        notes_satellite = f"Kp-індекс {space_kp:.1f} — магнітна буря! Супутниковий зв'язок може бути нестабільним."
    elif space_kp >= 3:
        notes_satellite = "Космічна активність середня — зв'язок стабільний, але можливі мікроперерви."
    else:
        notes_satellite = "Спокійний космос — супутниковий зв'язок стабільний."
    
    # Аграрії: залежно від фази місяця
    if moon_day >= 1 and moon_day <= 7:
        notes_farmers = "Молодий місяць — ідеально для посіву коренеплодів та бобових. Земля вбирає вологу."
    elif moon_day >= 8 and moon_day <= 14:
        notes_farmers = "Повний місяць — час для посадки листяних культур, поливу та підживлення."
    elif moon_day >= 15 and moon_day <= 21:
        notes_farmers = "Спадаючий місяць — збирай врожай, обрізуй дерева. Сік йде в коріння."
    else:
        notes_farmers = "Темний місяць — період спокою. Обробіть ґрунт, готуйте інвентар."
    
    # Туристи: залежно від UV та погоди
    uv = daily.get("uv_index_max", [5])[0] if daily.get("uv_index_max") else 5
    if uv >= 8:
        notes_tourists = f"🔥 UV-індекс {uv:.0f} (екстремальний)! Крем SPF 50+, головний убір, не на сонці 11-15."
    elif uv >= 5:
        notes_tourists = f"☀️ UV-індекс {uv:.0f} (високий). Крем SPF 30+, окуляри — до опіків далеко."
    elif storm_any:
        notes_tourists = "⛈ Грози очікуються! Уникай відкритих просторів, дерев, водойм."
    else:
        notes_tourists = "🌤 Погода підходить для прогулянок. Гарного дня!"
    
    # Медичні: залежно від тиску та Kp
    if space_kp >= 5:
        notes_medical = "⚠️ Магнітна буря (Kp≥5). Серцевикам — моніторинг тиску, літнім — обмежити навантаження."
    elif space_kp >= 3:
        notes_medical = "🔹 Помірний космічний вплив. Чутливим особам — більше відпочивати, пити воду."
    else:
        notes_medical = "✅ Космічна погода спокійна. Медичних обмежень немає."

    data = {
        # Meta
        "date_full": full_date,
        "scout_time": time_str,
        "location_text": loc_text,

        # Air Raid
        "air_raid_alert": air_raid_alert,
        "air_raid_time_display": air_raid_time_display,
        "air_raid_raion": air_raid_raion,
        "air_raid_previous": air_raid_previous_display,
        "air_raid_today_stats": air_raid_today_stats,
        "air_raid_color": air_raid_color,
        "air_raid_previous_html": air_raid_previous_html,
        "monty_alert_comment": monty_alert,

        # Weather
        "weather_condition": f"{current_condition}, {current_wind_desc}",
        "weather_temp_range": f"+{temp_min:.0f}° / +{temp_max:.0f}°",
        "weather_apparent_range": f"+{app_min:.0f}° / +{app_max:.0f}°",
        "weather_wind_desc": current_wind_desc,
        "weather_wind_gust": f"{wind_gust:.1f} м/с",
        "weather_pressure_range": current_pressure,
        "weather_precip": f"{precip:.1f} мм (ймов. до {precip_prob}%)",
        "weather_humidity_range": f"{humidity_min}–{humidity_max}%",
        "weather_cloudiness": f"{cloudiness}%",
        "weather_sunrise": sunrise,
        "weather_sunset": sunset,
        "weather_morning_block": morning_block,
        "weather_day_block": day_block,
        "weather_evening_block": evening_block,
        "weather_night_block": night_block,
        "folk_forecast": folk_forecast,
        "storm_warning": storm_warning,
        "monty_weather_comment": monty_weather,
        "monty_chrono_comment": monty_chrono,

        # Moon
        "moon_day": str(moon_day),
        "moon_period": moon_period,
        "moon_rise": moon_rise,
        "moon_set": moon_set,
        "moon_planning": moon_planning.strip(),
        "moon_energy": moon_energy,
        "moon_advice": moon_advice,
        "monty_moon_comment": monty_moon,

        # Space
        "space_kp_index": f"{space_kp:.2f} — {'ПОМІРНА 🟠' if space_kp >= 5 else 'МІНІМАЛЬНА 🟢' if space_kp < 3 else 'СЕРЕДНЯ 🟡'}",
        "space_events_detail": space_events_text,
        "space_forecast": space_forecast,
        "space_health_groups": space_health,
        "space_tech_detailed": space_tech,
        "monty_space_comment": monty_space,

        # News
        "news_sections": news_sections,
        "monty_news_comment": monty_news,

        # Notes — динамічні дані з API
        "notes_drivers": notes_drivers,
        "notes_military": notes_military,
        "notes_satellite": notes_satellite,
        "notes_farmers": notes_farmers,
        "notes_tourists": notes_tourists,
        "notes_medical": notes_medical,

        # Final
        "monty_anecdote": anecdote,
        "monty_final_closing": monty_closing
    }

    # ── 9. Template replacement ───────────────────────────────────────────
    result = template
    for key, value in data.items():
        placeholder = "{{" + key + "}}"
        result = result.replace(placeholder, str(value))

    # Check for unresolved placeholders
    import sys as _sys
    unresolved = []
    i = 0
    while True:
        start = result.find("{{", i)
        if start == -1:
            break
        end = result.find("}}", start + 2)
        if end == -1:
            break
        key = result[start+2:end].strip()
        if key and key.isidentifier():
            unresolved.append(key)
        i = end + 2
    if unresolved:
        print(f"[WARN] Unresolved placeholders: {set(unresolved)}", file=_sys.stderr)

    return result
