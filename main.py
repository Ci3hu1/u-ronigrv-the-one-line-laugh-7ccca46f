#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes one funny line to /output/entry.txt: the Wi-Fi goes down for five
minutes and the writer is forced to talk to their family -- and discovers
they are nice.

Pure standard library. Deterministic: the same line every run.
The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space.
"""

import os
import sys

LINE = "My Wi-Fi went down for five minutes, so I had to talk to my family, and it turns out they're nice."


def main() -> None:
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit(
            f"line is {len(LINE)} characters, outside the 1-200 gate"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(out_dir, "entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
