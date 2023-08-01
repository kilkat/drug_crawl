import requests
import json

def search_google(api_key, cse_id, query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query
    }
    response = requests.get(url, params=params)
    return response.json()

def save_results_to_txt(results, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        for result in results['items']:
            json.dump(result, file, ensure_ascii=False)
            file.write('\n')

# Get user input for API key, CSE ID, and search query
api_key = input("Enter your API key: ")
cse_id = input("Enter your Custom Search ID (CSE ID): ")
query = input("Enter your search query: ")

results = search_google(api_key, cse_id, query)

# Save search results to a TXT file
file_path = "search_results.txt"
save_results_to_txt(results, file_path)
