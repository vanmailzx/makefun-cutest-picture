"""Cutest picture entry (Python 3.13, standard library only).

The picture is the entry.png beside this file; the program copies it to
/output/entry.png. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The copy is byte-for-byte and deterministic: two runs write identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUT_DIR / "entry.png"
    shutil.copyfile(SRC, dest)
    # Fail loudly instead of shipping a truncated copy.
    if dest.stat().st_size != SRC.stat().st_size:
        raise RuntimeError("copied entry.png size does not match the source")


if __name__ == "__main__":
    main()
