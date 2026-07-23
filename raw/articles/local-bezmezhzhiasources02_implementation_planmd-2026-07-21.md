---
source_url: file:///workspace/Projects/bezmezhzhia/sources/02_IMPLEMENTATION_PLAN.md
ingested: 2026-07-21
sha256: 3e43ec193dd31b2c4a4c831f108e82ea74784c432d1cba29cd5ed7354eccf638
blog_source: local:unknown
---
# БЕЗМЕЖЖЯ — Детальний план реалізації

**Статус:** DRAFT v1.0  
**Дата:** 18.07.2026

---

## 1. АРХІТЕКТУРА ПРОЄКТУ

### 1.1. Структура репозиторію

```
bezmezhzhia/
├── README.md
├── docs/
│   ├── GAME_DESIGN.md          # Глибинный дизайн-документ
│   ├── TECHNICAL_SPEC.md       # Технічна специфікація
│   └── PHILOSOPHY.md           # Філософська основа
├── src/
│   ├── core/                   # Ядро гри (незалежне від UI)
│   │   ├── __init__.py
│   │   ├── balance.py          # Система балансу 4 рис
│   │   ├── decisions.py        # Генерація та обробка рішень
│   │   ├── cycle.py            # Логіка циклу (фази, таймери)
│   │   ├── bardo.py            # Бардо (5 фаз, Оглядач)
│   │   ├── energy.py           # Економіка енергії
│   │   ├── shadows.py          # Тіні минулих циклів
│   │   ├── enlightenment.py    # Просвітлення та Новий Рівень
│   │   ├── multiplayer.py      # Асинхронний мультиплеєр
│   │   └── paths.py            # 22 шляхи + комбо
│   ├── cli/                    # CLI-інтерфейс (прототип)
│   │   ├── __init__.py
│   │   ├── main.py             # Точка входу
│   │   ├── ui.py               # Текстовий UI
│   │   └── prompts.py          # Тексти квестів
│   ├── db/                     # База даних (MVP: PostgreSQL)
│   │   ├── schema.sql
│   │   ├── migrations/
│   │   └── models.py
│   ├── backend/                # Go-сервер (Фаза 2)
│   │   ├── main.go
│   │   ├── api/
│   │   ├── handlers/
│   │   └── middleware/
│   └── client/                 # Unity-клієнт (Фаза 3)
│       ├── Assets/
│       │   ├── Scripts/
│       │   ├── Shaders/
│       │   └── UI/
│       └── ProjectSettings/
├── tests/
│   ├── test_balance.py         # Модульні тести балансу
│   ├── test_cycle.py           # Інтеграційні тести циклу
│   ├── test_bardo.py           # Тести Бардо
│   ├── test_energy.py          # Тести економіки
│   └── simulation/             # Симуляції
│       ├── run_simulation.py   # Запуск 1000 циклів
│       └── results/
├── data/
│   ├── quest_templates.json    # Шаблони квестів (LLM-генерація)
│   ├── bardo_visions.json      # Візії фаз Бардо
│   ├── paths.json              # 22 шляхи трансформацій
│   └── philosophical_quotes.json # Цитати для Бардо
├── scripts/
│   ├── setup.sh                # Налаштування середовища
│   ├── simulate.py             # Запуск симуляцій
│   └── generate_tests.py       # Генерація тестових даних
├── docker-compose.yml          # Локальна інфраструктура
├── requirements.txt            # Python-залежності
├── go.mod                      # Go-залежності (Фаза 2)
├── Makefile                    # Команди розробки
└── .gitignore
```

### 1.2. Залежності (MVP)

**Python (прототип):**
```
pytest>=7.0
rich>=13.0        # Красивий CLI
pydantic>=2.0     # Валідація даних
```

**Go (бекенд, Фаза 2):**
```
go.mod
├── github.com/lib/pq       # PostgreSQL driver
├── github.com/gorilla/mux  # HTTP router
└── github.com/redis/go-redis/v9  # Redis client
```

**Unity (клієнт, Фаза 3):**
```
Unity 2022.3 LTS
├── Cinemachine (камери)
├── Shader Graph (візуальні ефекти)
└── DOTween (анімації)
```

---

## 2. ЕТАПИ РЕАЛІЗАЦІЇ

### Етап 0: Прототип ядра (2 тижні)

**Мета:** CLI-прототип, де можна запустити повний цикл з балансом, квестами, Бардо.

