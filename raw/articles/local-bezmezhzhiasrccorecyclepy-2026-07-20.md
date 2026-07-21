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
        'preparation': 2,    # Підготовка
        'entry': 3,          # Вхід
        'development': 20,   # Розвиток (рішення)
        'crisis': 7,         # Криза
        'finale': 5,         # Фінал/Бардо
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
        """Запустити фазу розвитку (рішення)."""
        num_decisions = num_decisions or self.DECISIONS_COUNT
        results = []

        print("\n" + "=" * 60)
        print(f"🔄 РОЗВИТОК — Фаза рішень ({num_decisions} рішень)")
        print("=" * 60)

        for i in range(num_decisions):
            print(f"\n--- Рішення {i+1}/{num_decisions} ---")

            # Отримати квест
            quest, purity = self.get_decision()

            print(f"📍 Тип: {quest['type']}")
            print(f"📍 Ситуація: {quest['situation']}")
            print(f"📍 Чистота: {'⭐' * purity}{'☆' * (10-purity)} ({purity}/10)")

            # Показати варіанти
            print("\nВаріанти:")
            symbols = Balance.SYMBOLS
            for j, (choice, data) in enumerate(quest['choices'].items()):
                print(f"  {j+1}. {symbols[choice]} {choice}: {data['text']}")

            # Отримати вибір гравця
            while True:
                try:
                    selection = int(input("\nТвій вибір (1-4): ")) - 1
                    if 0 <= selection < 4:
                        choice_type = list(quest['choices'].keys())[selection]
                        break
                except ValueError:
                    pass
                print("Неправильний вибір. Спробуй ще.")

            # Застосувати рішення
            result = self.make_decision(choice_type, purity)
            results.append(result)

            # Показати баланс
            print(f"\n{Balance.display(self.balance)}")
            print(f"Комбо: {self.current_combo_count}x {self.current_combo_type}")

        return results

    def run_crisis_phase(self) -> bool:
        """Запустити фазу кризи."""
        print("\n" + "=" * 60)
        print("⚡ КРИЗА")
        print("=" * 60)

        # Криза: чи витримує гравець навантаження?
        # Шанс успіху залежить від балансу (рівномірність = краще)
        balance_variance = sum((v - 25) ** 2 for v in self.balance.values()) / 4
        success_chance = max(0.3, 1.0 - (balance_variance / 1000))

        crisis_passed = random.random() < success_chance

        if crisis_passed:
            print("✅ Ти пройшов кризу! +30 енергії")
            self.crisis_passed = True
        else:
            print("❌ Ти не пройшов кризу. -20 енергії")
            self.crisis_passed = False

        return crisis_passed

    def run_bardo(self) -> dict:
        """Запустити Бардо."""
        self.phase = 'bardo'
        result = self.bardo_system.run_bardo(self.balance, self.decision_history)
        return result

    def calculate_energy(self) -> int:
        """Розрахувати енергію за цикл."""
        return self.energy_system.calculate_cycle_reward(
            self.avg_purity, self.crisis_passed
        )

    def complete(self) -> dict:
        """Завершити цикл і повернути результати."""
        energy = self.calculate_energy()

        return {
            'player_id': self.player_id,
            'final_balance': self.balance.copy(),
            'energy': energy,
            'decisions': len(self.decision_history),
            'avg_purity': self.avg_purity,
            'crisis_passed': self.crisis_passed,
            'is_enlightened': Balance.is_enlightened(self.balance),
            'status': 'completed',
        }
