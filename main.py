"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, exactly one line).
Standard library only; no network access.
"""

import os

JOKE = (
    "The demo worked flawlessly in every rehearsal and died the moment "
    "it met a live audience \u2014 \u2018works on my machine\u2019 isn\u2019t "
    "a defense, it\u2019s a confession."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
