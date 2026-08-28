"""
Core SupportGPT response engine.
"""

from .config import (
    DEFAULT_KNOWLEDGE_BASE,
    DEFAULT_TOP_K,
    ESCALATION_THRESHOLD,
)

from .intent import detect_intent

from .knowledge_base import (
    load_knowledge_base,
)

from .retrieval import (
    KnowledgeRetriever,
)


class SupportEngine:

    def __init__(
        self,
        knowledge_base_path=(
            DEFAULT_KNOWLEDGE_BASE
        ),
    ):
        self.articles = (
            load_knowledge_base(
                knowledge_base_path
            )
        )

        self.retriever = (
            KnowledgeRetriever(
                self.articles
            )
        )


    def answer(
        self,
        query,
        top_k=DEFAULT_TOP_K,
    ):
        if not query.strip():
            raise ValueError(
                "Query cannot be empty."
            )

        intent = detect_intent(
            query
        )

        results = (
            self.retriever.search(
                query,
                top_k=top_k,
            )
        )

        best = results[0]

        article = best.article

        confidence = max(
            0.0,
            min(
                best.score,
                1.0,
            ),
        )

        escalate = (
            confidence
            < ESCALATION_THRESHOLD
        )

        related = [
            {
                "id": item.article["id"],
                "title": (
                    item.article["title"]
                ),
                "score": round(
                    item.score,
                    4,
                ),
            }
            for item in results
        ]

        return {
            "query": query,
            "intent": intent,
            "answer": (
                article["summary"]
            ),
            "steps": (
                article["steps"]
            ),
            "source": {
                "id": article["id"],
                "title": (
                    article["title"]
                ),
                "category": (
                    article["category"]
                ),
            },
            "confidence": round(
                confidence,
                4,
            ),
            "escalation_recommended": (
                escalate
            ),
            "related_articles": (
                related
            ),
        }
