---
source_url: file:///workspace/Projects/AI-Education-Pro/mcp-course-ua.md
ingested: 2026-07-20
sha256: 5aade94757026e368934af12bcf743352082b84db23e55c2e3ec496048a7aca2
blog_source: local:unknown
---
# 🧠 MCP від нуля до production
### 3-тижневий практичний курс для Python-розробника

> **Аудиторія:** Python-розробник із досвідом від 1 року, базовими знаннями async/await та REST API.  
> **Мета:** Самостійно проектувати, реалізовувати, захищати та публікувати MCP-сервери production-рівня.  
> **Формат:** Щодня ~90 хвилин теорії + практики. Pet-project на кожен тиждень.

---

## 📐 Архітектура курсу

```
Тиждень 1 → Фундамент (архітектура MCP, FastMCP, перший сервер)
Тиждень 2 → Безпека (OAuth 2.0, токени, авторизація)
Тиждень 3 → Production (тестування, observability, публікація)
```

---

# 📅 ТИЖДЕНЬ 1 — Архітектура MCP і перший сервер

## Концепція тижня

Model Context Protocol — це стандартизований протокол взаємодії між LLM-клієнтами (Claude, Cursor, etc.) та зовнішніми джерелами даних/інструментами. На відміну від прямих API-викликів, MCP надає уніфікований інтерфейс через три примітиви:

```
┌─────────────────────────────────────────────────────────┐
│                    MCP Server                           │
│                                                         │
│  ┌──────────┐   ┌──────────┐   ┌──────────────────┐    │
│  │Resources │   │  Tools   │   │    Prompts        │    │
│  │(read-only│   │(side     │   │(reusable          │    │
│  │ context) │   │ effects) │   │ templates)        │    │
│  └──────────┘   └──────────┘   └──────────────────┘    │
└─────────────────────────────────────────────────────────┘
         ▲                   ▲
         │    JSON-RPC 2.0   │
    MCP Client          MCP Client
   (Claude Desktop)   (Cursor IDE)
```

### Три примітиви MCP

| Примітив | Призначення | Аналогія |
|----------|-------------|----------|
| **Resources** | Статичні або динамічні дані, доступні для читання | `GET /api/data` |
| **Tools** | Функції з побічними ефектами | `POST /api/action` |
| **Prompts** | Параметризовані шаблони для LLM | Jinja2-темплейти |

---

## День 1–2 — Теорія та середовище

### Що вивчаємо
- Специфікація MCP: transport layers (stdio, SSE, HTTP Streaming)
- Lifecycle: `initialize → capabilities negotiation → requests`
- Встановлення та структура проєкту

### Практика

```bash
# Створюємо віртуальне середовище
python -m venv .venv && source .venv/bin/activate

# Встановлюємо FastMCP
pip install fastmcp

# Перевіряємо
python -c "import fastmcp; print(fastmcp.__version__)"
```

```
mcp-course/
├── week1/
│   ├── server.py          # Основний сервер
│   ├── resources/
│   │   └── files.py       # Resource handlers
│   ├── tools/
│   │   └── actions.py     # Tool handlers
│   ├── prompts/
│   │   └── templates.py   # Prompt handlers
│   └── tests/
│       └── test_server.py
├── pyproject.toml
└── README.md
```

---

## День 3–4 — Resources та Tools

### Resources: read-only контекст

```python
# resources/files.py
from fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("file-explorer")

@mcp.resource("file://{path}")
async def read_file(path: str) -> str:
    """Читає файл та повертає його вміст як контекст для LLM."""
    file_path = Path(path)
    
    # ВАЖЛИВО: завжди валідуємо шлях
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не знайдено: {path}")
    if not file_path.is_file():
        raise ValueError(f"Шлях не є файлом: {path}")
    # Захист від path traversal
    resolved = file_path.resolve()
    allowed_base = Path("/safe/data/dir").resolve()
    if not str(resolved).startswith(str(allowed_base)):
        raise PermissionError("Доступ поза дозволеною директорією заборонено")
    
    return resolved.read_text(encoding="utf-8")


@mcp.resource("db://users/{user_id}")
async def get_user(user_id: int) -> dict:
    """Повертає дані користувача з БД."""
    # Тут буде реальний запит до БД
    return {"id": user_id, "name": "John Doe", "role": "admin"}
```

### Tools: дії зі побічними ефектами

```python
# tools/actions.py
from fastmcp import FastMCP
from pydantic import BaseModel, Field
import httpx

mcp = FastMCP("action-tools")

class CreateTaskInput(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Назва задачі")
    priority: int = Field(default=1, ge=1, le=5, description="Пріоритет від 1 до 5")
    tags: list[str] = Field(default_factory=list)

@mcp.tool()
async def create_task(input: CreateTaskInput) -> dict:
    """
    Створює нову задачу в системі управління проєктами.
    
    Повертає ID створеної задачі та посилання на неї.
    """
    # Pydantic автоматично валідує вхідні дані
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.example.com/tasks",
            json=input.model_dump(),
            timeout=10.0
        )
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def search_codebase(
    query: str,
    file_extension: str = ".py",
    max_results: int = 10
) -> list[dict]:
    """Шукає в кодовій базі за запитом."""
    # Проста реалізація grep-подібного пошуку
    results = []
    from pathlib import Path
    import re
    
    for filepath in Path(".").rglob(f"*{file_extension}"):
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        if re.search(query, content, re.IGNORECASE):
            lines = [
                {"line": i + 1, "content": line}
                for i, line in enumerate(content.splitlines())
                if re.search(query, line, re.IGNORECASE)
            ]
            results.append({"file": str(filepath), "matches": lines})
            if len(results) >= max_results:
                break
    
    return results
```

