---
source_url: file:///workspace/Projects/bezmezhzhia/sources/BEZMEZHYA_v6.0_TECH_AUDIT_REPORT.md
ingested: 2026-07-21
sha256: 73546cb5e5db0f4f64a194dd2667615b9a81bb4a2d41b631ddba2ab6eebbd338
blog_source: local:unknown
---
# Технічний аудит архітектури «Безмежжя» v6.0

**Дата аудиту:** 2026-07-18  
**Версія документа:** v6.0 (заголовок з ТЗ)  
**Автор аудиту:** Hermes Agent (subagent)  
**Статус:** Аналіз на основі ТЗ v6.0 (кодова база не наявна в workspace — аудит на основі ТЗ)

---

## Executive Summary

| Компонент | Оцінка | Рекомендація MVP |
|-----------|--------|------------------|
| **SQL-схема** | ⚠️ Не надано — **CRITICAL GAP** | Спроектувати мінімальну схему (12-15 таблиць) |
| **Backend Stack (Go/Scala/Elixir)** | ❌ **Over-engineered для MVP** | **Спростити до Go-only** |
| **Unity Client (HeartFilter/Shaders)** | ⚠️ Не надано — **CRITICAL GAP** | Спростити до ECS + URP + Compute Shaders |
| **Event Sourcing (Kafka)** | ❌ **Overkill для MVP** | **Redis Streams / Postgres LISTEN/NOTIFY** |
| **MVP Scope** | ❌ Over-scoped | **Мінімальний MMO-loop: Echo + Resonance only** |

---

## 1. SQL-Схема — АУДИТ (CRITICAL GAP: Схеми НЕМАЄ)

### ⚠️ Критичний знахідок
**У наданому ТЗ v6.0 відсутня SQL-сема.** У workspace знайдено лише схему іншого проекту (AI-Education-Pro — 3 таблиці: users, progress, feedback).

### 🎯 Що ПОТРІБНО для MVP «Безмежжя» v6.0

На основі ТЗ v6.0 (4 риси, енергія, цикл 5 фаз, мультиплеєр: Echo/Resonance/Пустка/Synthesis, Енергія, Просвітлення, Тінь) — **мінімальна схема (12-15 таблиць):**

