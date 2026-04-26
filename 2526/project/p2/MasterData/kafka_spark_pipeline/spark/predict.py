import os
import warnings
import joblib
import pickle
import numpy as np
import logging
import tensorflow as tf
from transformers import pipeline, logging as hf_logging
from keras.preprocessing.sequence import pad_sequences

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Suppress logs and warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf_logger = tf.get_logger()
tf_logger.setLevel(logging.ERROR)
warnings.filterwarnings("ignore")
hf_logging.set_verbosity_error()

# Build absolute model directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "model")

# Load LSTM model
lstm_model = tf.keras.models.load_model(os.path.join(MODEL_DIR, "lstm_glove_model.h5"))

# Load tokenizer
with open(os.path.join(MODEL_DIR, "tokenizer.pickle"), "rb") as handle:
    tokenizer = pickle.load(handle)

# Load Naive Bayes pipeline (includes vectorizer inside)
nb_model = joblib.load(os.path.join(MODEL_DIR, "nb_model.pkl"))

# Load Hugging Face pipeline
hf_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment", framework="pt")

# Preprocess helper
def preprocess(text):
    return text.lower().strip()

# Sentiment prediction using all 3 models
def predict_sentiment(text):
    clean_text = preprocess(text)

    # Hugging Face
    hf_result = hf_pipeline(clean_text)[0]
    hf_label = hf_result["label"]
    hf_score = hf_result["score"]
    hf_final = {"LABEL_0": -1, "LABEL_1": 0, "LABEL_2": 1}[hf_label]

    # Naive Bayes (pipeline)
    nb_pred = nb_model.predict([clean_text])[0]

    # LSTM
    seq = tokenizer.texts_to_sequences([clean_text])
    padded = pad_sequences(seq, maxlen=100, padding="post")
    lstm_pred = lstm_model.predict(padded)[0]
    reverse_label_map = {0: -1, 1: 0, 2: 1}
    lstm_final = reverse_label_map[np.argmax(lstm_pred)]

    tokens = [word for word in clean_text.split() if word not in stop_words]

    return {
    "text": text,
    "keywords": tokens,
    "hugging_face_label": hf_label,
    "hugging_face_score": round(hf_score, 3),
    "hugging_face_value": hf_final,
    "naive_bayes": int(nb_pred),
    "lstm": int(lstm_final)
}

# Test example
if __name__ == "__main__":
    sample = "Malaysia is a wonderful travel destination!"
    result = predict_sentiment(sample)
    print(result)
