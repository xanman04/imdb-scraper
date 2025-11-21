# IMDb Scraper

A command-line tool for scraping IMDb search results using Playwright and BeautifulSoup. The scraper fetches search results from IMDb’s public pages, extracts structured metadata for each title, and exports the data as CSV or JSON. The project is packaged with `pyproject.toml` so it can be installed as a local command-line tool providing the `imdb` command.

## Features

- Scrapes IMDb search results without requiring login or API access
- Uses Playwright with Firefox
- Parses HTML using BeautifulSoup
- Extracts structured metadata into a dataclass
- Exports data to CSV or JSON
- Provides an argparse-driven command-line interface
- Installs a global `imdb` command via a console script
- Uses standard Python packaging through `pyproject.toml`

## Installation

Clone the repository:

```bash
git clone https://github.com/xanman04/imdb-scraper.git
cd imdb-scraper
```

Install the package:

```bash
python -m pip install -e .
```

Install the required Playwright browser:

```bash
playwright install firefox
```

After installation, the `imdb` command becomes available system-wide (within your Python environment).

## Usage

Basic search (CSV output):

```bash
imdb "the matrix"
```

JSON output:

```bash
imdb "the matrix" -j
```

Custom output filename:

```bash
imdb "the matrix" -o matrix_results
```

Combined example:

```bash
imdb "the avengers" -j -o avengers_search
```

## Project Structure

```
imdb-scraper/
│
├── data/
│   ├── __init__.py
│   └── format.py
│
├── scraper/
│   ├── __init__.py
│   └── imdb.py
│
├── main.py
├── pyproject.toml
├── README.md
└── .gitignore
```

## How It Works

1. The user provides a search term at the command line.
2. `fetch_results()` loads the IMDb search page using Playwright (Firefox).
3. The resulting HTML list is extracted and passed to BeautifulSoup.
4. Metadata such as title, year, runtime, metascore, rating, vote count, and media type is parsed.
5. Parsed results are formatted and exported to CSV or JSON.
6. Output files are written using UTF-8 encoding.

## Requirements

Dependencies (installed automatically via `pip install -e .`):

- playwright
- beautifulsoup4

Playwright browser installation (required once):

```bash
playwright install firefox
```

Python version required: 3.11 or later.

## License

MIT

## Future Improvements

- Add `--limit` to restrict number of results
- Add `--headless` / `--no-headless` flags
- Add verbose logging
- Add timestamp-based output filenames