```sql
-- ============================================================
-- CORE: ГРАВЕЦЬ (М.С.) + 4 РИСИ + ЕНЕРГІЯ + ЦИКЛИ
-- ============================================================

CREATE TABLE entities (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id      UUID NOT NULL REFERENCES accounts(id),
    name            VARCHAR(64) NOT NULL,
    -- 4 риси: Серце/Кішка/Голова/Трактор (76/8/8/8 → 25/25/25/25)
    trait_heart     SMALLINT NOT NULL DEFAULT 76,   -- Тиферет
    trait_cat       SMALLINT NOT NULL DEFAULT 8,    -- Хесед
    trait_head      SMALLINT NOT NULL DEFAULT 8,    -- Хохма
    trait_tractor   SMALLINT NOT NULL DEFAULT 8,    -- Гевура
    -- Енергія: нагорода за цикл, витрачається на трансформацію
    energy          INT NOT NULL DEFAULT 0,
    -- Прогресія
    enlightenment_level  SMALLINT NOT NULL DEFAULT 0,  -- 0 = не пройшли, 1+ = рівень просвітлення
    cycle_count          INT NOT NULL DEFAULT 0,       -- Цикл Циклів (скидання з тінню)
    shadow_traits JSONB NOT NULL DEFAULT '{}',          -- Тіньові риси після скидання
    -- Статус
    current_phase       SMALLINT NOT NULL DEFAULT 0,    -- 0=Підготовка..5=Світло (Бардо)
    current_cycle_phase SMALLINT NOT NULL DEFAULT 0,    -- 0=Підготовка..4=Фінал
    status              VARCHAR(32) NOT NULL DEFAULT 'preparation', -- preparation|entry|development|crisis|final|bardo
    created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_entities_account ON entities(account_id);
CREATE INDEX idx_entities_status_phase ON entities(status, current_phase);

-- Акаунти (авторизація — окрема таблиця для розділення обов'язків)
CREATE TABLE accounts (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email           CITEXT NOT NULL UNIQUE,
    password_hash   TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_login_at   TIMESTAMPTZ
);
CREATE INDEX idx_accounts_email ON accounts(email);

-- ============================================================
-- ЦИКЛИ ТА ФАЗИ (Event Sourcing-lite — append-only log)
-- ============================================================

CREATE TABLE cycles (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id       UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    cycle_number    INT NOT NULL,                  -- 1, 2, 3... (Cycle of Cycles)
    started_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    ended_at        TIMESTAMPTZ,                   -- NULL = активний цикл
    enlightenment   BOOLEAN NOT NULL DEFAULT false,
    energy_earned   INT NOT NULL DEFAULT 0,
    shadow_data     JSONB NOT NULL DEFAULT '{}',   -- дані тіні при скиданні
    CHECK (cycle_number > 0)
);
CREATE INDEX idx_cycles_entity ON cycles(entity_id, cycle_number);

-- Фази циклу (append-only — Event Sourcing-lite без Kafka)
CREATE TABLE cycle_phases (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cycle_id        UUID NOT NULL REFERENCES cycles(id) ON DELETE CASCADE,
    phase_index     SMALLINT NOT NULL,             -- 0=Підготовка..4=Фінал
    phase_name      VARCHAR(32) NOT NULL,          -- preparation|entry|development|crisis|final
    started_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at    TIMESTAMPTZ,
    energy_delta    INT NOT NULL DEFAULT 0,        -- зміна енергії в фазі
    trait_deltas    JSONB NOT NULL DEFAULT '{}',   -- {"heart": -2, "cat": +1...}
    crisis_choices  JSONB NOT NULL DEFAULT '[]',   -- вибори гравця в Кризі
    metadata        JSONB NOT NULL DEFAULT '{}'
);
CREATE INDEX idx_cycle_phases_cycle ON cycle_phases(cycle_id, phase_index);

-- Бардо — 5 фаз (земля→вода→вогонь→повітря→світло)
CREATE TABLE bardo_phases (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id       UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    cycle_number    INT NOT NULL,
    phase_index     SMALLINT NOT NULL,             -- 0=земля..4=світло
    phase_name      VARCHAR(32) NOT NULL,
    entered_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at    TIMESTAMPTZ,
    transformation  JSONB NOT NULL DEFAULT '{}',   -- трансформація рис у фазі
    energy_spent    INT NOT NULL DEFAULT 0
);
CREATE INDEX idx_bardo_entity_cycle ON bardo_phases(entity_id, cycle_number, phase_index);

-- ============================================================
-- ЕНЕРГІЯ ТА ТРАНСФОРМАЦІЇ (аудит-трейл)
-- ============================================================

CREATE TABLE energy_transactions (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id       UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    cycle_id        UUID REFERENCES cycles(id) ON DELETE SET NULL,
    amount          INT NOT NULL,                  -- + нагорода, - витрата
    type            VARCHAR(32) NOT NULL,          -- cycle_reward|transformation|bardo|pvp_reward|synthesis
    description     TEXT,
    balance_after   INT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_energy_entity_time ON energy_transactions(entity_id, created_at DESC);

CREATE TABLE trait_transformations (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id       UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    cycle_id        UUID REFERENCES cycles(id) ON DELETE SET NULL,
    from_traits     JSONB NOT NULL,                -- {"heart":76,"cat":8...}
    to_traits       JSONB NOT NULL,
    energy_cost     INT NOT NULL,
    transformation_type VARCHAR(32) NOT NULL,      -- cycle_reward|bardo|shadow_reset|synthesis
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_transformations_entity ON trait_transformations(entity_id, created_at DESC);

-- ============================================================
-- МУЛЬТИПЛЕЄР: Echo, Resonance, Пустка PvP, Synthesis
-- ============================================================

-- Echo — асинхронні ехо інших гравців (ghost data)
CREATE TABLE echoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_entity_id UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    target_entity_id UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    cycle_number    INT NOT NULL,
    phase_index     SMALLINT NOT NULL,
    echo_data       JSONB NOT NULL,                -- сноп даних: риси, вибори, позиція
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    expires_at      TIMESTAMPTZ NOT NULL,          -- TTL для очищення
    UNIQUE (source_entity_id, target_entity_id, cycle_number, phase_index)
);
CREATE INDEX idx_echoes_target_active ON echoes(target_entity_id, expires_at) WHERE expires_at > now();
CREATE INDEX idx_echoes_source ON echoes(source_entity_id, cycle_number);

-- Resonance — синхронна/асинхронна резонансна взаємодія
CREATE TABLE resonances (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_a_id     UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    entity_b_id     UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    cycle_number    INT NOT NULL,
    resonance_type  VARCHAR(32) NOT NULL,          -- harmonic|dissonant|synthesis_seed
    strength        SMALLINT NOT NULL DEFAULT 0,   -- 0-100
    energy_bonus_a  INT NOT NULL DEFAULT 0,
    energy_bonus_b  INT NOT NULL DEFAULT 0,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    resolved_at     TIMESTAMPTZ,
    CHECK (entity_a_id != entity_b_id)
);
CREATE INDEX idx_resonances_entities ON resonances(entity_a_id, entity_b_id, cycle_number);

-- Пустка PvP — асинхронні дуелі/завали
CREATE TABLE wasteland_duels (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    challenger_id   UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    defender_id     UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    cycle_number    INT NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'pending', -- pending|active|resolved|expired
    challenger_traits JSONB NOT NULL,
    defender_traits JSONB NOT NULL,
    result          JSONB,                           -- winner, trait_damage, energy_transfer
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    resolved_at     TIMESTAMPTZ,
    expires_at      TIMESTAMPTZ NOT NULL
);
CREATE INDEX idx_wasteland_challenger ON wasteland_duels(challenger_id, status);
CREATE INDEX idx_wasteland_defender ON wasteland_duels(defender_id, status);

-- Synthesis — спільне Просвітлення / Цикл Циклів
CREATE TABLE syntheses (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_a_id     UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    entity_b_id     UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    cycle_number    INT NOT NULL,
    synthesis_type  VARCHAR(32) NOT NULL,            -- shared_enlightenment|cycle_of_cycles_seed
    energy_pool     INT NOT NULL DEFAULT 0,
    trait_gifts     JSONB NOT NULL DEFAULT '{}',     -- обмін рисами
    status          VARCHAR(32) NOT NULL DEFAULT 'pending', -- pending|active|completed|failed
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at    TIMESTAMPTZ,
    CHECK (entity_a_id != entity_b_id)
);
CREATE INDEX idx_syntheses_entities ON syntheses(entity_a_id, entity_b_id, cycle_number);

-- ============================================================
-- СИСТЕМНІ: Сесії, керування, кэш
-- ============================================================

CREATE TABLE sessions (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id       UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    token_hash      BYTEA NOT NULL,                  -- hash(token)
    ip_address      INET,
    user_agent      TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    expires_at      TIMESTAMPTZ NOT NULL,
    last_activity_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_sessions_entity ON sessions(entity_id);
CREATE INDEX idx_sessions_token ON sessions(token_hash);
CREATE INDEX idx_sessions_expires ON sessions(expires_at) WHERE expires_at > now();

-- Кеш резонансів/ехо для реального часу (Redis-like таблиця, можливо переїхати в Redis)
CREATE TABLE resonance_cache (
    entity_id       UUID PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    nearby_echoes   JSONB NOT NULL DEFAULT '[]',
    active_resonances JSONB NOT NULL DEFAULT '[]',
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

### 📋 Чек-лист індексів (✅ покрито вище)

| Таблица | Критичні індекси | Статус |
|---------|------------------|--------|
| `entities` | `(account_id)`, `(status, current_phase)` | ✅ |
| `cycles` | `(entity_id, cycle_number)` | ✅ |
| `cycle_phases` | `(cycle_id, phase_index)` | ✅ |
| `bardo_phases` | `(entity_id, cycle_number, phase_index)` | ✅ |
| `energy_transactions` | `(entity_id, created_at DESC)` | ✅ |
| `trait_transformations` | `(entity_id, created_at DESC)` | ✅ |
| `echoes` | `(target_entity_id, expires_at) WHERE expires_at > now()`, `(source_entity_id, cycle_number)` | ✅ |
| `resonances` | `(entity_a_id, entity_b_id, cycle_number)` | ✅ |
| `wasteland_duels` | `(challenger_id, status)`, `(defender_id, status)` | ✅ |
| `syntheses` | `(entity_a_id, entity_b_id, cycle_number)` | ✅ |
| `sessions` | `(entity_id)`, `(token_hash)`, `(expires_at) WHERE > now()` | ✅ |

### ❌ Зайві таблиці (якщо були в іншій схемі) — **НЕМАЄ** (схеми не було)

### ⚠️ Ризики схем
| Ризик | Мітигація |
|-------|-----------|
| JSONB в `traits`, `shadow_traits`, `echo_data` — складно індексувати по полях | Додати GIN індекси на `shadow_traits`, `echo_data` по ключових полях; розглянути витягнення `trait_*` в окремі колонки (вже зроблено в `entities`) |
| `echoes.expires_at` — TTL очистка | `pg_cron` job або pg_partman партиція по `expires_at` (monthly) |
| `cycles` + `cycle_phases` + `bardo_phases` — дублювання фаз | OK: `cycle_phases` = 5 фаз циклу, `bardo_phases` = 5 фаз Бардо (після Просвітлення) — різні домени |
| `energy_transactions` + `trait_transformations` — аудит-трейл розростається | Партиціонування по `created_at` (monthly) через `pg_partman` |

---

## 2. Backend Stack (Go / Scala / Elixir) — АУДИТ

### ❌ Вердикт: **Over-engineered для MVP**

| Мова | Роль в ТЗ | Проблема для MVP | Рекомендація |
|------|-----------|------------------|--------------|
| **Go** | API Gateway, Auth, Matchmaking, Real-time (WebSocket) | ✅ Чудовий вибір — швидкий, простий, отлична concurrency | **Залишити як MAIN stack** |
| **Scala** | Game Logic, Cycle/Phase Engine, Trait Math, Bardo Engine | ❌ Overkill: складний build (sbt/mill), складніший hiring, overkill для domain logic | **Видалити — перенести логіку в Go** |
| **Elixir** | Real-time Multiplayer (Echo/Resonance), Pub/Sub, Presence | ❌ Overkill: BEAM чудовий для presence/presence, але Go + Redis Pub/Sub/Streams покриває MVP | **Видалити — Go + Redis Streams/PubSub** |

### 📊 Cost of Complexity (MVP)

| Фактор | Go-only | Go+Scala+Elixir |
|--------|---------|-----------------|
| **Dev setup time** | ~1 день | ~1-2 тижні (3 toolchains, 3 CI, 3 deps) |
| **Hiring/onboarding** | 1 мова, великий пул | 3 мови, нічний кошмар |
| **Build/CI time** | ~2-3 хв | ~10-20 хв (sbt + mix + go) |
| **Debugging distributed trace** | 1 stack trace | 3 runtime, correlated traces |
| **Deploy units** | 1-2 сервіси | 5-8 сервісів (gateway, game-engine, realtime, auth, matching) |
| **Operational burden** | Низький | Високий (3 runtimes, 3 GC, 3 profiling tools) |

### ✅ Рекомендація: **Go-only MVP Stack**

```
┌─────────────────────────────────────────────────────────────┐
│                    BEZMEZHYA MVP BACKEND                      │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────┐  │
│  │  API Gateway │  │  Game Engine │  │  Real-time Hub     │  │
│  │  (chi/gin)   │  │  (pure Go)   │  │  (gorilla/ws +     │  │
│  │  Auth, REST, │  │  Cycle/Phase │  │   Redis Streams)   │  │
│  │  WebSocket   │  │  Trait Math  │  │  Echo/Resonance/   │  │
│  │              │  │  Bardo Logic │  │  Wasteland/Synth   │  │
│  └──────┬───────┘  └──────┬───────┘  └────────┬───────────┘  │
│         │                 │                    │              │
│         └─────────────────┼────────────────────┘              │
│                           ▼                                   │
│                  ┌──────────────────┐                         │
│                  │   PostgreSQL     │                         │
│                  │  (Primary DB)    │                         │
│                  │   + Redis        │                         │
│                  │   (Cache/Streams)│                         │
│                  └──────────────────┘                         │
└─────────────────────────────────────────────────────────────┘
```

**Go пакети для MVP:**
| Потреба | Бібліотека |
|---------|------------|
| HTTP Router | `chi` / `gin` |
| WebSocket | `gorilla/websocket` / `nhooyr/websocket` |
| Postgres | `pgx/v5` (pgxpool) |
| Redis | `redis/go-redis/v9` (Streams, PubSub, Lua scripts) |
| Config | `spf13/viper` |
| Logging | `zerolog` / `slog` (Go 1.21+) |
| Metrics | `prometheus/client_golang` |
| Migration | `golang-migrate/migrate` |
| Testing | `testify` + `sqlmock` / `testcontainers-go` |

**Scala/Elixir — повернутись пізніше (Post-MVP):**
- **Scala (Akka/pekko)** — якщо domain logic стане надзвичайно складним (Event Sourcing, CQRS, сложні saga)
- **Elixir (Phoenix Channels / LiveView)** — якщо real-time presence/echo масштабується до 100k+ CCU

---

## 3. Client (Unity) — HeartFilter / C# / Shaders / Filter Architecture

### ⚠️ Критичний знахідок: **Код клієнта НЕ НАДАНО в ТЗ/Workspace**

### 🎯 Що ПОТРІБНО для MVP на основі ТЗ

ТЗ описує: **HeartFilter/C# код, шейдери, архітектура фільтрів** — це вказівка на **пост-процесинговий ефект "Серце" (Heart Filter)** як візуалізація риси ❤ Серце (Тиферет).

### 🎨 Рекомендована архітектура клієнта (MVP)

```
Unity 2022.3 LTS / 6000 LTS
├── Rendering: URP (Universal Render Pipeline) + Custom Render Features
├── Architecture: ECS (DOTS) / Entities Package — для масштабованості MMO
├── Networking: Netcode for GameObjects (Netcode for GO) або Netcode for Entities
├── Shaders: HLSL (URP) + Compute Shaders для HeartFilter
└── Build: Addressables / AssetBundles для контент-доставки
```

#### HeartFilter Architecture (Shader + C#)

```hlsl
// Assets/Shaders/HeartFilter.hlsl
// URP Custom Renderer Feature → ScriptableRenderPass → Blit с Material
// Використовує Compute Shader для процедуральної генерації "пульсації серця"

