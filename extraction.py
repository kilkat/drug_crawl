import json
import re
from collections import Counter

with open('search_results.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def extract_hashtags(text):
    pattern = r'#(\w+)'
    return re.findall(pattern, text)

hashtags_list = []

for entry in data:
    title_hashtags = extract_hashtags(entry['title'])
    body_hashtags = extract_hashtags(entry['body'])
    hashtags_list.extend(title_hashtags)
    hashtags_list.extend(body_hashtags)

hashtags_counter = Counter(hashtags_list)

hashtags_sorted = hashtags_counter.most_common()

with open('hashtags_sorted.json', 'w', encoding='utf-8') as file:
    json.dump(dict(hashtags_sorted), file, ensure_ascii=False, indent=4)

print("추출된 해시태그 (내림차순):")
for hashtag, count in hashtags_sorted:
    print(f"{hashtag}: {count}번")
