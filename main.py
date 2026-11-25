#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes one line (at most 140 characters) inventing the most useless
superpower to /output/entry.txt, per the kit's RULES.txt gate.
"""

import os

ENTRY = "I can read minds \u2014 only my own, and only the thoughts I had five seconds ago."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert text.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars: {text}")


if __name__ == "__main__":
    main()
