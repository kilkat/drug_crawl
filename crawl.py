import json
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

# Create a DDGS instance
with DDGS() as ddgs:
    # Call the text function and save the results in a variable
    results = [result for result in ddgs.text('검색 쿼리', region='wt-wt', safesearch='Off', timelimit='y')]

# Save the results to a JSON file with ensure_ascii set to False and indent set to 4
with open('search_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

# Iterate over the search results
for result in results:
    # Get the URL of the result
    url = result['href']

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object from the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Do something with the soup object (e.g., extract some information)
    # ...