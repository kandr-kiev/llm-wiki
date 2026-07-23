---
source_url: local-document
ingested: 2026-07-22
sha256: 033db2a70d327924483fb73f09fe29122d601e84e47f8af7c77dbe4dd2970041
---

# Multiplexed Gateway (ОДИН GATEWAY НА ВСІХ)

Один процес gateway обслуговує всі профілі на машині.

## Як працює

```
┌─────────────────────────────────────────────┐
│  Machine                                     │
│                                              │
│  ┌──────────────────────────────────┐        │
│  │    DEFAULT GATEWAY (multiplexer) │        │
│  │                                  │        │
│  │  ┌────────┐ ┌────────┐ ┌──────┐ │        │
│  │  │default │ │ coder  │ │research│ │        │
│  │  │ profile│ │profile │ │profile│ │        │
│  │  └───┬────┘ └───┬────┘ └───┬───┘ │        │
│  └──────┼──────────┼──────────┼─────┘        │
│         │          │          │              │
│  ┌──────┴──────┐ ┌─┴──────┐ ┌┴──────────┐   │
│  │ Telegram    │ │Discord │ │ Telegram  │   │
│  │ Bot #1, #2  │ │ Bot #1 │ │ Bot #2    │   │
│  └─────────────┘ └────────┘ └───────────┘   │
└─────────────────────────────────────────────┘
```

## Вмикання

### Крок 1: Увімкнути multiplexing на default профілі

```bash
hermes config set gateway.multiplex_profiles true
hermes gateway restart
```

Або через `~/.hermes/config.yaml`:

```yaml
gateway:
  multiplex_profiles: true
```

### Крок 2: Налаштувати secondary профілі

```bash
hermes profile create coder
hermes profile create research
coder setup
research setup
```

### Крок 3: Запустити ТИЛЬКИ default gateway

```bash
# НЕ запускай: coder gateway start
# НЕ запускай: research gateway start
# Це буде помилка!

# Тільки:
hermes gateway start
```

## Routing — profile_routes

Коли кілька спільнот ділять один bot token (наприклад, один Discord bot для багатьох серверів):

```yaml
gateway:
  multiplex_profiles: true

  profile_routes:
    # Весь Discord сервер → один профіль
    - name: acme-server
      platform: discord
      guild_id: "1234567890"
      profile: acme

    # Один канал в тому ж сервері → інший профіль
    - name: acme-support
      platform: discord
      guild_id: "1234567890"
      chat_id: "9876543210"
      profile: acme-support

    # Telegram група
    - name: tg-group
      platform: telegram
      chat_id: "-1001234567890"
      profile: tg-profile
```

### Правила matching

- **Most-specific-first**: `thread_id > chat_id > guild_id`
- **AND logic**: всі declared fields must hold
- **Channel routes** також matching threads/forum posts з батьківським каналом
- **No match → default profile**

## HTTP Routing (`/p/<profile>/`)

Webhook трафік для secondary профілів приходить через prefix:

```bash
# Default profile
POST http://host:8644/webhooks/<route>

# Coder profile, той самий listener
POST http://host:8644/p/coder/webhooks/<route>

# Research profile
POST http://host:8644/p/research/webhooks/<route>
```

Невідомий profile повертає 404.

## Ключові відмінності

| Параметр | One-Process | Multiplexed |
|----------|-------------|-------------|
| Процесів | N профілів = N процесів | 1 процес для всіх |
| RAM | N × memory footprint | 1 × memory footprint |
| Isolation | Hard (окремі процеси) | Soft (окремі namespaces) |
| Crash domain | Незалежні | Спільний — падіння gateway = всі down |
| Restart | `coder gateway restart` | `hermes gateway restart` (все) |
| HTTP routing | Кожен на своєму порту | `/p/<profile>/` prefix |
| Token | Кожен профіль = свій токен | Кожен профіль = свій токен |
| Shared token | Не підтримує | Підтримує через `profile_routes` |

**Використовувати:**
- **One-Process**: 1-3 профілі
- **Multiplexed**: 4+ профілів або container

## Важливі правила

### 1. Secondary профілі НЕ запускають gateway

```bash
# ❌ ПОМИЛКА — hard error:
coder gateway start

# ✅ ПРАВИЛЬНО — default gateway вже serve 'coder':
hermes gateway start  # вже запущений
```

### 2. Port-binding platforms тільки на default

```bash
# ❌ НЕ можна в secondary profile:
# coder/.env:
# webhook:
#   enabled: true  ← це конфлікт!

# ✅ ТІЛЬКО default profile:
# default/.env:
# webhook:
#   enabled: true
```

Платформи що підпадають: `webhook`, `api_server`, `msgraph_webhook`, `feishu`, `wecom_callback`, `bluebubbles`, `sms`

### 3. Token conflict safety

```bash
# Перевірка дублікатів токенів:
grep -H 'TELEGRAM_BOT_TOKEN\|DISCORD_BOT_TOKEN' \
  ~/.hermes/.env ~/.hermes/profiles/*/.env
```

Якщо два профілі ділять один токен — gateway refuse to start з помилкою.

### 4. Session keys namespaced by profile

```
default profile:    agent:main:session_abc
coder profile:      agent:coder:session_abc
research profile:   agent:research:session_abc
```

## Керування

```bash
# Перевірити статус — всі профілі
hermes status

# Перевірити статус — один профіль
hermes status -p coder

# Перезапустити всі
hermes gateway restart

# Update
hermes update
hermes gateway restart

# Health check — всі
hermes doctor

# Health check — один
hermes -p coder doctor
```

## Коли що обирати

### Обирай One-Process, якщо:
- 1-3 профілі
- Потрібна hard isolation
- Профілі критичні (не хочеш щоб падіння одного тягнуло інші)
- Різні машини/deployments

### Обирай Multiplexed, якщо:
- 4+ профілів на одній машині
- Container deployment (обмежений ресурс)
- Потрібен shared-bot routing (`profile_routes`)
- Хочеш простіше керування (один процес замість N)
