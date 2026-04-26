import streamlit as st
import pandas as pd
import plotly.express as px
import os
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import defaultdict
import re

# ------------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------------
st.set_page_config(page_title="E‑Wallet Review Dashboard", layout="wide")

# ------------------------------------------------------------------
# Load review data from multiple CSVs
# ------------------------------------------------------------------
csv_paths = ['cleaned_reviews.csv', 'e_wallet_reviews.csv']
all_dfs = []
found_files = []

for csv_path in csv_paths:
    if os.path.exists(csv_path):
        try:
            # Read CSV and parse 'date' column
            df_temp = pd.read_csv(csv_path, parse_dates=['date'])
            all_dfs.append(df_temp)
            found_files.append(csv_path)
        except Exception as e:
            st.warning(f"⚠️ Could not load {csv_path}. Error: {e}")
    else:
        st.info(f"ℹ️ File not found: {csv_path}. Skipping.")

if not all_dfs:
    st.error("❌ No review data files found or loaded. Please ensure 'cleaned_reviews.csv' or 'e_wallet_reviews.csv' exist.")
    st.stop()

# Concatenate all loaded dataframes
df = pd.concat(all_dfs, ignore_index=True)

# Ensure 'sentiment' column exists, if not, create a placeholder or handle as needed
if 'sentiment' not in df.columns:
    st.warning("⚠️ 'sentiment' column not found in loaded data. Some visualizations may not work.")
    df['sentiment'] = 'neutral' # Placeholder for demonstration if truly missing

# ------------------------------------------------------------------
# Sidebar filters
# ------------------------------------------------------------------
st.sidebar.header("🔍 Filter Reviews")

# Date range filter (TOP)
min_date_df = df['date'].min().date() if not df['date'].empty else pd.to_datetime('2020-01-01').date()
max_date_df = df['date'].max().date() if not df['date'].empty else pd.to_datetime('2025-12-31').date()

if min_date_df > max_date_df:
    min_date_df = max_date_df

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date_df, max_date_df)
)

if len(date_range) == 2:
    start_date = date_range[0]
    end_date = date_range[1]
else:
    start_date = date_range[0]
    end_date = date_range[0]

# App filter (MIDDLE)
apps = df['app'].unique()
selected_apps = st.sidebar.multiselect("Select App(s)", apps, default=list(apps))

# Sentiment filter (BOTTOM)
sentiments = df['sentiment'].unique()
selected_sentiments = st.sidebar.multiselect(
    "Select Sentiment(s)",
    sentiments,
    default=list(sentiments)
)

# Apply all filters
mask = (
    df['app'].isin(selected_apps) &
    (df['date'].dt.date >= start_date) &
    (df['date'].dt.date <= end_date) &
    (df['sentiment'].isin(selected_sentiments))
)
filtered_df = df[mask]

# ------------------------------------------------------------------
# Main title & headline metrics
# ------------------------------------------------------------------
st.title("📊 Real‑Time E‑Wallet Sentiment Dashboard")

# Calculate counts
positive_count = filtered_df[filtered_df['sentiment'] == 'positive'].shape[0]
neutral_count = filtered_df[filtered_df['sentiment'] == 'neutral'].shape[0]
negative_count = filtered_df[filtered_df['sentiment'] == 'negative'].shape[0]
total_count = positive_count + neutral_count + negative_count # Calculate total

# Display metrics using st.metric
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Positive 😊", value=positive_count, delta_color="normal")

with col2:
    st.metric(label="Neutral 😐", value=neutral_count, delta_color="off") # 'off' for neutral to not show an arrow

with col3:
    st.metric(label="Negative 😠", value=negative_count, delta_color="inverse") # 'inverse' for negative to show red down arrow

with col4:
    st.metric(label="Total 📝", value=total_count)


# ------------------------------------------------------------------
# First Row: Pie and Line Charts
# ------------------------------------------------------------------
row1_col1, row1_col2 = st.columns([1, 2])

