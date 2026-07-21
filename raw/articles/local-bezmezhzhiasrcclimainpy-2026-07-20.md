---
source_url: file:///workspace/Projects/bezmezhzhia/src/cli/main.py
ingested: 2026-07-20
sha256: 882b85e4a45aa83a899fe9e0f3793f0d6121e8489ee9a8991cb275ac5b316eae
blog_source: local:unknown
---
"""Bezmezhzhia CLI — main entry point."""
import random
import sys
from typing import Dict, Optional

from ..core.balance import Balance
from ..core.cycle import Cycle
from ..core.enlightenment import EnlightenmentSystem


def print_banner():
    """Вивід банера гри."""
    print("\n" + "=" * 60)
    print("       БЕЗМЕЖЖЯ (BEZMEZHIA)")
    print("   Метаморфози Могутньої Сутності")
    print("=" * 60)
    print()
    print("🎯 Мета: досягти балансу 25/25/25/25")
    print()
    print("  ❤ Серце (Тіферет) — співчуття, емоції, зв'язок")
    print("  🐱 Кішка (Хесед) — інтуїція, енергія, зв'язки")
    print("  🧠 Голова (Хохма) — розум, логіка, пізнання")
    print("  🚜 Трактор (Гевура) — сила, воля, дії")
    print()
    print("  Початковий баланс: 55/15/15/15")
    print("  Стань рівноважним. Стань Безмежним.")
    print("=" * 60)
    print()


def print_cycle_summary(result: dict, bardo_result: Optional[dict] = None):
    """Вивід підсумків циклу."""
    print("\n" + "=" * 60)
    print("📊 ПІДСУМКИ ЦИКЛУ")
    print("=" * 60)
    print(f"  Гравець: {result['player_id']}")
    print(f"  Рішень: {result['decisions']}")
    print(f"  Середня чистота: {result['avg_purity']:.1f}/10")
    print(f"  Криза пройдена: {'✅' if result['crisis_passed'] else '❌'}")
    print(f"  Енергія: {result['energy']}")
    print()
    print("  Фінальний баланс:")
    print(Balance.display(result['final_balance']))

    if bardo_result:
        print(f"\n  🌙 Бардо: {bardo_result['choice']}")
        print(f"  🌙 Енергія: {bardo_result['energy_change']}")

    print("=" * 60)


def run_game(max_cycles: int = 100, auto_mode: bool = False):
    """Запустити гру."""
    print_banner()

    # Ініціалізація
    cycle = Cycle()
    enlightenment = EnlightenmentSystem()

    # Старт
    cycle.start()

    for cycle_num in range(1, max_cycles + 1):
        print(f"\n{'#' * 60}")
        print(f"# ЦИКЛ {cycle_num}")
        print(f"{'#' * 60}")

        # Показати баланс
        print(f"\n{Balance.display(cycle.balance)}")

        # Перевірка на просвітлення
        if enlightenment.enlightened:
            print(f"\n{enlightenment.display_status()}")

        if cycle_num > 1:
            # Перевірка на просвітлення з минулого циклу
            if enlightenment.enlightened:
                print("\n✨ Ти просвітлений! Обери шлях:")
                paths = enlightenment.get_available_paths()
                for i, path in enumerate(paths):
                    print(f"  {i+1}. {path['symbol']} {path['name']} — {path['philosophy']}")

                while True:
                    try:
                        selection = int(input("\nОбери шлях (1-3): ")) - 1
                        if 0 <= selection < len(paths):
                            enlightenment.choose_path(paths[selection]['id'])
                            break
                    except ValueError:
                        pass
                    print("Неправильний вибір. Спробуй ще.")

        # Фаза розвитку
        if not auto_mode:
            cycle.run_development_phase()
        else:
            # Автоматичний режим: випадкові рішення
            for i in range(Cycle.DECISIONS_COUNT):
                choice = random.choice(list(Balance.SYMBOLS.keys()))
                purity = random.randint(1, 10)
                cycle.make_decision(choice, purity)

        # Фаза кризи
        if not auto_mode:
            cycle.run_crisis_phase()
        else:
            # Автоматична криза: шанс залежить від балансу
            balance_variance = sum((v - 25) ** 2 for v in cycle.balance.values()) / 4
            success_chance = max(0.3, 1.0 - (balance_variance / 1000))
            cycle.crisis_passed = random.random() < success_chance

        # Перевірка на просвітлення
        if Balance.is_enlightened(cycle.balance):
            print("\n" + "!" * 60)
            print("✨ ПРОСВІТЛЕННЯ! ✨")
            print("!" * 60)
            print(f"\n{Balance.display(cycle.balance)}")
            print("\nТи досяг рівноваги 25/25/25/25!")
            print("Обери підшлях:")
            paths = enlightenment.get_available_paths()
            for i, path in enumerate(paths):
                print(f"  {i+1}. {path['symbol']} {path['name']}")
                print(f"     {path['description']}")

            while True:
                try:
                    selection = int(input("\nОбери шлях (1-3): ")) - 1
                    if 0 <= selection < len(paths):
                        enlightenment.choose_path(paths[selection]['id'])
                        break
                except ValueError:
                    pass
                print("Неправильний вибір. Спробуй ще.")

            # Бардо
            bardo_result = cycle.run_bardo()
        else:
            # Цикл не завершено — просто завершуємо
            cycle.run_crisis_phase()
            bardo_result = None

        # Підсумки
        result = cycle.complete()
        print_cycle_summary(result, bardo_result)

        # Готово до нового циклу?
        if not auto_mode:
            if Balance.is_enlightened(cycle.balance):
                print("\nГра завершена! Ти просвітлився.")
                break

            again = input("\nНовий цикл? (y/n): ").strip().lower()
            if again != 'y':
                break

        # Новий цикл
        cycle = Cycle(player_id=cycle.player_id)
        cycle.start()

    print("\n" + "=" * 60)
    print("🏁 ГРУ ЗАВЕРШЕНО")
    print("=" * 60)


