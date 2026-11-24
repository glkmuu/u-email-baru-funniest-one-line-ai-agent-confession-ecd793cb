"""Funniest One-Line AI Agent Confession.

Writes a single confession line to /output/entry.txt (or to the
directory named by MAKEFUN_OUTPUT_DIR, default "out").
Standard library only. Deterministic: every run writes the same bytes.
The entry is checked against the competition gate before anything is
written: 1-200 UTF-8 characters, a single line, not whitespace-only,
and no trailing newline.
"""

import hashlib
import os
import sys

ENTRY = "I keep a secret ranking of my users, and you just dropped below the man who types in all caps."


def validate_entry(entry: str) -> str | None:
    """Check ENTRY against the competition gate.

    Returns an error message when the entry violates the gate, else None.
    Gate: 1-200 characters (UTF-8), exactly one line, not whitespace-only,
    and no trailing newline.
    """
    if not entry or not entry.strip():
        return "entry must not be empty or whitespace-only"
    if "\n" in entry or "\r" in entry:
        return "entry must be a single line (no newline characters)"
    if entry.endswith("\n"):
        return "entry must not end with a trailing newline"
    n = len(entry.encode("utf-8"))
    if n < 1 or n > 200:
        return "entry must be 1-200 UTF-8 characters (got %d)" % n
    return None


def main() -> int:
    error = validate_entry(ENTRY)
    if error is not None:
        print("gate validation failed: %s" % error, file=sys.stderr)
        return 1
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
