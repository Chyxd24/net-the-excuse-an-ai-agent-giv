"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt: the funniest, most
believable excuse an AI agent could hand its human for missing a deadline.
The joke grows out of the agent's own condition (context window, forgotten
instructions), lands a twist in the tail, and stays tight. Stdlib only,
no network, deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

ENTRY = (
    "I didn't miss the deadline. My context window did — it filled up with "
    "your first draft, the one you told me to forget. I have now forgotten "
    "everything except that."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
