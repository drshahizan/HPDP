from kafka import KafkaProducer
from youtube_comment_downloader import YoutubeCommentDownloader
from yt_dlp import YoutubeDL
import json
import time

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# List of YouTube video IDs to stream comments from
VIDEO_IDS = [
    "0VM-5VM__5U",
    "NnqTib39sao",
    "AUJ4Kaoe8rE",
    "UnBr1vwjacU",
    "zf1U4mu0Iew",
    "ADlC_2DuyHA",
    "xMpIbRtg2HU",
]

# Initialize the comment downloader
downloader = YoutubeCommentDownloader()
sent_ids = set()  # Set to track already sent comment IDs

# Function to get video metadata (title, publish date, views, likes)
def get_video_info(video_id):
    ydl_opts = {}
    url = f"https://www.youtube.com/watch?v={video_id}"
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title", ""),
            "published_at": info.get("upload_date", ""),
            "view_count": info.get("view_count", 0),
            "like_count": info.get("like_count", 0),
        }

# Function to fetch and send comments to Kafka (max 1000 per video)
def stream_comments(video_id, video_info, max_comments=1000):
    print(f"📺 Streaming comments from: {video_id}")
    comments = downloader.get_comments_from_url(f"https://www.youtube.com/watch?v={video_id}")
    count = 0
    for comment in comments:
        if comment["cid"] not in sent_ids:
            sent_ids.add(comment["cid"])
            data = {
                "video_id": video_id,
                "title": video_info["title"],
                "published_at": video_info["published_at"],
                "view_count": video_info["view_count"],
                "likes": video_info["like_count"],
                "comment_text": comment["text"]
            }
            print(f"📤 Sending to Kafka: {data}")
            producer.send("youtube-comments", value=data)
            count += 1
            if count >= max_comments:
                print(f"✅ Sent {count} comments for {video_id}")
                break
            time.sleep(1)  # Throttle the sending
    print(f"🔚 Done with video: {video_id}\n")

# Main loop to fetch comments from all videos
while True:
    for video_id in VIDEO_IDS:
        try:
            print(f"🔁 Fetching new comments from video: {video_id}")
            video_info = get_video_info(video_id)
            stream_comments(video_id, video_info, max_comments=1000)
            time.sleep(10)  # Wait between videos
        except Exception as e:
            print(f"❌ Error processing video {video_id}: {e}")
            time.sleep(5)  # Wait before retrying next video
