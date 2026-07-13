#!/usr/bin/env python3
"""
test_wiki_doctor_layers.py — прямі тести для діагностичних функцій шарів Wiki Doctor.

Критичні функції, які раніше тестувалися лише опосередковано через diagnose():
  - diagnose_raw_sources (27 LOC)
  - diagnose_index (38 LOC)
  - diagnose_config (30 LOC)
  - diagnose_infrastructure (63 LOC)
  - diagnose_integrator (23 LOC)
"""

import hashlib
import shutil
import pytest


class TestDiagnoseRawSources:
    """Прямі тести для diagnose_raw_sources()."""

    def test_detect_sha256_drift(self, wiki_structure, wiki_root):
        """diagnose_raw_sources виявляє SHA256 drift."""
        raw = wiki_root / "raw" / "articles" / "drifted.md"
        raw.write_text(
            "---\ntype: raw\ntitle: Drifted\nsha256: deadbeef1234567890abcdef12345678deadbeef1234567890abcdef12345678\n---\n# Drifted\n\nBody.",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_raw_sources(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'raw_sources']
        assert len(issues) >= 1
        assert any('sha256' in i['message'].lower() for i in issues)

    def test_no_drift_when_hash_matches(self, wiki_structure, wiki_root):
        """diagnose_raw_sources не повідомляє про drift при збігу."""
        body = "# Valid\n\nContent."
        sha = hashlib.sha256(body.encode('utf-8')).hexdigest()
        raw = wiki_root / "raw" / "articles" / "valid.md"
        raw.write_text(
            f"---\ntype: raw\ntitle: Valid\nsha256: {sha}\n---\n{body}",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_raw_sources(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'raw_sources']
        assert len(issues) == 0

    def test_skip_readme_md(self, wiki_structure, wiki_root):
        """diagnose_raw_sources пропускає README.md."""
        wiki_structure.RAW_DIR.mkdir(exist_ok=True)
        readme = wiki_structure.RAW_DIR / "README.md"
        readme.write_text("# README", encoding='utf-8')

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_raw_sources(report)
        issues = report.get_all_issues()
        assert len(issues) == 0

    def test_missing_frontmatter_raw(self, wiki_structure, wiki_root):
        """diagnose_raw_sources виявляє відсутній frontmatter."""
        raw = wiki_root / "raw" / "articles" / "no-fm.md"
        raw.write_text("# No Frontmatter\n\nBody.", encoding='utf-8')

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_raw_sources(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'raw_sources']
        assert len(issues) >= 1
        assert any('frontmatter' in i['message'].lower() for i in issues)

    def test_no_sha256_field_skipped(self, wiki_structure, wiki_root):
        """diagnose_raw_sources пропускає файли без sha256."""
        raw = wiki_root / "raw" / "articles" / "no-sha.md"
        raw.write_text(
            "---\ntype: raw\ntitle: No SHA\n---\n# No SHA\n\nBody.",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_raw_sources(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'raw_sources']
        assert len(issues) == 0


class TestDiagnoseIndex:
    """Прямі тести для diagnose_index().
    
    Ключові моменти з коду:
    - 3a: шукає [[slug]] (wikilinks), а не [text](path)
    - 3b: перевіряє "Last updated:" і "Total pages:"
    - 3c: перевіряє wiki/{subdir}/{slug} з unknown section
    """

    def test_detect_duplicate_wikilink(self, wiki_structure, wiki_root):
        """diagnose_index виявляє дублі wikilink [[slug]]."""
        index = wiki_structure.INDEX_FILE
        index.write_text(
            "---\ntype: reference\ntitle: Wiki Index\n---\n# Wiki Index\n\nLast updated: 2026-07-13\n\nTotal pages: 1\n\n### Concepts\n\n- [[transformer]]\n- [[transformer]]\n\n*Auto-generated*\n",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_index(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'index']
        assert len(issues) >= 1
        assert any('duplicate' in i['message'].lower() for i in issues)

    def test_detect_stale_path_unknown_section(self, wiki_structure, wiki_root):
        """diagnose_index виявляє stale path з unknown section."""
        index = wiki_structure.INDEX_FILE
        index.write_text(
            "---\ntype: reference\ntitle: Wiki Index\n---\n# Wiki Index\n\nLast updated: 2026-07-13\n\nTotal pages: 1\n\n### Concepts\n\n- [[wiki/badsection/slug]]\n\n*Auto-generated*\n",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_index(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'index']
        assert len(issues) >= 1
        assert any('stale' in i['message'].lower() or 'unknown' in i['message'].lower() for i in issues)

    def test_no_issues_clean_index(self, wiki_structure, wiki_root):
        """diagnose_index не повідомляє про чистий index."""
        index = wiki_structure.INDEX_FILE
        index.write_text(
            "---\ntype: reference\ntitle: Wiki Index\n---\n# Wiki Index\n\nLast updated: 2026-07-13\n\nTotal pages: 0\n\n### Concepts\n\n### Entities\n\n### Playbooks\n\n*Auto-generated*\n",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_index(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'index']
        assert len(issues) == 0

    def test_missing_last_updated(self, wiki_structure, wiki_root):
        """diagnose_index виявляє відсутній last updated."""
        index = wiki_structure.INDEX_FILE
        index.write_text(
            "---\ntype: reference\ntitle: Wiki Index\n---\n# Wiki Index\n\nTotal pages: 0\n\n### Concepts\n\n*Auto-generated*\n",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_index(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'index']
        assert len(issues) >= 1
        assert any('last updated' in i['message'].lower() for i in issues)


class TestDiagnoseConfig:
    """Прямі тести для diagnose_config().
    
    Ключові моменти з коду:
    - Перевіряє tags used in wiki but NOT in SCHEMA.md taxonomy
    - Використовує extract_schema_tags() для парсингу
    """

    def test_schema_missing(self, wiki_structure, wiki_root):
        """diagnose_config виявляє відсутній SCHEMA.md."""
        schema = wiki_root / "SCHEMA.md"
        schema.unlink()

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_config(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'config']
        assert len(issues) >= 1
        assert any('schema' in i['message'].lower() for i in issues)

    def test_tags_used_not_in_schema(self, wiki_structure, wiki_root):
        """diagnose_config виявляє теги з wiki, яких немає в SCHEMA.md."""
        # Створюємо сторінку з тегом, якого немає в SCHEMA.md
        page = wiki_structure.WIKI_DIR / "concepts" / "test-tag.md"
        page.write_text(
            "---\ntype: concept\ntitle: Test Tag\ndescription: Has custom tag\ntags: [custom-unique-tag]\n---\n# Test Tag",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_config(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'config']
        assert len(issues) >= 1
        assert any('not in schema' in i['message'].lower() for i in issues)

    def test_no_issues_clean_config(self, wiki_structure, wiki_root):
        """diagnose_config не повідомляє про чисту конфігурацію."""
        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_config(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'config']
        assert len(issues) == 0


class TestDiagnoseInfrastructure:
    r"""Прямі тести для diagnose_infrastructure().
    
    Ключові моменти з коду:
    - 4a: wiki файли в root директорії
    - 4b: {base}_N дублікати (regex ^(.+)_\d+$)
    - 4c: APPROVED_TAGS drift vs SCHEMA.md
    - 4d: truncated files (astro-island)
    """

    def test_detect_root_wiki_files(self, wiki_structure, wiki_root):
        """diagnose_infrastructure виявляє wiki файли в root."""
        root_file = wiki_structure.WIKI_DIR / "orphan.md"
        root_file.write_text(
            "---\ntype: concept\ntitle: Orphan\n---\n# Orphan",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_infrastructure(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'infrastructure']
        assert len(issues) >= 1
        assert any('root' in i['message'].lower() for i in issues)

    def test_detect_base_N_duplicates(self, wiki_structure, wiki_root):
        """diagnose_infrastructure виявляє {base}_N дублікати."""
        # Створюємо base файл
        base = wiki_structure.WIKI_DIR / "concepts" / "transformer.md"
        base.write_text(
            "---\ntype: concept\ntitle: Transformer\n---\n# Transformer",
            encoding='utf-8',
        )
        # Створюємо _N дублікат
        dup = wiki_structure.WIKI_DIR / "concepts" / "transformer_1.md"
        dup.write_text(
            "---\ntype: concept\ntitle: Transformer 1\n---\n# Transformer 1",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_infrastructure(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'infrastructure']
        assert len(issues) >= 1
        assert any('duplicate' in i['message'].lower() for i in issues)

    def test_detect_truncated_astro(self, wiki_structure, wiki_root):
        """diagnose_infrastructure виявляє truncated astro-island файли."""
        page = wiki_structure.WIKI_DIR / "concepts" / "truncated.md"
        page.write_text(
            "---\ntype: concept\ntitle: Truncated\n---\n# Truncated\n\n<astro-island src=\"test\">",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_infrastructure(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'infrastructure']
        assert len(issues) >= 1
        assert any('truncated' in i['message'].lower() or 'astro' in i['message'].lower() for i in issues)

    def test_no_issues_clean_infrastructure(self, wiki_structure, wiki_root):
        """diagnose_infrastructure не повідомляє про чисту інфраструктуру.
        
        NOTE: APPROVED_TAGS drift завжди буде WARN, бо conftest.py створює
        SCHEMA.md з тегами, яких немає в utils.py. Тому цей тест перевіряє
        що немає інших проблем крім APPROVED_TAGS drift.
        """
        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_infrastructure(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'infrastructure']
        # APPROVED_TAGS drift — очікуваний WARN
        tag_issues = [i for i in issues if 'approved_tags' in i['message'].lower() or 'missing' in i['message'].lower() and 'tags' in i['message'].lower()]
        other_issues = [i for i in issues if i not in tag_issues]
        assert len(other_issues) == 0, f"Unexpected issues: {[i['message'] for i in other_issues]}"

    def test_no_base_version_duplicates(self, wiki_structure, wiki_root):
        """diagnose_infrastructure виявляє дублікати без base версії."""
        # Жодного base файлу, тільки _N версії
        dup1 = wiki_structure.WIKI_DIR / "concepts" / "orphan_1.md"
        dup1.write_text(
            "---\ntype: concept\ntitle: Orphan 1\n---\n# Orphan 1",
            encoding='utf-8',
        )
        dup2 = wiki_structure.WIKI_DIR / "concepts" / "orphan_2.md"
        dup2.write_text(
            "---\ntype: concept\ntitle: Orphan 2\n---\n# Orphan 2",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_infrastructure(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'infrastructure']
        assert len(issues) >= 1
        assert any('fallback' in i['message'].lower() or 'duplicate' in i['message'].lower() for i in issues)


class TestDiagnoseIntegrator:
    """Прямі тести для diagnose_integrator().
    
    Ключові моменти з коду:
    - Перевіряє "for key, value in " без ".items()"
    - Перевіряє regex з подвійними бекслішами
    """

    def test_integrator_missing(self, wiki_structure, wiki_root):
        """diagnose_integrator виявляє відсутній integrator.py."""
        integrator = wiki_root / "tools" / "integrator.py"
        if integrator.exists():
            integrator.unlink()

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_integrator(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'integrator']
        assert len(issues) >= 1
        assert any('integrator' in i['message'].lower() for i in issues)

    def test_integrator_dict_iteration_bug(self, wiki_structure, wiki_root):
        """diagnose_integrator виявляє ітерацію по dict без .items()."""
        integrator = wiki_root / "tools" / "integrator.py"
        integrator.write_text(
            "#!/usr/bin/env python3\nfor key, value in my_dict:\n    print(key, value)\n",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_integrator(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'integrator']
        assert len(issues) >= 1
        assert any('dict' in i['message'].lower() for i in issues)

    def test_integrator_clean(self, wiki_structure, wiki_root):
        """diagnose_integrator не повідомляє про чистий integrator.py."""
        integrator = wiki_root / "tools" / "integrator.py"
        integrator.write_text(
            "#!/usr/bin/env python3\nprint('Hello')\n",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_integrator(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'integrator']
        assert len(issues) == 0
