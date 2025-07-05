from googleapiclient.discovery import build
from kafka import KafkaProducer
import pandas as pd
import json
import time
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
SEARCH_QUERY = 'Vlog Traveling in Malaysia'
MAX_VIDEOS = 10
EXCEL_FILE = 'comments.xlsx'
SEEN_IDS_FILE = 'seen_comment_ids.txt'

producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers='localhost:9092'
)

# Load seen comment IDs
seen_comment_ids = set()
if os.path.exists(SEEN_IDS_FILE):
    with open(SEEN_IDS_FILE, 'r') as f:
        for line in f:
            seen_comment_ids.add(line.strip())

# Initialize Excel file if it doesn't exist
if not os.path.exists(EXCEL_FILE):
    pd.DataFrame(columns=['comment_id', 'video_id', 'text']).to_excel(EXCEL_FILE, index=False)

def save_seen_comment_id(comment_id):
    with open(SEEN_IDS_FILE, 'a') as f:
        f.write(comment_id + '\n')
    seen_comment_ids.add(comment_id)

def append_comments_to_excel(comments):
    if not comments:
        return
    new_df = pd.DataFrame(comments)
    existing_df = pd.read_excel(EXCEL_FILE)
    
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    combined_df.drop_duplicates(subset='comment_id', inplace=True)
    combined_df.to_excel(EXCEL_FILE, index=False)
    print(f"✅ Saved {len(new_df)} new comments to {EXCEL_FILE}")

def get_video_ids(query, max_results=5):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    return [item['id']['videoId'] for item in response['items']]

def get_comments(video_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,
        textFormat='plainText'
    )
    response = request.execute()

    new_comments = []
    for item in response.get('items', []):
        comment_id = item['id']
        if comment_id in seen_comment_ids:
            continue
        comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']

        # Send to Kafka
        producer.send('sentiment_comments', {'text': comment_text, 'video_id': video_id})
        save_seen_comment_id(comment_id)

        # Store for Excel
        new_comments.append({
            'comment_id': comment_id,
            'video_id': video_id,
            'text': comment_text
        })

    append_comments_to_excel(new_comments)

def stream_comments_for_query(query):
    video_ids = get_video_ids(query, MAX_VIDEOS)
    print(f"🔍 Found {len(video_ids)} videos for query '{query}'")
    for vid in video_ids:
        print(f"📥 Streaming comments from video: {vid}")
        try:
            get_comments(vid)
        except Exception as e:
            print(f"⚠️ Error fetching comments for {vid}: {e}")

# Run continuously
while True:
    stream_comments_for_query(SEARCH_QUERY)
    time.sleep(60)


# from googleapiclient.discovery import build
# from kafka import KafkaProducer
# import json
# import time
# import os

# API_KEY = 'AIzaSyAdF2o79fLTQ3tBThdiOgUNXKV7h4XE_18'
# SEARCH_QUERY = 'Vlog Traveling in Malaysia'
# MAX_VIDEOS = 10

# producer = KafkaProducer(
#     value_serializer=lambda v: json.dumps(v).encode('utf-8'),
#     bootstrap_servers='localhost:9092'
# )

# # Store already seen comment IDs
# seen_comment_ids = set()
# seen_ids_file = 'seen_comment_ids.txt'

# # Load from disk
# if os.path.exists(seen_ids_file):
#     with open(seen_ids_file, 'r') as f:
#         for line in f:
#             seen_comment_ids.add(line.strip())

# def save_seen_comment_id(comment_id):
#     with open(seen_ids_file, 'a') as f:
#         f.write(comment_id + '\n')
#     seen_comment_ids.add(comment_id)

# def get_video_ids(query, max_results=5):
#     youtube = build('youtube', 'v3', developerKey=API_KEY)
#     request = youtube.search().list(
#         part='snippet',
#         q=query,
#         type='video',
#         maxResults=max_results
#     )
#     response = request.execute()
#     return [item['id']['videoId'] for item in response['items']]

# def get_comments(video_id):
#     youtube = build('youtube', 'v3', developerKey=API_KEY)
#     request = youtube.commentThreads().list(
#         part='snippet',
#         videoId=video_id,
#         maxResults=100,
#         textFormat='plainText'
#     )
#     response = request.execute()

#     for item in response.get('items', []):
#         comment_id = item['id']
#         if comment_id in seen_comment_ids:
#             continue  # Skip already seen comment
#         comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
#         producer.send('sentiment_comments', {'text': comment_text, 'video_id': video_id})
#         save_seen_comment_id(comment_id)

# def stream_comments_for_query(query):
#     video_ids = get_video_ids(query, MAX_VIDEOS)
#     print(f"Found {len(video_ids)} videos for query '{query}'")
#     for vid in video_ids:
#         print(f"Streaming comments from video: {vid}")
#         try:
#             get_comments(vid)
#         except Exception as e:
#             print(f"Error fetching comments for {vid}: {e}")

# # Continuous streaming (optional)
# while True:
#     stream_comments_for_query(SEARCH_QUERY)
#     time.sleep(60)