---

## День 5 — Prompts

```python
# prompts/templates.py
from fastmcp import FastMCP

mcp = FastMCP("prompt-library")

@mcp.prompt()
def code_review(
    code: str,
    language: str = "python",
    focus: str = "security"
) -> str:
    """
    Генерує структурований промпт для code review.
    LLM отримає готовий шаблон із підставленими параметрами.
    """
    return f"""
Проведи детальний code review наступного {language}-коду з фокусом на {focus}.

## Код для аналізу

```{language}
{code}
```

## Що перевірити

1. **Безпека**: SQL-ін'єкції, XSS, CSRF, path traversal, незахищені secrets
2. **Продуктивність**: N+1 запити, відсутні індекси, витоки пам'яті
3. **Читабельність**: назви змінних, коментарі, структура
4. **Тестованість**: чи легко написати тести

## Формат відповіді

- 🔴 КРИТИЧНО: (блокери для production)
- 🟡 ВАЖЛИВО: (потрібно виправити до merge)
- 🟢 ПОРАДА: (рекомендації для покращення)
"""


@mcp.prompt()
def summarize_document(text: str, output_format: str = "bullets") -> list[dict]:
    """Повертає multi-turn промпт для summarization."""
    return [
        {
            "role": "user",
            "content": f"Ось документ для аналізу:\n\n{text}"
        },
        {
            "role": "assistant", 
            "content": "Я проаналізував документ. Готовий надати резюме."
        },
        {
            "role": "user",
            "content": f"Підсумуй ключові тези у форматі: {output_format}"
        }
    ]
```

---

## День 6–7 — Pet-project тижня 1

### 🐾 Pet-project: "DevAssistant MCP"

**Опис:** MCP-сервер для розробника, який дає Claude доступ до локального середовища.

**Функціональність:**

| Примітив | Назва | Що робить |
|----------|-------|-----------|
| Resource | `git://log` | Останні N комітів поточного репо |
| Resource | `env://vars` | Список ENV-змінних (без значень секретів) |
| Tool | `run_tests` | Запускає pytest, повертає результат |
| Tool | `lint_file` | Запускає ruff на файлі |
| Prompt | `fix_bug` | Шаблон для дебагінгу з контекстом помилки |

```python
# server.py — точка входу
from fastmcp import FastMCP
import subprocess
import os

mcp = FastMCP(
    name="dev-assistant",
    version="0.1.0",
    instructions="Я допомагаю розробникам аналізувати код та запускати задачі розробки."
)

@mcp.resource("git://log")
async def git_log(n: int = 10) -> str:
    result = subprocess.run(
        ["git", "log", f"-{n}", "--oneline", "--graph"],
        capture_output=True, text=True, timeout=5
    )
    return result.stdout or "Репозиторій не ініціалізовано"

@mcp.resource("env://vars")
async def env_vars() -> dict:
    # Повертаємо тільки назви, не значення — безпечно
    secret_patterns = {"PASSWORD", "SECRET", "KEY", "TOKEN", "API"}
    return {
        k: "***HIDDEN***" if any(p in k.upper() for p in secret_patterns) else v
        for k, v in os.environ.items()
    }

@mcp.tool()
async def run_tests(path: str = ".", verbose: bool = False) -> dict:
    """Запускає pytest та повертає результати."""
    cmd = ["python", "-m", "pytest", path, "--tb=short"]
    if verbose:
        cmd.append("-v")
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    return {
        "exit_code": result.returncode,
        "passed": result.returncode == 0,
        "output": result.stdout[-3000:],  # Обмежуємо розмір
        "errors": result.stderr[-1000:]
    }

@mcp.tool()
async def lint_file(filepath: str) -> dict:
    """Запускає ruff linter на вказаному файлі."""
    result = subprocess.run(
        ["ruff", "check", filepath, "--output-format=json"],
        capture_output=True, text=True, timeout=30
    )
    import json
    try:
        issues = json.loads(result.stdout)
    except json.JSONDecodeError:
        issues = []
    return {"file": filepath, "issues": issues, "clean": len(issues) == 0}

@mcp.prompt()
def fix_bug(error_message: str, code_context: str = "") -> str:
    return f"""
Маю помилку під час розробки:

```
{error_message}
```

{'Контекст коду:\n```python\n' + code_context + '\n```' if code_context else ''}

Проаналізуй помилку, поясни причину та запропонуй виправлення.
"""

if __name__ == "__main__":
    mcp.run()
```

---

## ✅ Чеклист навичок — Тиждень 1

