from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import urllib.parse
from dataclasses import dataclass

@dataclass
class SearchResult:
    title: str
    year: str
    runtime: str
    metascore: str
    stars: str
    num_ratings: str
    media_type: str

def fetch_results(search: str):
    results = []

    with sync_playwright() as pw:
        browser = pw.firefox.launch()
        page = browser.new_page()
        url = f'https://www.imdb.com/find/?q={urllib.parse.quote(search)}&s=tt&ref_=fn_ttl_pop'
        page.goto(url)

        page.wait_for_selector('ul.ipc-metadata-list')
        list_html = page.locator('ul.ipc-metadata-list').inner_html()
        soup = BeautifulSoup(list_html, "html.parser")
        
        movies_html = soup.select('li.ipc-metadata-list-summary-item')
    
    for li in movies_html:
        metadata = li.select('span.cli-title-metadata-item')
        type_data = li.select_one('span.cli-title-type-data')
        media_type = type_data.get_text(strip=True) if type_data is not None else "Movie"

        title = li.select_one('h3.ipc-title__text').get_text(strip=True)
        year = metadata[0].get_text(strip=True) if len(metadata) >= 1 else None
        runtime = next((item.get_text(strip=True) for item in metadata[1:] if "m" in item.get_text(strip=True)), None)

        score_tag = li.select_one('span.metacritic-score-box')
        metascore = score_tag.get_text(strip=True) if score_tag is not None else None

        star_tag = li.select_one('span.ipc-rating-star--rating')
        stars = star_tag.get_text(strip=True) if star_tag is not None else None
        
        rating_tag = li.select_one('span.ipc-rating-star--voteCount')
        ratings = rating_tag.get_text(strip=True).strip("()") if rating_tag is not None else None

        results.append(SearchResult(title, year, runtime, metascore, stars, ratings, media_type))
    
    browser.close()
    return results


if __name__ == '__main__':
    test = fetch_results("the matrix")
    for i in test:
        print(i)