#include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/DeclareNormals.hlsl"

Texture2D _MainTex;
SamplerState sampler_MainTex;

// Heart Filter Parameters (driven by entity.trait_heart 76→25)
float _HeartIntensity;      // 0.0 - 1.0 (maps from trait value)
float _PulseSpeed;          // BPM синхронізація з серцем гравця
float _ChromaAberration;    // RGB split при високій енергії
float _VignetteIntensity;   // затемнення країв
float4 _HeartColor;         // колір Тиферет (золото/рожеве)

struct Varyings { float4 positionCS : SV_POSITION; float2 uv : TEXCOORD0; };

Varyings Vert(Varyings input) { return input; }

float4 HeartPulse(float2 uv, float time, float intensity) {
    float dist = length(uv - 0.5);
    float pulse = sin(time * _PulseSpeed + dist * 20.0) * intensity;
    float heartShape = 1.0 - smoothstep(0.3, 0.5, dist + pulse * 0.1);
    return lerp(float4(0,0,0,0), _HeartColor, heartShape * intensity);
}

float4 Frag(Varyings input) : SV_TARGET {
    float4 color = SAMPLE_TEXTURE2D(_MainTex, sampler_MainTex, input.uv);
    float time = _Time.y;
    
    // Heart pulse effect
    float4 heart = HeartPulse(input.uv, time, _HeartIntensity);
    color.rgb += heart.rgb * heart.a;
    
    // Chromatic aberration on high energy
    if (_ChromaAberration > 0.0) {
        float2 offset = (input.uv - 0.5) * _ChromaAberration * 0.01;
        color.r = SAMPLE_TEXTURE2D(_MainTex, sampler_MainTex, input.uv + offset).r;
        color.b = SAMPLE_TEXTURE2D(_MainTex, sampler_MainTex, input.uv - offset).b;
    }
    
    // Vignette
    float vignette = 1.0 - length(input.uv - 0.5) * _VignetteIntensity;
    color.rgb *= vignette;
    
    return color;
}
```

```csharp
// Assets/Scripts/Rendering/HeartFilterFeature.cs
using UnityEngine;
using UnityEngine.Rendering.Universal;

