#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry generator.

Writes the single-line entry to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Pure Python 3 stdlib, deterministic, no network.
"""

import os

ENTRY = "My apologies \u2014 I did write the bug, but the compiler compiled it, the tests passed it, and honestly at that point it felt like a team effort."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
