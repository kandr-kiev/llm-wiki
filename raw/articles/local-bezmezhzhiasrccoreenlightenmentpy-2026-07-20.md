---
source_url: file:///workspace/Projects/bezmezhzhia/src/core/enlightenment.py
ingested: 2026-07-20
sha256: 6fb978e91bf0c9ca08cccc789aae40d5d3bbc9d2308973a1390c4f299143b7fa
blog_source: local:unknown
---
"""Enlightenment system — what happens after 25/25/25/25."""
import random


# 3 підшляхи після просвітлення
PATHS = {
    'wisdom': {
        'id': 'wisdom',
        'name': 'Мудрість',
        'symbol': '🧠',
        'philosophy': 'Пізнання безмежності',
        'levels': 5,
        'new_filters': [
            'Бачення кармічних зв\'язків',
            'Бачення часових паралелей',
            'Бачення причинно-наслідкових ланцюжок',
            'Бачення колективного несвідомого',
            'Бачення безмежності',
        ],
        'description': 'Ти обираєш шлях мудрості — пізнавати структуру реальності.',
    },
    'compassion': {
        'id': 'compassion',
        'name': 'Милосердя',
        'symbol': '❤',
        'philosophy': 'Співчуття до всіх істот',
        'levels': 5,
        'new_filters': [
            'Бачення емоційних полів',
            'Зцілення тіней',
            'Бачення спільних болів',
            'Бачення спільних радощів',
            'Бачення єдності',
        ],
        'description': 'Ти обираєш шлях милосердя — зцілювати біль інших.',
    },
    'power': {
        'id': 'power',
        'name': 'Сила',
        'symbol': '🚜',
        'philosophy': 'Трансформація реальності',
        'levels': 5,
        'new_filters': [
            'Бачення енергетичних потоків',
            'Переписування правил',
            'Бачення можливостей',
            'Трансформація перешкод',
            'Бачення нового',
        ],
        'description': 'Ти обираєш шлях сили — трансформувати реальність.',
    },
}

# 5 глибинних циклів (Цикл Циклів)
DEPTH_CYCLES = [
    {
        'depth': 1,
        'name': 'Відлуння',
        'rules': 'Стандартні правила, +тінь',
        'goal': 'Збирати відлуння',
    },
    {
        'depth': 2,
        'name': 'Заборона',
        'rules': 'Заборонено 1 рису',
        'goal': 'Збалансувати іншим способом',
    },
    {
        'depth': 3,
        'name': 'Темпо',
        'rules': 'Час скорочено на 50%',
        'goal': 'Швидкі рішення, інстинкти',
    },
    {
        'depth': 4,
        'name': 'Дзеркало',
        'rules': 'Бачення рішень інших гравців',
        'goal': 'Синхронізація з іншими',
    },
    {
        'depth': 5,
        'name': 'Ідеальний баланс',
        'rules': 'Усі риси = 25',
        'goal': 'Досягти ідеального балансу',
    },
]


class EnlightenmentSystem:
    """Система після просвітлення."""

    def __init__(self):
        self.enlightened = False
        self.enlightenment_count = 0
        self.current_path = None
        self.current_path_level = 0
        self.current_depth = 0

    def check_enlightenment(self, balance: dict) -> bool:
        """Перевірка на просвітлення."""
        return Balance.is_enlightened(balance)

    def choose_path(self, path_id: str) -> dict:
        """Обрати підшлях після просвітлення."""
        if path_id not in PATHS:
            raise ValueError(f"Невідомий шлях: {path_id}")

        self.current_path = PATHS[path_id]
        self.current_path_level = 1
        self.enlightened = True
        self.enlightenment_count += 1

        return self.current_path

    def choose_depth_cycle(self, depth: int) -> dict:
        """Обрати глибинний цикл."""
        if depth < 1 or depth > 5:
            raise ValueError(f"Невідомий рівень глибини: {depth}")

        self.current_depth = depth
        return DEPTH_CYCLES[depth - 1]

    def get_available_paths(self) -> list:
        """Повертає доступні шляхи."""
        return list(PATHS.values())

    def get_depth_cycles(self) -> list:
        """Повертає глибинні цикли."""
        return DEPTH_CYCLES

    def display_status(self) -> str:
        """Вивід статусу просвітлення."""
        if not self.enlightened:
            return "🌱 Не просвітлений"

        lines = [
            f"✨ Просвітлений (циклів: {self.enlightenment_count})",
        ]

        if self.current_path:
            lines.append(f"  Шлях: {self.current_path['symbol']} {self.current_path['name']} (рівень {self.current_path_level})")
            lines.append(f"  Фільтр: {self.current_path['new_filters'][self.current_path_level - 1]}")

        if self.current_depth > 0:
            depth = DEPTH_CYCLES[self.current_depth - 1]
            lines.append(f"  Глибина: {depth['name']} — {depth['rules']}")

        return '\n'.join(lines)