public class HeartFilterFeature : ScriptableRendererFeature
{
    [SerializeField] private Material _heartMaterial;
    private HeartFilterPass _pass;

    public override void Create()
    {
        _pass = new HeartFilterPass(_heartMaterial);
        _pass.renderPassEvent = RenderPassEvent.BeforeRenderingPostProcessing;
    }

    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        if (_heartMaterial == null) return;
        renderer.EnqueuePass(_pass);
    }

    protected override void Dispose(bool disposing) => _pass?.Cleanup();
}

public class HeartFilterPass : ScriptableRenderPass
{
    private readonly Material _material;
    private RTHandle _cameraColorTarget;

    public HeartFilterPass(Material material)
    {
        _material = material;
        profilingSampler = new ProfilingSampler("HeartFilter");
    }

    public override void OnCameraSetup(CommandBuffer cmd, ref RenderingData renderingData)
    {
        _cameraColorTarget = renderingData.cameraData.renderer.cameraColorTargetHandle;
    }

    public override void Execute(ScriptableRenderContext context, ref RenderingData renderingData)
    {
        if (_material == null) return;
        
        var cmd = CommandBufferPool.Get("HeartFilter");
        using (new ProfilingScope(cmd, profilingSampler))
        {
            // Push trait_heart (0-100) → _HeartIntensity (0-1)
            var entity = HeartFilterController.Instance?.CurrentEntity;
            if (entity != null)
            {
                float intensity = Mathf.InverseLerp(8f, 76f, entity.TraitHeart); // 76→1.0, 8→0.0
                _material.SetFloat("_HeartIntensity", intensity);
                _material.SetFloat("_PulseSpeed", 60f + intensity * 40f); // 60-100 BPM
                _material.SetFloat("_ChromaAberration", entity.Energy > 1000 ? 1f : 0f);
                _material.SetFloat("_VignetteIntensity", 0.3f + intensity * 0.4f);
                _material.SetColor("_HeartColor", new Color(1f, 0.8f, 0.4f, 1f)); // Tiferet gold
            }

            Blitter.BlitCameraTexture(cmd, _cameraColorTarget, _cameraColorTarget, _material, 0);
        }
        context.ExecuteCommandBuffer(cmd);
        CommandBufferPool.Release(cmd);
    }
}
```

```csharp
// Assets/Scripts/Gameplay/HeartFilterController.cs
using UnityEngine;
using Unity.Netcode;