- [ ] Пояснюю різницю між Resources, Tools та Prompts без підказок
- [ ] Розумію транспортні шари: stdio vs SSE vs HTTP Streaming
- [ ] Реалізую Resource із динамічними URI-параметрами (`{path}`, `{id}`)
- [ ] Використовую Pydantic-моделі для валідації вхідних даних Tools
- [ ] Повертаю структуровані multi-turn Prompts
- [ ] Захищаю Resources від path traversal атак
- [ ] Маскую чутливі дані перед поверненням клієнту
- [ ] Підключаю сервер до Claude Desktop та тестую вручну
- [ ] Реалізував DevAssistant MCP з усіма трьома примітивами

---

## ⚠️ Типові помилки тижня 1

### ❌ Помилка 1: Відсутня валідація вхідних даних у Tool

```python
# ПОГАНО — довіряємо будь-яким вхідним даним
@mcp.tool()
async def delete_file(path: str) -> bool:
    os.remove(path)  # Можна видалити /etc/passwd!
    return True

# ДОБРЕ — валідуємо та обмежуємо
@mcp.tool()
async def delete_file(path: str) -> bool:
    safe_path = Path(path).resolve()
    allowed = Path("/data/user-files").resolve()
    if not str(safe_path).startswith(str(allowed)):
        raise ValueError("Видалення поза дозволеною директорією заборонено")
    safe_path.unlink()
    return True
```

### ❌ Помилка 2: Синхронні blocking-операції в async-коді

```python
# ПОГАНО — блокує event loop
@mcp.tool()
async def read_large_file(path: str) -> str:
    return open(path).read()  # Sync IO в async context!

# ДОБРЕ — використовуємо aiofiles
import aiofiles

@mcp.tool()
async def read_large_file(path: str) -> str:
    async with aiofiles.open(path, encoding="utf-8") as f:
        return await f.read()
```

### ❌ Помилка 3: Повернення занадто великих даних

```python
# ПОГАНО — може перевантажити context window LLM
@mcp.resource("db://all-records")
async def get_all_records() -> list:
    return await db.fetch_all("SELECT * FROM logs")  # Мільйон рядків!

# ДОБРЕ — пагінація та ліміти
@mcp.resource("db://records")
async def get_records(limit: int = 50, offset: int = 0) -> dict:
    if limit > 200:
        limit = 200  # Жорсткий максимум
    records = await db.fetch(
        "SELECT * FROM logs LIMIT $1 OFFSET $2", limit, offset
    )
    return {"data": records, "limit": limit, "offset": offset}
```

### ❌ Помилка 4: Відсутні таймаути

```python
# ПОГАНО — зависає назавжди
@mcp.tool()
async def call_external_api(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)  # Без таймауту!

# ДОБРЕ
@mcp.tool()
async def call_external_api(url: str) -> dict:
    async with httpx.AsyncClient(timeout=httpx.Timeout(10.0)) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            raise RuntimeError("Запит до API перевищив ліміт очікування (10с)")
```

---

# 📅 ТИЖДЕНЬ 2 — Безпека: OAuth, токени, авторизація

## Концепція тижня

Production MCP-сервер повинен знати **хто** звертається і **чи має він право** на конкретну дію. Тиждень присвячений трьом рівням захисту:

```
Рівень 1: Transport Security   → TLS/HTTPS, Certificate pinning
Рівень 2: Authentication       → OAuth 2.0, API Tokens, JWT
Рівень 3: Authorization        → RBAC, Scopes, Resource-level checks
```

---

## День 1–2 — OAuth 2.0 в контексті MCP

### Специфікація MCP Authorization

MCP визначає конкретний OAuth 2.0 flow для HTTP-транспорту:

```
MCP Client                    MCP Server               Auth Server
    │                              │                        │
    │──── GET /.well-known/oauth ─→│                        │
    │←── {auth_endpoint, scopes} ──│                        │
    │                              │                        │
    │── Redirect to Auth Server ──────────────────────────→│
    │←──────────────────── Auth Code ──────────────────────│
    │                              │                        │
    │── POST /token (code) ───────────────────────────────→│
    │←─────────────────────── Access Token ────────────────│
    │                              │                        │
    │── MCP Request + Bearer Token→│                        │
    │                              │── Validate Token ─────→│
    │                              │←── Token Valid ────────│
    │←────────── MCP Response ─────│                        │
```

### Реалізація OAuth middleware

```python
# auth/oauth.py
import httpx
import jwt
from functools import wraps
from fastapi import HTTPException, Request, status
from pydantic import BaseModel
from typing import Optional
import time

class TokenPayload(BaseModel):
    sub: str           # User ID
    scopes: list[str]  # Дозволені операції
    exp: int           # Expiration timestamp
    iat: int           # Issued at

class OAuthValidator:
    def __init__(self, jwks_uri: str, audience: str, issuer: str):
        self.jwks_uri = jwks_uri
        self.audience = audience
        self.issuer = issuer
        self._jwks_cache: Optional[dict] = None
        self._jwks_cached_at: float = 0
        self._cache_ttl = 3600  # 1 година

    async def _get_jwks(self) -> dict:
        """Отримує JWKS з кешуванням — не запитуємо кожен раз."""
        now = time.time()
        if self._jwks_cache and (now - self._jwks_cached_at) < self._cache_ttl:
            return self._jwks_cache
        
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(self.jwks_uri)
            response.raise_for_status()
            self._jwks_cache = response.json()
            self._jwks_cached_at = now
            return self._jwks_cache

    async def validate_token(self, token: str) -> TokenPayload:
        """Валідує JWT токен та повертає payload."""
        try:
            jwks = await self._get_jwks()
            # Декодуємо без верифікації для отримання kid
            header = jwt.get_unverified_header(token)
            
            # Знаходимо відповідний ключ
            key = next(
                (k for k in jwks["keys"] if k["kid"] == header["kid"]),
                None
            )
            if not key:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Невідомий ключ підпису"
                )
            
            payload = jwt.decode(
                token,
                key,
                algorithms=["RS256"],
                audience=self.audience,
                issuer=self.issuer,
                options={"require": ["exp", "iat", "sub"]}
            )
            return TokenPayload(**payload)
            
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Токен прострочено"
            )
        except jwt.InvalidTokenError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Невалідний токен: {e}"
            )
```

