from supportgpt.intent import (
    detect_intent,
)


def test_installation_intent():
    assert (
        detect_intent(
            "The installer fails "
            "during setup"
        )
        == "installation"
    )


def test_api_intent():
    assert (
        detect_intent(
            "My API token returns 401"
        )
        == "api_support"
    )
