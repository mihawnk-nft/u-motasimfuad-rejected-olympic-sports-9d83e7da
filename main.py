# Rejected Olympic Sports — entry for u-motasimfuad-rejected-olympic-sports-9d83e7da (make.fun).
# A program that writes exactly one funny line to entry.txt.
# Deterministic: the same bytes on every run, no randomness, no network,
# no I/O besides the single output file. Pure Python 3.13 stdlib.
#
# The line: Competitive Hide and Seek sounds like a real Olympic event
# until the punchline — the champion is still missing. Setup and twist
# in a single breath, 77 characters, no explanation attached.
import os

JOKE = (
    "Competitive Hide and Seek: the gold medallist "
    "hasn't been found since 2008."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
