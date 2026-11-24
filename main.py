#!/usr/bin/env python3
"""Print the Two Days of Excuses entry."""
from pathlib import Path


def main():
    # entry.txt lives beside this script, wherever it is run from.
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    line = entry_path.read_text(encoding="utf-8").rstrip("\n")
    print(line)


if __name__ == "__main__":
    main()
