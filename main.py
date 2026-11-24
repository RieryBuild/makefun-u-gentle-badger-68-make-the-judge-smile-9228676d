"""Make the Judge Smile — make.fun bounty entry.

Writes one line about a small good thing that happened this morning to
/output/entry.txt. Deterministic: the same fixed text on every run.
Python 3.13 stdlib only.
"""

import os

# Final line, picked from 7 fresh candidates and refined (see gate-run.md):
# the corner-shop man presses HIS last mango into my hands and refuses
# the money — he'd already eaten two. Warmth shown through action,
# turn at the end. V4 wins over V1 ("the last mango" -> "his last mango":
# the sacrifice is personal, same length) and over V3 ("gave me": flatter,
# loses the pressing gesture that shows the insistence of the gift).
LINE = "This morning the old man at the corner shop pressed his last mango into my hands and waved my money away \u2014 he'd already eaten two."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
