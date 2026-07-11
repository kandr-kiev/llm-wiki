# tools/

Інфраструктурні скрипти LLM Wiki. Всі інструменти залежать від `utils.py` як єдиного джерела правди для хешування, frontmatter та тегів.

## Архітектура інструментів

```
utils.py (єдине джерело правди)
├── split_frontmatter()      — парсинг frontmatter (find-based)
├── compute_sha256()         — хешування тіла (NO .strip())
├── parse_simple_yaml()      — парсинг YAML frontmatter
├── verify_file_hash()       — перевірка хешу файлу → {status, stored, computed}
├── check_raw_integrity()    — сканування raw/ → {total, ok, mismatch, no_hash, no_fm}
├── fix_file_hash()          — оновлення хешу у frontmatter
├── build_frontmatter()      — генератор frontmatter для нових файлів
├── slugify()                — уніфікована генерація slug
├── APPROVED_TAGS            — словник валідних тегів (262 шт.)
└── print_status()           — канонічний формат статусу для cron

Инструменти, що використовують utils.py:
├── check_new_raw.py         → check_raw_integrity() — виявляє нові raw файли
├── verify_hashes.py         → check_raw_integrity() — верифікація хешів
├── wiki_lint.py             → utils.* — лінтинг wiki (теги, frontmatter, хеші)
├── rss_monitor.py           → utils.* — RSS-сканер
├── github_release_monitor.py → utils.* — моніторинг GitHub релізів
└── fix_sha256.py            → utils.* — оновлення хешів (використовується вручну)
```

## Запуск

```bash
# З кореня репозиторію:
python3 tools/check_new_raw.py
python3 tools/verify_hashes.py
python3 tools/wiki_lint.py
python3 tools/rss_monitor.py

# Або безпосередньо з директорії tools/:
cd tools && python3 check_new_raw.py
```

Скрипти автоматично додають `tools/` до `sys.path` при запуску як `python3 tools/script.py`.

## Ключові рішення

- **Уніфіковане хешування**: `compute_sha256()` НЕ виконує `.strip()` — відповідає байтовій точності `fix_sha256.py`
- **Frontmatter парсинг**: `split_frontmatter()` використовує find-based логіку (`---\n...\n---`) — уніфікована для всіх скриптів
- **APPROVED_TAGS**: єдине джерело правди (262 теги) у `utils.py`, а не в `wiki_lint.py` чи `integrator.py`
- **Рекурсивний скан**: `rglob('**/*.md')` для `raw/` — підтримує піддиректорії (`raw/articles/`, `raw/papers/`)
- **Resilient paths**: `os.path.isdir()` перед скануванням — запобігає `FileNotFoundError` в cron
