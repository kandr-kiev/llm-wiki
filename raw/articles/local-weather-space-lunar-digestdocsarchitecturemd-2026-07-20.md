---
source_url: file:///workspace/Projects/weather-space-lunar-digest/docs/architecture.md
ingested: 2026-07-20
sha256: cd659d6245915558a3e2b2d8c547dc55562b434d12890ed1c0104e2806b3cf9a
blog_source: local:unknown
---
# Архітектура Weather-Space-Lunar-Digest

Проект переведено на модульну структуру для покращення підтримки та спрощення тестування.

## Структура
- `src/adapters/`: Низькорівнева взаємодія із зовнішніми API (HTTP, NOAA, Open-Meteo, RSS).
- `src/services/`: Бізнес-логіка (парсинг, класифікація, підготовка даних).
- `src/formatters/`: Генерація фінального Markdown-дайджесту.
- `src/pipeline/`: Оркестрація виконання дайджесту.
- `tests/`: Модульні тести (`pytest`).

## CLI
Точка входу: `python3 -m src.cli`
