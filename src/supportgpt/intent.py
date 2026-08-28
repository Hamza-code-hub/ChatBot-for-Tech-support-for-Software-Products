"""
Lightweight intent detection.

Designed as a deterministic baseline that can later be
replaced by an ML classifier or LLM-based router.
"""

INTENT_KEYWORDS = {
    "installation": {
        "install",
        "installation",
        "installer",
        "setup",
        "dependency",
        "dependencies",
    },

    "bug_error": {
        "bug",
        "error",
        "crash",
        "failed",
        "failure",
        "exception",
        "broken",
    },

    "configuration": {
        "configure",
        "configuration",
        "setting",
        "settings",
        "environment",
        "config",
    },

    "api_support": {
        "api",
        "endpoint",
        "token",
        "request",
        "integration",
        "webhook",
        "authentication",
    },

    "performance": {
        "slow",
        "performance",
        "latency",
        "memory",
        "cpu",
        "timeout",
        "lag",
    },

    "account": {
        "password",
        "login",
        "account",
        "username",
        "reset",
        "credential",
    },
}


def detect_intent(text: str) -> str:
    normalized = (
        text.lower()
        .replace("/", " ")
        .replace("-", " ")
    )

    tokens = set(
        normalized.split()
    )

    best_intent = "general"
    best_score = 0

    for intent, keywords in (
        INTENT_KEYWORDS.items()
    ):
        score = len(
            tokens.intersection(
                keywords
            )
        )

        if score > best_score:
            best_score = score
            best_intent = intent

    return best_intent
