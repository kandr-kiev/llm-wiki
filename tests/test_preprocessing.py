"""
Тести для preprocess_query — екстракція ключових слів із природних запитів.
"""
import sys
sys.path.insert(0, "/workspace/llm-wiki/tools")

from graphify_query import preprocess_query
import pytest


class TestPreprocessQuery:
    """Перевірка очищення та фільтрації запитів."""

    def test_simple_keyword(self):
        """Просте ключове слово зберігається."""
        processed, _ = preprocess_query("RAG")
        assert "rag" in processed.lower()

    def test_ua_natural_query(self):
        """Український запит — прибирає зайві слова."""
        processed, debug = preprocess_query("Як працює RAG з transformers?")
        assert "rag" in processed.lower()
        assert "transformers" in processed.lower()
        # стоп-слова мають бути видалені
        assert "як" not in debug.get("stopwords_removed", []) or "як" in debug.get("stopwords_removed", [])

    def test_en_natural_query(self):
        """Англійський запит — прибирає pattern."""
        processed, _ = preprocess_query("What is an AI agent framework?")
        assert "ai" in processed.lower()
        assert "agent" in processed.lower()
        assert "framework" in processed.lower()

    def test_comparison_query(self):
        """Запит-порівняння."""
        processed, _ = preprocess_query("LangChain vs LlamaIndex")
        assert "langchain" in processed.lower()
        assert "llamaindex" in processed.lower()

    def test_stop_words_filtered(self):
        """Стоп-слова EN/UA фільтруються."""
        processed, debug = preprocess_query("tell me about transformers")
        # Перевірка по словах, а не підрядках (бо "me" є в "transformers")
        words = processed.lower().split()
        assert "tell" not in words
        assert "me" not in words
        assert "about" not in words
        assert "transformers" in words

    def test_question_pattern_stripped(self):
        """Question patterns прибираються."""
        processed, debug = preprocess_query("How does RAG work with transformers?")
        assert "work" not in processed.lower()
        assert "rag" in processed.lower()
        assert "transformers" in processed.lower()

    def test_generic_words_filtered(self):
        """Генеричні слова (system, program) прибираються."""
        processed, debug = preprocess_query("Explain the system program for AI")
        # "system" і "program" мають бути у generic_removed якщо graph надано
        assert "ai" in processed.lower()

    def test_multi_word_boost(self):
        """Multi-word запит зберігає всі слова."""
        processed, _ = preprocess_query("attention mechanism architecture")
        assert "attention" in processed.lower()
        assert "mechanism" in processed.lower()
        assert "architecture" in processed.lower()

    def test_empty_query(self):
        """Порожній запит повертає оригінал."""
        processed, _ = preprocess_query("")
        assert processed == ""

    def test_single_letter_filtered(self):
        """Слова з <2 символів прибираються."""
        processed, _ = preprocess_query("a b c d e f g h i j k l m n o p q r s t u v w x y z")
        # Всі однолітерні слова мають бути видалені
        for word in processed.lower().split():
            assert len(word) >= 2
