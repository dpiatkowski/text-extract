# text-extract

Extract text and tables from documents and save them in another format.
Currently: PDF (via [pymupdf4llm](https://github.com/pymupdf/pymupdf4llm)) to Markdown.

## Usage

Run straight from the git repository with [uvx](https://docs.astral.sh/uv/guides/tools/), no install needed:

```bash
uvx --from git+https://github.com/dpiatkowski/text-extract text-extract report.pdf            # writes report.md next to the PDF
uvx --from git+https://github.com/dpiatkowski/text-extract text-extract a.pdf b.pdf -o out/   # write into out/
```

Pin a branch, tag or commit with `@`:

```bash
uvx --from git+https://github.com/dpiatkowski/text-extract@main text-extract report.pdf
uvx --from git+https://github.com/dpiatkowski/text-extract@523ee7c text-extract report.pdf
```

Use SSH instead of HTTPS (e.g. for private access):

```bash
uvx --from git+ssh://git@github.com/dpiatkowski/text-extract.git text-extract report.pdf
```

From a local checkout:

```bash
uvx --from . text-extract report.pdf
```

Add `--refresh` to `uvx` to pick up new commits after the first run.

Options: `-i/--input-format` (default `pdf`), `-f/--output-format` (default `markdown`), `-o/--output-dir`.

New formats: register a function in `READERS` (`readers/__init__.py`) or `WRITERS` (`writers/__init__.py`).
