# Use google-play-scraper to pull reviews from three popular Malaysian apps.
# Aim for at least 5,000 reviews per app to have enough data for training.

import os
import pandas as pd
from google_play_scraper import reviews, Sort

# Malaysian apps to scrape
APPS = {
    'touch_n_go': 'my.com.tngdigital.ewallet',
    'grab':        'com.grabtaxi.passenger',
    'foodpanda':   'com.global.foodpanda.android',
}

all_reviews = []

for name, app_id in APPS.items():
    print(f"Scraping {name}...")

    result, _ = reviews(
        app_id,
        lang='en',
        country='my',       # Malaysia
        sort=Sort.NEWEST,
        count=5000,
    )

    print(f"-> Found {len(result)} reviews for {name}")

    for r in result:
        all_reviews.append({
            'app':    name,
            'text':   r['content'],
            'rating': r['score'],    # 1–5 stars
            'date':   r['at'],
        })

# --- VS CODE DIRECTORY ---
# Define your target directory relative to your VS Code workspace
output_dir = 'data/raw_data'

# Create the folders if they do not exist
os.makedirs(output_dir, exist_ok=True)

# Combine directory and filename safely
output_file = os.path.join(output_dir, 'raw_reviews.csv')
# -----------------------------

# Convert to DataFrame and save
df = pd.DataFrame(all_reviews)
df.to_csv(output_file, index=False)

print("---")
print(f"Success! Scraped {len(df)} reviews total.")
print(f"File saved to: {os.path.abspath(output_file)}")