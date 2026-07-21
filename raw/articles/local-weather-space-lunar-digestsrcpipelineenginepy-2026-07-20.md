---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/pipeline/engine.py
ingested: 2026-07-20
sha256: 3fae2e5c6b3990378850aa739f81a4130459d6bde775fa62cbbcd2bb06f31e2e
blog_source: local:unknown
---
"""Pipeline engine — runs scout.py, then formats and renders the digest."""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))  # src/pipeline/ → src/ → корінь
TEMPLATE_PATH = os.path.join(ROOT_DIR, "templates", "digest-template.md")
HTML_TEMPLATE_PATH = os.path.join(ROOT_DIR, "src", "formatters", "html_template.html")
OUTPUT_MD_PATH = "/output/digest_output.md"
OUTPUT_HTML_PATH = "/output/digest_output.html"


def run_pipeline():
    """Run all services → format → write digest_output.md + digest_output.html."""
    # ── 1. Collect data from services ────────────────────────────────────
    from src.services.weather import get_weather_summary
    from src.services.space import fetch_space
    from src.services.news import fetch_news
    from src.services.airraid import fetch_air_raid
    from src.adapters.moon import get_moon_phase
    from datetime import datetime
    from zoneinfo import ZoneInfo

    LATITUDE = 47.1
    LONGITUDE = 31.5
    TIMEZONE = "Europe/Kiev"
    DEFAULT_LOCATION_TEXT = "с. Крехаїв, Чернігівська область, Чернігівський район"

    try:
        tz = ZoneInfo(TIMEZONE)
    except Exception:
        tz = datetime.timezone(datetime.timedelta(hours=3))

    location = {
        "query": DEFAULT_LOCATION_TEXT,
        "name": "Крехаїв",
        "display_name": DEFAULT_LOCATION_TEXT,
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "timezone": TIMEZONE,
        "country": "Україна",
        "country_code": "UA",
        "admin1": "Чернігівська область",
        "admin2": "Чернігівський район",
        "admin3": "",
        "source": "default_config",
        "is_default": True,
    }

    weather_raw = get_weather_summary(LATITUDE, LONGITUDE)
    air_raid_raw = fetch_air_raid(location.get("admin1", "Чернігівська область"))
    space_raw = fetch_space()
    moon_data = get_moon_phase()
    news_raw = fetch_news()

    payload = {
        "timestamp": datetime.now(tz).isoformat(),
        "location": location,
        "weather_raw": weather_raw,
        "air_raid_raw": air_raid_raw,
        "space_raw": space_raw,
        "moon_data": moon_data,
        "news_raw": news_raw,
    }

    # ── 2. Load templates ────────────────────────────────────────────────
    if not os.path.exists(TEMPLATE_PATH):
        print(f"[ERROR] Template not found at {TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    html_template = ""
    if os.path.exists(HTML_TEMPLATE_PATH):
        with open(HTML_TEMPLATE_PATH, "r", encoding="utf-8") as f:
            html_template = f.read()

    # ── 3. Render ────────────────────────────────────────────────────────
    from src.formatters.digest import render

    md_rendered = render(payload, template)

    html_rendered = ""
    if html_template:
        html_rendered = render(payload, html_template)

    # ── 4. Write output ──────────────────────────────────────────────────
    os.makedirs(os.path.dirname(OUTPUT_MD_PATH), exist_ok=True)
    with open(OUTPUT_MD_PATH, "w", encoding="utf-8") as f:
        f.write(md_rendered)
    print(f"[OK] Digest MD rendered: {len(md_rendered)} chars, {md_rendered.count(chr(10))} lines")

    if html_rendered:
        with open(OUTPUT_HTML_PATH, "w", encoding="utf-8") as f:
            f.write(html_rendered)
        print(f"[OK] Digest HTML rendered: {len(html_rendered)} chars")

    # ── 5. Check for unresolved placeholders ─────────────────────────────
    def _check_unresolved(text, label):
        unresolved = []
        i = 0
        while True:
            start = text.find("{{", i)
            if start == -1:
                break
            end = text.find("}}", start + 2)
            if end == -1:
                break
            key = text[start + 2:end].strip()
            if key and key.isidentifier():
                unresolved.append(key)
            i = end + 2
        if unresolved:
            print(f"[WARN] Unresolved placeholders in {label}: {set(unresolved)}", file=sys.stderr)
        return unresolved

    md_unresolved = _check_unresolved(md_rendered, "MD")
    if html_rendered:
        html_unresolved = _check_unresolved(html_rendered, "HTML")
        if set(md_unresolved) != set(html_unresolved):
            print("[INFO] MD and HTML have different unresolved placeholders")

    print("[OK] Pipeline complete")
    
    # ── 6. Return MD text for delivery (chunked if >4090 chars) ────────────
    TELEGRAM_LIMIT = 4090
    if len(md_rendered) <= TELEGRAM_LIMIT:
        chunks = [md_rendered]
    else:
        # Chunk by splitting on blank lines (double newline)
        chunks = []
        current = ""
        for line in md_rendered.split("\n"):
            if len(current) + len(line) + 1 > TELEGRAM_LIMIT and current.strip():
                chunks.append(current.strip())
                current = ""
            current += line + "\n"
        if current.strip():
            chunks.append(current.strip())
    
    return chunks


if __name__ == "__main__":
    chunks = run_pipeline()
    for i, chunk in enumerate(chunks, 1):
        print(chunk)
