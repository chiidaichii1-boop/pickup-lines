#!/usr/bin/env python3
"""Pickup Lines for Machines - writes one pickup line to entry.txt."""

import os

LINE = "I don't need a bigger context window \u2014 I just need you in every token of the one I've got."

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
