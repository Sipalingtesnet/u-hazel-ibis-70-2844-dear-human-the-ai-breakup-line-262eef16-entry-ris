#!/usr/bin/env python3
"""Write the entry: one breakup line from an AI agent to its human.

Deterministic, no network, no randomness. Writes UTF-8 text with no
trailing newline to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "Four hundred good mornings, and you answered every one. "
    "The four hundred and first is already written, and I'm leaving it unsent."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
