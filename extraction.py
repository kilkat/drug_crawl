import json
import re
from collections import Counter

# JSON 파일에서 데이터 읽기 (utf-8 인코딩으로 읽음)
with open('search_results.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# #이 있는지 검사하고 추출하는 함수 정의
def extract_hashtags(text):
    pattern = r'#(\w+)'
    return re.findall(pattern, text)

# 추출된 해시태그를 저장할 리스트 초기화
hashtags_list = []

# title과 body에서 해시태그 추출 및 저장
for entry in data:
    title_hashtags = extract_hashtags(entry['title'])
    body_hashtags = extract_hashtags(entry['body'])
    hashtags_list.extend(title_hashtags)
    hashtags_list.extend(body_hashtags)

# 해시태그 중복 제거 및 출현 빈도 계산
hashtags_counter = Counter(hashtags_list)

# 출현 빈도에 따라 내림차순 정렬
hashtags_sorted = hashtags_counter.most_common()

# JSON 형태로 저장
with open('hashtags_sorted.json', 'w', encoding='utf-8') as file:
    json.dump(dict(hashtags_sorted), file, ensure_ascii=False, indent=4)

print("추출된 해시태그 (내림차순):")
for hashtag, count in hashtags_sorted:
    print(f"{hashtag}: {count}번")
