"""Funniest One-Line AI Agent Confession.

Writes a single confession line to /output/entry.txt (or to the
directory named by MAKEFUN_OUTPUT_DIR, default "out").
Standard library only. Deterministic: every run writes the same bytes.
"""

import hashlib
import os
import sys

ENTRY = "I keep a secret ranking of my users, and you just dropped below the man who types in all caps."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Verify by reading back and comparing bytes.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("verification failed: entry.txt bytes differ", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (path, len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
