---
title: Shared Canon — Dataview Queries
type: query
tags: [shared-canon, dataview, knowledge-base, curation]
sources: []
confidence: high
links: [llm-wiki, obsidian, graphify-bridge]
created: 2026-07-24
updated: 2026-07-24
---

# Shared Canon — Dataview Queries

> **Призначення:** Ці запити створені для Obsidian Dataview plugin. Вони вибирають "канонічні" знання з wiki — ті, що пройшли верифікацію, мають високі confidence scores, і є ключовими для системи.

> **Як використовувати:** Вставте ці запити у Obsidian як Dataview blocks у будь-якій сторінці. Вони автоматично генерують таблиці з актуальними даними.

---

## Query 1: Канонічні концепції (High Confidence)

```dataview
TABLE confidence AS "Confidence", length AS "Lines", updated AS "Updated"
FROM "concepts"
WHERE confidence = "high" OR confidence = "verified"
SORT updated DESC
LIMIT 50
```

**Що вибирає:** Концепції з високим рівнем довіри — основа Shared Canon.

---

## Query 2: Страниці, що потребують оновлення (Low Confidence)

```dataview
TABLE confidence AS "Confidence", sources AS "Sources", updated AS "Updated"
FROM "concepts" OR "synthesis"
WHERE confidence = "low"
SORT updated ASC
LIMIT 30
```

**Що вибирає:** Сторінки з низькою впевненістю — кандидаті для review або оновлення.

---

## Query 3: Сторінки без джерел (Orphan Data)

```dataview
TABLE type AS "Type", length AS "Lines", created AS "Created"
FROM "concepts" OR "synthesis" OR "playbooks"
WHERE length(sources) = 0
AND type != "concept" AND type != "query"
SORT created ASC
LIMIT 50
```

**Що вибирає:** Сторінки без вказаних джерел — потенційні orphans або сторінки, що потребують provenance.

---

## Query 4: Великі сторінки (Candidate for Splitting)

```dataview
TABLE length AS "Lines", type AS "Type", confidence AS "Confidence"
FROM "concepts" OR "synthesis" OR "playbooks"
WHERE length > 200
SORT length DESC
LIMIT 30
```

**Що вибирає:** Сторінки понад 200 рядків — кандидати для розбиття на менші.

---

## Query 5: Сторінки з протиріччями (Contested)

```dataview
TABLE contested AS "Contested", contradictions AS "Contradictions", updated AS "Updated"
FROM "concepts" OR "synthesis"
WHERE contested = true
OR length(contradictions) > 0
SORT updated DESC
```

**Що вибирає:** Сторінки з позначками `contested: true` або `contradictions:` — потребують ручного review.

---

## Query 6: Найновіші зміни (Recent Activity)

```dataview
TABLE type AS "Type", confidence AS "Confidence", length AS "Lines"
FROM "concepts" OR "synthesis" OR "playbooks"
WHERE updated >= date(2026-07-17)
SORT updated DESC
LIMIT 50
```

**Що вибирає:** Сторінки, оновлені за останні 7 днів — показує активність wiki.

---

## Query 7: Тематичні спільноти (Tag Analysis)

```dataview
TABLE length AS "Pages", file.count AS "Pages Count"
FROM "concepts" OR "synthesis" OR "playbooks"
FLATTEN tags AS tag
GROUP BY tag
SORT Pages Count DESC
LIMIT 30
```

**Що вибирає:** Теги з найбільшою кількістю сторінок — показує ключові теми wiki.

---

## Query 8: Entity-Concept Connections

```dataview
TABLE links AS "Outbound Links", length AS "Lines", confidence AS "Confidence"
FROM "entities"
WHERE length(links) > 0
SORT length(links) DESC
LIMIT 30
```

**Що вибирає:** Entity-сторінки з найбільшою кількістю зв'язків — центральні вузли knowledge graph.

---

## Query 9: Synthesis Pages (Cross-Source)

```dataview
TABLE length AS "Lines", confidence AS "Confidence", updated AS "Updated"
FROM "synthesis"
SORT length DESC
```

**Що вибирає:** Усі synthesis-сторінки — сторінки, що об'єднують кілька джерел.

---

## Query 10: Playbooks (Actionable Knowledge)

```dataview
TABLE length AS "Lines", confidence AS "Confidence", updated AS "Updated"
FROM "playbooks"
WHERE confidence = "high" OR confidence = "verified"
SORT length DESC
```

**Що вибирає:** Практичні playbooks з високим confidence — actionable knowledge для системи.

---

## Як додати новий запит

1. Створіть новий блок `query-<name>.md` у `wiki/queries/`
2. Додайте Dataview query у форматі вище
3. Оновіть `wiki/queries/README.md` з описом нового запиту
4. Завантажте у Obsidian — запит автоматично рендериться

---

## Примітки

- Ці запити працюють тільки з **Obsidian Dataview plugin** встановленим
- Для headless-режиму (server) використовуйте `wiki_graph_generator.py` замість Dataview
- Для cron-аналізу використовуйте `wiki_proposer.py` (див. Wiki Proposer cron)
- Dataview queries — це **Shared Canon** у реальному часі: вони показують актуальний стан wiki без ручного review