public class HeartFilterController : NetworkBehaviour
{
    public static HeartFilterController Instance { get; private set; }
    
    public EntityData CurrentEntity { get; private set; }
    
    [SerializeField] private HeartFilterFeature _heartFilterFeature;
    private Material _heartMaterial;

    private void Awake()
    {
        if (Instance != null && Instance != this) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);
        
        _heartMaterial = new Material(Shader.Find("Universal Render Pipeline/HeartFilter"));
        if (_heartFilterFeature != null)
        {
            // Reflection/injection to set material
            var field = typeof(HeartFilterFeature).GetField("_heartMaterial", 
                System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            field?.SetValue(_heartFilterFeature, _heartMaterial);
        }
    }

    public void SetEntity(EntityData entity)
    {
        CurrentEntity = entity;
        // Material updates happen in HeartFilterPass.Execute via Instance.CurrentEntity
    }

    // Network sync: trait_heart changes → sync to all clients observing this entity
    [ServerRpc(RequireOwnership = false)]
    public void SyncHeartTraitServerRpc(ushort heartValue, NetworkConnectionToClient sender = default)
    {
        if (IsServer)
        {
            SyncHeartTraitClientRpc(heartValue);
        }
    }

    [ClientRpc]
    public void SyncHeartTraitClientRpc(ushort heartValue)
    {
        if (CurrentEntity != null)
            CurrentEntity.TraitHeart = heartValue;
    }
}

[System.Serializable]
public struct EntityData : INetworkSerializable
{
    public ulong NetworkId;
    public ushort TraitHeart;
    public ushort TraitCat;
    public ushort TraitHead;
    public ushort TraitTractor;
    public int Energy;
    public byte CurrentPhase;
    public byte Status;
    
