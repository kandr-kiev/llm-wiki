---
title: "balance.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - system-design
---

# balance.py

> **Source:** local-bezmezhzhiasrccorebalancepy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/bezmezhzhia/src/core/balance.py ingested: 2026-07-20 sha256: 5aaef1e40ce648c767e29e1b2e2b36799d8ac03579f8029f897c49dcba2e89de blog_source: local:unknown ---...
> **Sources:**
>   - local-bezmezhzhiasrccorebalancepy-2026-07-20.md
> **Links:**
- [[main.py]]
- [[глибокий-аудит-ігрового-дизайну-безмежжя-v60]]
- [[безмежжя-детальний-план-реалізації]]
- [[безмежжя-bezmezhia]]
- [[безмежжя-глибокий-аналіз-та-альтернативна-версія]]

## Key Findings

---
source_url: file:///workspace/Projects/bezmezhzhia/src/core/balance.py
ingested: 2026-07-20
sha256: 5aaef1e40ce648c767e29e1b2e2b36799d8ac03579f8029f897c49dcba2e89de
blog_source: local:unknown
---
"""Balance system — 4 qualities (heart, cat, head, tractor)."""
from typing import Dict, Tuple
class Balance:
"""Система балансу 4 рис."""
START: Dict[str, int] = {
'heart': 55,
'cat': 15,
'head': 15,
'tractor': 15,
}
ENLIGHTENMENT: Dict[str, int] = {
'heart': 25,
'cat': 25,
'head': 25,
'tractor': 25,
}
QUALITIES = ['heart', 'cat', 'head', 'tractor']
SYMBOLS = {'heart': '❤', 'cat': '🐱', 'head': '🧠', 'tractor': '🚜'}
NAMES = {
'heart': 'Серце (Тіферет)',
'cat': 'Кішка (Хесед)',
'head': 'Голова (Хохма)',
'tractor': 'Трактор (Гевура)',
}
@classmethod
def initial(cls) -> Dict[str, float]:
"""Повертає початковий баланс."""
return cls.START.copy()
@classmethod
def apply_decision(cls, balance: Dict[str, float],
choice_type: str,
purity: int,
combo_count: int = 0) -> Dict[str, float]:
"""Застосувати рішення до балансу.
Args:
balance: Поточний баланс.
choice_type: Обрана риса.
purity: Чистота рішення (1-10).
combo_count: Кількість послідовних рішень тієї ж риси.
Returns:
Новий баланс.
"""
new_balance = balance.copy()
# Базовий зсув: обрана риса +2*(purity/10), інші -0.67
base_shift = 2.0 * (purity / 10.0)
other_shift = -base_shift / 3.0 # Розподіляємо рівномірно
for q in cls.QUALITIES:
if q == choice_type:
new_balance[q] += base_shift
else:
new_balance[q] += other_shift
# Комбо бонус: +10% за кожне комбо
if combo_count > 0:
combo_bonus = base_shift * 0.1 * combo_count
new_balance[choice_type] += combo_bonus
# Зеркало: якщо домінуюча риса > 50%, бонус до протилежних
dominant = max(new_balance.values())
if dominant > 50:
for q in cls.QUALITIES:
if new_balance[q] 25%, додатковий зсув до центру
max_val = max(new_balance.values())
min_val = min(new_balance.values())
if max_val - min_val > 25:
for q in cls.QUALITIES:
if new_balance[q] 25:
new_balance[q] -= 0.25
# Floor: мінімальне значення 5% (риси не можуть впасти до 0)
for q in cls.QUALITIES:
new_balance[q] = max(5.0, new_balance[q])
# Кліппінг (0-100)
for q in cls.QUALITIES:
new_balance[q] = min(100.0, new_balance[q])
# Перевірка суми = 100 (коригування домінуючої риси)
total = sum(new_balance.values())
if abs(total - 100.0) > 0.01:
dominant_q = max(new_balance, key=new_balance.get)
new_balance[dominant_q] -= (total - 100.0)
return new_balance
@classmethod
def is_enlightened(cls, balance: Dict[str, float],
tolerance: float = 2.0) -> bool:
"""Перевірка на просвітлення (25±tolerance)."""
return all(abs(balance[k] - 25.0) str:
"""Красивий вивід балансу."""
lines = []
for q in cls.QUALITIES:
symbol = cls.SYMBOLS[q]
name = cls.NAMES[q]
value = balance[q]
bar_len = int(value / 2) # 50 символів максимум
bar = '█' * bar_len + '░' * (50 - bar_len)
lines.append(f"{symbol} {name:20s} |{bar}| {value:5.1f}%")
return '\n'.join(lines)
@classmethod
def dominant_quality(cls, balance: Dict[str, float]) -> str:
"""Повертає домінуюч

## Summary

See Key Findings for full content.

## Related Articles

- [[main.py]]
- [[глибокий-аудит-ігрового-дизайну-безмежжя-v60]]
- [[безмежжя-детальний-план-реалізації]]
- [[безмежжя-bezmezhia]]
- [[безмежжя-глибокий-аналіз-та-альтернативна-версія]]