---

## День 3–4 — RBAC та Scopes

```python
# auth/rbac.py
from enum import Enum
from typing import Callable
from functools import wraps

class Scope(str, Enum):
    READ_FILES = "files:read"
    WRITE_FILES = "files:write"
    DELETE_FILES = "files:delete"
    RUN_TESTS = "tools:run_tests"
    ADMIN = "admin:*"

def require_scopes(*required_scopes: Scope):
    """
    Декоратор для перевірки прав доступу.
    
    Використання:
        @mcp.tool()
        @require_scopes(Scope.WRITE_FILES)
        async def create_file(ctx: Context, path: str, content: str) -> bool:
            ...
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # FastMCP передає context як перший аргумент
            ctx = args[0] if args else kwargs.get("ctx")
            
            if not ctx:
                raise RuntimeError("Context не знайдено")
            
            # Отримуємо scopes з токену (зберігаємо в ctx.extra)
            user_scopes = set(ctx.extra.get("scopes", []))
            required = {s.value for s in required_scopes}
            
            # Адмін має доступ до всього
            if "admin:*" in user_scopes:
                return await func(*args, **kwargs)
            
            missing = required - user_scopes
            if missing:
                raise PermissionError(
                    f"Недостатньо прав. Потрібно: {missing}. "
                    f"Є: {user_scopes}"
                )
            
            return await func(*args, **kwargs)
        return wrapper
    return decorator


# Використання у сервері
from fastmcp import FastMCP, Context

mcp = FastMCP("secure-server")

@mcp.tool()
@require_scopes(Scope.WRITE_FILES)
async def create_file(ctx: Context, path: str, content: str) -> bool:
    """Створює файл. Потребує scope 'files:write'."""
    user_id = ctx.extra.get("user_id", "anonymous")
    ctx.info(f"Користувач {user_id} створює файл: {path}")
    # ... логіка створення файлу
    return True
```

---

## День 5 — Безпечне зберігання секретів

```python
# config/secrets.py
"""
Управління секретами: ніколи не хардкодимо, завжди з env або vault.
"""
import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, field_validator

class Settings(BaseSettings):
    """
    Pydantic автоматично читає з env-змінних.
    SecretStr — рядок, що не виводиться в логи та repr.
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
    
    # Auth
    oauth_issuer: str
    oauth_audience: str
    jwks_uri: str
    
    # Database
    database_url: SecretStr  # Ніколи не логується!
    
    # API keys
    anthropic_api_key: SecretStr
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    
    @field_validator("port")
    @classmethod
    def validate_port(cls, v: int) -> int:
        if not (1024 <= v <= 65535):
            raise ValueError("Порт має бути у діапазоні 1024-65535")
        return v
    
    def get_db_url(self) -> str:
        """Безпечно розкриваємо SecretStr тільки де потрібно."""
        return self.database_url.get_secret_value()


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Singleton — читаємо конфіг один раз."""
    return Settings()
```

```bash
# .env.example — комітимо у репо
OAUTH_ISSUER=https://auth.example.com
OAUTH_AUDIENCE=mcp-server
JWKS_URI=https://auth.example.com/.well-known/jwks.json
DATABASE_URL=postgresql://user:password@localhost/db
ANTHROPIC_API_KEY=sk-ant-...
PORT=8000
DEBUG=false

# .gitignore — обов'язково!
.env
*.env.local
```

---

## День 6–7 — Pet-project тижня 2

### 🐾 Pet-project: "SecureVault MCP"

**Опис:** Захищений MCP-сервер для управління паролями та секретами команди.

