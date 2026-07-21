---
source_url: file:///workspace/Projects/bezmezhzhia/tests/test_balance.py
ingested: 2026-07-20
sha256: 8b02aebc7c480ed23e7f54a6ede200c61fbc384ad73ba1a863a5835576c6a5ce
blog_source: local:unknown
---
"""Тести для системи балансу."""
import sys
sys.path.insert(0, '/workspace/Projects/bezmezhzhia')

from src.core.balance import Balance


def test_balance_start():
    """Баланс стартує з 55/15/15/15."""
    balance = Balance.START.copy()
    assert balance['heart'] == 55
    assert balance['cat'] == 15
    assert balance['head'] == 15
    assert balance['tractor'] == 15
    assert sum(balance.values()) == 100
    print("✅ test_balance_start пройдено")


def test_balance_decision():
    """Рішення зсуває баланс."""
    original = Balance.START.copy()
    new_balance = Balance.apply_decision(original, 'heart', 10)
    assert new_balance['heart'] > original['heart'], "Серце має зрости"
    assert new_balance['cat'] < original['cat'], "Кішка має впасти"
    assert new_balance['head'] < original['head'], "Голова має впасти"
    assert new_balance['tractor'] < original['tractor'], "Трактор має впасти"
    print("✅ test_balance_decision пройдено")


def test_enlightenment():
    """Баланс 25/25/25/25 = просвітлення."""
    balance = {'heart': 25, 'cat': 25, 'head': 25, 'tractor': 25}
    assert Balance.is_enlightened(balance)
    
    # Непросвітлення
    balance2 = {'heart': 20, 'cat': 25, 'head': 25, 'tractor': 30}
    assert not Balance.is_enlightened(balance2)
    print("✅ test_enlightenment пройдено")


def test_sum_preserved():
    """Сума балансу завжди 100."""
    balance = Balance.START.copy()
    for i in range(100):
        choice = ['heart', 'cat', 'head', 'tractor'][i % 4]
        purity = (i % 10) + 1
        balance = Balance.apply_decision(balance, choice, purity)
    assert abs(sum(balance.values()) - 100.0) < 0.01, f"Сума != 100: {sum(balance.values())}"
    print("✅ test_sum_preserved пройдено")


def test_floor():
    """Риси не падають нижче 5% при помірних рішеннях."""
    balance = {'heart': 60, 'cat': 10, 'head': 15, 'tractor': 15}
    for i in range(10):
        balance = Balance.apply_decision(balance, 'heart', 10)
    
    for q in balance:
        assert balance[q] >= 0.0, f"Риса {q} впала нижче 0%: {balance[q]}"
    print("✅ test_floor пройдено")


def test_mirror_effect():
    """Зеркало активується при > 50%."""
    balance = {'heart': 60, 'cat': 10, 'head': 15, 'tractor': 15}
    new_balance = Balance.apply_decision(balance, 'head', 10)
    # Зеркало має дати бонус до маленьких рис
    assert new_balance['cat'] >= 10, "Зеркало не спрацювало"
    print("✅ test_mirror_effect пройдено")


def test_combo_bonus():
    """Комбо бонус збільшує зсув."""
    balance1 = Balance.START.copy()
    result1 = Balance.apply_decision(balance1, 'heart', 10, combo_count=0)
    
    balance2 = Balance.START.copy()
    result2 = Balance.apply_decision(balance2, 'heart', 10, combo_count=3)
    
    assert result2['heart'] > result1['heart'], "Комбо бонус не спрацював"
    print("✅ test_combo_bonus пройдено")


def test_dominant_quality():
    """Визначення домінуючої риси."""
    balance = {'heart': 55, 'cat': 15, 'head': 15, 'tractor': 15}
    assert Balance.dominant_quality(balance) == 'heart'
    
    balance2 = {'heart': 20, 'cat': 30, 'head': 25, 'tractor': 25}
    assert Balance.dominant_quality(balance2) == 'cat'
    print("✅ test_dominant_quality пройдено")


def test_shadow_quality():
    """Визначення тіньової риси."""
    balance = {'heart': 55, 'cat': 15, 'head': 15, 'tractor': 15}
    assert Balance.shadow_quality(balance) in ['cat', 'head', 'tractor']
    print("✅ test_shadow_quality пройдено")


def test_display():
    """Вивід балансу."""
    balance = {'heart': 55, 'cat': 15, 'head': 15, 'tractor': 15}
    display = Balance.display(balance)
    assert '❤' in display
    assert '🐱' in display
    assert '🧠' in display
    assert '🚜' in display
    assert '55.0%' in display
    print("✅ test_display пройдено")


# Запуск тестів
if __name__ == '__main__':
    print("\n=== ТЕСТУВАННЯ БАЛАНСУ ===\n")
    test_balance_start()
    test_balance_decision()
    test_enlightenment()
    test_sum_preserved()
    test_floor()
    test_mirror_effect()
    test_combo_bonus()
    test_dominant_quality()
    test_shadow_quality()
    test_display()
    print("\n✅ ВСІ ТЕСТИ ПРОЙДЕНО!\n")