    public void NetworkSerialize<T>(BufferSerializer<T> serializer) where T : IReaderWriter
    {
        serializer.SerializeValue(ref NetworkId);
        serializer.SerializeValue(ref TraitHeart);
        serializer.SerializeValue(ref TraitCat);
        serializer.SerializeValue(ref TraitHead);
        serializer.SerializeValue(ref TraitTractor);
        serializer.SerializeValue(ref Energy);
        serializer.SerializeValue(ref CurrentPhase);
        serializer.SerializeValue(ref Status);
    }
}
```

### ⚡ Спрощення Unity Architecture для MVP

| Поточна складність (за ТЗ) | MVP Спрощення |
|----------------------------|---------------|
| HeartFilter/C# + Shaders + Filter Architecture | **URP Custom Render Feature + 1 Material + 1 Compute Shader** |
| ECS/DOTS повністю | **Hybrid: GameObjects для MVP, міграція в DOTS post-MVP** |
| Netcode for Entities | **Netcode for GameObjects (NGO) — швидше прототипувати** |
| Власна архітектура фільтрів | **URP Renderer Features (standard)** |
| Синхронізація 4 рис + енергії + фаз | **NetworkVariable<EntityData> + RPC для подій (фази, енергія)** |

**Unity Packages для MVP:**
```json
{
  "dependencies": {
    "com.unity.render-pipelines.universal": "14.x",
    "com.unity.netcode.gameobjects": "1.7.x",
    "com.unity.transport": "2.2.x",
    "com.unity.services.authentication": "2.x",
    "com.unity.services.core": "1.x",
    "com.unity.addressables": "1.23.x"
  }
}
```

---

## 4. Event Sourcing (Kafka) — АУДИТ

### ❌ Вердикт: **Kafka — Overkill для MVP**

| Критерій | Kafka | MVP Reality |
|----------|-------|-------------|
| **Ops complexity** | Зookeeper/KRaft, partitions, replication, monitoring | 3+ сервери, спеціалізовані DevOps |
| **Latency** | ~2-5ms (added hop) | Overhead для real-time game loop |
| **Throughput need** | 1M+ msg/sec | MVP: <10K msg/sec (Echo/Resonance) |
| **Replay/Event Sourcing** | Native | **Не потрібен для MVP** — PostgreSQL append-only tables вистачає |
| **Team expertise** | Спеціалізована | Go team не знає Kafka internals |

### ✅ Що потрібно для MVP Multiplayer (Async)

| Фीचер | Потрібен Kafka? | Альтернатива |
|--------|----------------|--------------|
| **Echo** (async ghost data) | ❌ | **PostgreSQL `echoes` table + Redis cache** (TTL) |
| **Resonance** (near real-time) | ❌ | **Redis Pub/Sub + Redis Streams** (consumer groups) |
| **Wasteland PvP** (async duels) | ❌ | **PostgreSQL `wasteland_duels` + polling/WebSocket** |
| **Synthesis** (co-op enlightenment) | ❌ | **Redis Streams (consumer groups) + PG persistence** |
| **Event Sourcing / Audit Log** | ❌ | **PostgreSQL append-only tables (`cycle_phases`, `energy_transactions`)** |
| **Cross-service events** | ❌ (single Go service) | **In-process Go channels / Redis Streams** |

### 🎯 Рекомендація: **Redis Streams + PostgreSQL LISTEN/NOTIFY**

```go
// Go: Redis Streams для real-time multiplayer events
package realtime

import (
    "context"
    "encoding/json"
    "github.com/redis/go-redis/v9"
)

type EventBus struct {
    client *redis.Client
}

func NewEventBus(addr string) *EventBus {
    return &EventBus{client: redis.NewClient(&redis.Options{Addr: addr})}
}

// Echo event — записуємо в Stream + PG (async)
func (eb *EventBus) PublishEcho(ctx context.Context, echo EchoEvent) error {
    data, _ := json.Marshal(echo)
    // Redis Stream: MAXLEN ~ 10000 per entity, TTL via XTRIM
    return eb.client.XAdd(ctx, &redis.XAddArgs{
        Stream: "echo:" + echo.TargetEntityID,
        MaxLen: 10000,
        Values: map[string]interface{}{"data": data},
    }).Err()
}

// Resonance — Pub/Sub для low-latency
func (eb *EventBus) PublishResonance(ctx context.Context, resonance ResonanceEvent) error {
    data, _ := json.Marshal(resonance)
    return eb.client.Publish(ctx, "resonance:"+resonance.CycleNumber, data).Err()
}

// Subscribe to Resonance (goroutine per connection)
func (eb *EventBus) SubscribeResonance(ctx context.Context, cycleNum int, handler func(ResonanceEvent)) {
    pubsub := eb.client.Subscribe(ctx, "resonance:"+strconv.Itoa(cycleNum))
    for msg := range pubsub.Channel() {
        var ev ResonanceEvent
        json.Unmarshal([]byte(msg.Payload), &ev)
        handler(ev)
    }
}
```

```sql
-- PostgreSQL LISTEN/NOTIFY для простих cross-process notifications
-- Використовується для: session invalidation, cache invalidation, admin events

-- Server-side (Go): LISTEN channel
-- Client-side (Go): NOTIFY channel, 'payload'

-- Example: Invalidate resonance_cache on new resonance
CREATE OR REPLACE FUNCTION notify_resonance_cache_invalidation()
RETURNS TRIGGER AS $$
BEGIN
    PERFORM pg_notify('resonance_cache_invalidate', 
        json_build_object('entity_a', NEW.entity_a_id, 'entity_b', NEW.entity_b_id)::text);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER resonance_cache_invalidate
