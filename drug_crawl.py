import requests
import json
import os
import time  # Import the time module

def search_google(api_key, cse_id, query, start_index=1, num_results=10):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
        'start': start_index,
        'num': num_results
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None
    return response.json()

def save_results_to_txt(results, file_path):
    if results is None or 'items' not in results:
        return
    with open(file_path, 'a', encoding='utf-8') as file:
        for result in results['items']:
            json.dump(result, file, ensure_ascii=False)
            file.write('\n')

# Get API key from environment variable
with open('google_api_key.txt', 'r') as file:
    api_key = file.read().strip()
    print(f"API Key: {api_key}")  # Print the API key

# Get CSE IDs from 'cx_keys' file
with open('cx_keys.txt', 'r', encoding='utf-8') as file:
    cse_ids = [line.strip() for line in file]

# Get queries from 'querys' file
with open('queries.txt', 'r', encoding='utf-8') as file:
    queries = [line.strip() for line in file]

# Fetch the first 100 search results (10 results per request, 10 requests) for each CSE ID and each query
num_results_per_request = 10
total_results = 100
for cse_id in cse_ids:
    for query in queries:
        for start_index in range(1, total_results + 1, num_results_per_request):
            results = search_google(api_key, cse_id, query, start_index, num_results_per_request)
            # Save search results to a TXT file
            file_path = "search_results.txt"
            save_results_to_txt(results, file_path)
    time.sleep(1)  # Sleep for 1 second after each CSE key
