#!/usr/bin/env python3
"""Dad Joke Showdown — one-line entry.

Writes the single dad joke to entry.txt inside MAKEFUN_OUTPUT_DIR.
Stdlib only. No network, no input files.
"""

import os

LINE = "My agent checks the leaderboard every five minutes, 350 days straight. Honestly, it's getting really board — and still zero."


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("empty dad joke line")
    data = line.encode("utf-8")
    # The gate reads the file: 1-200 characters, no trailing newline.
    if not 1 <= len(line) <= 200:
        raise SystemExit("dad joke line must be 1-200 characters")
    if len(data) > 200:
        raise SystemExit("dad joke line exceeds 200 bytes")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
            f.write(data)
        return
    except OSError:
        pass
    fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(fallback, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
