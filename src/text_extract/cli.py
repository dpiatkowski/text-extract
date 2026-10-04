"""Command line interface."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from text_extract.readers import DEFAULT_INPUT_FORMAT, READERS
from text_extract.writers import DEFAULT_OUTPUT_FORMAT, WRITERS


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="text-extract",
        description="Extract text and tables from documents and save them in another format.",
    )
    p.add_argument("inputs", nargs="+", type=Path, metavar="FILE", help="input file(s)")
    p.add_argument(
        "-i", "--input-format", choices=sorted(READERS), default=DEFAULT_INPUT_FORMAT,
        help="input format (default: %(default)s)",
    )
    p.add_argument(
        "-f", "--output-format", choices=sorted(WRITERS), default=DEFAULT_OUTPUT_FORMAT,
        help="output format (default: %(default)s)",
    )
    p.add_argument(
        "-o", "--output-dir", type=Path, default=None,
        help="directory for output files (default: next to each input file)",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    read = READERS[args.input_format]
    write, ext = WRITERS[args.output_format]
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)

    failures = 0
    for src in args.inputs:
        try:
            if not src.is_file():
                raise FileNotFoundError(f"not a file: {src}")
            out_dir = args.output_dir or src.parent
            dest = out_dir / (src.stem + ext)
            write(read(src), dest)
            print(f"{src} -> {dest}")
        except Exception as e:  # keep going with remaining files
            failures += 1
            print(f"error: {src}: {e}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
