#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261120.

The entry is one image: news.png, a 1024x1024 poster summing up the world
news of Friday 20 November 2026. This program copies that image, byte for
byte, to /output/entry.png. It uses only the Python standard library, needs
no network, and is deterministic: copying the same file twice writes the
same bytes twice.
"""

import os
import shutil
import sys

SOURCE_NAME = "news.png"
TARGET_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_dir():
    """Where the entry image goes: /output in the grader, or the override."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(source):
        print("missing bundled image: %s" % source, file=sys.stderr)
        return 1
    with open(source, "rb") as handle:
        magic = handle.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        print("bundled image is not a PNG: %s" % source, file=sys.stderr)
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, TARGET_NAME)
    shutil.copyfile(source, target)
    print("wrote %s (%d bytes)" % (target, os.path.getsize(target)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
