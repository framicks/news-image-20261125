#!/usr/bin/env python3
"""Publish the 25 November 2026 front page as the competition entry.

The newspaper image ships in this repository as ``front-page.png``.
This program draws nothing and reaches for no network: it checks
that the shipped file really is a 1024x1024 PNG and then writes an
exact copy to ``$MAKEFUN_OUTPUT_DIR/entry.png`` (``/output`` when
the variable is unset). Because the image is only ever copied,
repeated runs agree byte for byte.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
WANT_WIDTH = 1024
WANT_HEIGHT = 1024
SHIPPED = "front-page.png"
TARGET = "entry.png"


def die(message):
    print(f"main.py: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_shipped():
    here = Path(__file__).resolve().parent
    path = here / SHIPPED
    if not path.is_file():
        die(f"missing {SHIPPED} next to {Path(__file__).name}")
    return path.read_bytes()


def check_png(blob):
    if blob[:8] != PNG_MAGIC:
        die("front-page.png does not start with the PNG signature")
    if len(blob) < 33 or blob[12:16] != b"IHDR":
        die("front-page.png has no IHDR chunk where one is expected")
    width, height = struct.unpack(">II", blob[16:24])
    if (width, height) != (WANT_WIDTH, WANT_HEIGHT):
        die(f"front-page.png is {width}x{height}, expected 1024x1024")


def main():
    blob = load_shipped()
    check_png(blob)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / TARGET
    target.write_bytes(blob)
    digest = hashlib.sha256(blob).hexdigest()
    # Re-read what landed on disk so a short write can never pass
    # silently: the entry must be the shipped image, byte for byte.
    if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
        die(f"{target} does not match the shipped image after writing")
    print(f"wrote {target} ({len(blob)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