def run_simulation(num_cycles: int = 1000, num_players: int = 100):
    """Запустити симуляцію."""
    print(f"\n🧪 Симуляція: {num_players} гравців × {num_cycles} циклів")
    print("=" * 60)

    from ..core.balance import Balance
    import random

    results = []

    for p in range(num_players):
        balance = Balance.START.copy()
        cycles_completed = 0
        enlightened = False

        for c in range(num_cycles):
            if enlightened:
                break

            cycles_completed += 1

            # Випадкове рішення
            choice = random.choice(['heart', 'cat', 'head', 'tractor'])
            purity = random.randint(1, 10)
            balance = Balance.apply_decision(balance, choice, purity)

            # Перевірка на просвітлення
            if Balance.is_enlightened(balance):
                enlightened = True

        results.append({
            'player': p + 1,
            'cycles': cycles_completed,
            'enlightened': enlightened,
            'final_balance': balance,
        })

    # Аналіз результатів
    enlightened_count = sum(1 for r in results if r['enlightened'])
    non_enlightened = [r for r in results if not r['enlightened']]
    avg_cycles = sum(r['cycles'] for r in results if r['enlightened']) / max(enlightened_count, 1)

    print(f"\n📊 РЕЗУЛЬТАТИ СИМУЛЯЦІЇ")
    print(f"  Просвітлені: {enlightened_count}/{num_players} ({100*enlightened_count/num_players:.1f}%)")
    print(f"  Середній цикл: {avg_cycles:.1f}")
    print(f"  Не просвітлені: {len(non_enlightened)}")

    # Розподіл циклів
    if results:
        cycles_list = [r['cycles'] for r in results if r['enlightened']]
        if cycles_list:
            print(f"  Мінімальний цикл: {min(cycles_list)}")
            print(f"  Максимальний цикл: {max(cycles_list)}")
            print(f"  Медіана: {sorted(cycles_list)[len(cycles_list)//2]}")

    print("=" * 60)


def main():
    """Точка входу."""
    print("Безмежжя — Обери режим:")
    print("  1. Гра (інтерактивна)")
    print("  2. Симуляція (автоматична)")
    print("  3. Тест балансу (швидкий)")
    print()

    choice = input("Твій вибір (1-3): ").strip()

    if choice == '1':
        max_cycles = int(input("Максимум циклів (100): ") or "100")
        run_game(max_cycles=max_cycles)
    elif choice == '2':
        num_players = int(input("Гравців (100): ") or "100")
        num_cycles = int(input("Циклів на гравця (1000): ") or "1000")
        run_simulation(num_cycles=num_cycles, num_players=num_players)
    elif choice == '3':
        # Швидкий тест балансу
        balance = Balance.START.copy()
        print(f"\nПочатковий баланс: {Balance.display(balance)}")

        # 50 випадкових рішень
        for i in range(50):
            choice = random.choice(['heart', 'cat', 'head', 'tractor'])
            purity = random.randint(1, 10)
            balance = Balance.apply_decision(balance, choice, purity)

        print(f"\nПісля 50 рішень: {Balance.display(balance)}")
        print(f"Просвітлений: {Balance.is_enlightened(balance)}")
        print(f"Домінуюча: {Balance.dominant_quality(balance)}")
        print(f"Тінь: {Balance.shadow_quality(balance)}")
    else:
        print("Невідомий вибір. Вихід.")
        sys.exit(1)


if __name__ == '__main__':
    main()
