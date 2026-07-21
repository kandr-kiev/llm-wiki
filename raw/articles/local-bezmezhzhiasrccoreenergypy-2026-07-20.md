---
source_url: file:///workspace/Projects/bezmezhzhia/src/core/energy.py
ingested: 2026-07-20
sha256: bdb902ca6fbcdc492be143ce967e7c7a958627ad3ff05598eb318da32c01e420
blog_source: local:unknown
---
"""Energy economy — rewards and costs per cycle."""
import random


class EnergySystem:
    """Система економіки енергії."""

    BASE_REWARD = 60  # Базова нагорода за цикл
    PURITY_BONUS = 5  # За кожну одиницю середньої чистоти
    CRISIS_BONUS = 30 # За успішне проходження кризи
    PATH_COST_MIN = 100  # Мінімальна вартість трансформації
    PATH_COST_MAX = 250  # Максимальна вартість

    @classmethod
    def calculate_cycle_reward(cls, avg_purity: float, crisis_passed: bool = True) -> int:
        """Розрахувати нагороду за цикл.

        Args:
            avg_purity: Середня чистота рішень (1-10).
            crisis_passed: Чи пройдено кризу.

        Returns:
            Кількість енергії.
        """
        reward = cls.BASE_REWARD
        reward += int(cls.PURITY_BONUS * avg_purity)
        if crisis_passed:
            reward += cls.CISIS_BONUS
        return reward

    @classmethod
    def calculate_path_cost(cls, complexity: int = 1) -> int:
        """Розрахувати вартість трансформації шляху.

        Args:
            complexity: Складність шляху (1-5).

        Returns:
            Кількість енергії.
        """
        return cls.PATH_COST_MIN + (cls.PATH_COST_MAX - cls.PATH_COST_MIN) * (complexity - 1) / 4

    @classmethod
    def simulate_economy(cls, num_cycles: int = 50) -> dict:
        """Симулювати економіку на N циклів."""
        total_energy = 0
        total_spent = 0
        path_costs = []

        for i in range(num_cycles):
            # Випадкова чистота
            avg_purity = 5.0  # Середнє
            reward = cls.calculate_cycle_reward(avg_purity, crisis_passed=True)
            total_energy += reward

            # Випадкова трансформація кожні 2-5 циклів
            if i % random.randint(2, 5) == 0:
                cost = cls.calculate_path_cost(random.randint(1, 5))
                total_spent += cost
                path_costs.append(cost)

        return {
            'total_energy': total_energy,
            'total_spent': total_spent,
            'net_energy': total_energy - total_spent,
            'path_costs': path_costs,
            'avg_cost_per_path': sum(path_costs) / max(len(path_costs), 1),
        }
