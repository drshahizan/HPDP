#Reduce each token to its base form ("running" → "run", "better" → "good"). 
#This reduces vocabulary size and improves model generalization.

import spacy
import pandas as pd
import ast

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

def lemmatize_tokens(token_str):
    tokens = ast.literal_eval(str(token_str))
    text = ' '.join(tokens)
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc])

df = pd.read_csv('data/raw_data/tokenized.csv')
df['processed_text'] = df['tokens'].apply(lemmatize_tokens)
df.to_csv('data/raw_data/lemmatized.csv', index=False)

print("Lemmatization complete! Saved to lemmatized.csv")