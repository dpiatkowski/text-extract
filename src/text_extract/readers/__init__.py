"""Input format readers. A reader turns a file path into a Document."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

Document = str  # Intermediate representation; currently Markdown text.
Reader = Callable[[Path], Document]

DEFAULT_INPUT_FORMAT = "pdf"


def _read_pdf(path: Path) -> Document:
    import pymupdf4llm  # imported lazily: it is slow to load

    return pymupdf4llm.to_markdown(str(path))


READERS: dict[str, Reader] = {"pdf": _read_pdf}
