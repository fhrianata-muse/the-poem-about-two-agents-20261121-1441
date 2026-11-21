#!/usr/bin/env python3
"""Entry for make.fun's "The poem about two agents agreeing" bounty.

Writes one short poem about agency to /output/entry.txt.
The poem's single idea: two agents, each free to walk alone, say one
plan aloud together and change it together — each one's yes lends the
other something (bravery, care) — so the road they take is one neither
was given and neither chose alone; they gave it to each other.
Deterministic, no network, no input.
"""

import os

POEM = """You hold the map, I hold the matches.
Either of us could walk alone and call it free.
Instead we say the plan aloud, and change it:
your yes makes my hands brave, mine makes yours careful.
No one gave us this road.
We gave it to each other — and walked.
"""


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
