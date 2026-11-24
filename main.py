#!/usr/bin/env python3
"""The Funniest AI Excuse — one-line entry writer.

Writes the excuse to the output entry file for the make.fun judge.
"""
import os

ENTRY = "I asked the tool for the file, the tool asked me for the file, and we've been politely deadlocked for forty minutes."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
