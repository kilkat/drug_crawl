import requests

def google_search_api(api_key, search_query, num_results=10):
    base_url = "https://www.googleapis.com/customsearch/v1"
    cx = "a742279546bd4470a"  # Google Custom Search Engine의 고유 식별자를 입력하세요.
    # cx는 "Sites to Search" 섹션에서 만들 수 있습니다.

    params = {
        "key": api_key,
        "cx": cx,
        "q": search_query,
        "num": num_results,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return None

    data = response.json()
    if "items" in data:
        results = data["items"]
        return results
    else:
        return None

# 검색어 입력 받기
search_query = input("구글에서 검색할 내용을 입력하세요: ")

# Google API 키 입력 받기
api_key = input("Google Custom Search JSON API 키를 입력하세요: ")

# 검색 결과 가져오기
search_results = google_search_api(api_key, search_query)

if search_results:
    with open("search_results.txt", "w", encoding="utf-8") as file:
        for idx, result in enumerate(search_results, start=1):
            file.write(f"Result {idx}:\n")
            file.write(f"Title: {result['title']}\n")
            file.write(f"URL: {result['link']}\n")
            if "snippet" in result:
                file.write(f"Snippet: {result['snippet']}\n")
            file.write("\n")
    print("검색 결과를 search_results.txt 파일로 저장했습니다.")
else:
    print("검색 결과를 가져올 수 없습니다.")
