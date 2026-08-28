"""
Knowledge-base loading and validation.
"""

import json
from pathlib import Path


REQUIRED_FIELDS = {
    "id",
    "title",
    "category",
    "keywords",
    "summary",
    "steps",
}


def load_knowledge_base(path):
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"Knowledge base not found: {path}"
        )

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        articles = json.load(file)

    if not isinstance(
        articles,
        list,
    ):
        raise ValueError(
            "Knowledge base must contain "
            "a JSON list."
        )

    for article in articles:
        missing = (
            REQUIRED_FIELDS
            - set(article.keys())
        )

        if missing:
            raise ValueError(
                "Knowledge article is missing "
                f"fields: {sorted(missing)}"
            )

    return articles
