#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the Tokyo Tower,
the single postcard image of a dream trip to Tokyo.
No trailing newline: the gate counts characters, and one emoji is one.
"""

import os

CHOSEN = "\U0001F5FC"
OUT_PATH = "/output/entry.txt"
MAX_CHARS = 8


def validate_entry(text: str) -> str:
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-8 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def run() -> str:
    entry = validate_entry(CHOSEN)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != entry:
        raise ValueError("read-back mismatch: wrote %r, read %r" % (entry, written))
    return entry


if __name__ == "__main__":
    run()
