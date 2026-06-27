import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Keep negations — they matter for sentiment!
keep_words = {'not', 'no', 'never', 'but'}
stop_words -= keep_words

def tokenize_and_filter(text):
    tokens = word_tokenize(str(text))
    return [t for t in tokens if t not in stop_words and len(t) > 2]

df = pd.read_csv('data/raw_data/cleaned_step1.csv')
df['tokens'] = df['clean_text'].apply(tokenize_and_filter)
df.to_csv('data/raw_data/tokenized.csv', index=False)

print("Tokenization complete and saved to tokenized.csv")