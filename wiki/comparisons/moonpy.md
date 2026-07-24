---
title: "moon.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - data
  - energy
  - library
---

# moon.py

> **Source:** local-weather-space-lunar-digestsrcadaptersmoonpy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/moon.py ingested: 2026-07-20 sha256: 64c46f7d443e89942525cc9fbc8325eb0995c70224016092ddf2fc6a4a92bca1 blog_source: lo...
> **Sources:**
>   - local-weather-space-lunar-digestsrcadaptersmoonpy-2026-07-20.md
> **Links:**
- [[airraid.py]]
- [[дайджест-аудит-повний-чек-лист-помилок-2026-07-15]]
- [[get-ready-for-the-powerful-css-border-shape-property]]
- [[translatex]]
- [[translatez]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/adapters/moon.py
ingested: 2026-07-20
sha256: 64c46f7d443e89942525cc9fbc8325eb0995c70224016092ddf2fc6a4a92bca1
blog_source: local:unknown
---
"""Moon phase adapter using astral library for accurate astronomical data."""
import math
from datetime import datetime, date
from zoneinfo import ZoneInfo
def _get_phase_name(age: float) -> str:
"""Get Ukrainian moon phase name from age in days (0-29.53)."""
synodic_month = 29.53058867
# Normalize to 0-29.53 range
age = age % synodic_month
if age float:
"""Calculate moon illumination percentage from age."""
synodic_month = 29.53058867
age = age % synodic_month
# Simple cosine approximation (accurate to ~2%)
phase_angle = (age / synodic_month) * 2 * math.pi
illumination = (1 - math.cos(phase_angle)) / 2 * 100
return round(max(0, min(100, illumination)), 1)
def _get_lunar_day(age: float) -> int:
"""Calculate lunar day (1-29) from moon age."""
synodic_month = 29.53058867
lunar_day = int(age) + 1
if lunar_day > 29:
lunar_day = 1
return lunar_day
def _get_zodiac_sign(age: float) -> str:
"""Get zodiac sign from moon age and sun's ecliptic longitude.
Moon advances ~12.2°/day through zodiac. On July 16, sun is at ~123° (Cancer).
At age 2.1 days, moon is ~25.6° past sun = ~148.6° = Leo.
"""
# Sun's ecliptic longitude approximation for any date
# J2000.0 epoch: Jan 1, 2000 at 12:00 UTC = JD 2451545.0
from datetime import date
import math
from astral.moon import julianday
jd = julianday(date.today())
# Sun's mean ecliptic longitude (simplified, accurate to ~1°)
T = (jd - 2451545.0) / 36525.0 # Julian centuries from J2000
sun_lon = (280.46646 + 36000.76983 * T + 0.0003032 * T * T) % 360
# Moon's elongation from sun (degrees)
elongation = age * (360.0 / 29.53058867)
# Moon's ecliptic longitude
moon_lon = (sun_lon + elongation) % 360
# Convert to zodiac sign
signs = [
(0, "♈️ Овен"), (30, "♉️ Телець"), (60, "♊️ Близнюки"),
(90, "♋️ Рак"), (120, "♌️ Лев"), (150, "♍️ Діва"),
(180, "♎️ Терези"), (210, "♏️ Скорпіон"), (240, "♐️ Стрілець"),
(270, "♑️ Козоріг"), (300, "♒️ Водолій"), (330, "♓️ Риби"),
]
sign = "♈️ Овен"
for threshold, s in reversed(signs):
if moon_lon >= threshold:
sign = s
break
return sign
def _get_lunar_symbol(lunar_day: int) -> str:
"""Get lunar day symbol from the traditional calendar table."""
symbols = {
1: "🪔 Світильник", 2: "🦈 Ріг достатку", 3: "🐆 Барс", 4: "🌳 Дерево Пізнання",
5: "🦄 Єдиноріг", 6: "🐦 Журавель", 7: "🐓 Жезл", 8: "🔥 Фенікс",
9: "🦇 Кажан", 10: "⛲️ Джерело", 11: "⚔️ Вогняний меч", 12: "❤️ Чаша Грааля",
13: "🎡 Колесо", 14: "📯 Труба", 15: "🐍 Змія", 16: "🕊 Голуб",
17: "🍇 Виноград", 18: "🪞 Дзеркало", 19: "🕷 Павук", 20: "🦅 Орел",
21: "🐎 Кінь", 22: "🐘 Ганеша", 23: "🐊 Крокодил", 24: "🐻 Ведмідь",
25: "🐢 Черепаха", 26: "🐸 Жаба", 27: "🔱 Тризуб", 28: "🪷 Лотос",
29: "🐙 Спрут", 30: "🦢 Лебідь",
}
return symbols.get(lunar_day, "🌙 —")
def _get_lunar_energy(lunar_day: int) -> str:
"""Get lunar day energy description from the traditio

## Summary

nal calendar table."""
energies = {
1: "Чиста, творча, пасивна", 2: "Сприятлива, накопичувальна",
3: "Активна, напориста, бойова", 4: "Подвійна, стабільна",
5: "Трансформаційна, динамічна", 6: "Спокійна, споглядальна",
7: "Творча, вербальна", 8: "Очищувальна, перехідна",
9: "Важка, ілюзорна, критична", 10: "Потужна, родова, будівнича",
11: "Найсильніша, некерована", 12: "М'яка, милосердна",
13: "Оновлювальна, циклічна", 14: "Заклична, рішуча",
15: "Астральна, спокуслива", 16: "Гармонійна, чиста, мирна",
17: "Святкова, радісна, вільна", 18: "Пасивна, віддзеркалювальна",
19: "Важка, небезпечна", 20: "Потужна, духовна",
21: "Активна, колективна", 22: "Мудра, інформаційна",
23: "Важка, руйнівна", 24: "Творча, заземлена",
25: "Повільна, споглядальна", 26: "Критична, марнославна",
27: "Інтуїтивна, містична", 28: "Світла, підсумкова",
29: "Найважча, тривожна", 30: "Гармонійна, підсумкова",
}
return energies.get(lunar_day, "—")
def _get_lunar_advice(lunar_day: int) -> str:
"""Get lunar day advice from the traditional calendar table."""
advices = {
1: "Плануйте майбутнє. Візуалізуйте мрії. Нові справи не починайте.",
2: "Набирайтеся знань. Закладайте фундамент проєктів. Проявляйте щедрість.",
3: "Дійте рішуче. Займіться спортом. Спрямуйте внутрішню агресію у роботу.",
4: "Аналізуйте інформацію. Робіть вибір зважено. Проведіть час із родиною.",
5: "Захищайте свої принципи. Вживайте корисну їжу. Сміливо змінюйте плани.",
6: "Слухайте інтуїцію. Уникайте поспіху та тиску. Займіться дихальними практиками.",
7: "Контролюйте слова. Говоріть правду. Сприятливий час для переговорів.",
8: "Прощайте образи. Починайте внутрішні зміни. Позбудьтеся непотребу.",
9: "Проявляйте обережність. Уникайте конфліктів та нових знайомств. Очищуйте думки.",
10: "Зміцнюйте родинні зв'язки. Починайте ремонт або будівництво. Відпочивайте активно.",
11: "Доводьте справи до кінця. Дійте обережно, контролюйте силу. Не лінуйтеся.",
12: "Допомагайте іншим. Даруйте подарунки. Уникайте егоїзму та сліз.",
13: "Навчайтеся, розплутуйте старі проблеми. Займіться омолодженням організму.",
14: "Починайте найважливіші справи місяця. Реагуйте на знаки. Не марнуйте час.",
15: "Тримайте емоції під контролем. Обмежуйте контакти. Боріться зі спокусами.",
16: "Відпочивайте від суєти. Дотримуйтеся спокою. Уникайте криків та агресії.",
17: "Святкуйте, спілкуйтеся, кохайте. Сприятливий час для шлюбу та творчості.",
18: "Спостерігайте за реакціями людей на вас. Аналізуйте свої помилки. Очищуйте шкіру.",
19: "Очищуйте дім вогнем. Прощайте борги. Не піддавайтеся чужому впливу.",
20: "Долайте сумніви. Приймайте важливі рішення. Дивіться на проблеми глобально.",
21: "Працюйте в команді. Будьте чесними та рішучими. Сприятливий день для подорожей.",
22: "Вивчайте нові науки. Діліться досвідом. Використовуйте отримані знання.",
23: "Захищайте свій простір. Завершуйте розпочате. Не починайте нових справ.",
24: "Займіться фізичною працею. Реалізуйте великі проєкти. Зміцнюйте здоров'я.",
25: "Усамітніться. Послухайте

## Related Articles

- [[airraid.py]]
- [[дайджест-аудит-повний-чек-лист-помилок-2026-07-15]]
- [[get-ready-for-the-powerful-css-border-shape-property]]
- [[translatex]]
- [[translatez]]