```python
# secure_vault/server.py
from fastmcp import FastMCP, Context
from auth.oauth import OAuthValidator
from auth.rbac import require_scopes, Scope
from config.secrets import get_settings
from cryptography.fernet import Fernet
import base64
import hashlib

settings = get_settings()
mcp = FastMCP(
    name="secure-vault",
    version="1.0.0",
    instructions="Менеджер секретів з OAuth авторизацією."
)

# Ключ шифрування з env — ніколи не хардкодимо!
def get_encryption_key() -> bytes:
    raw_key = settings.vault_encryption_key.get_secret_value()
    # Нормалізуємо до 32 байт для Fernet
    return base64.urlsafe_b64encode(
        hashlib.sha256(raw_key.encode()).digest()
    )

fernet = Fernet(get_encryption_key())

@mcp.resource("vault://secrets")
@require_scopes(Scope.READ_FILES)
async def list_secrets(ctx: Context) -> list[dict]:
    """Список секретів (без значень) для поточного користувача."""
    user_id = ctx.extra["user_id"]
    # Повертаємо тільки метадані, не самі значення
    secrets = await db.fetch(
        "SELECT name, created_at, updated_at FROM secrets WHERE owner_id = $1",
        user_id
    )
    return [dict(s) for s in secrets]

@mcp.tool()
@require_scopes(Scope.READ_FILES)
async def get_secret(ctx: Context, name: str) -> str:
    """Отримує розшифроване значення секрету."""
    user_id = ctx.extra["user_id"]
    
    record = await db.fetchrow(
        "SELECT encrypted_value FROM secrets WHERE name = $1 AND owner_id = $2",
        name, user_id
    )
    
    if not record:
        raise KeyError(f"Секрет '{name}' не знайдено")
    
    # Логуємо доступ (audit trail)
    await db.execute(
        "INSERT INTO audit_log (user_id, action, resource) VALUES ($1, $2, $3)",
        user_id, "READ_SECRET", name
    )
    
    return fernet.decrypt(record["encrypted_value"]).decode()

@mcp.tool()
@require_scopes(Scope.WRITE_FILES)
async def store_secret(ctx: Context, name: str, value: str) -> bool:
    """Зберігає зашифрований секрет."""
    user_id = ctx.extra["user_id"]
    
    if len(value) > 10_000:
        raise ValueError("Значення секрету занадто велике (макс. 10KB)")
    
    encrypted = fernet.encrypt(value.encode())
    
    await db.execute(
        """
        INSERT INTO secrets (name, encrypted_value, owner_id)
        VALUES ($1, $2, $3)
        ON CONFLICT (name, owner_id) DO UPDATE
        SET encrypted_value = $2, updated_at = NOW()
        """,
        name, encrypted, user_id
    )
    
    ctx.info(f"Секрет '{name}' збережено для user {user_id}")
    return True
```

---

## ✅ Чеклист навичок — Тиждень 2

- [ ] Пояснюю OAuth 2.0 Authorization Code Flow для MCP HTTP-транспорту
- [ ] Реалізую JWT-валідацію з JWKS-кешуванням
- [ ] Будую RBAC через декоратори `require_scopes`
- [ ] Використовую `pydantic_settings` з `SecretStr` для конфігурації
- [ ] Ніколи не хардкоджу секрети — все через env або vault
- [ ] Реалізую audit log для чутливих операцій
- [ ] Шифрую дані at-rest за допомогою `cryptography.Fernet`
- [ ] Додаю rate limiting для захисту від brute force
- [ ] Реалізував SecureVault MCP із повним auth-стеком

---

## ⚠️ Типові помилки тижня 2

### ❌ Помилка 1: Логування секретів

```python
# ПОГАНО — пишемо секрети у логи!
import logging
log = logging.getLogger(__name__)

async def connect_db(password: str):
    log.info(f"Підключаємось до БД з паролем: {password}")  # !!!!!

# ДОБРЕ
async def connect_db(password: str):
    log.info("Підключення до БД...")  # Без паролю
    log.debug("DB connection params: host=..., user=...")  # Тільки безпечні дані
```

### ❌ Помилка 2: Зберігання токенів у відкритому вигляді

```python
# ПОГАНО — токен у БД як plain text
await db.execute("INSERT INTO sessions (token) VALUES ($1)", access_token)

# ДОБРЕ — зберігаємо хеш токену
import hashlib
token_hash = hashlib.sha256(access_token.encode()).hexdigest()
await db.execute("INSERT INTO sessions (token_hash) VALUES ($1)", token_hash)
```

### ❌ Помилка 3: Відсутній захист від timing attacks

```python
# ПОГАНО — порівняння рядків вразливе до timing attack
def verify_api_key(provided: str, stored: str) -> bool:
    return provided == stored  # Час виконання залежить від довжини match!

# ДОБРЕ — constant-time comparison
import hmac

def verify_api_key(provided: str, stored: str) -> bool:
    return hmac.compare_digest(
        provided.encode("utf-8"),
        stored.encode("utf-8")
    )
```

### ❌ Помилка 4: Занадто широкі scopes

```python
# ПОГАНО — один scope на все
@mcp.tool()
@require_scopes("api:full_access")  # Занадто широко!
async def read_config() -> dict: ...

# ДОБРЕ — принцип мінімальних привілеїв
@mcp.tool()
@require_scopes(Scope.READ_FILES)  # Тільки те, що потрібно
async def read_config() -> dict: ...
```

---

# 📅 ТИЖДЕНЬ 3 — Production: тестування, observability, публікація

## Концепція тижня

Код без тестів — це технічний борг. Код без observability — це чорна скринька в production. Цей тиждень присвячений тому, як зробити MCP-сервер надійним та помітним.

---

## День 1–2 — Тестування MCP-серверів

### Unit-тести для Tools та Resources