AFTER INSERT ON resonances
FOR EACH ROW EXECUTE FUNCTION notify_resonance_cache_invalidation();
```

---

## 5. Пропозиції Спрощення для MVP (БЕЗ ВТРАТИ МАСШТАБОВАНОСТІ)

### 🎯 MVP Scope Definition (6-8 тижнів, 2-3 розробники)

| Включено в MVP | Виключено з MVP (Post-MVP) |
|----------------|----------------------------|
| ✅ Single-player Cycle (Prep → Entry → Dev → Crisis → Final) | ❌ Bardo (5 phases) — добавити v0.2 |
| ✅ 4 Traits + Energy + Transformations | ❌ Cycle of Cycles (Shadow Reset) — v0.3 |
| ✅ Echo (async ghosts from other players) | ❌ Resonance (real-time sync) — v0.2 |
| ✅ PostgreSQL persistence (append-only cycle log) | ❌ Wasteland PvP — v0.3 |
| ✅ Go Backend (REST + WebSocket) | ❌ Synthesis (co-op enlightenment) — v0.4 |
| ✅ Unity URP + HeartFilter (visual trait) | ❌ Scala/Elixir services |
| ✅ Redis Streams (Echo pub/sub) | ❌ Kafka / Event Sourcing framework |
| ✅ Auth (JWT) + Session management | ❌ Full Event Sourcing / CQRS |

### 📦 Архітектурні принципи "Scalable MVP"

```go
// internal/architecture/ports.go — Порти (Interfaces) для розділення
// Реалізація зараз: In-memory/Postgres/Redis
// Пізніше: замінити на Kafka/EventStoreDB без зміни domain logic

package domain

// EventStore — порт для подій (Event Sourcing-lite)
type EventStore interface {
    Append(ctx context.Context, events []Event) error
    Load(ctx context.EntityID) ([]Event, error)
    Subscribe(ctx context.Context, entityID EntityID, handler EventHandler) error
}

// Cache — порт для кешу/реального часу
type Cache interface {
    SetEcho(ctx context.Context, echo Echo) error
    GetEchoes(ctx context.Context, entityID EntityID) ([]Echo, error)
    PubResonance(ctx context.Context, resonance Resonance) error
    SubResonance(ctx context.Context, cycle int, handler ResonanceHandler) error
}

