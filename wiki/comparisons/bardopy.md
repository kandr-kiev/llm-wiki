---
title: "bardo.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - computer-vision
  - self-supervised
  - system-design
---

# bardo.py

> **Source:** local-bezmezhzhiasrccorebardopy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/bezmezhzhia/src/core/bardo.py ingested: 2026-07-20 sha256: acc511aae7e18c20638ef6140143659eaf39a87bd6561706ada37eae02455d5c blog_source: local:unknown --- ""...
> **Sources:**
>   - local-bezmezhzhiasrccorebardopy-2026-07-20.md
> **Links:**
- [[balance.py]]
- [[main.py]]
- [[безмежжя-глибокий-аналіз-та-альтернативна-версія]]
- [[безмежжя-детальний-план-реалізації]]
- [[безмежжя-bezmezhia]]

## Key Findings

---
source_url: file:///workspace/Projects/bezmezhzhia/src/core/bardo.py
ingested: 2026-07-20
sha256: acc511aae7e18c20638ef6140143659eaf39a87bd6561706ada37eae02455d5c
blog_source: local:unknown
---
"""Bardo system — 5 phases of dissolution and final choice."""
import random
BARDOS_PHASES = [
{
'name': 'earth_dissolving',
'title': 'Розпад тіла',
'duration': 60,
'vision': 'Ти бачиш, як матеріальне зникає. Тіло стає прозорим, важкі речі розсипаються на частинки.',
'quote': 'Все, що має форму, повертається до форми.',
},
{
'name': 'water_dissolving',
'title': 'Розпад емоцій',
'duration': 60,
'vision': 'Емоції розчиняються. Радість і біль стають одним потоком, який несе тебе кудись.',
'quote': 'Емоції — це хвилі на поверхні безмежного океану.',
},
{
'name': 'fire_dissolving',
'title': 'Розпад волі',
'duration': 60,
'vision': 'Воля розчиняється. Ти більше не контролюєш — ти спостерігаєш за тим, як рішення приймаються без тебе.',
'quote': 'Хто обирає, коли немає обранця?',
},
{
'name': 'air_dissolving',
'title': 'Розпад розуму',
'duration': 60,
'vision': 'Думки розчиняються. Ти більше не мислиш — ти є. Чисте буття без вмісту.',
'quote': 'Розум — це міст між тим, що є, і тим, що здається.',
},
{
'name': 'light_appearance',
'title': 'Повне бачення',
'duration': 120,
'vision': 'Ти бачиш ВСІ свої рішення з циклу як кінострічку. Кожен вибір, кожен наслідок. Ти бачиш себе ззовні.',
'quote': 'Світло не питає — воно просто є.',
},
]
BARDOS_FINAL_CHOICES = [
{
'id': 'accept',
'text': 'Прийняти світло — завершити цикл',
'energy_bonus': 100,
'shadow': True,
'description': 'Ти впускаєш світло. Цикл завершено, енергія накопичена.',
},
{
'id': 'examine',
'text': 'Розглянути — повернутись з інсайтом',
'energy_penalty': 20,
'insight': True,
'description': 'Ти вивчаєш світло, шукаючи глибший зміст. Повертаєшся з інсайтом, але втрачаєш частину енергії.',
},
{
'id': 'reject',
'text': 'Відхилити — втеча',
'debuff': -30,
'cooldown': True,
'description': 'Ти відвертаєшся від світла. Тимчасовий дебаф на наступний цикл.',
},
]
class BardoSystem:
"""Система Бардо — фази розпаду і фінальний вибір."""
@classmethod
def get_phases(cls) -> list:
"""Повертає список фаз Бардо."""
return BARDOS_PHASES
@classmethod
def get_choices(cls) -> list:
"""Повертає фінальні варіанти."""
return BARDOS_FINAL_CHOICES
@classmethod
def run_bardo(self, balance: dict, decision_history: list) -> dict:
"""Запустити Бардо з Оглядачем.
Args:
balance: Баланс на момент Бардо.
decision_history: Історія рішень циклу.
Returns:
Результат Бардо (вибір, наслідки).
"""
print("\n" + "=" * 60)
print("🌙 БАРДО — Фази розпаду та повного бачення")
print("=" * 60)
# Фізи 1-4: розпад
for phase in BARDOS_PHASES[:-1]:
print(f"\n--- {phase['title']} ---")
print(f"👁 {phase['vision']}")
quote = phase.get('quote', '')
print(f"💬 {quote}")
input("\n[Натисни Enter для продовження...]")
# Фаза 5: Оглядач — перегляд всього циклу
print("\n--- Повне бачення ---")
print(f"👁 Ти бачиш ВСІ свої рішення з циклу:")
print(f" Всього рішень: {l

## Summary

See Key Findings for full content.

## Related Articles

- [[balance.py]]
- [[main.py]]
- [[безмежжя-глибокий-аналіз-та-альтернативна-версія]]
- [[безмежжя-детальний-план-реалізації]]
- [[безмежжя-bezmezhia]]