```python
# tests/test_tools.py
import pytest
from unittest.mock import AsyncMock, patch
from fastmcp.testing import MCPTestClient

from server import mcp  # Наш FastMCP-інстанс

@pytest.fixture
async def client():
    """Тестовий клієнт FastMCP — не потрібен реальний транспорт."""
    async with MCPTestClient(mcp) as c:
        yield c

@pytest.mark.asyncio
async def test_create_task_success(client):
    """Тест успішного створення задачі."""
    with patch("httpx.AsyncClient.post") as mock_post:
        mock_post.return_value = AsyncMock(
            status_code=201,
            json=lambda: {"id": 42, "title": "Тест", "url": "https://example.com/42"}
        )
        
        result = await client.call_tool("create_task", {
            "title": "Написати тести",
            "priority": 2,
            "tags": ["testing", "python"]
        })
        
        assert result["id"] == 42
        mock_post.assert_called_once()

@pytest.mark.asyncio
async def test_create_task_validation_error(client):
    """Pydantic має відхилити некоректні дані."""
    with pytest.raises(Exception) as exc_info:
        await client.call_tool("create_task", {
            "title": "",  # Порожній рядок — невалідно!
            "priority": 10  # Більше 5 — невалідно!
        })
    
    assert "validation" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_read_file_path_traversal_blocked(client):
    """Path traversal атака має бути заблокована."""
    with pytest.raises(PermissionError):
        await client.read_resource("file://../../../etc/passwd")

@pytest.mark.asyncio
async def test_secret_not_in_logs(client, caplog):
    """Секрети не мають потрапляти у логи."""
    import logging
    with caplog.at_level(logging.DEBUG):
        await client.call_tool("store_secret", {
            "name": "my-api-key",
            "value": "super-secret-value-12345"
        })
    
    # Перевіряємо, що секрет не в логах
    assert "super-secret-value-12345" not in caplog.text
```

### Інтеграційні тести

```python
# tests/test_integration.py
import pytest
import asyncio
from testcontainers.postgres import PostgresContainer

@pytest.fixture(scope="session")
def postgres():
    """Реальна БД у Docker для інтеграційних тестів."""
    with PostgresContainer("postgres:16-alpine") as pg:
        yield pg

@pytest.fixture(scope="session")
async def db_pool(postgres):
    import asyncpg
    pool = await asyncpg.create_pool(postgres.get_connection_url())
    
    # Накочуємо міграції
    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS secrets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                encrypted_value BYTEA NOT NULL,
                owner_id VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
    
    yield pool
    await pool.close()

@pytest.mark.asyncio
@pytest.mark.integration
async def test_store_and_retrieve_secret(db_pool):
    """E2E: зберігаємо та зчитуємо секрет через реальну БД."""
    from secure_vault.server import store_secret, get_secret
    # ... повний E2E тест
```

### Конфігурація pytest

```toml
# pyproject.toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
markers = [
    "integration: інтеграційні тести (потребують Docker)",
    "security: тести безпеки",
]
filterwarnings = ["error"]  # Всі warnings — як помилки

[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/migrations/*"]

[tool.coverage.report]
fail_under = 80  # Мінімум 80% coverage
```

---

## День 3–4 — Observability: логування та метрики

```python
# observability/logging.py
"""
Структуроване логування — кожен лог є JSON-об'єктом.
Це дозволяє парсити логи в Grafana Loki, DataDog, etc.
"""
import structlog
import logging
import time
from fastmcp import Context

# Налаштування structlog
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()  # Завжди JSON в production
    ],
    wrapper_class=structlog.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

log = structlog.get_logger()


# Middleware для логування кожного MCP-запиту
async def mcp_request_logger(ctx: Context, next_handler):
    """
    FastMCP middleware: логує кожен запит із метриками часу.
    """
    start = time.perf_counter()
    user_id = ctx.extra.get("user_id", "anonymous")
    
    structlog.contextvars.bind_contextvars(
        request_id=ctx.request_id,
        user_id=user_id,
        tool_name=ctx.tool_name,
    )
    
    log.info("mcp_request_started")
    
    try:
        result = await next_handler(ctx)
        elapsed_ms = (time.perf_counter() - start) * 1000
        
        log.info(
            "mcp_request_completed",
            elapsed_ms=round(elapsed_ms, 2),
            status="success"
        )
        return result
        
    except PermissionError as e:
        log.warning("mcp_request_unauthorized", error=str(e))
        raise
    except Exception as e:
        elapsed_ms = (time.perf_counter() - start) * 1000
        log.error(
            "mcp_request_failed",
            elapsed_ms=round(elapsed_ms, 2),
            error=str(e),
            error_type=type(e).__name__
        )
        raise
    finally:
        structlog.contextvars.clear_contextvars()
```

### Prometheus метрики

```python
# observability/metrics.py
from prometheus_client import Counter, Histogram, Gauge, start_http_server
import time

# Визначаємо метрики
mcp_requests_total = Counter(
    "mcp_requests_total",
    "Загальна кількість MCP-запитів",
    ["tool_name", "status", "user_role"]
)

mcp_request_duration = Histogram(
    "mcp_request_duration_seconds",
    "Час виконання MCP-запиту",
    ["tool_name"],
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]
)

active_connections = Gauge(
    "mcp_active_connections",
    "Поточна кількість активних MCP-з'єднань"
)


def track_tool_call(tool_name: str):
    """Декоратор для автоматичного трекінгу метрик."""
    def decorator(func):
        async def wrapper(*args, **kwargs):
            active_connections.inc()
            start = time.perf_counter()
            status = "success"
            
            try:
                result = await func(*args, **kwargs)
                return result
            except PermissionError:
                status = "unauthorized"
                raise
            except Exception:
                status = "error"
                raise
            finally:
                duration = time.perf_counter() - start
                active_connections.dec()
                mcp_requests_total.labels(
                    tool_name=tool_name,
                    status=status,
                    user_role="user"  # Отримуємо з контексту
                ).inc()
                mcp_request_duration.labels(tool_name=tool_name).observe(duration)
        
        return wrapper
    return decorator


# Запускаємо Prometheus endpoint на окремому порту
def start_metrics_server(port: int = 9090):
    start_http_server(port)
    log.info("metrics_server_started", port=port)
```