with row1_col1:
    sentiment_color_map = {
        'positive': '#2ecc71',
        'neutral':  '#f1c40f',
        'negative': '#e74c3c'
    }
    fig_pie = px.pie(
        filtered_df,
        names='sentiment',
        title='Sentiment Distribution',
        color='sentiment',
        color_discrete_map=sentiment_color_map,
        height=400
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with row1_col2:
    if not filtered_df.empty:
        filtered_df['day'] = filtered_df['date'].dt.date
        trend_df = (
            filtered_df
            .groupby(['day', 'sentiment'])
            .size()
            .reset_index(name='count')
        )
        fig_line = px.line(
            trend_df,
            x='day',
            y='count',
            color='sentiment',
            title='Sentiment Trend Over Time',
            color_discrete_map=sentiment_color_map,
            height=400
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("No data to display sentiment trend over time.")

# ------------------------------------------------------------------
# Second Row: Word Cloud and Recent Data
# ------------------------------------------------------------------
row2_col1, row2_col2 = st.columns([2, 3]) # Adjusted width to 2/5 and 3/5

with row2_col1:
    st.subheader("☁️ Word Cloud Analysis")
    sentiment_colors = {
        'positive': 'green',
        'neutral': 'goldenrod',
        'negative': 'red'
    }

    # Custom color function for word cloud
    def generate_sentiment_colored_wordcloud(df_sentiment):
        if df_sentiment.empty:
            return None

        word_frequencies = defaultdict(int)
        word_sentiment_association = {} # To store which sentiment a word is most associated with

        # Prepare stopwords to exclude common words
        stopwords = set(STOPWORDS)
        custom_stopwords = {'app', 'wallet', 'e-wallet', 'service', 'use', 'using', 'get', 'can', 'one', 'money', 'time', 'like', 'good', 'great', 'bad'} # Add more as needed
        stopwords.update(custom_stopwords)

        for _, row in df_sentiment.iterrows():
            sentiment = row['sentiment']
            # Convert to string and clean the text (remove non-alphabetic, make lowercase)
            text = str(row['review']).lower()
            words = re.findall(r'\b[a-z]{3,}\b', text) # Only words with 3 or more letters

            for word in words:
                if word not in stopwords:
                    word_frequencies[word] += 1
                    # Associate the word with the sentiment of the current review
                    # This is a simple assignment; for more advanced, you'd track counts per sentiment
                    word_sentiment_association[word] = sentiment

        # Filter out words that don't belong to the selected sentiments, if applicable
        final_word_freq = {}
        for word, freq in word_frequencies.items():
            if word_sentiment_association.get(word) in selected_sentiments:
                final_word_freq[word] = freq

        if not final_word_freq:
            return None

        # Custom color function for the WordCloud
        def color_func_for_sentiment(word, font_size, position, orientation, random_state=None, **kwargs):
            sentiment = word_sentiment_association.get(word, 'neutral') # Default to neutral if not found
            return sentiment_colors.get(sentiment, 'grey')

        wc = WordCloud(
            width=800,
            height=400,
            background_color='white',
            color_func=color_func_for_sentiment,
            max_words=100,
            stopwords=stopwords, # Use updated stopwords
            collocations=False # Prevents duplicate words from being too large if they appear together often
        ).generate_from_frequencies(final_word_freq)

        return wc

    if not filtered_df.empty:
        wc = generate_sentiment_colored_wordcloud(filtered_df)
        if wc:
            fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
            ax_wc.imshow(wc, interpolation='bilinear')
            ax_wc.axis("off")
            st.pyplot(fig_wc)
        else:
            st.info("No relevant words found for the selected filters to generate a word cloud. Try adjusting your filters or adding more review data. 😔")
    else:
        st.info("No reviews available for selected filters to generate a word cloud. Please adjust your filters. 😔")


with row2_col2:
    st.subheader("💬 Latest Reviews")
    if not filtered_df.empty:
        st.dataframe(
            filtered_df
            .sort_values(by='date', ascending=False)[['date', 'app', 'review', 'sentiment']]
            .head(20),
            height=500
        )
    else:
        st.info("No recent reviews available for selected filters.")