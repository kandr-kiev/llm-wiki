#!/usr/bin/env python3
"""
test_wiki_doctor_coverage.py — Тести покриття для методів без тестів.

Методи, що покриваються:
  1. diagnose_infrastructure() — L4: root files, _N dups, APPROVED_TAGS drift, Astro truncation
  2. diagnose_integrator() — L5: integrator.py existence, critical bugs
  3. diagnose_config() — L6: SCHEMA.md existence, tag taxonomy completeness
  4. extract_schema_tags() — L6 helper: tag extraction from SCHEMA.md
  5. _set_dry_run() / _write_if_not_dry() — dry-run infrastructure
  6. cure_missing_index_entries() — P6: add missing pages to index
  7. cure_approved_tags_drift() — P7: sync APPROVED_TAGS with SCHEMA.md

Кожен тест ізолюваний — жодна зміна не потрапить у реальний wiki.
"""

import hashlib
import json
import sys
from pathlib import Path

import pytest


# ============================================================================
# Група 1: Diagnose Infrastructure (L4)
# ============================================================================


class TestDiagnoseInfrastructure:
    """Тести diagnose_infrastructure()."""

    def test_detect_root_wiki_files(self, wiki_structure, wiki_root):
        """diagnose_infrastructure вияляє файли wiki в корені wiki/."""
        rogue = wiki_root / "wiki" / "rogue-page.md"
        rogue.write_text("""---
type: concept
title: Rogue Page
description: Should not be in wiki root
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Rogue Page

Body.
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        infra_issues = [i for i in report.get_all_issues()
                        if i['layer'] == 'infrastructure'
                        and 'root directory' in i.get('message', '').lower()]

        assert len(infra_issues) >= 1, \
            f"Не виявлено файл у корені wiki/. Issues: {[i['message'] for i in infra_issues]}"

    def test_detect_n_duplicates(self, wiki_structure, wiki_root):
        """diagnose_infrastructure вияляє _N дублікати."""
        base = wiki_root / "wiki" / "concepts" / "test-dup.md"
        base.write_text("""---
type: concept
title: Test Dup
description: Base version
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test Dup

Body.
""", encoding='utf-8')

        dup = wiki_root / "wiki" / "concepts" / "test-dup_1.md"
        dup.write_text("""---
type: concept
title: Test Dup
description: Duplicate
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test Dup

Duplicate body.
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        dup_issues = [i for i in report.get_all_issues()
                      if i['layer'] == 'infrastructure'
                      and 'duplicate' in i.get('message', '').lower()]

        assert len(dup_issues) >= 1, \
            f"Не виявлено _N дублікат. Issues: {[i['message'] for i in dup_issues]}"

    def test_no_detect_n_dup_without_base(self, wiki_structure, wiki_root):
        """_N дублікати без base версії — не вважаються дублікатами."""
        no_base = wiki_root / "wiki" / "concepts" / "no-base_1.md"
        no_base.write_text("""---
type: concept
title: No Base
description: No base version
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# No Base

Body.
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        dup_issues = [i for i in report.get_all_issues()
                      if i['layer'] == 'infrastructure'
                      and 'fallback duplicate' in i.get('message', '').lower()]

        assert len(dup_issues) == 0, \
            f"Один _1 без base не має бути дублікатом: {[i['message'] for i in dup_issues]}"

    def test_detect_truncated_astro(self, wiki_structure, wiki_root):
        """diagnose_infrastructure вияляє обрізані Astro файли."""
        truncated = wiki_root / "wiki" / "concepts" / "truncated-astro.md"
        truncated.write_text("""---
type: concept
title: Truncated Astro
description: Has open astro-island
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Truncated Astro

<div>Some content</div>
<astro-island component-name="test" props="{}">
This file was truncated.
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        astro_issues = [i for i in report.get_all_issues()
                        if i['layer'] == 'infrastructure'
                        and 'truncated' in i.get('message', '').lower()]

        assert len(astro_issues) >= 1, \
            f"Не виявлено обрізаний Astro файл: {[i['message'] for i in astro_issues]}"

    def test_approved_tags_drift_warn(self, wiki_structure, wiki_root):
        """diagnose_infrastructure вияляє APPROVED_TAGS drift."""
        utils = wiki_root / "tools" / "utils.py"
        content = utils.read_text(encoding='utf-8')
        # Додаємо тег якого немає в SCHEMA.md
        content = content.replace(
            'APPROVED_TAGS = {',
            'APPROVED_TAGS = {\n    "fake-schema-mismatch-tag",'
        )
        utils.write_text(content, encoding='utf-8')

        report = wiki_structure.diagnose()
        drift_issues = [i for i in report.get_all_issues()
                        if i['layer'] == 'infrastructure'
                        and 'APPROVED_TAGS' in i.get('message', '')]

        assert len(drift_issues) >= 1, \
            f"Не виявлено APPROVED_TAGS drift: {[i['message'] for i in drift_issues]}"


# ============================================================================
# Група 2: Diagnose Integrator (L5)
# ============================================================================


class TestDiagnoseIntegrator:
    """Тести diagnose_integrator()."""

    def test_integrator_missing(self, wiki_structure, wiki_root):
        """diagnose_integrator вияляє відсутній integrator.py."""
        integrator = wiki_root / "tools" / "integrator.py"
        if integrator.exists():
            integrator.unlink()

        report = wiki_structure.diagnose()
        integrator_issues = [i for i in report.get_all_issues()
                             if i['layer'] == 'integrator'
                             and 'missing' in i.get('message', '').lower()]

        assert len(integrator_issues) >= 1, \
            f"Не виявлено відсутній integrator.py: {[i['message'] for i in integrator_issues]}"

    def test_integrator_dict_iteration_bug(self, wiki_structure, wiki_root):
        """diagnose_integrator вияляє dict iteration без .items()."""
        integrator = wiki_root / "tools" / "integrator.py"
        integrator.write_text("#!/usr/bin/env python3\nfor key, value in some_dict:\n    print(key)\n", encoding='utf-8')

        report = wiki_structure.diagnose()
        integrator_issues = [i for i in report.get_all_issues()
                             if i['layer'] == 'integrator'
                             and '.items()' in i.get('message', '')]

        assert len(integrator_issues) >= 1, \
            f"Не виявлено dict iteration bug: {[i['message'] for i in integrator_issues]}"

    def test_integrator_regex_escaping_bug(self, wiki_structure, wiki_root):
        r"""diagnose_integrator вияляє double-escaped regex.

        Джерело: re.search(r'r\\[\\s\\+\\]', content)
        Raw string r'r\\[\\s\\+\\]' = 13 символів: r,\\,\\,[,\\,\\,s,\\,\\,+,\\,\\,]
        Як regex: \\ = one literal backslash. Шукає: r\\[\\s\\+\\]
        Тобто рядок: r + \\ + [ + \\ + s + \\ + + + \\ + ]

        write_text("r'r\\\\[\\\\s\\\\+\\\\]'") записує в файл: r'r\\[\\s\\+\\]'
        regex r\\[\\s\\+\\] шукає r\\[\\s\\+\\] — має збіг!
        """
        integrator = wiki_root / "tools" / "integrator.py"
        integrator.write_text("#!/usr/bin/env python3\nimport re\npattern = r'r\\\\[\\\\s\\\\+\\\\]'\nresult = re.search(pattern, text)\nwrite_file(pattern)\n", encoding='utf-8')

        report = wiki_structure.diagnose()
        integrator_issues = [i for i in report.get_all_issues()
                             if i['layer'] == 'integrator'
                             and ('double-escape' in i.get('message', '').lower()
                                  or 'backslash' in i.get('message', '').lower())]

        assert len(integrator_issues) >= 1, \
            f"Не виявлено regex escaping bug: {[i['message'] for i in integrator_issues]}"

    def test_integrator_clean(self, wiki_structure, wiki_root):
        """diagnose_integrator не повідомляє про чистий integrator.py."""
        integrator = wiki_root / "tools" / "integrator.py"
        integrator.write_text("#!/usr/bin/env python3\nfor key, value in some_dict.items():\n    print(key, value)\n", encoding='utf-8')

        report = wiki_structure.diagnose()
        integrator_issues = [i for i in report.get_all_issues()
                             if i['layer'] == 'integrator']

        assert len(integrator_issues) == 0, \
            f"Чистий integrator викликає помилки: {[i['message'] for i in integrator_issues]}"


# ============================================================================
# Група 3: Diagnose Config (L6)
# ============================================================================


class TestDiagnoseConfig:
    """Тести diagnose_config()."""

    def test_schema_missing(self, wiki_structure, wiki_root):
        """diagnose_config вияляє відсутній SCHEMA.md."""
        schema = wiki_root / "SCHEMA.md"
        schema.unlink()

        report = wiki_structure.diagnose()
        config_issues = [i for i in report.get_all_issues()
                         if i['layer'] == 'config'
                         and 'SCHEMA.md' in i.get('message', '')]

        assert len(config_issues) >= 1, \
            f"Не виявлено відсутній SCHEMA.md: {[i['message'] for i in config_issues]}"
        assert any(i['severity'] == 'ERROR' for i in config_issues), \
            "Відсутній SCHEMA.md має бути ERROR"

    def test_schema_tag_taxonomy_incomplete(self, wiki_structure, wiki_root):
        """diagnose_config виявляє теги в wiki, яких немає в SCHEMA.md."""
        page = wiki_root / "wiki" / "concepts" / "test-unknown-tag.md"
        page.write_text("""---
type: concept
title: Test Unknown Tag
description: Has unknown tag
tags: [nonexistent-schema-tag]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test Unknown Tag

Body.
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        config_issues = [i for i in report.get_all_issues()
                         if i['layer'] == 'config'
                         and 'not in SCHEMA.md' in i.get('message', '')]

        assert len(config_issues) >= 1, \
            f"Не виявлено тег поза SCHEMA.md: {[i['message'] for i in config_issues]}"


# ============================================================================
# Група 4: extract_schema_tags helper
# ============================================================================


class TestExtractSchemaTags:
    """Тести extract_schema_tags()."""

    def test_extract_dash_separated_tags(self, wiki_structure, wiki_root):
        """extract_schema_tags парсить теги формату '- tag-name — description'."""
        schema = wiki_root / "SCHEMA.md"
        schema.write_text("""---
type: reference
title: Schema
---
# Schema

## Tag Taxonomy

- ai — artificial intelligence
- machine-learning — ML
- deep-learning — DL
- custom-tag — custom
""", encoding='utf-8')

        tags = wiki_structure.extract_schema_tags()
        assert tags is not None
        assert 'ai' in tags
        assert 'machine-learning' in tags
        assert 'deep-learning' in tags
        assert 'custom-tag' in tags
        assert 'llm-wiki' not in tags

    def test_extract_yaml_flow_tags(self, wiki_structure, wiki_root):
        """extract_schema_tags парсить YAML flow sequence 'tags: [tag1, tag2]'."""
        schema = wiki_root / "SCHEMA.md"
        schema.write_text("""---
type: reference
title: Schema
tags: [yaml-flow-tag1, yaml-flow-tag2, yaml-flow-tag3]
---
# Schema

## Tag Taxonomy

- regular-tag — regular
""", encoding='utf-8')

        tags = wiki_structure.extract_schema_tags()
        assert tags is not None
        assert 'yaml-flow-tag1' in tags
        assert 'yaml-flow-tag2' in tags
        assert 'yaml-flow-tag3' in tags
        assert 'regular-tag' in tags

    def test_extract_no_tags(self, wiki_structure, wiki_root):
        """extract_schema_tags повертає пустий set коли SCHEMA.md немає тегів."""
        schema = wiki_root / "SCHEMA.md"
        schema.write_text("""---
type: reference
title: Schema
---
# Schema

No taxonomy section at all.
""", encoding='utf-8')

        tags = wiki_structure.extract_schema_tags()
        assert tags is not None
        assert len(tags) == 0

    def test_extract_no_schema_file(self, wiki_structure, wiki_root):
        """extract_schema_tags повертає None коли SCHEMA.md відсутній."""
        schema = wiki_root / "SCHEMA.md"
        schema.unlink(missing_ok=True)

        tags = wiki_structure.extract_schema_tags()
        assert tags is None


# ============================================================================
# Група 5: _set_dry_run / _write_if_not_dry
# ============================================================================


class TestDryRunInfrastructure:
    """Тести _set_dry_run() та _write_if_not_dry()."""

    def test_set_dry_run_true(self, wiki_structure, wiki_root):
        """_set_dry_run(True) встановлює режим dry-run."""
        wiki_structure._set_dry_run(True)
        test_file = wiki_root / "test-dryrun.txt"
        result = wiki_structure._write_if_not_dry(test_file, "content")
        assert result is False, "У dry-run mode має повернути False"
        assert not test_file.exists(), "Файл не має бути створений у dry-run"

    def test_set_dry_run_false(self, wiki_structure, wiki_root):
        """_set_dry_run(False) вимикає dry-run, файл пишеться."""
        wiki_structure._set_dry_run(False)
        test_file = wiki_root / "test-live.txt"
        result = wiki_structure._write_if_not_dry(test_file, "live content")
        assert result is True, "У live mode має повернути True"
        assert test_file.exists(), "Файл має бути створений у live mode"
        assert test_file.read_text(encoding='utf-8') == "live content"

    def test_set_dry_run_toggle(self, wiki_structure, wiki_root):
        """Перемикання між dry-run і live."""
        test_file = wiki_root / "test-toggle.txt"

        wiki_structure._set_dry_run(True)
        assert not wiki_structure._write_if_not_dry(test_file, "dry")
        assert not test_file.exists()

        wiki_structure._set_dry_run(False)
        assert wiki_structure._write_if_not_dry(test_file, "live")
        assert test_file.read_text(encoding='utf-8') == "live"

        wiki_structure._set_dry_run(True)
        assert not wiki_structure._write_if_not_dry(test_file, "dry again")
        assert test_file.read_text(encoding='utf-8') == "live"


# ============================================================================
# Група 6: cure_missing_index_entries (P6)
# ============================================================================


class TestCureMissingIndexEntries:
    """Тести cure_missing_index_entries()."""

    def test_add_page_to_correct_section(self, wiki_structure, wiki_root):
        """cure_missing_index_entries додає сторінку в правильний розділ index."""
        page = wiki_root / "wiki" / "entities" / "test-index-entry.md"
        page.write_text("""---
type: entity
title: Test Index Entry
description: Should be added to index
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test Index Entry

Body.
""", encoding='utf-8')

        index = wiki_root / "wiki" / "index.md"
        index.write_text("""---
type: reference
title: Wiki Index
---
# Wiki Index

Last updated: 2026-07-13

Total pages: 0

### Concepts

### Entities

### Playbooks

### Comparisons

### Synthesis

### Queries

### References

*Auto-generated*
""", encoding='utf-8')

        fixes = wiki_structure.cure_missing_index_entries(wiki_structure.diagnose())

        assert fixes >= 1, f"Не додано жодного запису. fixes={fixes}"
        content = index.read_text(encoding='utf-8')
        assert 'test-index-entry' in content, \
            f"Сторінка не додана в index. Контент:\\n{content}"
        assert '### Entities' in content
        assert 'Total pages: 1' in content, \
            f"Total pages не оновлено. Контент:\\n{content}"

    def test_no_duplicate_index_entry(self, wiki_structure, wiki_root):
        """cure_missing_index_entries не додає дублікат."""
        page = wiki_root / "wiki" / "concepts" / "test-no-dup-index.md"
        page.write_text("""---
type: concept
title: Test No Dup Index
description: Already in index
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test No Dup Index

Body.
""", encoding='utf-8')

        index = wiki_root / "wiki" / "index.md"
        index.write_text("""---
type: reference
title: Wiki Index
---
# Wiki Index

Last updated: 2026-07-13

Total pages: 1

### Concepts

| Test No Dup Index | `wiki/concepts/test-no-dup-index.md` |

### Entities

### Playbooks

### Comparisons

### Synthesis

### Queries

### References

*Auto-generated*
""", encoding='utf-8')

        fixes = wiki_structure.cure_missing_index_entries(wiki_structure.diagnose())

        assert fixes == 0, f"Додано дублікат! fixes={fixes}"
        content = index.read_text(encoding='utf-8')
        count = content.count('test-no-dup-index')
        assert count <= 2, f"Дублікат додано: зустрічається {count} разів"


# ============================================================================
# Група 7: cure_approved_tags_drift (P7)
# ============================================================================


class TestCureApprovedTagsDrift:
    """Тести cure_approved_tags_drift()."""

    def test_sync_tags_add_missing(self, wiki_structure, wiki_root):
        """cure_approved_tags_drift додає теги з SCHEMA.md в APPROVED_TAGS."""
        schema = wiki_root / "SCHEMA.md"
        schema.write_text("""---
type: reference
title: Schema
---
# Schema

## Tag Taxonomy

- existing-tag — already in APPROVED_TAGS
- new-schema-tag — not in APPROVED_TAGS yet
""", encoding='utf-8')

        utils = wiki_root / "tools" / "utils.py"
        content = utils.read_text(encoding='utf-8')
        # Замінюємо APPROVED_TAGS на лише existing-tag
        content = content.replace(
            'APPROVED_TAGS = {',
            'APPROVED_TAGS = {\n    "existing-tag",'
        )
        utils.write_text(content, encoding='utf-8')

        fixes = wiki_structure.cure_approved_tags_drift(wiki_structure.diagnose())

        # cure_approved_tags_drift об'єднує schema_tags | used_tags | current_tags
        # new-schema-tag є в schema_tags і НЕ в current_tags
        # Тому fixes >= 1 (новий тег додано)
        assert fixes >= 1, f"Не додано жодного нового тегу. fixes={fixes}"
        new_content = utils.read_text(encoding='utf-8')
        assert 'new-schema-tag' in new_content, \
            f"new-schema-tag не додано в APPROVED_TAGS"

    def test_sync_tags_preserves_existing(self, wiki_structure, wiki_root):
        """cure_approved_tags_drift зберігає існуючі теги."""
        schema = wiki_root / "SCHEMA.md"
        schema.write_text("""---
type: reference
title: Schema
---
# Schema

## Tag Taxonomy

- existing-tag — already in APPROVED_TAGS
""", encoding='utf-8')

        utils = wiki_root / "tools" / "utils.py"
        content = utils.read_text(encoding='utf-8')
        content = content.replace(
            'APPROVED_TAGS = {',
            'APPROVED_TAGS = {\n    "existing-tag",'
        )
        utils.write_text(content, encoding='utf-8')

        fixes = wiki_structure.cure_approved_tags_drift(wiki_structure.diagnose())

        new_content = utils.read_text(encoding='utf-8')
        assert 'existing-tag' in new_content, \
            "Існуючий тег видалено!"

    def test_sync_empty_schema_returns_zero(self, wiki_structure, wiki_root):
        """cure_approved_tags_drift повертає 0 коли SCHEMA.md немає тегів."""
        schema = wiki_root / "SCHEMA.md"
        schema.write_text("""---
type: reference
title: Schema
---
# Schema

No taxonomy section.
""", encoding='utf-8')

        fixes = wiki_structure.cure_approved_tags_drift(wiki_structure.diagnose())
        assert fixes == 0, f"Очікувалось 0 fixes, отримано: {fixes}"

    def test_sync_merges_wiki_usage(self, wiki_structure, wiki_root):
        """cure_approved_tags_drift об'єднує теги з wiki usage."""
        schema = wiki_root / "SCHEMA.md"
        schema.write_text("""---
type: reference
title: Schema
---
# Schema

## Tag Taxonomy

- schema-tag — from schema
""", encoding='utf-8')

        page = wiki_root / "wiki" / "concepts" / "test-merge-tag.md"
        page.write_text("""---
type: concept
title: Test Merge Tag
description: Has wiki-only tag
tags: [wiki-only-tag]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test Merge Tag

Body.
""", encoding='utf-8')

        utils = wiki_root / "tools" / "utils.py"
        content = utils.read_text(encoding='utf-8')
        content = content.replace(
            'APPROVED_TAGS = {',
            'APPROVED_TAGS = {\n    "existing-tag",'
        )
        utils.write_text(content, encoding='utf-8')

        fixes = wiki_structure.cure_approved_tags_drift(wiki_structure.diagnose())

        new_content = utils.read_text(encoding='utf-8')
        assert 'schema-tag' in new_content, "schema-tag не додано"
        assert 'wiki-only-tag' in new_content, "wiki-only-tag не додано"
        assert 'existing-tag' in new_content, "existing-tag видалено"


# ============================================================================
# Група 8: diagnose_index (L3) — додаткові тести
# ============================================================================


class TestDiagnoseIndex:
    """Додаткові тести diagnose_index()."""

    def test_detect_missing_last_updated(self, wiki_structure, wiki_root):
        """diagnose_index виявляє відсутній 'Last updated'."""
        index = wiki_root / "wiki" / "index.md"
        index.write_text("""---
type: reference
title: Wiki Index
---
# Wiki Index

Total pages: 0

### Concepts

*Auto-generated*
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        index_issues = [i for i in report.get_all_issues()
                        if i['layer'] == 'index'
                        and 'Last updated' in i.get('message', '')]

        assert len(index_issues) >= 1, \
            f"Не виявлено відсутній 'Last updated': {[i['message'] for i in index_issues]}"

    def test_detect_stale_path_singular(self, wiki_structure, wiki_root):
        """diagnose_index виявляє singular path wiki/concept/ → wiki/concepts/."""
        index = wiki_root / "wiki" / "index.md"
        index.write_text("""---
type: reference
title: Wiki Index
---
# Wiki Index

Last updated: 2026-07-13

Total pages: 0

### Concepts

[[wiki/concept/some-slug]]

### Entities

### Playbooks

### Comparisons

### Synthesis

### Queries

### References

*Auto-generated*
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        index_issues = [i for i in report.get_all_issues()
                        if i['layer'] == 'index'
                        and 'stale path' in i.get('message', '').lower()]

        assert len(index_issues) >= 1, \
            f"Не виявлено stale path: {[i['message'] for i in index_issues]}"

    def test_no_stale_path_plural(self, wiki_structure, wiki_root):
        """diagnose_index не повідомляє про правильний plural path."""
        index = wiki_root / "wiki" / "index.md"
        index.write_text("""---
type: reference
title: Wiki Index
---
# Wiki Index

Last updated: 2026-07-13

Total pages: 0

### Concepts

[[wiki/concepts/some-slug]]

### Entities

### Playbooks

### Comparisons

### Synthesis

### Queries

### References

*Auto-generated*
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        stale_issues = [i for i in report.get_all_issues()
                        if i['layer'] == 'index'
                        and 'stale path' in i.get('message', '').lower()]

        assert len(stale_issues) == 0, \
            f"Правильний path викликає stale: {[i['message'] for i in stale_issues]}"


# ============================================================================
# Група 9: diagnose_wiki_pages (L1) — додаткові тести
# ============================================================================


class TestDiagnoseWikiPagesExtra:
    """Додаткові тести diagnose_wiki_pages()."""

    def test_detect_broken_wikilink(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє поломані wikilinks."""
        page = wiki_root / "wiki" / "concepts" / "test-broken-wl.md"
        page.write_text("""---
type: concept
title: Test Broken Wikilink
description: Has broken link
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test Broken Wikilink

See [[totally-nonexistent-page]] for details.
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        wl_issues = [i for i in report.get_all_issues()
                     if i['layer'] == 'wiki_pages'
                     and 'broken wikilink' in i.get('message', '').lower()]

        assert len(wl_issues) >= 1, \
            f"Не виявлено поломаний wikilink: {[i['message'] for i in wl_issues]}"

    def test_detect_low_confidence(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє low confidence."""
        page = wiki_root / "wiki" / "concepts" / "test-low-conf.md"
        page.write_text("""---
type: concept
title: Test Low Confidence
description: Low confidence page
tags: [test]
sources: []
confidence: low
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test Low Confidence

Body.
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        conf_issues = [i for i in report.get_all_issues()
                       if i['layer'] == 'wiki_pages'
                       and 'low confidence' in i.get('message', '').lower()]

        assert len(conf_issues) >= 1, \
            f"Не виявлено low confidence: {[i['message'] for i in conf_issues]}"

    def test_detect_contested_page(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє contested page."""
        page = wiki_root / "wiki" / "concepts" / "test-contested.md"
        page.write_text("""---
type: concept
title: Test Contested
description: Contested page
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
contested: true
---
# Test Contested

Body.
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        contested_issues = [i for i in report.get_all_issues()
                            if i['layer'] == 'wiki_pages'
                            and 'contested' in i.get('message', '').lower()]

        assert len(contested_issues) >= 1, \
            f"Не виявлено contested page: {[i['message'] for i in contested_issues]}"

    def test_detect_missing_source_file(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє відсутні source файли."""
        page = wiki_root / "wiki" / "concepts" / "test-missing-src.md"
        page.write_text("""---
type: concept
title: Test Missing Source
description: Missing source
tags: [test]
sources: [raw/articles/nonexistent.md]
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test Missing Source

Body.
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        src_issues = [i for i in report.get_all_issues()
                      if i['layer'] == 'wiki_pages'
                      and 'source file missing' in i.get('message', '').lower()]

        assert len(src_issues) >= 1, \
            f"Не виявлено missing source: {[i['message'] for i in src_issues]}"

    def test_no_issues_clean_page(self, wiki_structure, wiki_root, sample_concept_page):
        """diagnose_wiki_pages не повідомляє ERROR для чистих сторінок."""
        # Додаємо sample_concept_page в index щоб уникнути "missing from index"
        index = wiki_root / "wiki" / "index.md"
        index.write_text("""---
type: reference
title: Wiki Index
---
# Wiki Index

Last updated: 2026-07-13

Total pages: 1

### Concepts

| Transformer Architecture | `wiki/concepts/transformer-architecture.md` |

### Entities

### Playbooks

### Comparisons

### Synthesis

### Queries

### References

*Auto-generated*
""", encoding='utf-8')

        report = wiki_structure.diagnose()
        page_issues = [i for i in report.get_all_issues()
                       if i['layer'] == 'wiki_pages'
                       and 'transformer-architecture' in i.get('path', '')]

        errors = [i for i in page_issues if i['severity'] == 'ERROR']
        assert len(errors) == 0, \
            f"Чиста сторінка викликає ERROR: {[i['message'] for i in errors]}"
