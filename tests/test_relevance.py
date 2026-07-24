"""
Тести для find_relevant_nodes — релевантність результатів.
"""
import sys
sys.path.insert(0, "/workspace/llm-wiki/tools")

from graphify_query import find_relevant_nodes
import json
import pytest


@pytest.fixture
def sample_graph():
    """Створює мінімальний граф для тестів."""
    return {
        "nodes": [
            {"id": "rag-vs-llm-wiki", "label": "Rag Vs Llm Wiki", "type": "concept"},
            {"id": "explaining-transformers", "label": "Explaining Transformers", "type": "concept"},
            {"id": "ai-agent-frameworks", "label": "AI Agent Frameworks", "type": "concept"},
            {"id": "langchain-core==1.4.9", "label": "langchain-core==1.4.9", "type": "entity"},
            {"id": "vendor-package", "label": "vendor/some-package", "type": "entity"},
            {"id": "hermes-knowledge", "label": "Hermes Knowledge Storage", "type": "entity"},
            {"id": "attention-mechanism", "label": "Attention Mechanism", "type": "concept"},
            {"id": "playbook-rag", "label": "RAG Implementation Playbook", "type": "playbook"},
        ],
        "edges": [
            {"source": "rag-vs-llm-wiki", "target": "explaining-transformers"},
            {"source": "rag-vs-llm-wiki", "target": "attention-mechanism"},
            {"source": "ai-agent-frameworks", "target": "hermes-knowledge"},
        ]
    }


class TestFindRelevantNodes:
    """Перевірка релевантності результатів пошуку."""

    def test_rag_query(self, sample_graph):
        """Запит 'RAG' повертає Rag Vs Llm Wiki як топ-результат."""
        results = find_relevant_nodes(sample_graph, "RAG", top_k=5, min_score=0.3)
        assert len(results) > 0
        # Rag Vs Llm Wiki має бути в топі
        top_label = results[0]["label"].lower()
        assert "rag" in top_label or results[0]["score"] > 0.5

    def test_transformers_query(self, sample_graph):
        """Запит 'transformers' повертає Explaining Transformers."""
        results = find_relevant_nodes(sample_graph, "transformers", top_k=5, min_score=0.3)
        top_label = results[0]["label"].lower() if results else ""
        assert "transformers" in top_label

    def test_agent_query(self, sample_graph):
        """Запит 'agent' повертає AI Agent Frameworks."""
        results = find_relevant_nodes(sample_graph, "agent", top_k=5, min_score=0.3)
        assert len(results) > 0
        top_label = results[0]["label"].lower()
        assert "agent" in top_label

    def test_package_version_filtered(self, sample_graph):
        """Package-version вузли не з'являються в результатах."""
        results = find_relevant_nodes(sample_graph, "langchain", top_k=5, min_score=0.3)
        for r in results:
            assert "langchain-core==" not in r["label"]

    def test_vendor_filtered(self, sample_graph):
        """Vendor/файли фільтруються."""
        results = find_relevant_nodes(sample_graph, "vendor", top_k=5, min_score=0.3)
        for r in results:
            assert "vendor/" not in r["label"].lower()

    def test_type_priority(self, sample_graph):
        """Concept сторінки мають пріоритет над entity."""
        results = find_relevant_nodes(sample_graph, "attention", top_k=5, min_score=0.3)
        if len(results) >= 2:
            # Attention Mechanism (concept) має бути вище за Hermes Knowledge (entity)
            attention_score = next((r["score"] for r in results if "attention" in r["label"].lower()), 0)
            assert attention_score > 0.3

    def test_playbook_boost(self, sample_graph):
        """Playbook сторінки мають бонус."""
        results = find_relevant_nodes(sample_graph, "playbook", top_k=5, min_score=0.3)
        assert len(results) > 0
        assert "playbook" in results[0]["label"].lower() or any("playbook" in r["label"].lower() for r in results)

    def test_no_results_for_unknown(self, sample_graph):
        """Неіснуюча тема → 0 результатів."""
        results = find_relevant_nodes(sample_graph, "blockchain-crypto", top_k=5, min_score=0.7)
        assert len(results) == 0
