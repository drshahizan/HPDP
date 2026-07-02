# Visual Analysis: Malaysian Telecommunication App Review Sentiment

## 1. Dashboard Overview

The Kibana dashboard visualizes sentiment prediction results from Malaysian telecommunication Google Play reviews. The data was processed through the Kafka and Spark streaming pipeline, stored in Elasticsearch, and analyzed in Kibana.

## 2. Sentiment Distribution

The sentiment distribution chart shows that negative sentiment is the largest category, representing 60.64% of the processed reviews. Positive sentiment represents 39.23%, while neutral sentiment is very small at 0.13%. This indicates that the overall customer feedback is more negative than positive.

## 3. Sentiment Breakdown by Provider

The provider breakdown chart compares sentiment across Celcom, Maxis, Digi, and U Mobile. All providers show both positive and negative reviews, but negative sentiment appears strongly across the providers.

## 4. Correct Prediction Records

The metric chart shows 32,743 records marked as correctly predicted. This provides a simple validation indicator for the sentiment prediction output.

## 5. Reviews Over Time

The time-series chart shows review sentiment trends by month. Negative and positive reviews are mostly concentrated between 2021 and 2023, based on the available review dates in the dataset.

## 6. Top Negative Providers

The top negative providers table shows that Celcom has the highest number of negative reviews, followed by Maxis, Digi, and U Mobile. This helps identify which providers received more negative customer feedback.

## 7. Rating Distribution

The rating distribution chart shows that 1-star reviews form the largest group, followed by 5-star reviews. This supports the sentiment result because low ratings are strongly related to negative sentiment, while high ratings are related to positive sentiment.

## 8. Key Findings

- Negative sentiment is the dominant sentiment category in the dataset.
- Celcom has the highest number of negative reviews.
- The rating distribution supports the sentiment analysis result, with many 1-star reviews.
- The keyword “slow” appears in negative review summaries, suggesting performance or network speed issues as a common complaint.
- Kibana successfully converts the Elasticsearch prediction output into useful visual insights.

## 9. Conclusion

The dashboard successfully presents the sentiment analysis results stored in Elasticsearch. It allows users to understand overall sentiment, compare providers, observe sentiment trends over time, and identify common negative feedback patterns.