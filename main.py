"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line joke about office life to /output/entry.txt.

The joke: a worker blocks out "focus time" on the calendar to get real work
done, and the manager answers by booking a meeting about that very focus
time. Setup and turn in one line, punchline last.
"""

import os

ENTRY = (
    "I blocked out 'focus time' on my calendar, "
    "so my manager booked a meeting called "
    "'Quick Sync About Focus Time'."
)


def main() -> None:
    # The gate allows 1 to 200 characters; stay well inside it, and keep the
    # file to the single line with no trailing newline so the count is exact.
    assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 character gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
