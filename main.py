from scraper.imdb import fetch_results
from data.format import format_output
import argparse

def main():
    parser = argparse.ArgumentParser(description="Scrape IMDb search results")
    parser.add_argument('query', type=str, 
                        help='IMDb search term. Example: "The Matrix"')
    parser.add_argument('-j', '--json', action='store_true', 
                        help="Returns JSON instead of CSV")
    parser.add_argument('-o', '--output', default="output",
                        help="Output filename without extension")
    args = parser.parse_args()

    results = fetch_results(args.query)
    if not results:
        print(f"ERROR: No results found for query: {args.query}")
        return

    if args.json:
        format_output(results, args.output, "json")
    else:
        format_output(results, args.output)

if __name__ == '__main__':
    main()