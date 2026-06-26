from googleapiclient.discovery import build
from kafka import KafkaProducer
import json
import time
from datetime import datetime, timezone, timedelta

API_KEY = 'AIzaSyDVIHOU49YBjhcPhU-P1Ec60WyJToGNGl4'
VIDEO_IDS = ["_XsO0ub5-8k", "3qCCJotR5c4", "1p1zhiZecUg"]

youtube = build("youtube", "v3", developerKey=API_KEY)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=100,
            pageToken=next_page_token,
            order="time"  # Most recent first — stops early pagination once comments are old
        ).execute()

        comments.extend(response["items"])
        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return comments

# Track the last poll time per video
last_poll_time = {vid: datetime.now(timezone.utc) - timedelta(days=30) for vid in VIDEO_IDS}

while True:
    for vid in VIDEO_IDS:
        try:
            print(f"\nFetching comments for video: {vid}")
            items = fetch_comments(vid)
            print(f"Fetched {len(items)} total comments")

            new_count = 0
            latest_timestamp = last_poll_time[vid]

            for item in items:
                snippet = item["snippet"]["topLevelComment"]["snippet"]
                comment_id = item["snippet"]["topLevelComment"]["id"]
                published_at = datetime.fromisoformat(
                    snippet["publishedAt"].replace("Z", "+00:00")
                )

                # Only send comments newer than last poll
                if published_at <= last_poll_time[vid]:
                    continue

                # Track the most recent timestamp seen this cycle
                if published_at > latest_timestamp:
                    latest_timestamp = published_at

                new_count += 1
                msg = {
                    "video_id": vid,
                    "comment_id": comment_id,
                    "comment": snippet["textDisplay"],
                    "author": snippet["authorDisplayName"],
                    "timestamp": snippet["publishedAt"]
                }

                future = producer.send("youtube_comments", msg)
                future.get(timeout=10)
                print("Sent:", msg)

            # Advance the watermark for this video
            last_poll_time[vid] = latest_timestamp
            print(f"New comments sent for {vid}: {new_count}")

        except Exception as e:
            print(f"Error processing video {vid}: {e}")

    producer.flush()
    print("\nSleeping 60s before next poll...")
    time.sleep(60)