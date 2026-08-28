"""
TF-IDF knowledge retrieval.

This keeps the baseline project:
- local
- reproducible
- API-key free
- easy to extend to embeddings / RAG later
"""

from dataclasses import dataclass

from sklearn.feature_extraction.text import (
    TfidfVectorizer,
)

from sklearn.metrics.pairwise import (
    cosine_similarity,
)


@dataclass
class SearchResult:
    article: dict
    score: float


class KnowledgeRetriever:

    def __init__(self, articles):
        self.articles = articles

        self.documents = [
            self._article_to_text(article)
            for article in articles
        ]

        self.vectorizer = (
            TfidfVectorizer(
                stop_words="english",
                ngram_range=(1, 2),
            )
        )

        self.matrix = (
            self.vectorizer.fit_transform(
                self.documents
            )
        )


    @staticmethod
    def _article_to_text(article):
        return " ".join(
            [
                article["title"],
                article["category"],
                " ".join(
                    article["keywords"]
                ),
                article["summary"],
                " ".join(
                    article["steps"]
                ),
            ]
        )


    def search(
        self,
        query,
        top_k=3,
    ):
        query_vector = (
            self.vectorizer.transform(
                [query]
            )
        )

        scores = cosine_similarity(
            query_vector,
            self.matrix,
        )[0]

        ranking = (
            scores.argsort()[::-1]
        )

        results = []

        for index in ranking[
            :top_k
        ]:
            results.append(
                SearchResult(
                    article=(
                        self.articles[
                            int(index)
                        ]
                    ),
                    score=float(
                        scores[
                            int(index)
                        ]
                    ),
                )
            )

        return results
