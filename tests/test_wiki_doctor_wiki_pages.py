#!/usr/bin/env python3
"""
test_wiki_doctor_wiki_pages.py — прямі тести для diagnose_wiki_pages().

Найбільша діагностична функція (70 LOC), перевіряє:
  1a. Missing frontmatter
  1b. Missing required fields
  1c. Unapproved tags
  1d. Missing from index.md
  1e. Page too large (>200 lines)
  1f. Low confidence
  1g. Contested page
  1h. Broken wikilinks
  1i. Source files missing
"""

import pytest


class TestDiagnoseWikiPages:
    """Прямі тести для diagnose_wiki_pages()."""

    def test_missing_frontmatter(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє відсутній frontmatter (1a)."""
        page = wiki_structure.WIKI_DIR / "concepts" / "no-frontmatter.md"
        page.write_text("# No Frontmatter\n\nBody.", encoding='utf-8')

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        assert len(issues) >= 1
        assert any('frontmatter' in i['message'].lower() for i in issues)

    def test_missing_required_fields(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє missing fields (1b)."""
        page = wiki_structure.WIKI_DIR / "concepts" / "missing-fields.md"
        page.write_text(
            "---\ntype: concept\ntitle: Missing Fields\n---\n# Missing Fields\n\nBody.",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        assert len(issues) >= 1
        assert any('missing fields' in i['message'].lower() for i in issues)

    def test_unapproved_tag(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє unapproved tag (1c)."""
        page = wiki_structure.WIKI_DIR / "concepts" / "bad-tag.md"
        page.write_text(
            "---\ntype: concept\ntitle: Bad Tag\ndescription: Has bad tag\ntags: [nonexistent-tag-xyz]\n---\n# Bad Tag",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        assert len(issues) >= 1
        assert any('unapproved' in i['message'].lower() for i in issues)

    def test_missing_from_index(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє page missing from index.md (1d)."""
        # Створюємо сторінку, якої немає в index.md
        page = wiki_structure.WIKI_DIR / "concepts" / "not-in-index.md"
        page.write_text(
            "---\ntype: concept\ntitle: Not In Index\ndescription: Missing from index\ntags: [test]\nsources: []\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n# Not In Index\n\nBody.",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        assert len(issues) >= 1
        assert any('missing from index' in i['message'].lower() for i in issues)

    def test_page_too_large(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє page over 200 lines (1e)."""
        lines = ["# Large Page"]
        for i in range(205):
            lines.append(f"Line {i}")
        page = wiki_structure.WIKI_DIR / "concepts" / "large-page.md"
        page.write_text(
            "---\ntype: concept\ntitle: Large Page\ndescription: Too big\ntags: [test]\nsources: []\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n" + "\n".join(lines),
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        assert len(issues) >= 1
        assert any('200 lines' in i['message'].lower() for i in issues)

    def test_low_confidence(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє low confidence (1f)."""
        page = wiki_structure.WIKI_DIR / "concepts" / "low-conf.md"
        page.write_text(
            "---\ntype: concept\ntitle: Low Confidence\ndescription: Low confidence\ntags: [test]\nsources: []\nconfidence: low\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n# Low Confidence",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        assert len(issues) >= 1
        assert any('low confidence' in i['message'].lower() for i in issues)

    def test_contested_page(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє contested page (1g)."""
        page = wiki_structure.WIKI_DIR / "concepts" / "contested.md"
        page.write_text(
            "---\ntype: concept\ntitle: Contested\ndescription: Contested page\ntags: [test]\nsources: []\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\ncontested: true\n---\n# Contested",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        assert len(issues) >= 1
        assert any('contested' in i['message'].lower() for i in issues)

    def test_broken_wikilink(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє broken wikilink (1h)."""
        page = wiki_structure.WIKI_DIR / "concepts" / "broken-link.md"
        page.write_text(
            "---\ntype: concept\ntitle: Broken Link\ndescription: Has broken wikilink\ntags: [test]\nsources: []\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n# Broken Link\n\nSee [[nonexistent-page]] for details.",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        assert len(issues) >= 1
        assert any('broken wikilink' in i['message'].lower() for i in issues)

    def test_source_file_missing(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages виявляє source file missing (1i)."""
        page = wiki_structure.WIKI_DIR / "concepts" / "missing-source.md"
        page.write_text(
            "---\ntype: concept\ntitle: Missing Source\ndescription: Has missing source\ntags: [test]\nsources: [raw/articles/nonexistent.md]\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n# Missing Source",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        assert len(issues) >= 1
        assert any('source file missing' in i['message'].lower() for i in issues)

    def test_skips_templates_dir(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages пропускає templates/ директорію."""
        page = wiki_structure.WIKI_DIR / "templates" / "template-page.md"
        page.write_text("# No Frontmatter\n\nBody.", encoding='utf-8')

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages' and 'index.md' not in i['path']]
        assert len(issues) == 0

    def test_skips_comparisons_dir(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages пропускає comparisons/ директорію."""
        page = wiki_structure.WIKI_DIR / "comparisons" / "no-fm.md"
        page.write_text("# No Frontmatter\n\nBody.", encoding='utf-8')

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages' and 'index.md' not in i['path']]
        assert len(issues) == 0

    def test_valid_page_no_issues(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages не повідомляє про валідну сторінку.
        
        NOTE: page missing from index.md — очікуваний ERROR для нової сторінки.
        Тому цей тест перевіряє що немає frontmatter/fields/tags issues.
        Використовуємо APPROVED_TAG 'llm' замість 'test'.
        """
        page = wiki_structure.WIKI_DIR / "concepts" / "valid.md"
        page.write_text(
            "---\ntype: concept\ntitle: Valid Page\ndescription: Valid\ntags: [llm]\nsources: []\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n# Valid Page\n\nBody.",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages' and 'index.md' not in i['path']]
        # Є тільки "missing from index" — це нормально для нової сторінки
        fm_issues = [i for i in issues if 'frontmatter' in i['message'].lower()]
        field_issues = [i for i in issues if 'missing fields' in i['message'].lower()]
        tag_issues = [i for i in issues if 'unapproved' in i['message'].lower()]
        assert len(fm_issues) == 0, f"Frontmatter issues: {fm_issues}"
        assert len(field_issues) == 0, f"Field issues: {field_issues}"
        assert len(tag_issues) == 0, f"Tag issues: {tag_issues}"

    def test_valid_wikilink_not_flagged(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages не повідомляє про valid wikilink."""
        # Створюємо дві сторінки, які посилаються одна на одну
        page1 = wiki_structure.WIKI_DIR / "concepts" / "valid-link.md"
        page1.write_text(
            "---\ntype: concept\ntitle: Valid Link\ndescription: Has valid wikilink\ntags: [test]\nsources: []\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n# Valid Link\n\nSee [[valid-link-target]].",
            encoding='utf-8',
        )
        page2 = wiki_structure.WIKI_DIR / "concepts" / "valid-link-target.md"
        page2.write_text(
            "---\ntype: concept\ntitle: Valid Link Target\ndescription: Target\ntags: [test]\nsources: []\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n# Valid Link Target",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        wikilink_issues = [i for i in issues if 'wikilink' in i['message'].lower()]
        assert len(wikilink_issues) == 0, f"Unexpected wikilink issues: {wikilink_issues}"

    def test_wikilink_with_hash_skipped(self, wiki_structure, wiki_root):
        """diagnose_wiki_pages пропускає [[slug#anchor]] (anchor part)."""
        page = wiki_structure.WIKI_DIR / "concepts" / "anchor-link.md"
        page.write_text(
            "---\ntype: concept\ntitle: Anchor Link\ndescription: Has anchor link\ntags: [test]\nsources: []\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n# Anchor Link\n\nSee [[valid-link-target#section]].",
            encoding='utf-8',
        )
        # Створюємо ціль
        target = wiki_structure.WIKI_DIR / "concepts" / "valid-link-target.md"
        target.write_text(
            "---\ntype: concept\ntitle: Valid Link Target\ndescription: Target\ntags: [test]\nsources: []\nconfidence: high\nlinks: []\ncreated: 2026-07-13\nupdated: 2026-07-13\n---\n# Valid Link Target",
            encoding='utf-8',
        )

        report = wiki_structure.DoctorReport()
        wiki_structure.diagnose_wiki_pages(report)
        issues = [i for i in report.get_all_issues() if i['layer'] == 'wiki_pages']
        wikilink_issues = [i for i in issues if 'wikilink' in i['message'].lower()]
        # Anchor-link має broken link бо valid-link-target не існує як slug для anchor-link
        # Але anchor part (#section) має бути відкинутий regex
        anchor_issues = [i for i in wikilink_issues if 'valid-link-target' in i['message'].lower()]
        assert len(anchor_issues) == 0, f"Anchor link issues: {anchor_issues}"