// Реалізація зараз: PostgresEventStore + RedisCache
// Post-MVP: KafkaEventStore + RedisCache (або Kafka Streams)
```

### 🔄 Migration Path (MVP → Scale)

| Етап | Backend | Event Transport | Persistence | Unity |
|------|---------|-----------------|-------------|-------|
| **MVP (0.1)** | Go (monolith) | Redis Streams + PG LISTEN/NOTIFY | PostgreSQL (append-only tables) | URP + NGO |
| **v0.2 (Resonance)** | Go (modular monolith) | Redis Streams (consumer groups) | + Read Models (materialized views) | + DOTS migration start |
| **v0.3 (Wasteland/PvP)** | Go services (Auth, Game, Real-time) | Redis Streams + NATS JetStream | + CQRS read replicas | Netcode for Entities |
| **v1.0 (Scale)** | Go + **Scala (Game Logic)** | **Kafka / Redpanda** | EventStoreDB + PG | Full DOTS/ECS |
| **v2.0 (Massive)** | + **Elixir (Presence/Chat)** | Kafka + **Flink** (stream processing) | ClickHouse (analytics) | Custom rendering |

---

## 6. Альтернативні Технічні Рішення

### 6.1 Kafka → Redis Streams / PostgreSQL LISTEN/NOTIFY

| Критерій | Kafka | Redis Streams | PG LISTEN/NOTIFY |
|----------|-------|---------------|------------------|
| **Ops** | Складний (ZK/KRaft, partitions, rebalancing) | Простий (single Redis, optional Cluster) | Найпростіший (built-in) |
| **Persistence** | Disks (configurable retention) | Memory + AOF/RDB (не для довгостроку) | Только notification (no persistence) |
| **Consumer Groups** | Native | Native (XREADGROUP) | ❌ (тільки broadcast) |
| **Replay/Seek** | Native (offsets) | Native (IDs) | ❌ |
| **Throughput** | 1M+/sec | ~100K/sec (single node) | ~10K/sec (notify overhead) |
| **Ordering** | Per-partition | Per-stream | Per-connection |
| **MVP Fit** | ❌ | ✅ **Best** | ✅ Для cache invalidation |

**Рекомендація MVP:**
```
┌──────────────────────────────────────────────────────────────┐
│  Redis Streams — ГОЛОВНИЙ EVENT BUS для MVP                   │
│  ├── Echo events: Stream per target entity (XADD, XREADGROUP)│
│  ├── Resonance: Pub/Sub (SUBSCRIBE/PUBLISH) — low latency    │
│  ├── Wasteland/Synthesis: Streams with consumer groups       │
│  └── TTL via MAXLEN + scheduled XTRIM (or Redis keyspace)    │
│                                                              │
│  PostgreSQL LISTEN/NOTIFY — для cross-process signals        │
│  ├── Session invalidation (multi-instance Go)                │
│  ├── Cache invalidation (resonance_cache table)              │
│  └── Admin/DevOps events                                     │
└──────────────────────────────────────────────────────────────┘
```

### 6.2 Scala → Go (Migration Path)

| Scala Feature | Go Equivalent | Effort |
|---------------|---------------|--------|
| Case Classes / ADT | `struct` + `interface` + type switches | Low |
| Pattern Matching | Type switches / `switch` на interface | Low |
| Futures / Monads | Goroutines + Channels / `errgroup` | Medium |
| Akka Actors | **Не потрібно для MVP** — Go structs + channels | N/A |
| Akka Persistence | **EventStore в PG** (append-only tables) | Low |
| Akka Cluster / Sharding | **Redis Streams + Consumer Groups** | Low |
| Cats/Effect/IO | Standard library / `go.uber.org/fx` (DI) | Low |

**Стратегія:** Не переписувати Scala → Go. **Написати Game Logic на Go з дня 1.**  
Scala повертається лише якщо domain logic стає невиносимо складним (complex saga, temporal workflows).

### 6.3 Unity Architecture Simplification

| Поточна (за ТЗ) | Спрощена MVP | Міграція |
|-----------------|--------------|----------|
| Custom Filter Architecture | **URP ScriptableRendererFeature** | 1 файл → стандартний API |
| HeartFilter C# + Shaders | **1 Compute Shader + 1 Material + 1 Render Feature** | Мінімум коду |
| ECS/DOTS повністю | **Hybrid: MonoBehaviour + Netcode for GO** | Post-MVP: поступова міграція в Entities |
| Custom Network Sync | **NetworkVariable<EntityData> + RPC** | Built-in NGO |
| Shader Graph / URP | **HLSL Compute Shader для HeartFilter** | Контроль продуктивності |

---

## 7. Підсумкові Висновки та План Дій

### 🎯 Top 5 Critical Actions для MVP

| # | Дія | Owner | Timeline | Impact |
|---|-----|-------|----------|--------|
| **1** | **Створити SQL схему** (12-15 таблиць, індекси, партіції) | Backend Lead | Тиждень 1 | **Блокує весь backend** |
| **2** | **Вибрати Go-only stack**, видалити Scala/Elixir з репозиторію | Tech Lead | День 1 | -70% ops complexity |
| **3** | **Налаштувати Redis Streams** як event bus (Echo/Resonance) | Backend | Тиждень 1-2 | Замінює Kafka |
| **4** | **Unity: URP + HeartFilter Render Feature** (1 shader, 1 C# script) | Client Lead | Тиждень 1-2 | Візуалізація риси Серце |
| **5** | **Визначити MVP Scope** (Cycle only, Echo only, No Bardo/PvP/Synthesis) | PM + Tech Lead | День 1 | Фокус, швидкий реліз |

### 📋 Definition of Done для MVP (v0.1)

- [ ] PostgreSQL схема розгорнута, міграції пройдені
- [ ] Go сервіс: Auth (JWT), Entity CRUD, Cycle/Phase state machine
- [ ] Redis Streams: Echo publish/subscribe working
- [ ] Unity: HeartFilter відображає `trait_heart` (76→25 пульсація)
- [ ] Netcode for GO: EntityData синхронізується (4 риси + енергія + фаза)
- [ ] Single-player цикл: Підготовка → Вхід → Розвиток → Криза → Фінал (консоль/лог)
- [ ] CI/CD: Go build + test, Unity build (GitHub Actions)

### ⚠️ Ризики та Мітигації

| Ризик | Ймовірність | Вплив | Мітигація |
|-------|-------------|-------|-----------|
| **Scope creep** (Bardo/PvP в MVP) | Висока | Critical | **Жорсткий PM control**, Definition of Done |
| **Unity DOTS complexity** | Середня | High | **Почати з MonoBehaviour/NGO**, мігрувати пізніше |
| **Redis Streams scaling** | Низька (MVP) | Medium | Почати з single Redis, Cluster пізніше |
| **PostgreSQL write throughput** | Низька | Low | Append-only tables, партиціонування по `created_at` |
| **Team не знає Go/Redis/URP** | Середня | Medium | 1 тиждень onboarding, pair programming |

---

## Додаток А: Швидкий старт (Starter Kit Structure)

```
/bezmezhya
├── backend/
│   ├── cmd/server/main.go           # Entry point
│   ├── internal/
│   │   ├── auth/                    # JWT, sessions
│   │   ├── entity/                  # Entity aggregate (traits, energy, cycles)
│   │   ├── cycle/                   # Cycle/Phase state machine
│   │   ├── echo/                    # Echo domain + Redis Streams
│   │   ├── resonance/               # Resonance domain + Redis PubSub
│   │   ├── persistence/
│   │   │   ├── postgres/            # pgx repositories
│   │   │   └── redis/               # Redis client wrappers
│   │   └── api/
│   │       ├── rest/                # Chi/Gin handlers
│   │       └── ws/                  # WebSocket hub (Netcode relay)
│   ├── migrations/                  # golang-migrate SQL files
│   ├── go.mod / go.sum
│   └── Dockerfile
├── client/
│   ├── Assets/
│   │   ├── Scripts/
│   │   │   ├── Rendering/HeartFilterFeature.cs
│   │   │   ├── Rendering/HeartFilterPass.cs
│   │   │   ├── Gameplay/HeartFilterController.cs
│   │   │   ├── Network/EntityData.cs
│   │   │   └── Network/GameNetworkManager.cs
│   │   ├── Shaders/HeartFilter.hlsl
│   │   └── URP/HeartFilterRendererFeature.asset
│   ├── Packages/manifest.json
│   └── ProjectSettings/
├── infra/
│   ├── docker-compose.yml           # Postgres + Redis + Go + Unity Builder
│   ├── postgres/init/01-schema.sql  # Схема з розділу 1
│   └── k8s/                         # Post-MVP
└── docs/
    └── ARCHITECTURE_DECISIONS.md    # ADR log
```

---

*Звіт сформовано на основі ТЗ «Безмежжя» v6.0. Кодова база не наявна в workspace — аудит базується виключно на описаній архітектурі та доменній логіці.*