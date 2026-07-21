---
title: "space.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - data
  - search
---

# space.py

> **Source:** local-weather-space-lunar-digestsrcservicesspacepy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/src/services/space.py ingested: 2026-07-20 sha256: 47b24ebc7f23c38491259dffecb3bc18a781c95f7c0d8fd82f26336c1f9dbb39 blog_source: l...
> **Sources:**
>   - local-weather-space-lunar-digestsrcservicesspacepy-2026-07-20.md
> **Links:**
- [[── Translation helpers (moved from old adapters/noaa_swpc.py) ──]]
- [[news.py]]
- [[airraid.py]]
- [[wiki.py]]
- [[digest.py]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/services/space.py
ingested: 2026-07-20
sha256: 47b24ebc7f23c38491259dffecb3bc18a781c95f7c0d8fd82f26336c1f9dbb39
blog_source: local:unknown
---
"""
Space weather service.
Цей модуль відповідає за отримання та обробку даних космічної погоди
від NOAA SWPC.
"""
import re
from src.adapters.noaa import fetch_forecast, _translate_forecast_line
def parse_space(raw: str) -> dict:
"""
Парсить сирий текст прогнозу NOAA та повертає структурований словник.
Args:
raw: Сирий текст прогнозу NOAA.
Returns:
Словник із ключами: 'kp', 'events', 'forecast', 'events_detail',
'solar_activity_level', 'solar_radiation', 'radio_blackout'.
"""
if not raw:
return {
"kp": 0,
"events": "Даних немає",
"forecast": "Даних немає",
"events_detail": "",
"solar_activity_level": "",
"solar_radiation": "",
"radio_blackout": "",
}
result = {
"kp": 0,
"events": "",
"forecast": "",
"events_detail": "",
"solar_activity_level": "",
"solar_radiation": "",
"radio_blackout": "",
}
# ── Kp-індекс ──
kp_match = re.search(r"greatest expected 3 hr Kp.*?is ([\d.]+)", raw, re.IGNORECASE)
if kp_match:
result["kp"] = float(kp_match.group(1))
# ── NOAA Scale levels ──
g1_match = re.search(r"No G1 \(Minor\).*?expected", raw, re.IGNORECASE)
if g1_match:
result["solar_activity_level"] = "Нормальний (немає магнітних бурь)"
else:
g1_match2 = re.search(r"G1 \(Minor\).*?expected", raw, re.IGNORECASE)
if g1_match2:
result["solar_activity_level"] = "Помірний (очікується G1 буря)"
else:
result["solar_activity_level"] = "Невідомо"
# ── Section A: Geomagnetic ──
section_a = _extract_section(raw, "A.")
if section_a:
rationale = _extract_rationale(section_a)
if rationale:
result["events"] = rationale
# ── Section B: Solar Radiation ──
section_b = _extract_section(raw, "B.")
if section_b:
# Extract S-class probabilities
s1_match = re.search(r"S1 or greater\s+(\d+)%\s+(\d+)%\s+(\d+)%", section_b)
if s1_match:
d1, d2, d3 = s1_match.groups()
# Dynamically generate dates based on forecast period
solar_rad = (
f"Прогноз сонячної радіаційної штормової активності\n"
f"S1 або вищий {d1}% {d2}% {d3}%"
)
result["solar_radiation"] = solar_rad
rationale = _extract_rationale(section_b)
if rationale:
result["solar_radiation"] += f"\n{rationale}"
# ── Section C: Radio Blackout ──
section_c = _extract_section(raw, "C.")
if section_c:
# Extract R1-R2 and R3 probabilities
r12_match = re.search(r"R1-R2\s+(\d+)%\s+(\d+)%\s+(\d+)%", section_c)
r3_match = re.search(r"R3 or greater\s+(\d+)%\s+(\d+)%\s+(\d+)%", section_c)
if r12_match and r3_match:
d1_12, d2_12, d3_12 = r12_match.groups()
d1_3, d2_3, d3_3 = r3_match.groups()
radio = (
f"Прогноз радіоперешкод\n"
f"R1-R2 {d1_12}% {d2_12}% {d3_12}%\n"
f"R3 або вищий {d1_3}% {d2_3}% {d3_3}%"
)
result["radio_blackout"] = radio
rationale = _extract_rationale(section_c)
if rationale:
result["radio_blackout"] += f"\n{rationale}"
# ── Events detail ──
detail_parts = []
if result["solar_radiation"]:
detail_parts.append(f"☀️ Со

## Summary

нячна радіація:\n{result['solar_radiation']}")
if result["radio_blackout"]:
detail_parts.append(f"📡 Радіоперешкоди:\n{result['radio_blackout']}")
if detail_parts:
result["events_detail"] = "\n\n".join(detail_parts)
else:
result["events_detail"] = "🔺 Немає значних подій"
# ── Forecast summary ──
if result["events"]:
result["forecast"] = result["events"]
else:
result["forecast"] = "Прогноз: стабільно."
return result
def _extract_section(text: str, section_marker: str) -> str:
"""Extract text between section marker and next section marker or end."""
start = text.find(section_marker)
if start == -1:
return ""
# Find next section (A., B., C., D., etc.)
next_section = text.find("\n\nA.", start + 1)
if next_section == -1:
next_section = text.find("\n\nB.", start + 1)
if next_section == -1:
next_section = text.find("\n\nC.", start + 1)
if next_section == -1:
next_section = text.find("\n\nD.", start + 1)
if next_section == -1:
return text[start:]
return text[start:next_section]
def _extract_rationale(text: str) -> str:
"""Extract rationale from a section and translate to Ukrainian."""
match = re.search(r"Rationale:\s*(.+?)(?:\n\n[A-Z]\.|$)", text, re.DOTALL)
if match:
rationale = match.group(1).strip()
# Clean up extra whitespace/newlines
rationale = re.sub(r'\s+', ' ', rationale).strip()
# Full English → Ukrainian translation map
translations = [
("below NOAA Scale levels", "нижче порогів шкали NOAA"),
("No significant transient or recurrent solar wind features are forecast.", "Значних транзєнтних або рекурентних сонячних вітрів не прогнозується."),
("No G1 (Minor) or greater geomagnetic storms are expected.", "Магнітних бурь рівня G1 (помірний) або вище не очікується."),
("No significant active region activity favorable for radiation storm production is forecast.", "Значної активності на активних областях, сприятливої для радіаційних штормів, не прогнозується."),
("A slight chance for M-class flaring (R1-R2/Minor-Moderate radio blackouts) exists due to Regions 4482 and 4489, alongside regions soon anticipated to rotate over the east limb.", "Можливе слабке спалахування M-класу (R1-R2/помірні-середні радіоперешкоди) через регіони 4482 та 4489, а також регіони, що скоро обернуться над східним краєм Сонця."),
("No radio blackouts were observed over the past 24 hours.", "Протягом останніх 24 годин радіоперешкод не спостерігалося."),
("Solar radiation, as observed by NOAA GOES-18 over the past 24 hours, was below S-scale storm level thresholds.", "Сонячна радіація, спостережена NOAA GOES-18 протягом останніх 24 годин, була нижче порогів штормового рівня S-шкали."),
("The greatest observed 3 hr Kp over the past 24 hours was", "Найбільший спостережуваний Kp за 3 години за останні 24 години становив"),
("The greatest expected 3 hr Kp for", "Найбільший очікуваний Kp за 3 години для"),
("No S1 (Minor) or greater solar radiation storms are expected.", "Сонячних радіаційних штормів рівня S1 (помірний) або вище не очікується."),
]
for eng, uk in translations:
ration

## Related Articles

- [[── Translation helpers (moved from old adapters/noaa_swpc.py) ──]]
- [[news.py]]
- [[airraid.py]]
- [[wiki.py]]
- [[digest.py]]
