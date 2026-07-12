---
type: concept
title: Local LLM Hardware
description: Апаратне забезпечення для локального інференсу LLM: GPU з достатнім VRAM, CPU, RAM та NVMe SSD.
created: 2026-07-05
updated: 2026-07-05
tags: [architecture, automation, mcp]
sources: [raw/articles/rtx-5070-ti-build-reference.md]
confidence: medium
contested: false
links: [rtx-5070-ti, llm-wiki, model-context-protocol]
---# Local LLM Hardware

Апаратне забезпечення для локального інференсу LLM визначається трьома ключовими параметрами: **VRAM GPU**, **швидкість CPU** для попередньої обробки, та **швидкість NVMe SSD** для завантаження моделей.

## Ключові вимоги

### GPU (найважливіший компонент)
- **VRAM**: мінімум 8 GB для 7B-моделей, 16 GB для 14B, 24 GB+ для 30B+
- **Тип пам'яті**: GDDR6X/GDDR7 — вища пропускна здатність = швидший інференс
- **Tensor Cores**: покоління 4+ для кращого INT8/FP8
- **Приклад**: [[rtx-5070-ti]] (16 GB GDDR7) — оптимальний баланс ціна/продуктивність

### CPU
- Кількість потоків впливає на preprocessing та batch-інференс
- Приклад: AMD Ryzen 7 9700X (8c/16t, 5.5 ГГц) — достатньо для більшості задач
- Для великих моделей (>30B) — бажано 16+ потоків

### RAM
- Мінімум 32 GB DDR5 для системи + LLM
- Для контекстів >128K — 64 GB+
- Частота: 6000 MHz для Ryzen 9000 (EXPO 1:1)

### SSD
- NVMe PCIe 4.0/5.0 для швидкого завантаження моделей
- Моделі LLM займають 5-15 GB кожна
- Приклад: Samsung 990 EVO Plus (7250 MB/s, TLC з DRAM)

### Блок живлення
- Запас 40%+ від пікового споживання
- Для збірки з RTX 5070 Ti: 850W Gold — оптимально
- Пікове споживання (LLM інференс): ~280-320W

## Типові конфігурації

| Бюджет | GPU | VRAM | Моделі | Приклад |
|---|---|---|---|---|
| Бюджетний | RTX 4060 Ti 16GB | 16 GB | 7B-14B | — |
|| Середній | RTX 5070 Ti | 16 GB | 7B-14B | [[rtx-5070-ti]] |
| Високий | RTX 4090 24GB | 24 GB | 14B-34B | — |
| Ентерпрайз | RTX 6000 Ada 48GB | 48 GB | 30B+ | — |

## Цікаві факти

- GPU має становити 40-50% бюджету збірки
- 16 GB VRAM — "золота середина" для локальних LLM
- Для 70B+ моделей потрібні multi-GPU або 24 GB+ VRAM

# Citations
[1] [RTX 5070 Ti Build Reference raw source](../../raw/articles/rtx-5070-ti-build-reference.md)
