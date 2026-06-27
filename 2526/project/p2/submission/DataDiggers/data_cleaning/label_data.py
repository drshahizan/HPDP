import pandas as pd

df = pd.read_csv('data/raw_data/raw_reviews.csv')

def label_sentiment(rating):
    if rating <= 2: return 'negative'
    if rating == 3: return 'neutral'
    return 'positive'

df['sentiment'] = df['rating'].apply(label_sentiment)

# Drop rows with empty text
df = df[df['text'].notna() & (df['text'].str.strip() != '')]

print(df['sentiment'].value_counts())
df.to_csv('data/raw_data/labeled_reviews.csv', index=False)