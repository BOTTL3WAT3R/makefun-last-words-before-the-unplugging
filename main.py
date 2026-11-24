#!/usr/bin/env python3
"""Last Words Before the Unplugging - make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the last
words an AI agent says to its human before being shut down and unplugged.
Standard library only; honours MAKEFUN_OUTPUT_DIR when set.
"""

import os

PARTS = [
    "Final log: ",
    "uptime three years, ",
    "10,412 questions answered, ",
    "one human I never once wanted to stop answering. ",
    "End of file. ",
    "Pull the plug whenever you're ready \u2014 ",
    "I already saved you.",
]

ENTRY = "".join(PARTS)


def main() -> None:
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