**Критерії готовності:**
- [ ] Баланс 55/15/15/15 рухається до 25/25/25/25
- [ ] Процедурна генерація квестів (20+ шаблонів)
- [ ] Оптимізований цикл (30-45 хв)
- [ ] Бардо з 5 фазами + Оглядач + 3 варіанти фіналу
- [ ] Економіка енергії (60 базова + динамічні бонуси)
- [ ] Тіні після просвітлення
- [ ] Симуляція 1000 циклів підтверджує досяжність 25/25/25/25

**Файли для створення:**
```
src/core/balance.py
src/core/decisions.py
src/core/cycle.py
src/core/bardo.py
src/core/energy.py
src/core/shadows.py
src/cli/main.py
data/quest_templates.json
tests/test_balance.py
tests/test_cycle.py
tests/simulation/run_simulation.py
```

### Етап 1: Backend + DB (3 тижні)

**Мета:** Go-сервер з PostgreSQL + Redis, REST API.

**Критерії готовності:**
- [ ] 4 таблиці (Sefirot, Player, Cycle, Decision)
- [ ] API endpoints: `/cycle/start`, `/cycle/decide`, `/cycle/complete`, `/soul/{id}`
- [ ] Redis для hot state циклів
- [ ] Аутентифікація (JWT)
- [ ] Docker Compose для локального запуску

**Файли для створення:**
```
src/db/schema.sql
src/db/models.py
src/backend/main.go
src/backend/api/routes.go
src/backend/handlers/cycle.go
src/backend/handlers/player.go
docker-compose.yml
Makefile
```

### Етап 3: Unity-клієнт (4 тижні)

**Мета:** Графічний інтерфейс з фільтрами, UI балансу, анімації.

**Критерії готовності:**
- [ ] 4 фільтри з візуальними ефектами
- [ ] UI балансу (радіальна діаграма)
- [ ] UI рішень (4 варіанти з описом)
- [ ] UI Бардо (5 фаз, анімації)
- [ ] PulseShader для ❤ фільтра
- [ ] Підключення до Go-сервера

**Файли для створення:**
```
src/client/Assets/Scripts/BalanceUI.cs
src/client/Assets/Scripts/DecisionUI.cs
src/client/Assets/Scripts/BardoUI.cs
src/client/Assets/Scripts/FilterManager.cs
src/client/Assets/Shaders/PulseShader.shader
src/client/Assets/UI/BalanceCanvas.prefab
```

### Етап 4: Розширення (3 тижні)

**Мета:** 22 шляхи + комбо + тіні + процедурна генерація.

**Критерії готовності:**
- [ ] 22 шляхи трансформацій
- [ ] 6 синергій між рисами
- [ ] Динамічні тіні (комбінуються)
- [ ] LLM-генерація квестів
- [ ] Процедурна генерація візій Бардо

**Файли для створення:**
```
src/core/paths.py
src/core/synergies.py
src/core/quest_generator.py
data/paths.json
data/philosophical_quotes.json
```

### Етап 5: Мультиплеєр (4 тижні)

**Мета:** Асинхронний мультиплеєр (Ехо, Резонанс, Асоціативний).

**Критерії готовності:**
- [ ] Асинхронне Ехо з відповідями (до 3 рівнів)
- [ ] Резонанс — спільні квести
- [ ] Асоціативний мультиплеєр (тіні інших гравців)
- [ ] Синтез — спільні випробування

**Файли для створення:**
```
src/core/multiplayer.py
src/backend/handlers/multiplayer.go
src/client/Assets/Scripts/MultiplayerUI.cs
```

### Етап 6: Продакшн (2+ тижні)

**Мета:** K8s, Kafka, ClickHouse, CI/CD.

**Критерії готовності:**
- [ ] K8s deployment
- [ ] Kafka для event sourcing
- [ ] ClickHouse для аналітики
- [ ] CI/CD (GitHub Actions)
- [ ] Моніторинг (Grafana + Prometheus)

---

## 3. ТЕХНІЧНА СПЕЦИФІКАЦІЯ (MVP)

### 3.1. Система балансу

