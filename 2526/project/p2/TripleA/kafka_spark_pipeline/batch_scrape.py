from googleapiclient.discovery import build
import csv
import os

API_KEY = 'AIzaSyDVIHOU49YBjhcPhU-P1Ec60WyJToGNGl4'

# Different videos for batch
BATCH_VIDEO_IDS = ["Ae0YvD04duU", "iwzWrLy9o9k", "THyI2jiwMq4"]

youtube = build("youtube", "v3", developerKey=API_KEY)

def fetch_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=50,
            pageToken=next_page_token,
            order="time"
        ).execute()

        comments.extend(response["items"])
        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return comments

csv_file = "comments.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["video_id", "comment_id", "comment", "author", "timestamp"])
    writer.writeheader()

    for vid in BATCH_VIDEO_IDS:
        print(f"Fetching comments for video: {vid}")
        items = fetch_comments(vid)
        print(f"Fetched {len(items)} comments")

        for item in items:
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            writer.writerow({
                "video_id": vid,
                "comment_id": item["snippet"]["topLevelComment"]["id"],
                "comment": snippet["textDisplay"],
                "author": snippet["authorDisplayName"],
                "timestamp": snippet["publishedAt"]
            })

print(f"Saved to {csv_file}")