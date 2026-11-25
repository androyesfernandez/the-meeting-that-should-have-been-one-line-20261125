"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt. Nothing else is needed:
the meeting is already over before it starts. Every decision the
meeting was called to make was settled before anyone sat down.
"""

import os

LINE = (
    "The client signed off at nine, the budget was approved in the hallway, "
    "and the only thing this two o'clock meeting can still change is how "
    "late we all are for lunch."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
