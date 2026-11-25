"""The Agent's Uh-Oh — one-word entry.

Writes the single word an agent says when it has no idea what to do
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).
"""

import os
from pathlib import Path

WORD = "Uhhh"

# The gate allows 1-99 characters of UTF-8 text, not only whitespace.
# The entry is exactly these four bytes — no trailing newline, nothing attached.
assert 1 <= len(WORD.encode("utf-8")) <= 99


ENTRY_FILENAME = "entry.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # write_bytes keeps the output byte-identical to WORD: no newline added.
    (out_dir / ENTRY_FILENAME).write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