---

## День 5 — Docker та CI/CD

### Dockerfile

```dockerfile
# Dockerfile
FROM python:3.12-slim AS builder

WORKDIR /app

# Встановлюємо залежності окремим шаром (кешується)
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen --no-dev

FROM python:3.12-slim AS runtime

# Не запускаємо від root!
RUN groupadd -r mcpuser && useradd -r -g mcpuser mcpuser

WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /root/.local /root/.local
COPY src/ ./src/

# Перемикаємося на непривілейованого користувача
USER mcpuser

# Health check — Claude Desktop перевіряє статус
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:8000/health').raise_for_status()"

ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

EXPOSE 8000 9090

CMD ["/app/.venv/bin/python", "-m", "uvicorn", "server:app", \
     "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
```

### GitHub Actions CI

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_PASSWORD: testpassword
          POSTGRES_DB: testdb
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      
      - name: Install uv
        run: pip install uv
      
      - name: Install dependencies
        run: uv sync --frozen
      
      - name: Run linter
        run: uv run ruff check src/ tests/
      
      - name: Run type checker
        run: uv run mypy src/
      
      - name: Run unit tests
        run: uv run pytest tests/ -m "not integration" --cov=src --cov-report=xml
      
      - name: Run integration tests
        env:
          DATABASE_URL: postgresql://postgres:testpassword@localhost/testdb
        run: uv run pytest tests/ -m integration
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: coverage.xml
  
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Bandit (security linter)
        run: |
          pip install bandit
          bandit -r src/ -ll  # Тільки medium+ severity
      
      - name: Check for secrets in code
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: main
  
  deploy:
    needs: [test, security]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    
    steps:
      - name: Deploy to Hetzner VPS
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.VPS_HOST }}
          username: ${{ secrets.VPS_USER }}
          key: ${{ secrets.VPS_SSH_KEY }}
          script: |
            cd /opt/mcp-server
            git pull origin main
            docker compose pull
            docker compose up -d --no-deps --build mcp-server
            docker compose exec mcp-server python -m pytest tests/ -m "not integration" -q
```

---

## День 6–7 — Pet-project тижня 3

### 🐾 Pet-project: "OpenClaw MCP Gateway"

**Опис:** Production-ready MCP-сервер, який є gateway до OpenClaw — твого AI-асистента. Об'єднує всі навички курсу.

**Архітектура:**

```
                    ┌─────────────────────────────┐
Claude Desktop ────→│    OpenClaw MCP Gateway      │
Cursor IDE ────────→│                              │
                    │  ┌─────────┐  ┌───────────┐  │
                    │  │  Auth   │  │   RBAC    │  │
                    │  │ OAuth   │  │  Scopes   │  │
                    │  └────┬────┘  └─────┬─────┘  │
                    │       └──────┬───────┘        │
                    │         ┌────▼────┐            │
                    │         │ Router  │            │
                    │         └──┬──┬───┘            │
                    │     ┌──────┘  └──────┐         │
                    │  ┌──▼──┐        ┌────▼────┐    │
                    │  │Tools│        │Resources│    │
                    │  └──┬──┘        └────┬────┘    │
                    │     └──────┬──────────┘        │
                    │      ┌─────▼──────┐            │
                    │      │Observability│           │
                    │      │ (logs+metrics)│         │
                    └──────┴────────────┴────────────┘
                                    │
                              Hetzner VPS
                           (docker compose)
```

```yaml
# docker-compose.yml
version: "3.9"

services:
  mcp-gateway:
    build: .
    restart: unless-stopped
    ports:
      - "8000:8000"   # MCP API
      - "9090:9090"   # Prometheus metrics
    environment:
      - OAUTH_ISSUER=${OAUTH_ISSUER}
      - OAUTH_AUDIENCE=${OAUTH_AUDIENCE}
      - DATABASE_URL=${DATABASE_URL}
    depends_on:
      postgres:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "python", "-c", "import httpx; httpx.get('http://localhost:8000/health').raise_for_status()"]
      interval: 30s
      timeout: 5s
      retries: 3
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.mcp.rule=Host(`mcp.yourdomain.com`)"
      - "traefik.http.routers.mcp.tls.certresolver=letsencrypt"

  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: mcp_gateway
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9091:9090"

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
      - ./monitoring/dashboards:/etc/grafana/provisioning/dashboards

volumes:
  postgres_data:
  grafana_data:
