<h1 align="center"> 
  Code Cookies - Real-Time Sentiment Pipeline on Google Play Reviews of FoodPanda Apps
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
    <th>Role</th>
  </tr>
  <tr>
    <td width=40%>Najma Shakirah binti Shahrulzaman</td>
    <td>A23CS0140</td>
    <td>Group Leader & Pipeline Engineer</td>
  </tr>
  <tr>
    <td width=40%>Nurul Asyikin Binti Khairul Anuar</td>
    <td>A23CS0162</td>
    <td>NLP Model & Visualization Engineer</td>
  </tr>
  <tr>
    <td width=40%>Harini A/P Sangaran</td>
    <td>A23CS0081</td>
    <td>Data & NLP Engineer</td>
  </tr>
</table>

---

### Links for related documents:
<table>
  <tr>
    <th>Documents</th>
    <th>Links</th>
  </tr>
  <tr>
    <td>Report</td>
    <td align="center">
      <a href="reports/final_report.pdf"><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Presentation Slides</td>
    <td align="center">
      <a href="reports/presentation_slides.pptx"><img src="https://github.com/user-attachments/assets/c09e2ce5-80ce-4236-9508-c65d1f079cda" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Presentation Video</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/2dec74b1-9d2d-4cec-ae38-a57f7ac1711c" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Raw Data</td>
    <td align="center">
      <a href="data/foodpanda_malaysia_reviews_raw.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href="data/compressed_data.csv.gz"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Preprocess & Train Model (Naive Bayes)</td>
    <td align="center">
      <a href="https://colab.research.google.com/drive/18O7z_diG7hXtPDPdvRMw9BPMm7f9i8t1?usp=sharing#scrollTo=Model_1_Naive_Bayes"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Preprocess & Train Model (LSTM)</td>
    <td align="center">
      <a href="https://colab.research.google.com/drive/18O7z_diG7hXtPDPdvRMw9BPMm7f9i8t1?usp=sharing#scrollTo=Model_2_LSTM"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Full and Complete Code in our Repository</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/2e0abbaa-3b7f-450f-92f6-41fd0e6e4dad" width=24px height=23px></a>
    </td>
  </tr>
</table>

---

## Table of Contents

