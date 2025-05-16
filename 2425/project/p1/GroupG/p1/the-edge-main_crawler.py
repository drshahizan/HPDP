import requests
import csv
import time
from datetime import UTC, datetime

def convert_timestamp(ms):
    if ms is None:
        return ""
    return datetime.fromtimestamp(ms / 1000, tz=UTC).strftime('%Y-%m-%d %H:%M:%S')

def fetch_articles(offset):
    url = f"https://theedgemalaysia.com/api/loadMoreCategories?offset={offset}&categories=malaysia"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Request failed: {response.status_code}")
        return []

all_articles = []

for i in range(1, 1000):  
    offset = i * 10  
    print(f"Fetching articles {offset}...")
    articles = fetch_articles(offset)
    
    if not articles:
        print("No more articles found.")
        break

    for item in articles:
        article = {
            "category": item.get("category", ""),
            "sub-category": item.get("flash", ""),  
            "title": item.get("title", ""),
            "author": item.get("author", ""),
            "source": item.get("source", ""),
            "summary": item.get("summary", ""),
            "created date": convert_timestamp(item.get("created", 0)),
            "updated date": convert_timestamp(item.get("updated", 0))
        }
        all_articles.append(article)

    time.sleep(0.3)  # avoid overloading the server

    # ✅ [NEW] Save every 10,000 articles
    if len(all_articles) >= 10000:
        batch_start = offset - len(all_articles) + 10  # starting offset for this chunk
        batch_end = offset + 9                         # ending offset for this chunk
        filename = f"theedge_{batch_start}_{batch_end}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["category", "sub-category", "title", "author", "source", "summary", "created date", "updated date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_articles)
        print(f"💾 Saved chunk: {filename}")
        all_articles = []  # ✅ reset buffer


if all_articles:
    with open("theedge_final_batch.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["category", "sub-category", "title", "author", "source", "summary", "created date", "updated date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_articles)
    print(f"✅ Done! Saved final {len(all_articles)} articles to 'theedge_final_batch.csv'")
