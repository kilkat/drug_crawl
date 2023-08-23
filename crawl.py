import json
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = [result for result in ddgs.text('검색 쿼리', region='wt-wt', safesearch='Off', timelimit='y')]

with open('search_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

for result in results:
    url = result['href']

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')