import pandas as pd
import re
from textblob import TextBlob
from nltk.tokenize import RegexpTokenizer

# Ensure you've installed required packages:
# pip install pandas textblob nltk

# Initialize tokenizer
tokenizer = RegexpTokenizer(r'\b\w{3,}\b')  # Keep words with 3+ letters

# Function to clean text
def clean_text(text):
    if not isinstance(text, str) or text.strip() == '':
        return ""
    
    # Remove URLs
    text = re.sub(r'https?://\S+', '', text)

    # Remove emails
    text = re.sub(r'\S+@\S+', '', text)

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove emojis and special characters
    text = re.sub(r'[^\w\s#@_/-]', '', text)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip().lower()
    
    # Tokenize
    words = tokenizer.tokenize(text)

    return ' '.join(words)

# Function to get sentiment label
def get_sentiment(text):
    if not text:
        return 'neutral'
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'

# Load your CSV
print("Loading dataset...")
df = pd.read_csv("reddit_movies_comments_cleaned_init.csv")

# Clean comment body
print("Cleaning comments...")
df['cleaned_comment'] = df['comment_body'].apply(clean_text)

# Add sentiment labels
print("Labeling sentiments...")
df['sentiment'] = df['cleaned_comment'].apply(get_sentiment)

# Filter out empty comments
df = df[df['cleaned_comment'].str.len() > 5]

# Save final dataset
output_file = "reddit_movies_sentiment_ready.csv"
df.to_csv(output_file, index=False)
print(f"✅ Cleaned and labeled dataset saved to {output_file}")

#########################
df = pd.read_csv("reddit_movies_sentiment_ready.csv")
print(df['sentiment'].value_counts(normalize=True))

print("Positive Examples:")
print(df[df['sentiment'] == 'positive']['cleaned_comment'].head().to_string())

print("\nNegative Examples:")
print(df[df['sentiment'] == 'negative']['cleaned_comment'].head().to_string())

print("\nNeutral Examples:")
print(df[df['sentiment'] == 'neutral']['cleaned_comment'].head().to_string())