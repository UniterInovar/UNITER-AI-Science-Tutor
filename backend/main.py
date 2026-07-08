"""
UNITER AI Science Tutor

Main application entry point.
"""

from __future__ import annotations

from ai_engine.tutor import ScienceTutor


def display_answer(answer) -> None:
    """
    Display the tutor's answer in a readable format.
    """

    if isinstance(answer, dict):

        for key, value in answer.items():

            print(f"\n{key.upper()}")

            if isinstance(value, dict):

                for sub_key, sub_value in value.items():
                    print(f"  {sub_key}: {sub_value}")

            elif isinstance(value, list):

                for item in value:
                    print(f"  - {item}")

            else:
                print(value)

    else:
        print(answer)


def main() -> None:
    """
    Run the AI Science Tutor.
    """

    tutor = ScienceTutor()

    print("=" * 60)
    print("UNITER AI SCIENCE TUTOR")
    print("=" * 60)

    while True:

        subject = input("\nSubject (or 'exit'): ").strip()

        if subject.lower() == "exit":
            break

        topic = input("Topic: ").strip()

        answer = tutor.answer(
            subject,
            topic,
        )

        print("\n" + "-" * 60)

        display_answer(answer)

        print("-" * 60)

    print("\nThank you for using UNITER AI Science Tutor.")


if __name__ == "__main__":
    main()