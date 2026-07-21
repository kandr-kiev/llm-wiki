---
source_url: file:///workspace/Projects/bezmezhzhia/src/core/shadows.py
ingested: 2026-07-20
sha256: cc80162b0cb1d76b03d1616a3b2886a58f476a68b69356542b554d05b953a380
blog_source: local:unknown
---
"""Shadow system — persistent effects from past cycles."""
import random


SHADOW_TEMPLATES = [
    {
        'id': 'heart_blindness',
        'name': 'Сліпота серця',
        'type': 'passive',
        'description': '❤ рішення дають -30% чистоти',
        'effect': {'heart': -0.3},
    },
    {
        'id': 'iron_will',
        'name': 'Залізна воля',
        'type': 'active',
        'description': '🚜 рішення дають +50% зсуву',
        'effect': {'tractor': 0.5},
    },
    {
        'id': 'eternal_search',
        'name': 'Вічний пошук',
        'type': 'passive',
        'description': '🧠 рішення дають +20% інсайтів',
        'effect': {'head': 0.2},
    },
    {
        'id': 'quiet_observer',
        'name': 'Тихий спостерігач',
        'type': 'active',
        'description': '🐱 рішення дають +30% резонансу',
        'effect': {'cat': 0.3},
    },
    {
        'id': 'emotional_echo',
        'name': 'Емоційне відлуння',
        'type': 'passive',
        'description': '❤ рішення дають +10% енергії, але -20% чистоти',
        'effect': {'heart': -0.2, 'energy': 0.1},
    },
    {
        'id': 'logic_trap',
        'name': 'Пастка логіки',
        'type': 'active',
        'description': '🧠 рішення дають +40% зсуву, але блокують ❤ на 1 цикл',
        'effect': {'head': 0.4},
        'block': {'heart': 1},
    },
    {
        'id': 'compassion_flood',
        'name': 'Потік співчуття',
        'type': 'passive',
        'description': '❤ і 🐱 рішення дають +25% комбо-бонус',
        'effect': {'heart': 0.25, 'cat': 0.25},
    },
    {
        'id': 'tractor_rage',
        'name': 'Гнів трактора',
        'type': 'active',
        'description': '🚜 рішення дають +60% зсуву, але -20% до всіх інших',
        'effect': {'tractor': 0.6, 'other': -0.2},
    },
]


class ShadowSystem:
    """Система тіней — постійні ефекти минулих циклів."""

    def __init__(self):
        self.active_shadows = []
        self.shadow_history = []

    def generate_shadow(self, balance: dict) -> dict:
        """Згенерувати тінь на основі балансу."""
        # Тінь залежить від домінуючої та найменшої риси
        dominant = max(balance, key=balance.get)
        shadow_q = min(balance, key=balance.get)

        # Фільтруємо тіні, що стосуються домінуючої/тіньової риси
        relevant = [s for s in SHADOW_TEMPLATES
                    if dominant in s['effect'] or shadow_q in s['effect']]

        if not relevant:
            relevant = SHADOW_TEMPLATES

        shadow = random.choice(relevant)
        return shadow.copy()

    def add_shadow(self, shadow: dict) -> None:
        """Додати тінь до активних."""
        self.active_shadows.append(shadow)
        self.shadow_history.append(shadow)

    def apply_shadow_effects(self, balance: dict, choice_type: str) -> dict:
        """Застосувати ефекти тіней до балансу."""
        new_balance = balance.copy()

        for shadow in self.active_shadows:
            for quality, effect in shadow['effect'].items():
                if quality == choice_type:
                    if quality == 'other':
                        # Застосовуємо до всіх інших
                        for q in balance:
                            if q != choice_type:
                                new_balance[q] += effect
                    else:
                        new_balance[quality] += effect

        return new_balance

    def get_shadow_description(self) -> str:
        """Опис активних тіней."""
        if not self.active_shadows:
            return "  Тіней немає."

        lines = ["  Активні тіні:"]
        for i, shadow in enumerate(self.active_shadows, 1):
            lines.append(f"    {i}. {shadow['name']} ({shadow['type']})")
            lines.append(f"       {shadow['description']}")
        return '\n'.join(lines)

    def reset(self) -> None:
        """Скинути тіні (для нового рівня)."""
        self.active_shadows = []
