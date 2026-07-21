---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/content/folk_forecasts.py
ingested: 2026-07-20
sha256: e7f312c794a033050b6e9863a13c0da7f1d2dd71c790f6d3e0e7467a392559f4
blog_source: local:unknown
---
"""Folk weather forecasts pool — randomized proverbs."""
import random

FOLK_FORECASTS = [
    "🌿 Якщо ввечері вітерець — завтра буде світло",
    "🌿 Якщо зранку туман — буде дощ",
    "🌿 Ясно вранці — весь день буде добре",
    "🌿 Рання осінь — довга зима",
    "🌿 Весняні холоди — добрий урожай",
    "🌿 Дощ у четвер — до суботи перестане",
    "🌿 Яскраві зірки — буде холодно",
    "🌿 Косар у травні — урожай у жовтні",
]


def get_random() -> str:
    """Get a random folk forecast."""
    return random.choice(FOLK_FORECASTS)
