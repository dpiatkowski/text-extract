# text-extract

Extract text and tables from documents and save them in another format.
Currently: PDF (via [pymupdf4llm](https://github.com/pymupdf/pymupdf4llm)) to Markdown.

```bash
uvx --from . text-extract report.pdf            # writes report.md next to the PDF
uvx --from . text-extract a.pdf b.pdf -o out/   # write into out/
uvx --from git+<repo-url> text-extract report.pdf
```

Options: `-i/--input-format` (default `pdf`), `-f/--output-format` (default `markdown`), `-o/--output-dir`.

New formats: register a function in `READERS` (`readers/__init__.py`) or `WRITERS` (`writers/__init__.py`).
