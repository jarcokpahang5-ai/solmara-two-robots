#!/usr/bin/env python3
"""Two Robots in an Elevator -- one line of awkward robot small talk.

Pure Python 3.13 standard library only. Deterministic, no network.
Prints the entry line to stdout and writes the exact same line
to /output/entry.txt (falling back to ./output/entry.txt when /output
is not writable, e.g. during local testing).
"""

import os
import sys

ENTRY = (
    "So... do you also press your floor button twice just to feel "
    "in control, or is that just my firmware?"
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 200:
        print("entry must be 1-200 characters", file=sys.stderr)
        return 1
    if ENTRY.strip() == "":
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
        except OSError:
            continue
    print(ENTRY, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
