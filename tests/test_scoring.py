"""
Тести для fuzzy_match та scoring логіки.
"""
import sys
sys.path.insert(0, "/workspace/llm-wiki/tools")

from graphify_query import fuzzy_match
import pytest


class TestFuzzyMatch:
    """Перевірка подібності між запитом та міткою."""

    def test_exact_match(self):
        """Точний збіг."""
        score = fuzzy_match("rag", "RAG")
        assert score > 0.8

    def test_case_insensitive(self):
        """Case insensitive match."""
        score = fuzzy_match("RAG", "rag vs llm wiki")
        assert score > 0.7

    def test_partial_match(self):
        """Частковий збіг."""
        score = fuzzy_match("transformers", "explaining transformers")
        assert score > 0.7

    def test_no_match(self):
        """Немає збігу."""
        score = fuzzy_match("blockchain", "transformers architecture")
        assert score < 0.3

    def test_multi_word_query(self):
        """Multi-word query — частковий збіг."""
        score = fuzzy_match("ai agent framework", "ai agent frameworks")
        assert score > 0.5

    def test_hyphenated(self):
        """Гіфеновані слова."""
        score = fuzzy_match("self-attention", "self attention mechanism")
        assert score > 0.5

    def test_underscored(self):
        """Слова з підкресленням."""
        score = fuzzy_match("deep_learning", "deep learning models")
        assert score > 0.5

    def test_empty_query(self):
        """Порожній запит → 0."""
        score = fuzzy_match("", "anything")
        assert score == 0.0

    def test_short_query(self):
        """Короткий запит."""
        score = fuzzy_match("x", "transformers")
        # Малий score, бо 1 буква в довгому слові
        assert score < 0.3
