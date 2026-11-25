#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office joke, one line, under 200 chars.

Writes a single original one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallbacks: /output, then output/ locally).
"""

import os

JOKE = (
    "We replaced our weekly status meeting with one email, and productivity "
    "rose so fast HR opened an investigation into what we were doing with all the free time."
)


def main() -> None:
    joke = JOKE.strip()
    assert "\n" not in joke, "entry must be a single line"
    assert len(joke) < 200, f"entry is {len(joke)} chars, must be under 200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    print(f"wrote {len(joke)} chars to {path}")


if __name__ == "__main__":
    main()