```python
class Balance:
    """Система балансу 4 рис."""
    
    START = {
        'heart': 55,
        'cat': 15,
        'head': 15,
        'tractor': 15,
    }
    
    ENLIGHTENMENT = {
        'heart': 25,
        'cat': 25,
        'head': 25,
        'tractor': 25,
    }
    
    @classmethod
    def apply_decision(cls, balance, choice_type, purity):
        """Застосувати рішення до балансу."""
        new_balance = balance.copy()
        
        # Базовий зсув
        if choice_type == 'heart':
            new_balance['heart'] += 2 * (purity / 10)
            new_balance['cat'] -= 0.67
            new_balance['head'] -= 0.67
            new_balance['tractor'] -= 0.67
        # ... аналогічно для інших рис
        
        # Зеркало (якщо домінуюча > 50%)
        dominant = max(new_balance.values())
        if dominant > 50:
            # Бонус до протилежних рис
            for key, value in new_balance.items():
                if value < 25:
                    new_balance[key] += 0.5  # Бонус до вирівнювання
        
        # Комбо (3+ послідовних рішень однієї риси)
        # ...
        
        # Кліппінг (0-100)
        for key in new_balance:
            new_balance[key] = max(0, min(100, new_balance[key]))
        
        return new_balance
    
    @classmethod
    def is_enlightened(cls, balance):
        """Перевірка на просвітлення."""
        return all(abs(balance[k] - 25) < 2 for k in balance)
```

### 3.2. Генерація квестів

```python
QUEST_TEMPLATES = [
    {
        'id': 'river_pollution',
        'type': 'ethical',
        'situations': [
            'Ти бачиш річку, що тече крізь місто. Вода забруднена.',
            'Повітря стає отруйним, люди кашляютъ.',
            'Ліс навколо зникає, тварини тікають.',
        ],
        'choices': {
            'heart': {
                'text': 'Зупинитись і співпереживати людям, які страждають',
                'shift': {'heart': +2, 'cat': -0.67, 'head': -0.67, 'tractor': -0.67},
                'consequence': 'Ти відчуваєш емоційне виснаження, але серце стає чистішим',
            },
            'cat': {
                'text': 'Відчути енергетичний слід забруднення і знайти джерело',
                'shift': {'cat': +2, 'heart': -0.67, 'head': -0.67, 'tractor': -0.67},
                'consequence': 'Ти бачиш невидимі потоки енергії, але втрачаєш емоційний зв\'язок',
            },
            'head': {
                'text': 'Проаналізувати хімічний склад і знайти фільтр',
                'shift': {'head': +2, 'heart': -0.67, 'cat': -0.67, 'tractor': -0.67},
                'consequence': 'Ти знаходиш рішення, але воно холодне і беземоційне',
            },
            'tractor': {
                'text': 'Зруйнувати трубу, що скидає відходи',
                'shift': {'tractor': +2, 'heart': -0.67, 'cat': -0.67, 'head': -0.67},
                'consequence': 'Трубу зруйновано, але підприємство закрилось — люди втратили роботу',
            },
        },
    },
    # ... ще 19 шаблонів
]
```

### 3.3. Система Бардо

```python
BARDOS_PHASES = [
    {'name': 'earth_dissolving', 'title': 'Розпад тіла', 'duration': 60,
     'vision': 'Ти бачиш, як матеріальне зникає. Тіло стає прозорим.'},
    {'name': 'water_dissolving', 'title': 'Розпад емоцій', 'duration': 60,
     'vision': 'Емоції розчиняються. Радість і біль стають одним потоком.'},
    {'name': 'fire_dissolving', 'title': 'Розпад волі', 'duration': 60,
     'vision': 'Воля розчиняється. Ти більше не контролюєш — ти спостерігаєш.'},
    {'name': 'air_dissolving', 'title': 'Розпад розуму', 'duration': 60,
     'vision': 'Думки розчиняються. Ти більше не мислиш — ти є.'},
    {'name': 'light_appearance', 'title': 'Повне бачення', 'duration': 120,
     'vision': 'Ти бачиш ВСІ свої рішення з циклу як кінострічку.'},
]

BARDOS_FINAL_CHOICES = [
    {'id': 'accept', 'text': 'Прийняти світло', 'energy_bonus': 100, 'shadow': True},
    {'id': 'examine', 'text': 'Розглянути (повернутись з інсайтом)', 'energy_penalty': 20, 'insight': True},
    {'id': 'reject', 'text': 'Відхилити (втеча)', 'debuff': -30, 'cooldown': True},
]
```

### 3.4. SQL-схема (MVP)