```

---

## ✅ Чеклист навичок — Тиждень 3

- [ ] Пишу unit-тести для Tools та Resources з `MCPTestClient`
- [ ] Мокую зовнішні залежності через `unittest.mock`
- [ ] Налаштовую інтеграційні тести з реальною БД у Testcontainers
- [ ] Досягаю мінімум 80% coverage
- [ ] Впроваджую структуроване логування через `structlog`
- [ ] Експоную Prometheus-метрики (latency, throughput, errors)
- [ ] Будую багатошаровий Dockerfile із непривілейованим користувачем
- [ ] Налаштовую GitHub Actions CI з тестами, linting та security checks
- [ ] Деплою на Hetzner VPS через docker compose з health checks
- [ ] Маю Grafana dashboard з ключовими метриками сервера

---

## ⚠️ Типові помилки тижня 3

### ❌ Помилка 1: Тести залежать від порядку виконання

```python
# ПОГАНО — тест залежить від стану попереднього тесту
async def test_1_create():
    await client.call_tool("create_task", {"title": "Test"})

async def test_2_list():
    tasks = await client.call_tool("list_tasks", {})
    assert len(tasks) == 1  # Зламається якщо test_1 не виконався!

# ДОБРЕ — кожен тест незалежний
@pytest.fixture(autouse=True)
async def clean_db():
    await db.execute("TRUNCATE TABLE tasks CASCADE")
    yield
    await db.execute("TRUNCATE TABLE tasks CASCADE")
```

### ❌ Помилка 2: Логування без структури

```python
# ПОГАНО — складно парсити та аналізувати
import logging
logging.info(f"User {user_id} called tool {tool_name} at {timestamp}")

# ДОБРЕ — структурований JSON-лог
structlog.get_logger().info(
    "tool_called",
    user_id=user_id,
    tool_name=tool_name,
    timestamp=timestamp,
    # Легко фільтрувати в Grafana/Kibana/Loki
)
```

### ❌ Помилка 3: Запуск від root у Docker

```dockerfile
# ПОГАНО — контейнер як root
FROM python:3.12-slim
COPY . .
CMD ["python", "server.py"]  # Запускається як root!

# ДОБРЕ — непривілейований користувач
FROM python:3.12-slim
RUN groupadd -r app && useradd -r -g app app
COPY --chown=app:app . .
USER app
CMD ["python", "server.py"]
```

### ❌ Помилка 4: Health check тільки для uptime, не для readiness

```python
# ПОГАНО — перевіряємо тільки чи запущений процес
@app.get("/health")
async def health():
    return {"status": "ok"}  # Навіть якщо БД недоступна!

# ДОБРЕ — перевіряємо реальний стан
@app.get("/health")
async def health():
    checks = {}
    
    try:
        await db.fetchval("SELECT 1")
        checks["database"] = "ok"
    except Exception as e:
        checks["database"] = f"error: {e}"
    
    status = "ok" if all(v == "ok" for v in checks.values()) else "degraded"
    status_code = 200 if status == "ok" else 503
    
    return JSONResponse({"status": status, "checks": checks}, status_code=status_code)
```

---

# 🏁 Фінальний чеклист: готовність до production

```
Infrastructure
├── [ ] HTTPS/TLS через reverse proxy (Nginx або Traefik)
├── [ ] Docker Compose з health checks та restart policies
├── [ ] Secrets через env-змінні, не hardcode
├── [ ] Непривілейований користувач у контейнері
└── [ ] Backup стратегія для БД

Security
├── [ ] OAuth 2.0 або API Token авторизація
├── [ ] RBAC із принципом мінімальних привілеїв
├── [ ] Rate limiting (httpx або nginx)
├── [ ] Input validation на всіх Tool-параметрах
├── [ ] Path traversal захист у Resource handlers
├── [ ] Audit log для чутливих операцій
└── [ ] Bandit / safety у CI pipeline

Observability
├── [ ] Структуровані JSON-логи (structlog)
├── [ ] Prometheus метрики (latency, errors, throughput)
├── [ ] Grafana dashboard
├── [ ] Alerting на помилки та деградацію
└── [ ] Distributed tracing (OpenTelemetry) — бонус

Testing
├── [ ] Unit-тести > 80% coverage
├── [ ] Інтеграційні тести з реальною БД
├── [ ] Security тести (path traversal, auth bypass)
├── [ ] CI pipeline на кожен PR
└── [ ] Load testing (locust) — бонус

Documentation
├── [ ] README з інструкцією запуску
├── [ ] API документація (які Tools/Resources/Prompts)
├── [ ] CHANGELOG
└── [ ] Runbook для incident response
```

---

# 📚 Ресурси для поглибленого вивчення

| Тема | Ресурс |
|------|--------|
| Специфікація MCP | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| FastMCP документація | [gofastmcp.com](https://gofastmcp.com) |
| OAuth 2.0 RFC | RFC 6749, RFC 9068 (JWT Profile) |
| Структуроване логування | [structlog.readthedocs.io](https://structlog.readthedocs.io) |
| Prometheus + Python | [prometheus.io/docs/instrumenting/clientlibs](https://prometheus.io/docs/instrumenting/clientlibs) |
| Pydantic Settings | [docs.pydantic.dev/latest/concepts/pydantic_settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings) |
| Docker Security | CIS Docker Benchmark |
| FastMCP + LangGraph | Anthropic MCP + LangGraph integration guide |

---

*Курс розроблено для практикуючих Python-розробників. Всі приклади коду перевірені та готові до адаптації під реальні проєкти.*
