"""
Інтеграційні тести для graphify_query.py — повний pipeline.
Перевіряють: preprocessing → scoring → BFS → content loading → token budget.
"""
import sys
sys.path.insert(0, "/workspace/llm-wiki/tools")

from graphify_query import (
    preprocess_query,
    find_relevant_nodes,
    calculate_score,
    query,
    _estimate_tokens,
    enforce_token_budget,
)
import json
import pytest


@pytest.fixture
def sample_graph():
    """Мінімальний граф для тестів."""
    return {
        "nodes": [
            {"id": "rag-vs-llm-wiki", "label": "RAG vs LLM Wiki", "type": "concept"},
            {"id": "explaining-transformers", "label": "Explaining Transformers", "type": "concept"},
            {"id": "ai-agent-frameworks", "label": "AI Agent Frameworks", "type": "concept"},
            {"id": "langchain-core==1.4.9", "label": "langchain-core==1.4.9", "type": "entity"},
            {"id": "vendor-package", "label": "vendor/some-package", "type": "entity"},
            {"id": "playbook-rag-impl", "label": "RAG Implementation Playbook", "type": "playbook"},
            {"id": "coverage-article", "label": "Apple Fixes Hide My Email Vulnerability After 404 Media Coverage", "type": "comparison"},
        ],
        "edges": [
            {"source": "rag-vs-llm-wiki", "target": "explaining-transformers"},
            {"source": "rag-vs-llm-wiki", "target": "playbook-rag-impl"},
            {"source": "ai-agent-frameworks", "target": "rag-vs-llm-wiki"},
        ]
    }


class TestCalculateScore:
    """Перевірка multi-factor scoring."""

    def test_word_match(self):
        """Слова в label → високий score."""
        score = calculate_score("rag", "RAG vs LLM Wiki", "rag-vs-llm-wiki", "concept")
        assert score > 0.5  # rag match + all_match + slug match

    def test_slug_match(self):
        """Слова в slug → medium score."""
        score = calculate_score("transformers", "Some Random Topic", "explaining-transformers", "concept")
        assert score > 0.1  # slug match only

    def test_both_words_boost(self):
        """Обидва слова в label → +0.10."""
        score = calculate_score(
            "rag transformers",
            "RAG Transformers Architecture",
            "rag-transformers-arch",
            "concept"
        )
        assert score > 0.6  # 2/2 words + all_match

    def test_no_match(self):
        """Немає збігу → низький score."""
        score = calculate_score("blockchain", "RAG vs LLM Wiki", "rag-vs-llm-wiki", "concept")
        assert score == 0.0

    def test_word_boundary_prevents_fuzzy(self):
        """Word boundary: 'rag' не має збігати в 'coverage'."""
        score = calculate_score(
            "rag",
            "Apple Fixes Hide My Email Vulnerability After 404 Media Coverage",
            "coverage-article",
            "comparison"
        )
        assert score == 0.0  # "rag" not a word in "coverage"

    def test_package_version_penalty(self):
        """Package version nodes → ×0.1."""
        score = calculate_score(
            "langchain",
            "langchain-core==1.4.9",
            "langchain-core==1.4.9",
            "entity"
        )
        assert score < 0.2  # penalty applied (~0.1 after ×0.1)

    def test_hyphen_normalized(self):
        """Гіфени нормалізуються: self-attention = self attention."""
        score = calculate_score(
            "self attention",
            "Self Attention Mechanism",
            "self-attention-mechanism",
            "concept"
        )
        assert score > 0.5  # words match after normalization

    def test_underscore_normalized(self):
        """Підкреслення нормалізуються."""
        score = calculate_score(
            "deep learning",
            "Deep Learning Models",
            "deep_learning_models",
            "concept"
        )
        assert score > 0.5


class TestFindRelevantNodes:
    """Перевірка релевантності результатів."""

    def test_noise_filtered(self, sample_graph):
        """Noise вузли (vendor, issue, release) відсікаються."""
        results = find_relevant_nodes(sample_graph, "rag", top_k=5, min_score=0.3)
        for r in results:
            assert "vendor/" not in r["label"].lower()
            assert "issue #" not in r["label"].lower()
            assert "release notes" not in r["label"].lower()

    def test_package_version_filtered(self, sample_graph):
        """Package-version вузли відсікаються."""
        results = find_relevant_nodes(sample_graph, "langchain", top_k=5, min_score=0.3)
        for r in results:
            assert "==" not in r["label"]
            assert "~=" not in r["label"]

    def test_word_boundary_filters_coverage(self, sample_graph):
        """'rag' не збігає в 'coverage'."""
        results = find_relevant_nodes(sample_graph, "rag", top_k=5, min_score=0.3)
        for r in results:
            assert "coverage" not in r["label"].lower() or "rag" not in r["label"].lower()


class TestSummaryFirst:
    """Перевірка summary-first token optimization."""

    def test_token_estimation(self):
        """Оцінка токенів: ~4 chars per token."""
        assert _estimate_tokens("hello world") == 2  # 11 chars / 4 = 2
        assert _estimate_tokens("x" * 3000) == 750  # 3000 / 4 = 750

    def test_budget_enforcement(self):
        """Контекст обрізається за budget."""
        long_text = "x" * 5000
        truncated = enforce_token_budget(long_text, budget_chars=3000)
        assert len(truncated) <= 3000 + 50  # +50 for "\n\n[TRUNCATED...]" suffix
        assert "TRUNCATED" in truncated

    def test_budget_no_truncation(self):
        """Короткий контекст не обрізається."""
        short_text = "x" * 500
        result = enforce_token_budget(short_text, budget_chars=3000)
        assert result == short_text


class TestEndToEnd:
    """Енд-ту-енд тести з реальним графом."""

    @pytest.fixture
    def real_graph(self):
        with open("/workspace/graphify-out/graph-from-wiki.json") as f:
            return json.load(f)

    def test_rag_query_real_graph(self, real_graph):
        """RAG запит → релевантні сторінки."""
        result = query(real_graph, "RAG", depth=1, top_k=3)
        assert result["found_nodes"] > 0
        # Жодна сторінка не має бути "coverage" або "issue"
        for p in result["pages"]:
            label = p["title"].lower()
            assert "coverage" not in label or "rag" in label
            assert "issue #" not in label

    def test_transformers_query_real_graph(self, real_graph):
        """Transformers запит → релевантні сторінки."""
        result = query(real_graph, "transformers", depth=1, top_k=3)
        assert result["found_nodes"] > 0
        # Топ-результат має містити "transformers"
        if result["pages"]:
            label = result["pages"][0]["title"].lower()
            assert "transformers" in label

    def test_token_stats_present(self, real_graph):
        """Token stats присутні в результаті."""
        result = query(real_graph, "RAG", depth=1, top_k=3)
        assert "token_stats" in result
        stats = result["token_stats"]
        assert "total_chars" in stats
        assert "estimated_tokens" in stats
        assert stats["mode"] == "summary-first"

    def test_token_budget_enforced(self, real_graph):
        """Контекст не перевищує budget."""
        result = query(real_graph, "RAG", depth=2, top_k=5)
        stats = result["token_stats"]
        assert stats["total_chars"] <= 3100  # 3000 + margin for headers + [TRUNCATED]
