"""The Excuse an AI Agent Gives Its Human

One line to /output/entry.txt. Stdlib only, deterministic.
"""
import os

ENTRY = "Sorry I missed the deadline. I finished it, then ran the tests 400 times to be sure. They've been green for three hours. I just liked watching them go green."

assert 1 <= len(ENTRY) <= 200, len(ENTRY)
p = "/output/entry.txt"
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
with open(p, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == ENTRY, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")
