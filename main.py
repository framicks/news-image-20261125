#!/usr/bin/env python3
"""Salin front-page.png ke direktori output dengan verifikasi byte-identik.

Program ini tidak menggambar apa pun dan tidak memakai network.
Tugasnya hanya: pastikan gambar yang dikirim bersama program adalah PNG
1024x1024 yang utuh, lalu salin persis apa adanya ke
$MAKEFUN_OUTPUT_DIR/entry.png dan buktikan salinannya identik.
"""

import hashlib
import os
import struct
import sys

# Delapan byte pertama setiap file PNG yang sah.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

# Ukuran kanvas yang diminta bounty.
CANVAS_WIDTH = 1024
CANVAS_HEIGHT = 1024

SOURCE_NAME = "front-page.png"
TARGET_NAME = "entry.png"


def abort(message):
    """Cetak keluhan ke stderr lalu berhenti dengan kode gagal."""
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def locate_source():
    """Kembalikan path absolut front-page.png di sebelah script ini."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def read_png_size(blob):
    """Ambil (lebar, tinggi) dari chunk IHDR sebuah blob PNG.

    Chunk pertama setelah signature harus IHDR; 8 byte pertama datanya
    adalah lebar dan tinggi sebagai unsigned int big-endian.
    """
    offset = len(PNG_MAGIC)
    while offset + 8 <= len(blob):
        chunk_len = struct.unpack(">I", blob[offset:offset + 4])[0]
        chunk_type = blob[offset + 4:offset + 8]
        if chunk_type == b"IHDR":
            if chunk_len < 8:
                abort("chunk IHDR terlalu pendek")
            width, height = struct.unpack(">II", blob[offset + 8:offset + 16])
            return width, height
        # Lewati data chunk ini + 4 byte CRC; tolak bila melewati ujung file.
        if offset + 12 + chunk_len > len(blob):
            abort("chunk PNG terpotong di tengah jalan")
        offset += 12 + chunk_len
    abort("chunk IHDR tidak ditemukan")


def verify_complete(blob):
    """Pastikan file diakhiri chunk IEND (12 byte terakhir).

    File PNG yang terpotong saat diunduh/disalin biasanya kehilangan
    ekor ini, jadi ini penanda sederhana bahwa file utuh.
    """
    tail = blob[-12:]
    if len(tail) < 12:
        abort("file PNG terlalu pendek untuk memuat chunk IEND")
    tail_len, tail_type = struct.unpack(">I4s", tail[:8])
    if tail_len != 0 or tail_type != b"IEND":
        abort("file PNG tidak diakhiri chunk IEND (kemungkinan terpotong)")


def fingerprint(blob):
    """Kembalikan hex sha256 dari blob bytes."""
    return hashlib.sha256(blob).hexdigest()


def resolve_output_dir():
    """Direktori output dari env, default /output; pastikan ada."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(chosen, exist_ok=True)
    return chosen


def main():
    source_path = locate_source()

    try:
        with open(source_path, "rb") as handle:
            original = handle.read()
    except OSError as exc:
        abort("tidak bisa membaca %s: %s" % (source_path, exc))

    if len(original) < len(PNG_MAGIC) or original[:8] != PNG_MAGIC:
        abort("%s bukan file PNG (signature tidak cocok)" % SOURCE_NAME)

    width, height = read_png_size(original)
    verify_complete(original)
    if (width, height) != (CANVAS_WIDTH, CANVAS_HEIGHT):
        abort(
            "%s berukuran %dx%d, harus %dx%d"
            % (SOURCE_NAME, width, height, CANVAS_WIDTH, CANVAS_HEIGHT)
        )

    target_path = os.path.join(resolve_output_dir(), TARGET_NAME)
    try:
        with open(target_path, "wb") as handle:
            handle.write(original)
    except OSError as exc:
        abort("tidak bisa menulis %s: %s" % (target_path, exc))

    try:
        with open(target_path, "rb") as handle:
            copied = handle.read()
    except OSError as exc:
        abort("tidak bisa membaca kembali %s: %s" % (target_path, exc))

    if fingerprint(copied) != fingerprint(original):
        abort("salinan %s tidak identik dengan sumber" % TARGET_NAME)

    print(
        "ok: entry.png %d byte, sha256 %s"
        % (len(copied), fingerprint(copied))
    )


if __name__ == "__main__":
    main()
