"""
scrape_reviews.py

Week 1 deliverable: collects Google Play Store reviews for a single
Malaysian-relevant app (Touch 'n Go eWallet) and saves them as a raw CSV.

Usage:
    python scrape_reviews.py

Requirements:
    pip install google-play-scraper pandas

Output:
    data/raw_data/my_com_tngdigital_ewallet.csv  -- all scraped reviews
    data/raw_data/combined_raw.csv                -- same data, standard name
                                                      used by downstream notebooks

Each row contains:
    app_id, app_name, review_id, review_text, score (1-5 stars),
    thumbs_up_count, review_date, reply_content, reply_date
"""

import time
import pandas as pd
from google_play_scraper import Sort, reviews

# ---------------------------------------------------------------------------
# CONFIG: single Malaysian-relevant target app.
# Package ID verified against the Google Play Store listing.
# If this fails with "App not found", double check the ID on the
# Play Store URL: play.google.com/store/apps/details?id=<PACKAGE_ID>
# ---------------------------------------------------------------------------
TARGET_APPS = [
    {"app_id": "my.com.tngdigital.ewallet", "app_name": "Touch 'n Go eWallet"},
]

REVIEWS_PER_APP = 10000     # target review count for the single app
COUNTRY = "my"              # Malaysia
LANG = "en"                 # English reviews (Malay reviews also appear; see note below)
SORT_ORDER = Sort.MOST_RELEVANT  # Google's relevance ranking -- surfaces longer,
                                  # more substantive reviews than NEWEST does
BATCH_SIZE = 200            # reviews fetched per request (library handles pagination)
SLEEP_BETWEEN_BATCHES = 1.0  # seconds, be polite to the server


def scrape_app_reviews(app_id: str, app_name: str, target_count: int) -> pd.DataFrame:
    """Scrape up to target_count reviews for a single app, paginating as needed.

    Tries SORT_ORDER first (e.g. MOST_RELEVANT). If that sort mode runs out of
    reviews before reaching target_count, automatically tops up the shortfall
    using Sort.NEWEST so we reliably end up with the full target_count.
    """
    all_reviews = []
    seen_ids = set()
    review_sort_source = {}  # review_id -> which sort mode found it
    continuation_token = None

    print(f"\n[scrape] Starting: {app_name} ({app_id}) | sort={SORT_ORDER}")

    while len(all_reviews) < target_count:
        try:
            result, continuation_token = reviews(
                app_id,
                lang=LANG,
                country=COUNTRY,
                sort=SORT_ORDER,
                count=BATCH_SIZE,
                continuation_token=continuation_token,
            )
        except Exception as e:
            print(f"[scrape] ERROR fetching {app_name}: {e}")
            break

        if not result:
            print(f"[scrape] '{SORT_ORDER}' sort exhausted at {len(all_reviews)} reviews.")
            break

        for r in result:
            rid = r.get("reviewId")
            if rid not in seen_ids:
                seen_ids.add(rid)
                all_reviews.append(r)
                review_sort_source[rid] = str(SORT_ORDER)

        print(f"[scrape]   {app_name}: {len(all_reviews)}/{target_count} collected")

        if continuation_token is None:
            print(f"[scrape] No continuation token -- '{SORT_ORDER}' sort exhausted.")
            break

        time.sleep(SLEEP_BETWEEN_BATCHES)

    # Fallback: if MOST_RELEVANT (or whatever SORT_ORDER is) ran dry before
    # reaching target_count, top up the shortfall using NEWEST sort so the
    # final dataset still reliably hits target_count rows.
    if len(all_reviews) < target_count and SORT_ORDER != Sort.NEWEST:
        shortfall = target_count - len(all_reviews)
        print(f"[scrape] Shortfall of {shortfall} reviews -- topping up with Sort.NEWEST")
        continuation_token = None
        while len(all_reviews) < target_count:
            try:
                result, continuation_token = reviews(
                    app_id,
                    lang=LANG,
                    country=COUNTRY,
                    sort=Sort.NEWEST,
                    count=BATCH_SIZE,
                    continuation_token=continuation_token,
                )
            except Exception as e:
                print(f"[scrape] ERROR during top-up fetch for {app_name}: {e}")
                break

            if not result:
                print(f"[scrape] NEWEST sort also exhausted at {len(all_reviews)} total reviews.")
                break

            for r in result:
                rid = r.get("reviewId")
                if rid not in seen_ids:
                    seen_ids.add(rid)
                    all_reviews.append(r)
                    review_sort_source[rid] = "Sort.NEWEST (top-up)"

            print(f"[scrape]   {app_name} (top-up): {len(all_reviews)}/{target_count} collected")

            if continuation_token is None:
                break

            time.sleep(SLEEP_BETWEEN_BATCHES)

    # Trim to target count and convert to DataFrame
    all_reviews = all_reviews[:target_count]
    rows = []
    for r in all_reviews:
        rid = r.get("reviewId")
        rows.append({
            "app_id": app_id,
            "app_name": app_name,
            "review_id": rid,
            "review_text": r.get("content"),
            "score": r.get("score"),
            "thumbs_up_count": r.get("thumbsUpCount"),
            "review_date": r.get("at"),
            "reply_content": r.get("replyContent"),
            "reply_date": r.get("repliedAt"),
            "source_sort": review_sort_source.get(rid, str(SORT_ORDER)),
        })

    df = pd.DataFrame(rows)
    print(f"[scrape] Finished {app_name}: {len(df)} reviews collected.")
    return df


def main():
    import os
    output_dir = os.path.join(os.path.dirname(__file__), "data", "raw_data")
    os.makedirs(output_dir, exist_ok=True)

    combined_frames = []

    for app in TARGET_APPS:
        df = scrape_app_reviews(app["app_id"], app["app_name"], REVIEWS_PER_APP)
        if df.empty:
            print(f"[scrape] WARNING: 0 reviews collected for {app['app_name']}. "
                  f"Check the package ID or your internet connection.")
            continue

        # Save per-app file
        safe_name = app["app_id"].replace(".", "_")
        out_path = os.path.join(output_dir, f"{safe_name}.csv")
        df.to_csv(out_path, index=False)
        print(f"[scrape] Saved -> {out_path}")

        combined_frames.append(df)

    if combined_frames:
        combined = pd.concat(combined_frames, ignore_index=True)
        combined_path = os.path.join(output_dir, "combined_raw.csv")
        combined.to_csv(combined_path, index=False)
        print(f"\n[scrape] Combined dataset saved -> {combined_path}")
        print(f"[scrape] Total reviews collected: {len(combined)}")
        print("\n[scrape] Score distribution:")
        print(combined["score"].value_counts().sort_index())
    else:
        print("\n[scrape] No data collected from any app. Check package IDs / network.")


if __name__ == "__main__":
    main()
