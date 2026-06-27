import re
import pandas as pd

def clean_text(text):
    text = str(text).lower()                           # lowercase
    text = re.sub(r'http\S+|www\S+', '', text)       # remove URLs
    text = re.sub(r'<.*?>', '', text)               # remove HTML tags
    text = re.sub(r'@\w+', '', text)                  # remove @mentions
    text = re.sub(r'[^\w\s]', '', text)              # remove punctuation
    text = re.sub(r'\d+', '', text)                   # remove numbers
    # remove emojis
    emoji_pattern = re.compile("["\
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U00002702-\U000027B0"
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub('', text)
    text = re.sub(r'\s+', ' ', text).strip()          # extra whitespace
    return text

df = pd.read_csv('data/raw_data/labeled_reviews.csv')
df['clean_text'] = df['text'].apply(clean_text)
df = df[df['clean_text'].str.len() > 5]  # drop near-empty rows
print(df[['text', 'clean_text']].head(3))
df.to_csv('data/raw_data/cleaned_step1.csv', index=False)