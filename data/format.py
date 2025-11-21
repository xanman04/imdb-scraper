from scraper.imdb import SearchResult, fetch_results
from dataclasses import asdict
import json
import csv

def format_output(result_list: list[SearchResult], filename: str, fmt: str = 'csv'):
    fmt = fmt.lower()

    if not result_list:
        raise ValueError("ERROR: result_list received an empty list")
    
    results = [asdict(result) for result in result_list]

    if fmt == 'json':
        with open(f'{filename}.{fmt}', 'w', encoding="utf-8", newline="") as output:
            json.dump(results, output, ensure_ascii=False, indent=2)
    elif fmt == 'csv':
        cleaned_results = [{i : (j if j is not None else "None") for i,j in result.items()} for result in results]
        keys = cleaned_results[0].keys()
        
        with open(f'{filename}.{fmt}', 'w', encoding="utf-8", newline="") as output:
            writer = csv.DictWriter(output, keys)
            writer.writeheader()
            writer.writerows(cleaned_results)
    else:
        raise ValueError(f"ERROR: Unsupported file type {fmt}")

if __name__ == '__main__':
    format_output(fetch_results("the avengers"), fmt='json')