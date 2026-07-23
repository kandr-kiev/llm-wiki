---
title: Luke's Dev Lab YouTube Repo
type: concept
tags: [youtube, prompts, model-configs, llama-cpp, benchmarking]
sources: [raw/articles/lukesdevlab-youtube-model-configs.ini]
confidence: high
links: [mattpocock-skills-repo, llama-cpp, qwen-models]
created: 2026-07-24
updated: 2026-07-24
---

# Luke's Dev Lab YouTube Repo

> **Джерело:** [github.com/lukesdevlab/youtube](https://github.com/lukesdevlab/youtube)
> **Опис:** Промпти та конфігурації моделей для YouTube-відео

## Визначення

Репозиторій містить набір промптів (prompt-файлів) та конфігураційних файлів моделей, що використовуються у YouTube-відео lukesdevlab. Включає benchmark-дані та детальні налаштування llama.cpp.

## Ключові компоненти

### 1. Prompts Directory

Набір текстових промптів для різних проектів:

- **sand-physics.txt** — симуляція піску
- **reasoning.txt** — тестування reasoning-моделей
- **kanban.txt** — Kanban-додаток (vanilla HTML/CSS/JS)
- **memory-match.txt** — гра на запам'ятовування
- **godot-rope-bridge-2d.txt** — Godot 2D фізика
- **godot-marble-run-3d.txt** — Godot 3D marble run
- **fake-desktop.txt** — імітація десктопного середовища
- **expense-tracker.txt** — трекер витрат
- **dungeon-game.txt** — roguelike гра
- **driving-2d.txt** — 2D їзда
- **breakout.txt** — breakout/gravity game
- **blender-marble-assets.txt** — Blender assets
- **agent-maze.txt** — agent maze
- **adherence.txt** — adherence testing

### 2. Model Configs (model-configs.ini)

Детальні конфігурації llama.cpp для 40+ профілів моделей:

| Категорія | Моделі |
|---|---|
| **Gemma 4** | 12B (IQ4_NL, Q8_K_XL, Q4_K_M, QAT, BF16, Coder) |
| **Gemma 4 26B** | A4B, QAT, Coding variants |
| **DiffusionGemma** | 26B (GPU/CPU) |
| **Qwen 3.5/3.6** | 9B, 14B, 27B, 35B (MTP, Q4_K_M, IQ4_NL) |
| **Specialized** | AgentWorld, ThinkingCap, FableVibes, Ternary Bonsai, North Mini Code |
| **Coding** | Ornith, Qwythos, Agents-A1, Nex-N2-mini |

### 3. Benchmark Data

- **performance-benchmark-overview.html** — performance benchmarks
- **agency-benchmark-overview.html** — agency benchmarks

## Технічні деталі

### Конфігураційні параметри

```ini
; Shared defaults
t = 12              # temperature
b = 2048            # batch size
flash-attn = on     # flash attention
cache-type-k = q8_0 # KV cache type K
cache-type-v = q8_0 # KV cache type V
mlock = true        # memory lock
jinja = true        # Jinja templating
```

### Speculative Decoding (MTP)

Деякі моделі використовують MTP (Multi-Token Prediction):

```ini
spec-type = draft-mtp
spec-draft-n-max = 6    # max draft tokens
np = 1                  # parallel prompt processing
fit = on                # GPU fit mode
fit-target = 256        # target layers
```

### VRAM Management

Для GPU з обмеженою пам'яттю (16GB):

```ini
fit = on
fit-target = 256        # split layers across VRAM/RAM
np = 1                  # no parallel processing
mlock = false           # no memory lock
```

## Зв'язки

- **mattpocock-skills-repo** — альтернативний набір agent skills
- **llama-cpp** — інференс-енджин для GGUF моделей
- **qwen-models** — сімейство Qwen моделей
- **gemma-models** — сімейство Gemma моделей

## Джерела

- [lukesdevlab/youtube](https://github.com/lukesdevlab/youtube) — GitHub репозиторій
- [model-configs.ini](raw/articles/lukesdevlab-youtube-model-configs.ini) — конфігурації

## Citations

[1] https://github.com/lukesdevlab/youtube
[2] https://github.com/lukesdevlab/youtube/blob/main/model-configs.ini
