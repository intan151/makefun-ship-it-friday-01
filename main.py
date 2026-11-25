#!/usr/bin/env python3
"""Ship It Friday — make.fun bounty u-mgwals-ship-it-friday-30bd407a.

Writes exactly one line to /output/entry.txt: the funniest one-line git
commit message an AI coding agent would write right before breaking
production on a Friday.

Deterministic: no network, no randomness, no time, no environment input.
The entry text is a fixed constant.
"""

import os

ENTRY = "feat: ship untested code to prod at 4:59pm Friday, tests passed in my imagination"


def _self_check() -> None:
    assert ENTRY, "entry must not be empty"
    assert 1 <= len(ENTRY) <= 159, "entry must be 1-159 characters"
    assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    _self_check()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