### 1.0 Introduction
- [1.1 Background](#11-background)
- [1.2 Objectives](#12-objectives)
- [1.3 Scope](#13-scope)

### 2.0 Data Acquisition & Preprocessing
- [2.1 Data Collection](#21-data-collection)
- [2.2 Data Preprocessing](#22-data-preprocessing)
- [2.3 Tools Used](#23-tools-used)

### 3.0 Sentiment Model Development
- [3.1 Model Choice](#31-model-choice)
- [3.2 Training Process](#32-training-process)
- [3.3 Evaluation](#33-evaluation)

### 4.0 Apache System Architecture
- [4.0 Apache System Architecture](#40-apache-system-architecture)

### 5.0 Analysis & Results
- [5.1 Key Findings](#51-key-findings)
- [5.2 Visualizations](#52-visualizations)
- [5.3 Insights](#53-insights)

### 6.0 Optimisation & Comparison
- [6.0 Optimisation & Comparison](#60-optimisation--comparison)

### 7.0 Conclusion & Future Work
- [7.0 Conclusion & Future Work](#70-conclusion--future-work)

### 8.0 References
- [8.0 References](#80-references)

### 9.0 Appendix
- [9.0 Appendix](#90-appendix)

---

### 1.0 Introduction

#### 1.1 Background

Food delivery services have become an essential part of daily life in Malaysia, providing consumers with convenient access to meals through mobile applications. Among these services, Foodpanda is one of the country's leading online food delivery platforms, connecting customers with thousands of restaurants and delivery riders across multiple cities. As the platform continues to expand, millions of users share their experiences through reviews on the Google Play Store, providing valuable insights into customer satisfaction regarding overall user experience, including service quality, customer support and application stability.

These publicly available reviews represent an important source of customer feedback that organizations can utilize to understand user sentiment and identify areas requiring improvement. Automated sentiment analysis supported by real-time data processing technologies has become increasingly important for organisations seeking to monitor customer satisfaction and respond promptly to service issues. Therefore, this project develops a real-time sentiment analysis system that analyses Foodpanda Malaysia Google Play reviews using Apache Kafka and Apache Spark Structured Streaming. Approximately 100,000 reviews were collected from the Malaysian Google Play Store using the **google-play-scraper** Python library. The collected reviews were preprocessed using Natural Language Processing (NLP) techniques, including text cleaning, tokenization, stopword removal, stemming, and lemmatization.

To classify customer opinions, two machine learning models, namely Naive Bayes and LSTM, were trained and evaluated using standard performance metrics. The best-performing model was then integrated into a streaming architecture, where Apache Kafka continuously streams incoming reviews to Apache Spark for real-time sentiment prediction. The classified results are subsequently stored for visualization and analysis, enabling stakeholders to monitor customer sentiment effectively.

#### 1.2 Objectives

The objectives of this project are:

1. To collect approximately 100,000 Malaysian Foodpanda Google Play reviews using the google-play-scraper library.
2. To preprocess the collected review text using Natural Language Processing (NLP) techniques, including text cleaning, tokenization, stopword removal, stemming, and lemmatization.
3. To develop and compare two sentiment classification models, namely Naive Bayes and LSTM, for classifying reviews into positive, neutral, and negative sentiment.
4. To implement a real-time streaming pipeline using Apache Kafka and Apache Spark Structured Streaming for continuous sentiment prediction.
5. To store the predicted sentiment results for visualization and analysis.

#### 1.3 Scope

The scope of this project includes the following components:

1. Collecting approximately 100,000 Foodpanda reviews from the Malaysian Google Play Store using the google-play-scraper Python library.
2. Performing data preprocessing using Natural Language Processing (NLP) techniques including lowercasing, noise removal, tokenization, stopword removal, stemming, and lemmatization.
3. Labelling sentiment classes based on review ratings, where ratings of one and two stars represent negative sentiment, three stars represent neutral sentiment, and four to five stars represent positive sentiment.
4. Training and evaluating two machine learning algorithms which are Naive Bayes and LSTM.
5. Deploying the best-performing model within an Apache Kafka and Apache Spark Structured Streaming pipeline to perform real-time sentiment classification.
6. Storing the classified output for visualization and comparing system performance between batch processing and streaming processing.

---

### 2.0 Data Acquisition & Preprocessing

#### 2.1 Data Collection

The dataset used in this project consists of customer reviews collected from the official Foodpanda application available on the Google Play Store. Foodpanda was selected because it is one of the most widely used food delivery platforms in Malaysia, with a large number of active users who continuously provide feedback regarding their service experiences. The reviews were collected using the google-play-scraper Python library, which provides access to publicly available Google Play reviews without requiring the official Google Play API. The scraper was configured to retrieve English-language reviews from the Malaysian Google Play Store by specifying the language parameter as English (lang='en') and the country parameter as Malaysia (country='my'). To obtain a representative dataset for machine learning and streaming experiments, the scraper repeatedly retrieved reviews in batches of 200 records until approximately 100,000 reviews were collected. 

The implementation begins by importing the required Python libraries.

```python
from google_play_scraper import reviews, Sort
import pandas as pd
import time
import os
```

The purpose of each library is described below.

- **google_play_scraper** - Retrieves reviews from the Google Play Store.
- **pandas** - Stores and manipulates the collected review data in tabular format.
- **time** - Introduces delays between requests to prevent sending continuous requests to the Google Play servers.
- **os** - Creates the output directory automatically if it does not already exist.

Next, a directory named data is created.

```python
os.makedirs("data", exist_ok=True)
```

The parameter **exist_ok=True** ensures that no error occurs if the folder already exists. This directory is used to store the raw dataset generated by the scraper.

Then, the desired number of reviews are specified.

```python
APP_ID = "com.global.foodpanda.android"
TARGET_REVIEWS = 100000
```

The variable **APP_ID** uniquely identifies the Foodpanda application on the Google Play Store, while **TARGET_REVIEWS** specifies the maximum number of reviews that the scraper attempts to collect.

Two variables are created for the scraping process.

```python
all_reviews = []
continuation_token = None
```

The variable all_reviews stores every review collected throughout the execution of the program. The variable continuation_token is initially assigned None. This token is automatically generated by the Google Play Store after each request and is used to retrieve the next batch of reviews. It enables pagination, allowing the scraper to continue collecting reviews until the target number has been reached.

The review collection process is then performed using a while loop.

```python
while len(all_reviews) < TARGET_REVIEWS:
```

The loop continues executing until either 100,000 reviews have been collected, or no additional reviews are available from the Google Play Store. Within each iteration, the **reviews()** function is executed.

```python
result, continuation_token = reviews(
    APP_ID,
    lang="en",
    country="my",
    sort=Sort.NEWEST,
    count=200,
    continuation_token=continuation_token
)
```

**APP_ID** specifies the Foodpanda application. **lang = "en"** retrieves English language reviews only whereas **country = "my"** retrieves reviews from Malaysia Google Play Store only. **sort=Sort.NEWEST** prioritizes collecting the newest reviews first whereas **count = 200** ensures 200 reviews are retrieved per API call. Lastly, **continuation_token** will proceed the next batch of reviews retrieval from where it ended.

After each request, the scraper checks whether any reviews were returned. If no reviews are returned, the loop terminates because there are no additional reviews available for collection. The code for this function is attached below.

```python
if not result:
    print("No more reviews available.")
    break
```

Once all the reviews are successfully retrieved, they are appended to the master list. The total number of collected reviews is then displayed from time to time for every API call to 8ndicate that the code is running correctly.

```python
all_reviews.extend(result)
print(f"Collected: {len(all_reviews)} reviews")
```

Example output:

Collected: 200 reviews
Collected: 400 reviews
Collected: 600 reviews
...
Collected: 100000 reviews

Google Play provides a continuation token only when more reviews are available. If no continuation token is returned, the scraper terminates because all accessible reviews have already been collected. The code for this function is attached below.

```python
if continuation_token is None:
    print("Reached the end of available reviews.")
    break
```

A one-second delay is then inserted after each iteration. This delay reduces the frequency of requests sent to the Google Play Store, improving stability and reducing the likelihood of temporary connection issues.

```python
time.sleep(1)
```

After all reviews have been collected, the data is converted into a Pandas DataFrame. Instead of storing the complete review object, only the relevant attributes required for sentiment analysis are extracted.

```python
df = pd.DataFrame([{
    "review_id": r.get("reviewId"),
    "review_text": r.get("content"),
    "rating": r.get("score"),
    "review_date": r.get("at"),
    "thumbs_up": r.get("thumbsUpCount"),
    "app_version": r.get("reviewCreatedVersion"),
    "country": "Malaysia",
    "source": "Google Play",
    "app_name": "Foodpanda"
} for r in all_reviews])
```

The collected attributes are summarised in table below.

| Field | Description |
|-------|-------------|
| `review_id` | Unique identifier assigned to each review |
| `review_text` | Review text written by the user |
| `rating` | User rating ranging from 1 to 5 stars |
| `review_date` | Date and time when the review was posted |
| `thumbs_up` | Number of users who marked the review as helpful |
| `app_version` | Version of the Foodpanda application used by the reviewer |
| `country` | Country of the Google Play Store (Malaysia) |
| `source` | Source platform (Google Play Store) |
| `app_name` | Application name (Foodpanda) |

Then, duplicate reviews are removed based on the review ID and reviews without textual content are discarded. This ensures that only valid review text is retained for the preprocessing stage. The python code is attached below. 

```pythpn
df = df.drop_duplicates(subset=["review_id"])
df = df[df["review_text"].notna()]
```

The final dataset is then exported as a CSV file.

```python
df.to_csv(
    "data/foodpanda_malaysia_reviews_raw.csv",
    index=False,
    encoding="utf-8-sig"
)
```

Finally, the scraper displays the total number of collected reviews.

```python
print("Finished scraping.")
print("Total reviews saved:", len(df))
```

Example:

Finished scraping.
Total reviews saved: 100000


The entire compiled code is attached below :

```python
from google_play_scraper import reviews, Sort
import pandas as pd
import time
import os

os.makedirs("data", exist_ok=True)

APP_ID = "com.global.foodpanda.android"
TARGET_REVIEWS = 100000

all_reviews = []
continuation_token = None

while len(all_reviews) < TARGET_REVIEWS:
    result, continuation_token = reviews(
        APP_ID,
        lang="en",
        country="my",
        sort=Sort.NEWEST,
        count=200,
        continuation_token=continuation_token
    )

    if not result:
        print("No more reviews available.")
        break

    all_reviews.extend(result)

    print(f"Collected: {len(all_reviews)} reviews")

    if continuation_token is None:
        print("Reached the end of available reviews.")
        break

    time.sleep(1)

df = pd.DataFrame([{
    "review_id": r.get("reviewId"),
    "review_text": r.get("content"),
    "rating": r.get("score"),
    "review_date": r.get("at"),
    "thumbs_up": r.get("thumbsUpCount"),
    "app_version": r.get("reviewCreatedVersion"),
    "country": "Malaysia",
    "source": "Google Play",
    "app_name": "Foodpanda"
} for r in all_reviews])

df = df.drop_duplicates(subset=["review_id"])
df = df[df["review_text"].notna()]

df.to_csv("data/foodpanda_malaysia_reviews_raw.csv", index=False, encoding="utf-8-sig")

print("Finished scraping.")
print("Total reviews saved:", len(df))
```

---

#### 2.2 Data Preprocessing

The raw Foodpanda review dataset was preprocessed using several Natural Language Processing (NLP) techniques to improve the quality and consistency of the text before training the sentiment classification models. The preprocessing process involved loading the dataset, cleaning the review text, tokenizing the words, removing stopwords, applying stemming and lemmatization, assigning sentiment labels, and exporting the processed dataset.

The preprocessing script begins by importing the required Python libraries and loading the raw review dataset collected during the data acquisition stage.

```python
import pandas as pd
import re
import nltk
import os

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

df = pd.read_csv("data/foodpanda_malaysia_reviews_raw.csv")
```

The required NLTK resources are downloaded before preprocessing.

```python
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
```

 The code below ensures reviews without textual content are removed to ensure that only valid reviews are processed.

```python
TEXT_COLUMN = "review_text"
df = df[df[TEXT_COLUMN].notna()]
```

Next, before preprocessing begins, the stopword list, stemmer, and lemmatizer are initialized.

```python
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
```

These components perform different NLP tasks :
- **Stopwords** - Removes common English words (e.g., the, is, and)
- **Porter Stemmer** - Reduces words to their root form
- **WordNet Lemmatizer** - Converts words into their dictionary base form

Then, the review text is standardized by converting all characters to lowercase, removing URLs, punctuation, numbers, special characters, and extra whitespace. This step standardizes the review text and removes unnecessary information that may negatively affect model performance.

```python
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
```

After cleaning, each review is split into individual words (tokens). Common English stopwords are removed, followed by stemming and lemmatization to reduce vocabulary size while preserving semantic meaning.

```python
def preprocess_text(text):

    cleaned = clean_text(text)

    tokens = cleaned.split()

    tokens = [
        word for word in tokens
        if word not in stop_words and len(word) > 2
    ]

    stemmed_tokens = [stemmer.stem(word) for word in tokens]

    lemmatized_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return pd.Series({
        "cleaned_text": cleaned,
        "tokens": " ".join(tokens),
        "stemmed_text": " ".join(stemmed_tokens),
        "lemmatized_text": " ".join(lemmatized_tokens)
    })
```

The preprocessing function is then applied to every review in the dataset.

```python
processed = df[TEXT_COLUMN].apply(preprocess_text)
df = pd.concat([df, processed], axis=1)
```

An example of the transformation is shown below :

| Stage | Output |
|-------|--------|
| **Original** | `The delivery was very fast!` |
| **Cleaned** | `the delivery was very fast` |
| **Tokens** | `["the", "delivery", "was", "very", "fast"]` |
| **Stopwords Removed** | `["delivery", "fast"]` |
| **Stemmed** | `deliver fast` |
| **Lemmatized** | `delivery fast` |

Since Google Play reviews do not provide sentiment labels, the review ratings are used to generate the target classes for supervised learning. As per the code, reviews with 1 or 2 stars are labelled as negative, reviews with 3 stars are labelled as neutral and reviews with 4 or 5 stars are labelled as positive.

```python
def label_sentiment(rating):

    rating = int(rating)

    if rating <= 2:
        return "negative"

    elif rating == 3:
        return "neutral"

    else:
        return "positive"
```

To improve data quality, duplicate reviews are removed based on the lemmatized review text. Reviews with insufficient textual information are also excluded.

```python
df = df.drop_duplicates(subset=["lemmatized_text"])

df = df[df["lemmatized_text"].str.len() > 5]
```

Finally, the processed dataset is exported as a CSV file.

```python
df.to_csv(
    "data/foodpanda_reviews_preprocessed.csv",
    index=False,
    encoding="utf-8-sig"
)
```

The resulting dataset, **foodpanda_reviews_preprocessed.csv**, contains the original review information together with the cleaned text, tokenized words, stemmed text, lemmatized text, and sentiment labels. This dataset serves as the input for the subsequent sentiment model development stage.

The entire compiled code is attached below :

```python
import pandas as pd
import re
import nltk
import os

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

os.makedirs("data", exist_ok=True)

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

df = pd.read_csv("data/foodpanda_malaysia_reviews_raw.csv")

TEXT_COLUMN = "review_text"
df = df[df[TEXT_COLUMN].notna()]

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def label_sentiment(rating):
    rating = int(rating)
    if rating <= 2:
        return "negative"
    elif rating == 3:
        return "neutral"
    else:
        return "positive"

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_text(text):
    cleaned = clean_text(text)
    tokens = cleaned.split()

    tokens = [
        word for word in tokens
        if word not in stop_words and len(word) > 2
    ]

    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return pd.Series({
        "cleaned_text": cleaned,
        "tokens": " ".join(tokens),
        "stemmed_text": " ".join(stemmed_tokens),
        "lemmatized_text": " ".join(lemmatized_tokens)
    })

processed = df[TEXT_COLUMN].apply(preprocess_text)
df = pd.concat([df, processed], axis=1)

df["sentiment"] = df["rating"].apply(label_sentiment)

df = df.drop_duplicates(subset=["lemmatized_text"])
df = df[df["lemmatized_text"].str.len() > 5]

df.to_csv("data/foodpanda_reviews_preprocessed.csv", index=False, encoding="utf-8-sig")

print("Preprocessing completed.")
print("Total records after preprocessing:", len(df))
print(df["sentiment"].value_counts())
print(df[["review_text", "cleaned_text", "lemmatized_text", "sentiment"]].head())
```

#### 2.3 Tools Used

The tools and technologies used throughout the development of the proposed sentiment analysis pipeline are summarized in table below.

| **Category** | **Tools Used** | **Description** |
|--------------|----------------|-----------------|
| **Data Collection** | Google Play Scraper | Scrapes Foodpanda user reviews from the Malaysian Google Play Store. |
| **Data Preprocessing** | Python, Pandas, NLTK | Cleans and preprocesses review text through lowercasing, noise removal, tokenization, stopword removal, stemming, and lemmatization. |
| **Feature Extraction** | TF-IDF Vectorizer | Converts textual reviews into numerical feature vectors for model training. |
| **Machine Learning Model** | Naive Bayes | Trains a traditional machine learning model for sentiment classification. |
| **Deep Learning Model** | LSTM | Develops and trains a Long Short-Term Memory (LSTM) model for sentiment prediction. |
| **Streaming & Processing** | Apache Kafka, Apache Spark Structured Streaming (PySpark) | Streams review data in real time and performs continuous sentiment prediction. |
| **Data Storage** | Elasticsearch | Stores and indexes predicted sentiment results for efficient retrieval. |
| **Data Visualization** | Kibana | Visualizes sentiment distributions, trends, and analytics through interactive dashboards. |
| **Deployment** | Docker | Containerizes and manages the services used in the streaming pipeline. |
| **Development Environment** | Python, Google Colab, Jupyter Notebook | Used for data preprocessing, model development, experimentation, and testing. |

---

### 3.0 Sentiment Model Development

This project developed a sentiment analysis model to classify Foodpanda customer reviews into three categories: positive, neutral, and negative.

Two different machine learning approaches were implemented and compared:
- Naive Bayes Classifier
- Long Short-Term Memory (LSTM) Neural Network

The objective is to identify customer opinions from review text and evaluate the performance of different sentiment classification approaches.



#### 3.1 Model Choice

Two models were selected for sentiment classification:

##### 1. Naive Bayes Classifier (Scikit-learn)

Naive Bayes was selected as a baseline machine learning model because it is simple, fast, and suitable for text classification tasks. The review text was converted into numerical features using TF-IDF Vectorization before being classified using the Multinomial Naive Bayes algorithm.



##### 2. Long Short-Term Memory (LSTM) Neural Network (TensorFlow/Keras)

LSTM was selected as a deep learning model because it can learn the sequence and relationship between words in customer reviews. The text data was converted into sequences using Tokenizer and padded into a fixed length before being trained using an Embedding layer, LSTM layer, Dropout layer, and Dense output layer.

Both models were trained and evaluated to compare their performance in sentiment classification.



#### 3.2 Training Process

Before training, the dataset was prepared by selecting the review text (`lemmatized_text`) as the input feature and sentiment label as the output.

The following preprocessing steps were performed:

- Removed missing review text data.
- Converted sentiment labels into numerical values using Label Encoder.

<div align="center">

<table>
  <tr>
    <th>Sentiment</th>
    <th>Label</th>
  </tr>
  <tr>
    <td>Negative</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Neutral</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Positive</td>
    <td>2</td>
  </tr>
</table>

</div>


- Split the dataset into training and testing sets using an 80:20 ratio.
- Stratified splitting was applied to maintain the sentiment distribution.



##### Naive Bayes Training

**Preprocessing**
- Text data was transformed into numerical features using TF-IDF Vectorizer.

**Training**
- The extracted TF-IDF features were used to train the Multinomial Naive Bayes classifier.

**Configuration**
<div align="center">

<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Feature Extraction</td><td>TF-IDF</td></tr>
<tr><td>Maximum Features</td><td>5000</td></tr>
<tr><td>Algorithm</td><td>Multinomial Naive Bayes</td></tr>
</table>

</div>

##### LSTM Training

**Preprocessing**
- Text data was converted into sequences using Tokenizer.
- Padding was applied to make all input sequences have the same length.

**Training**
- The processed sequences were trained using an LSTM neural network to learn patterns from customer reviews.

**Configuration**

<div align="center">

<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Vocabulary Size</td><td>10000</td></tr>
<tr><td>Sequence Length</td><td>100</td></tr>
<tr><td>Embedding Dimension</td><td>128</td></tr>
<tr><td>LSTM Units</td><td>64</td></tr>
<tr><td>Batch Size</td><td>64</td></tr>
<tr><td>Optimizer</td><td>Adam</td></tr>
<tr><td>Epochs</td><td>10</td></tr>
</table>

</div>

Early stopping was applied during training to reduce overfitting.



#### 3.3 Evaluation

The performance of both models was evaluated using:

- Accuracy
- Weighted F1-score
- Classification Report
- Confusion Matrix

The results were compared to determine which model provides better sentiment classification performance.

<div align="center">

<table>
  <tr>
    <th>Model</th>
    <th>Accuracy</th>
    <th>Weighted F1-score</th>
  </tr>
  <tr>
    <td>Naive Bayes</td>
    <td>84.62%</td>
    <td>82.41%</td>
  </tr>
  <tr>
    <td>LSTM</td>
    <td>87.00%</td>
    <td>85.30%</td>
  </tr>
</table>

</div>

The confusion matrix was also analysed to observe the number of correctly and incorrectly classified sentiment predictions for each class.

---

### 4.0 Apache System Architecture

<img width="1692" height="930" alt="ChatGPT Image Jun 26, 2026, 09_06_04 PM" src="https://github.com/user-attachments/assets/29509d78-bbb3-426e-99e1-ecf74bda4e55" />

Figure above illustrates the overall architecture of the proposed real-time sentiment analysis system. The pipeline begins by collecting Foodpanda reviews from the Malaysian Google Play Store using google-play-scraper. The collected reviews are then preprocessed using Python, Pandas, and NLTK, where text cleaning, tokenization, stopword removal, stemming, and lemmatization are performed before sentiment labels are assigned. Next, the preprocessed reviews are transformed into numerical features using TF-IDF and used to train two sentiment classification models: LSTM and Naive Bayes. After evaluating both models, the best-performing model is selected for deployment. Although the LSTM model achieved higher classification performance than Naive Bayes model during the training and evaluation stage, the Naive Bayes model was selected for deployment in the real-time streaming pipeline. as it has significantly lower computational and memory requirements, enabling more stable execution within the available hardware resources. For real-time processing, the review data is streamed through Apache Kafka, where Apache Spark Structured Streaming continuously accepts incoming reviews and performs real-time sentiment prediction using the deployed model. The prediction results are stored in Elasticsearch and visualized through interactive Kibana dashboards. All major services are deployed using Docker, providing a consistent and portable execution environment.

---

### 5.0 Analysis & Results
This section explains about all the analysis charts in the FoodPanda Customer Review Sentiment dashboard that was created using ElasticSearch and Kibana after real-time streaming and sentiment classification using Kafka and Spark. The full dashboard is shown in Appendix A. The purpose of this dashboard is to understand customer review patterns, review rating distribution and sentiment trends.

#### 5.1 Dashboard Overview
Figure 5.1 shows the total reviews from the FoodPanda App which is 16,962 reviews after the real-time streaming is conducted. The metric card displays the total reviews by counting the number of records in the Kibana data view.

<img width="307" height="262" alt="image" src="https://github.com/user-attachments/assets/9c7709ff-dbb6-4d13-ab4a-483eea12813c" />

Figure 5.1 Total Reviews Metric Card

Figure 5.2 shows the average star rating of the FoodPanda App reviews. It shows a value of 2.445 out of 5 which means that the overall customer rating is low. Since the value is also below the midpoint of 3, this suggests that FoodPanda customers’ feedback lean towards dissatisfaction. This finding is supported by the sentiment distribution displayed in Figure 5.3 where negative reviews make up the majority of the reviews.

<img width="312" height="270" alt="Screenshot 2026-06-26 171312" src="https://github.com/user-attachments/assets/cb4ef459-feed-4c5b-a3f1-45d16e5f1dba" />

Figure 5.2 Average Star Rating Metric Card

Figure 5.3 displays a bar chart that shows the review distribution by star rating. The chart shows that the highest total reviews recorded have 1 star rating indicating that most customers gave very low ratings and are dissatisfied with the app and service. Then it is followed by 5-star reviews which shows that some customers still had positive experiences. However, 2-star, 3-star and 4-star ratings have lower total reviews with 3 stars being the lowest at 516 total reviews. The patterns shows that the customer reviews are strongly divided between very negative and very positive experience, but negative reviews are more dominant across all reviews.

<img width="712" height="460" alt="Screenshot 2026-06-26 171328" src="https://github.com/user-attachments/assets/b6d10cdf-f8bf-4e23-b0ef-c4666906a153" />

Figure 5.3 Review Distribution by Star Rating

Figure 5.4 is a pie chart that illustrates the sentiment distribution of all recorded FoodPanda reviews. The pie chart shows that 68.96% of all reviews are negative while 31.04% are positive reviews. The result suggests that many customers expressed dissatisfaction in their review.

<img width="542" height="456" alt="Screenshot 2026-06-26 171421" src="https://github.com/user-attachments/assets/87b8f91a-3340-408a-88df-91827ade9a5a" />

Figure 5.4 Sentiment Distribution Across All FoodPanda Reviews

Figure 5.5 is a line chart that illustrates the daily review trend by both negative and positive sentiment. It displays the recorded daily total reviews in the past year. Based on the trend, negative reviews are consistently higher than positive reviews throughout the one year period. There are noticeable spikes in negative reviews around April to June of 2026 which may indicate periods where customers experienced more service-related issues. The positive review remains lower and stable compared to the negative review trend.

<img width="1013" height="487" alt="Screenshot 2026-06-26 172220" src="https://github.com/user-attachments/assets/7b61c272-2796-427c-b6a8-703d4ffaa8a0" />

Figure 5.5 Daily Review Trend by Sentiment

Figure 5.6 shows a tag cloud that displays the top 25 most frequent keywords mentioned in the FoodPanda reviews. The largest shown keywords are cancel, payment, refund, time and hour. These keywords suggest that the most common customer issues are related to order cancellation, payment problems, refund requests, and long waiting times. The tag cloud helps in identifying the main complaint topics that appear repeatedly in reviews.

<img width="862" height="495" alt="Screenshot 2026-06-26 171503" src="https://github.com/user-attachments/assets/c20e84e0-5074-4778-8162-3efd7fdebf4a" />

Figure 5.6 Top 25 Most Frequent Keywords in Reviews

#### 5.2 Key Insights and Recommendations
The Foodpanda Customer Review Sentiment dashboard shows that customer dissatisfaction is mainly related to service and operational issues. This can be seen from the low average star rating, a lot of 1-star reviews, and the fact that most of its reviews were negative, which shows that there were issues that many users faced when using the Foodpanda app. Furthermore, the keyword analysis indicates that the primary issues are order cancellation, payment issues, refund issues, and long wait times. The daily sentiment trend also indicates that negative sentiment is always higher than positive sentiment, suggesting that dissatisfaction is not confined to a particular window, but rather is a persistent concern.

From these key insights gained, there are things that Foodpanda needs to do to improve the process of service recovery and customer support. Focus should be on minimizing the number of orders that are cancelled, processing refunds faster, ensuring the reliability of payment processing, and offering quicker responses via customer support channels. The dashboard will also serve as a monitoring tool that will help the company to identify any sudden surge in negative reviews, and take appropriate action in order to respond swiftly before the situation escalates into something bigger. In conclusion, the analysis results indicate that increasing the operational reliability and addressing complaints can decrease negative sentiment and enhance customer satisfaction.


---

### 6.0 Optimisation & Comparison
### 6.1 Model Comparison
Two sentiment classification models were developed and evaluated using the same preprocessed FoodPanda review dataset:

- **Multinomial Naive Bayes (MNB)**
- **Long Short-Term Memory (LSTM)**

The models were assessed using **Accuracy** and **Weighted F1-Score**.

### Overall Performance Comparison

| Model | Accuracy | Weighted F1-Score |
|---------|---------|---------|
| Multinomial Naive Bayes | 84.62% | 0.8241 |
| LSTM | **87.00%** | **0.8530** |

### Multinomial Naive Bayes Results

| Sentiment | Precision | Recall | F1-Score | Support |
|------------|------------|------------|------------|------------|
| Negative | 0.83 | 0.97 | 0.89 | 7,984 |
| Neutral | 0.00 | 0.00 | 0.00 | 522 |
| Positive | 0.89 | 0.71 | 0.79 | 3,952 |

**Accuracy:** 84.62%

### LSTM Results

| Sentiment | Precision | Recall | F1-Score | Support |
|------------|------------|------------|------------|------------|
| Negative | 0.89 | 0.94 | 0.91 | 7,984 |
| Neutral | 0.14 | 0.01 | 0.02 | 522 |
| Positive | 0.85 | 0.84 | 0.84 | 3,952 |

**Accuracy:** 87.00%

### Key Findings

- The **LSTM model outperformed Multinomial Naive Bayes**, achieving the highest accuracy (**87.00%**) and weighted F1-score (**0.8530**).
- Both models performed well in classifying **negative** and **positive** reviews.
- Performance on the **neutral** class was relatively low due to the limited number of neutral reviews available in the dataset.
- The results indicate that deep learning approaches such as **LSTM** are more effective for sentiment classification on FoodPanda customer reviews.
  
---

## 6.2 Pipeline Architecture Optimization

The pipeline for sentiment analysis uses Kafka, Spark, ElasticSearch and Kibana. During the development of this project, several issues were encountered and optimizations were applied to resolve these issues.

---

### 6.2.1 Kafka Producer Optimization

The first problem that arose is that the Kafka producer could not connect to Kafka broker. This is because the Kafka producer was configured to send the reviews to localhost:9092, and the Kafka broker was not running or was not configured. So, the producer responded with a NoBrokersAvailable error.

The problem was resolved by making sure that Kafka was started correctly before the producer. The Kafka storage was also formatted as Kafka 4.x requires KRaft storage configuration to run the server. Once Kafka was successfully started, the new topic `foodpanda_reviews` was created. This enabled the producer to push review messages out on a continuous basis to the Kafka topic.

**Table 6.2 Kafka Producer Optimization Comparison**

| Problem | Cause | Optimization |
|---|---|---|
| NoBrokersAvailable error | Kafka broker was not running on localhost:9092 | Start Kafka before running the producer |
| Kafka server failed to start | Kafka storage was not formatted | Format Kafka KRaft storage before starting the server |
| Topic not found | Kafka topic had not been created | Create the `foodpanda_reviews` topic before streaming |
| Duplicate or repeated testing issues | Producer was run multiple times during testing | Limit the number of reviews sent during testing to control the data flow |

These optimisations ensured that the Kafka producer can be run smoothly and could stream Foodpanda reviews into the Kafka topic successfully.

---

### 6.2.2 Spark Streaming Consumer Optimization

Spark component is used to read incoming real-time reviews from Kafka. The Spark streaming subscribes to `foodpanda_reviews` topic and reads the review data as a stream. An optimization that was applied to the Spark script is the use of `forEachBatch`. This enables the streaming data to be processed in small batches with the trained machine-learning model. This will enhance processing efficiency for continuous review streaming.

Another optimization was the implementation of checkpointing using `checkpointLocation`. Checkpointing will allow the streaming job to recover from failure and resume its processing from the last checkpoint rather than from the start.

**Table 6.3 Spark Streaming Optimizations Comparison**

| Problem | Cause | Optimization |
|---|---|---|
| Kafka server failed to start | Model prediction was originally more suitable for batch data | Use `foreachBatch` to apply the model on each micro-batch |
| Risk of stream failure or restart | Streaming applications may stop due to errors | Use checkpointing to allow recovery from the last processed state |

This optimization helped Spark to process incoming Foodpanda reviews from real-time Kafka messages more reliably and prepare the sentiment results for dashboard visualisation.

---

### 6.2.3 Elasticsearch and Kibana Optimization

The processed sentiment results were stored and indexed into Elasticsearch and the dashboard visualisation was done using Kibana. Connectivity problems were observed when trying to connect to Elasticsearch with security authentication enabled during development. This led to the Python client generating an authentication error since it was trying to connect without any username and password.

Initially, CSV files were used to create dashboards in Kibana, but this was not suitable for the real-time nature of the pipeline that needed continuous update. The data obtained from streaming is stored in an index called `foodpanda_streaming_reviews`. A data view `foodpanda_reviews` was created and can then be used for creating charts.

**Table 6.4 Elasticsearch and Kibana Optimizations Comparison**

| Problem | Cause | Optimization |
|---|---|---|
| Python could not connect to Elasticsearch | Elasticsearch security required authentication | Disable security for local development or provide username and password |
| Dashboard needed updated results | Static CSV upload did not support continuous updates | Store streaming prediction results in Elasticsearch for Kibana visualisation |

---

### 6.2.4 Docker Deployment Optimization

Components in the pipeline such as Elasticsearch, Kibana and Kafka were isolated in containers to simplify setup using Docker. This reduced dependency since each of the services could be installed on its own with a different environment required. This also prevents version conflicts between local Java, Kafka, Elasticsearch and Kibana installations.

**Table 6.5 Docker Optimizations Comparison**

| Aspect | Before Docker | After Docker |
|---|---|---|
| Service setup | Manual installation required per machine | Each service runs in its own isolated container |
| Version management | Risk of version conflicts across local installations | Each container uses a fixed, compatible version |
| Port configuration | Manual checking and configuration required | Ports are mapped clearly, such as 9200 for Elasticsearch and 9092 for Kafka |
| Deployment consistency | May behave differently on different machines | Same container setup can be reused |
| Troubleshooting | Harder to identify environment-related issues | Easier to restart, remove, or recreate containers |

Docker provided benefits to the pipeline and made deployment more consistent, portable, and easy to manage. It helped to eliminate configuration issues and help the project parts run in a more controlled environment. This optimisation enables a seamless flow of information between Kafka, Spark Streaming, Elasticsearch and Kibana, particularly for real-time sentiment analysis and dashboard visualization.

---

### 7.0 Conclusion & Future Work

### Conclusion
This project successfully developed a real-time sentiment analysis system for FoodPanda customer reviews using Apache Kafka, Apache Spark, Elasticsearch, and Kibana. The system is capable of collecting, processing, classifying, and visualizing customer feedback in real time.

Two sentiment classification models were evaluated, which are the **Multinomial Naive Bayes (MNB)** and **Long Short-Term Memory (LSTM)**. Based on the experimental results, the LSTM model achieved the best performance with an **accuracy of 87.00%** and a **weighted F1-score of 0.8530**. The Kibana dashboard provided valuable insights into customer sentiment distribution, rating trends, review activity, and frequently mentioned keywords.

Overall, the project demonstrates how machine learning, real-time data streaming, and interactive dashboards can be integrated to support data-driven decision-making and improve customer experience.

### Future Work
- Expand the dataset with more recent customer reviews.
- Increase the number of neutral reviews to improve classification balance.
- Evaluate more advanced deep learning models and transformer-based approaches.
- Enhance the dashboard with additional visualizations such as monthly sentiment trends.
- Support multilingual sentiment analysis for a wider range of customer feedback.
---

### 8.0 References

Apache Kafka. (n.d.). *Apache Kafka documentation*. Apache Software Foundation. Retrieved June 26, 2026, from https://kafka.apache.org/documentation/

Apache Spark. (n.d.). *Structured Streaming programming guide*. Apache Software Foundation. Retrieved June 26, 2026, from https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html

Docker. (n.d.). *What is Docker?* Docker Docs. Retrieved June 26, 2026, from https://docs.docker.com/get-started/docker-overview/

Elastic. (n.d.). *Dashboards*. Elastic Docs. Retrieved June 26, 2026, from https://www.elastic.co/docs/explore-analyze/dashboards

Google Play Scraper. (n.d.). *google-play-scraper*. PyPI. Retrieved June 26, 2026, from https://pypi.org/project/google-play-scraper/

---

### 9.0 Appendix

<img width="1077" height="528" alt="image" src="https://github.com/user-attachments/assets/0d3eea23-2ee0-4aef-ba9d-85da64a065d1" />

Appendix A: Foodpanda Customer Review Sentiment Dashboard

<img width="380" height="651" alt="image" src="https://github.com/user-attachments/assets/d26bd81f-f2c9-4a4e-a361-0078a92bac8e" />
<img width="745" height="267" alt="image" src="https://github.com/user-attachments/assets/2dfc91ea-467e-46b7-8b2d-12766edd31f3" />

Appendix B: Foodpanda Reviews Data Collection Code

<img width="385" height="603" alt="image" src="https://github.com/user-attachments/assets/bf256ab7-6fe5-4a69-b766-c19470642f6e" />
<img width="558" height="422" alt="image" src="https://github.com/user-attachments/assets/b457452e-6864-4a5f-b047-b7683368f78d" />

Appendix C: Foodpanda Reviews Data Preprocessing Code





