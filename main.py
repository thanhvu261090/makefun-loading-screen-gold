#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one sharp, funny loading-screen tip for stressed developers
and AI coding agents to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

ENTRY = (
    "Tip: the loading bar is not stuck. Your AI agent is reading your code, "
    "sighing, and quietly rewriting it for the third time."
)

MAX_CHARS = 200


def gate_check(text: str) -> None:
    """Enforce the kit gate: UTF-8 text, 1-200 chars, not only whitespace.

    Also enforces the single-line loading-screen shape: no newlines,
    no control characters, and no leading/trailing padding.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    for ch in text:
        if ch == "\n" or ch == "\r" or ord(ch) < 0x20:
            raise ValueError("entry must be a single line with no control characters")
    text.encode("utf-8")


def main() -> None:
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
