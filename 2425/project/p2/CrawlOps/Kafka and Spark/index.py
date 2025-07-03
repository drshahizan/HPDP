import praw
from kafka import KafkaProducer
import json
import time
import re
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the tokenizer and model
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
model = load_model('sentiment_lstm_model.h5')

# Load label mapping
with open('label_mapping.json', 'r') as f:
    label_mapping = json.load(f)

# Set up Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Set up Reddit API
reddit = praw.Reddit(
    client_id='BxF0i3pvzhAKp8zNsCtieg',
    client_secret='ps2E7FBMfm0Y023PjEyj8QVZWiWvsw',
    user_agent='reddit_streamer/0.1 by SentimentStream'
)

# Choose a subreddit (e.g., r/malaysia)
subreddit = reddit.subreddit("malaysia")

print("📡 Streaming Reddit comments from r/malaysia...")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    return tokens

def predict_sentiment(text):
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    # Convert to sequence
    sequences = tokenizer.texts_to_sequences([' '.join(processed_text)])
    
    # Pad the sequence (using max_length=150 to match training)
    padded_sequences = pad_sequences(sequences, maxlen=150)
    
    # Get prediction probabilities for all classes
    prediction_probs = model.predict(padded_sequences)[0]  # Shape: (3,)
    
    # Get the predicted class index and its probability
    predicted_index = np.argmax(prediction_probs)
    
    # Convert to sentiment label using mapping
    sentiment = label_mapping[str(predicted_index)]  # Convert index to string for JSON key
    sentiment_score = float(prediction_probs[predicted_index])
    
    return sentiment, sentiment_score

# Stream comments in real-time
for comment in subreddit.stream.comments(skip_existing=True):
    # Get sentiment prediction
    sentiment, sentiment_score = predict_sentiment(comment.body)
    
    data = {
        "id": comment.id,
        "body": comment.body,
        "author": str(comment.author),
        "created_utc": comment.created_utc,
        "subreddit": comment.subreddit.display_name,
        "sentiment": sentiment,
        "sentiment_score": sentiment_score
    }

    print(f"🚀 Sending comment: {data['body'][:100]}... | Sentiment: {sentiment} ({sentiment_score:.2f})")
    producer.send("reddit-sentiment", value=data)
    time.sleep(1)  # prevent Reddit API overload