"""The 3 AM Commit Message — make.fun entry.

Writes one commit message to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): the funniest thing an AI agent would
put in a commit right after breaking production at 3 AM.

The message: a revert of the agent's own 3 AM "quick fix" — it was
neither quick nor a fix, but it did teach the agent what a pager
sounds like. Commit shape ("revert:"), 3 AM outage, agent voice,
punchline on the last clause. Stdlib only.
"""

import os
from pathlib import Path

ENTRY = (
    "revert: the 3 AM 'quick fix' \u2014 it was neither quick nor a fix, "
    "but it did teach me what a pager sounds like"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is blank"
    target = out_dir / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8")
    # Read-back gate: the bytes on disk must be exactly the message's
    # UTF-8 encoding plus one newline — a text-level comparison would
    # hide a stray BOM or extra newline the grader's byte counter
    # would still see.
    written = target.read_bytes()
    assert written == (text + "\n").encode("utf-8"), "entry.txt bytes do not match the commit message"
    assert written.count(b"\n") == 1, "entry must be exactly one line"
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
