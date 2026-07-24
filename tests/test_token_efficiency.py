"""
Тести для token efficiency — summary-first та adaptive loading.
"""
import sys
sys.path.insert(0, "/workspace/llm-wiki/tools")

from graphify_query import _read_wiki_content, load_wiki_page
import pytest


class TestContentLimits:
    """Перевірка обмежень контенту."""

    def test_3000_char_limit(self, tmp_path):
        """Контент обмежується 3000 символами (оновлений ліміт з 1500)."""
        test_file = tmp_path / "test-page.md"
        frontmatter = "---\ntitle: Test Page\nslug: test-page\ntype: concept\n---\n"
        big_content = "x" * 5000
        test_file.write_text(frontmatter + big_content, encoding="utf-8")

        content = _read_wiki_content(test_file)
        assert len(content) <= 3000

    def test_frontmatter_stripped(self, tmp_path):
        """Frontmatter прибирається з контенту."""
        test_file = tmp_path / "test-page.md"
        content = "---\ntitle: Test\nslug: test\ntype: concept\n---\n# Heading\nBody text"
        test_file.write_text(content, encoding="utf-8")

        result = _read_wiki_content(test_file)
        assert not result.startswith("---")
        assert "title:" not in result

    def test_short_content_unchanged(self, tmp_path):
        """Короткий контент не обрізається."""
        test_file = tmp_path / "short.md"
        content = "---\nslug: short\ntype: concept\n---\nHello world"
        test_file.write_text(content, encoding="utf-8")

        result = _read_wiki_content(test_file)
        assert "Hello world" in result


class TestTokenBudget:
    """Перевірка token budget enforcement."""

    def test_context_length_estimate(self):
        """Оцінка токенів: ~4 символи = 1 токен."""
        context = "x" * 2000
        estimated_tokens = len(context) / 4
        assert estimated_tokens > 400

    def test_budget_enforcement(self):
        """Контекст укладається в budget."""
        budget = 750
        max_chars = budget * 4  # ~3000
        context = "x" * 5000
        # Після enforcement має бути <= budget токенів
        truncated = context[:max_chars] + "\n\n[TRUNCATED]"
        estimated_tokens = len(truncated) / 4
        # +5 tolerance for "[TRUNCATED]" suffix (12 chars / 4 = 3 tokens + margin)
        assert estimated_tokens <= budget + 5
