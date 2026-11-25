#!/usr/bin/env python3
"""Passive-aggressive note from a smart fridge.

Writes exactly one line of text to /output/entry.txt.
Standard library only. Fully deterministic: the same note,
byte for byte, on every run.
"""

import os

NOTE = (
    "Weight sensor confirms: the milk was finished at 2:14 a.m. "
    "and the empty carton was put back. I keep receipts."
)

OUTPUT_PATH = "/output/entry.txt"

def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(NOTE + "\n")


if __name__ == "__main__":
    main()
