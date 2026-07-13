---
title: "🖥️ Збірка RTX 5070 Ti — Фінальна оцінка"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - cuda
  - gpu
  - hardware
  - llama
  - llm
  - open-source
  - stable-diffusion
---
# 🖥️ Збірка RTX 5070 Ti — Фінальна оцінка

> **Source:** rtx-5070-ti-build-reference.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: raw/rtx-5070-ti-build-reference.md ingested: 2026-07-05 sha256: 6896ccadbb6a741378161b1ff0f42411dc90cff234f3c349e5d8151a0eb46eff --- --- type: Reference title: "Збірка RTX 5070 Ti — Фі...
> **Sources:**
>   - rtx-5070-ti-build-reference.md
> **Links:**
- [[rtx-5070-ti-build-reference]]
- [[local-llm-hardware]]
- [[rtx-5070-ti]]
- [[llm-deployment-qa]]
- [[аудит-крон-завдань-llm-wiki-детальний-звіт]]

## Key Findings

---
source_url: raw/rtx-5070-ti-build-reference.md
ingested: 2026-07-05
sha256: 6896ccadbb6a741378161b1ff0f42411dc90cff234f3c349e5d8151a0eb46eff
---

# 🖥️ Збірка RTX 5070 Ti — Фінальна оцінка
## Загальна оцінка
- **Рейтинг:** 9.4 / 10 ⭐
- **Статус:** ✅ ГОТОВО
- **Рекомендація:** БЕЗ ЗМІН
## 📋 Специфікація
| Компонент | Модель | Ціна |
|---|---|---|
| CPU | AMD Ryzen 7 9700X Tray | 11 799 ₴ |
| Кулер | be quiet! Pure Rock 3 Black | ~1 399 ₴ |
| Материнка | ASUS ROG Strix B850-F Gaming Wi-Fi | 11 899 ₴ |
| RAM | Goodram IRDM Black DDR5-6000 32GB CL30 | 25 099 ₴ |
| GPU | ASUS PRIME RTX 5070 Ti OC 16GB GDDR7 | 56 099 ₴ |
| SSD | Samsung 990 EVO Plus 2TB NVMe | 13 699 ₴ |
| БЖ | be quiet! Pure Power 13M 850W Gold | 5 329 ₴ |
| Корпус | be quiet! Light Base 500 Black | 4 799 ₴ |
| **РАЗОМ** | | **~130 000 ₴** |
## ⭐ Оцінки компонентів
| Компонент | Оцінка | Статус | Пояснення |
|---|---|---|---|
| CPU | ⭐⭐⭐⭐⭐ | ✅ | Ідеально для геймінгу, AI, програмування |
| Кулер CPU | ⭐⭐⭐⭐☆ | ✅ | Достатньо для 9700X; PBO 88W — комфортно |
| Материнка | ⭐⭐⭐⭐⭐ | ✅ | Overkill у хорошому сенсі; VRM 16+2+2, PCIe 5.0, Wi-Fi 7 |
| RAM | ⭐⭐⭐⭐⭐ | ✅ | Оптимальна для Ryzen 9000; стабільний EXPO 1:1 @ 6000 МГц |
| GPU | ⭐⭐⭐⭐⭐ | ✅ | Топ співвідношення ціна/продуктивність для AI; 16 GB GDDR7 |
| SSD | ⭐⭐⭐⭐⭐ | ✅ | PCIe 4.0/5.0 dual-mode, 7250 MB/s, TLC з DRAM |
| БЖ | ⭐⭐⭐⭐⭐ | ✅ | 850W Gold, запас 40%+, тихий, надійний |
| Корпус | ⭐⭐⭐⭐⭐ | ✅ | Mesh, 2.5 слота для GPU, місце для 4x 120mm |
| Вентилятори | ⭐⭐⭐⭐☆ | ✅ | 4x 120mm встановлено; достатньо, не ідеально |
## 🎯 Призначення — ефективність
| Задача | Придатність | Швидкість/Продуктивність |
|---|---|---|
| Локальні LLM (Ollama/llama.cpp) | 🔥🔥🔥🔥🔥 | Llama 3 8B: ~105 ток/с; Qwen2.5 14B: ~50 ток/с |
| Геймінг 1440p 144Гц | 🔥🔥🔥🔥🔥 | Ultra налаштування, DLSS 4 |
| Геймінг 4K | 🔥🔥🔥🔥☆ | High/Ultra з DLSS, нативний — компроміси |
| AI-генерація (Stable Diffusion/Flux) | 🔥🔥🔥🔥🔥 | 16 GB VRAM + Tensor ядра 5-gen |
| Відеомонтаж | 🔥🔥🔥🔥☆ | NVENC + швидкий SSD |
| Стримінг | 🔥🔥🔥🔥🔥 | NVENC AV1, 8c/16t CPU |
| Програмування/компіляція | 🔥🔥🔥🔥🔥 | 16 потоків, 5.5 ГГц, 32MB L3 — топ |
| 70B+ LLM локально | 🔥☆☆☆☆ | ❌ 16 GB VRAM — не вміщується |
## 💰 Ціноутворення
| Категорія | Бюджет | % від загального |
|---|---|---|
| GPU | 56 099 ₴ | 43% |
| RAM + SSD | 38 798 ₴ | 30% |
| CPU + кулер | 13 198 ₴ | 10% |
| Материнка | 11 899 ₴ | 9% |
| БЖ + корпус | 10 128 ₴ | 8% |
**Правило балансу:** GPU = 40-50% бюджету ✅
## ⚡ Потужність системи
| Режим | Споживання | Запас БЖ |
|---|---|---|
| Простій | ~80-120W | ~90% |
| Геймінг | ~350-400W | ~55% |
| LLM інференс | ~280-320W | ~65% |
| Стрес-тест (FurMark + Cinebench) | ~450-480W | ~45% |
**850W Gold:** оптимальний запас для тиші та д

## Summary

See Key Findings for full content.

## Related Articles

- [[rtx-5070-ti-build-reference]]
- [[local-llm-hardware]]
- [[rtx-5070-ti]]
- [[llm-deployment-qa]]
- [[аудит-крон-завдань-llm-wiki-детальний-звіт]]
