# Produce the final dataset with only the columns Member B needs: processed_text and sentiment.

import pandas as pd

df = pd.read_csv('data/raw_data/lemmatized.csv')

# Keep only what B needs
final = df[['app', 'processed_text', 'sentiment']].copy()
final = final.dropna().reset_index(drop=True)

print("=== Final dataset ===")
print(final.shape)
print(final['sentiment'].value_counts())
print(final.head(5))

final.to_csv('data/cleaned_data.csv', index=False)
print("\n✓ Exported to data/cleaned_data.csv")