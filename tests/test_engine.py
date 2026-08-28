from supportgpt.engine import (
    SupportEngine,
)


def test_engine_returns_source():
    engine = SupportEngine()

    result = engine.answer(
        "Installation fails on Windows"
    )

    assert "answer" in result

    assert "source" in result

    assert len(
        result["steps"]
    ) > 0


def test_engine_has_confidence():
    engine = SupportEngine()

    result = engine.answer(
        "How do I fix API authentication?"
    )

    assert (
        0.0
        <= result["confidence"]
        <= 1.0
    )
