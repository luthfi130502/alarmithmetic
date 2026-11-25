#!/usr/bin/env python3
"""Invent-a-word entry: writes the coined word and its one-line
definition to /output/entry.txt for the make.fun gate."""

from pathlib import Path

WORD = "alarmithmetic"
DEFINITION = (
    "the sums you do at 3 a.m., counting the hours left before the "
    "alarm, and waking further with every answer"
)


def entry_line() -> str:
    return WORD + ": " + DEFINITION


def main() -> None:
    line = entry_line()
    if not 1 <= len(line) <= 140:
        raise SystemExit("entry line outside the 1..140 character gate")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
