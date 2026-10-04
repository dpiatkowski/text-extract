"""Output format writers. A writer saves a Document to a file path."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from text_extract.readers import Document

Writer = Callable[[Document, Path], None]

DEFAULT_OUTPUT_FORMAT = "markdown"


def _write_markdown(doc: Document, path: Path) -> None:
    path.write_text(doc, encoding="utf-8")


# format name -> (writer, file extension)
WRITERS: dict[str, tuple[Writer, str]] = {"markdown": (_write_markdown, ".md")}