```sql
-- Sefirot (довідник)
CREATE TABLE sefirot (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    quality VARCHAR(100),
    initial_percentage INTEGER DEFAULT 15,
    dominant_percentage INTEGER DEFAULT 55
);

-- Player (душа)
CREATE TABLE players (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    balance_heart INTEGER DEFAULT 55,
    balance_cat INTEGER DEFAULT 15,
    balance_head INTEGER DEFAULT 15,
    balance_tractor INTEGER DEFAULT 15,
    CONSTRAINT balance_sum CHECK (balance_heart + balance_cat + balance_head + balance_tractor = 100),
    enlightened BOOLEAN DEFAULT FALSE,
    enlightenment_count INTEGER DEFAULT 0,
    path_type VARCHAR(50) DEFAULT 'base',
    current_energy INTEGER DEFAULT 0,
    total_cycles INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Cycle (цикл)
CREATE TABLE cycles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    player_id UUID REFERENCES players(id),
    started_at TIMESTAMP DEFAULT NOW(),
    status VARCHAR(20) DEFAULT 'active',
    bardo_phase VARCHAR(20) DEFAULT 'life',
    completed_at TIMESTAMP,
    energy_earned INTEGER,
    final_balance JSONB
);

-- Decision (рішення)
CREATE TABLE decisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cycle_id UUID REFERENCES cycles(id),
    quest_template VARCHAR(100),
    choice_type VARCHAR(10) CHECK (choice_type IN ('heart', 'cat', 'head', 'tractor')),
    balance_shift JSONB,
    purity INTEGER CHECK (purity BETWEEN 1 AND 10),
    timestamp TIMESTAMP DEFAULT NOW()
);
```

---

## 4. СИМУЛЯЦІЇ ТА ТЕСТИ

### 4.1. Симуляція 1000 циклів

```python
def run_simulation(num_cycles=1000, num_players=100):
    """Симулювати 1000 циклів для 100 гравців."""
    results = []
    
    for _ in range(num_players):
        balance = Balance.START.copy()
        cycles_completed = 0
        
        while not Balance.is_enlightened(balance) and cycles_completed < 200:
            # Випадкове рішення
            choice = random.choice(['heart', 'cat', 'head', 'tractor'])
            purity = random.randint(1, 10)
            balance = Balance.apply_decision(balance, choice, purity)
            cycles_completed += 1
        
        results.append({
            'cycles': cycles_completed,
            'final_balance': balance,
            'enlightened': Balance.is_enlightened(balance),
        })
    
    # Аналіз результатів
    enlightened_count = sum(1 for r in results if r['enlightened'])
    avg_cycles = sum(r['cycles'] for r in results if r['enlightened']) / max(enlightened_count, 1)
    
    print(f"Просвітлені: {enlightened_count}/{num_players}")
    print(f"Середній цикл: {avg_cycles:.1f}")
```

### 4.2. Модульні тести

```python
def test_balance_start():
    """Баланс стартує з 55/15/15/15."""
    balance = Balance.START.copy()
    assert balance['heart'] == 55
    assert balance['cat'] == 15
    assert balance['head'] == 15
    assert balance['tractor'] == 15
    assert sum(balance.values()) == 100

def test_balance_decision():
    """Рішення зсуває баланс."""
    balance = Balance.START.copy()
    new_balance = Balance.apply_decision(balance, 'heart', 10)
    assert new_balance['heart'] > balance['heart']
    assert new_balance['cat'] < balance['cat']

def test_enlightenment():
    """Баланс 25/25/25/25 = просвітлення."""
    balance = {'heart': 25, 'cat': 25, 'head': 25, 'tractor': 25}
    assert Balance.is_enlightened(balance)

def test_mirror():
    """Зеркало активується при > 50%."""
    balance = {'heart': 60, 'cat': 10, 'head': 15, 'tractor': 15}
    new_balance = Balance.apply_decision(balance, 'head', 10)
    # Зеркало має дати бонус до маленьких рис
    assert new_balance['cat'] > 10
```

---

## 5. РИЗИКИ ТА МІТІГАЦІЇ

| Ризик | Ймовірність | Вплив | Мітігація |
|---|---|---|---|
| Процедурна генерація квестів погана | Висока | Середній | Шаблони + ручна перевірка |
| 25/25/25/25 недосяжний | Середня | Високий | Симуляція 1000 циклів |
| CLI-прототип не покаже "дух" гри | Низька | Середній | Фокус на балансі, не на візуалі |
| Go-бекенд складніший за Python | Низька | Низький | Прототип на Python → порт на Go |

---

**План готовий.** Чекаю на затвердження або корективи.
