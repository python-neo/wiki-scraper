# Wiki Scraper

Wiki Scraper is a small Python utility that downloads Wikipedia article text and
saves each page as a UTF-8 text file in a local `pages/` directory. It uses the
`wikipedia-api` package to fetch pages asynchronously and preserves the article
title at the top of each saved file.

## Features

- Asynchronous page fetches for faster downloads
- Safe filename sanitization for Windows and POSIX file systems
- Automatic duplicate-title handling to avoid clobbering files
- Simple CLI entry point via the `wiki-scraper` command

## Installation

```bash
python -m pip install -e .
```

## Usage

After installation, run the scraper:

```bash
wiki-scraper
```

This will fetch the linked pages from the Python article and save them under
`pages/` in the project root.

## Project Structure

```text
wiki-scraper/
├── pages/                  # Downloaded wiki pages
├── src/
│   └── wiki_scraper/
│       ├── __init__.py
│       └── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Notes

- The scraper writes files named after the article title with unsafe filename
characters replaced by underscores.
- If two articles would collide on the same sanitized title, a numeric suffix is
appended to keep both files.
- The script intentionally visits the links of the Python article and does not
recursively crawl the whole Wikipedia graph.
