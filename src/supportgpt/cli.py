"""
Interactive terminal client.
"""

from .engine import SupportEngine


def main():
    engine = SupportEngine()

    print(
        "\nSupportGPT AI"
    )

    print(
        "Technical Support Assistant"
    )

    print(
        "Type 'exit' to quit.\n"
    )

    while True:
        query = input(
            "You > "
        ).strip()

        if query.lower() in {
            "exit",
            "quit",
        }:
            break

        result = engine.answer(
            query
        )

        print(
            "\nSupportGPT > "
            + result["answer"]
        )

        if result["steps"]:
            print(
                "\nSuggested steps:"
            )

            for index, step in (
                enumerate(
                    result["steps"],
                    start=1,
                )
            ):
                print(
                    f"{index}. {step}"
                )

        print(
            "\nSource: "
            + result["source"][
                "title"
            ]
        )

        print(
            "Confidence: "
            f"{result['confidence']:.2f}"
        )

        if result[
            "escalation_recommended"
        ]:
            print(
                "Escalation recommended."
            )

        print()


if __name__ == "__main__":
    main()
