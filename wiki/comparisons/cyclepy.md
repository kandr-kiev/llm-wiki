---
title: "cycle.py"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - data
  - energy
  - self-supervised
  - system-design
---

# cycle.py

> **Source:** local-bezmezhzhiasrccorecyclepy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/bezmezhzhia/src/core/cycle.py ingested: 2026-07-20 sha256: e66600a4cda040a4c81e1a163e4bb7142ebd9f61ed390ec9b458f49dcf95fd91 blog_source: local:unknown --- ""...
> **Sources:**
>   - local-bezmezhzhiasrccorecyclepy-2026-07-20.md
> **Links:**
- [[balance.py]]
- [[main.py]]
- [[БЕЗМЕЖЖЯ — Детальний план реалізації]]
- [[Глибокий аудит ігрового дизайну «Безмежжя» v6.0]]
- [[БЕЗМЕЖЖЯ (BEZMEZHIA)]]

## Key Findings

---
source_url: file:///workspace/Projects/bezmezhzhia/src/core/cycle.py
ingested: 2026-07-20
sha256: e66600a4cda040a4c81e1a163e4bb7142ebd9f61ed390ec9b458f49dcf95fd91
blog_source: local:unknown
---
"""Cycle system — phases, decisions, and flow."""
import random
from typing import Dict, List, Optional, Tuple
from .balance import Balance
from .decisions import QuestGenerator
from .energy import EnergySystem
from .bardo import BardoSystem
from .shadows import ShadowSystem
class Cycle:
"""Один повний цикл гри."""
# Фази циклу (час у хвилинах)
PHASES = {
'preparation': 2, # Підготовка
'entry': 3, # Вхід
'development': 20, # Розвиток (рішення)
'crisis': 7, # Криза
'finale': 5, # Фінал/Бардо
}
# Кількість рішень під час розвитку
DECISIONS_COUNT = 8
def __init__(self, player_id: str = None):
self.player_id = player_id or f"player_{random.randint(1000, 9999)}"
self.balance = Balance.initial()
self.quest_generator = QuestGenerator()
self.energy_system = EnergySystem()
self.bardo_system = BardoSystem()
self.shadow_system = ShadowSystem()
self.decision_history = []
self.current_combo_count = 0
self.current_combo_type = None
self.avg_purity = 0
self.crisis_passed = False
self.status = 'active'
self.phase = 'preparation'
def start(self) -> dict:
"""Запустити цикл."""
self.status = 'active'
self.phase = 'preparation'
# Застосувати тіні з минулих циклів
if self.shadow_system.active_shadows:
print("\n" + "=" * 60)
print("🌑 ТІНІ МИНУЛОГО ЦИКЛУ")
print("=" * 60)
print(self.shadow_system.get_shadow_description())
return {
'player_id': self.player_id,
'balance': self.balance.copy(),
'phase': 'preparation',
}
def get_decision(self, purity: int = None) -> Tuple[dict, int]:
"""Отримати наступне рішення."""
if self.current_combo_type is None:
self.current_combo_type = None
self.current_combo_count = 0
quest, purity = self.quest_generator.generate_with_purity()
if purity is None:
purity = random.randint(1, 10)
return quest, purity
def make_decision(self, choice_type: str, purity: int) -> dict:
"""Зробити рішення і застосувати до балансу."""
# Перевірка комбо
if choice_type == self.current_combo_type:
self.current_combo_count += 1
else:
self.current_combo_type = choice_type
self.current_combo_count = 1
# Застосувати рішення до балансу
new_balance = Balance.apply_decision(
self.balance, choice_type, purity, self.current_combo_count
)
# Застосувати тіні
if self.shadow_system.active_shadows:
new_balance = self.shadow_system.apply_shadow_effects(
new_balance, choice_type
)
# Оновити баланс
self.balance = new_balance
# Записати в історію
decision_record = {
'choice': choice_type,
'purity': purity,
'combo_count': self.current_combo_count,
'balance_after': self.balance.copy(),
}
self.decision_history.append(decision_record)
# Оновити середню чистоту
purities = [d['purity'] for d in self.decision_history]
self.avg_purity = sum(purities) / len(purities)
return decision_record
def run_development_phase(self, num_decisions: int = None) -> List[dict]:
"""Запустити фазу розвитку (рішен

## Summary

See Key Findings for full content.

## Related Articles

- [[balance.py]]
- [[main.py]]
- [[БЕЗМЕЖЖЯ — Детальний план реалізації]]
- [[Глибокий аудит ігрового дизайну «Безмежжя» v6.0]]
- [[БЕЗМЕЖЖЯ (BEZMEZHIA)]]
