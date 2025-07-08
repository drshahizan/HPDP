# nb_lstm_demo_with_saving.py
"""
An interactive, notebook‑style script that trains and evaluates:
  • Multinomial Naïve Bayes (TF‑IDF)
  • Bidirectional LSTM (embedding → Bi‑LSTM → dense)

--- MODIFIED TO SAVE ARTIFACTS FOR DEPLOYMENT ---
"""

import argparse
import os
import sys
import warnings
import pickle # Added for saving objects

warnings.filterwarnings("ignore", category=FutureWarning)

import numpy as np
import pandas as pd
import random
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline # Added for cleaner NB model saving
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ---------------------------------------------------------------------------
# CLI Arguments
# ---------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="NB + LSTM sentiment demo")
parser.add_argument("--csv", type=str, default="balanced_dataset.csv", help="CSV path")
parser.add_argument("--test_size", type=float, default=0.20, help="Test‑set proportion")
parser.add_argument("--threshold", type=float, default=0.70, help="Prob threshold")
args = parser.parse_args() if "__file__" in globals() else parser.parse_args("")

CSV_PATH = args.csv
TEST_SIZE = args.test_size
THRESH = args.threshold

# ---------------------------------------------------------------------------
# Reproducibility & Setup
# ---------------------------------------------------------------------------
np.random.seed(42)
random.seed(42)
tf.random.set_seed(42)

ARTIFACTS_DIR = "artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# 1  Load & clean data
# ---------------------------------------------------------------------------
print(f"🔄 Loading data from {CSV_PATH} …")
try:
    df = pd.read_csv(CSV_PATH)
except FileNotFoundError:
    sys.exit(f"❌ CSV file not found: {CSV_PATH}")

TEXT_COL = "cleaned_comment"
LABEL_COL = "sentiment"
df["label"] = df[LABEL_COL].map({"negative": 0, "positive": 1, "neutral": 2})

# ---------------------------------------------------------------------------
# 2  Train/test split
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    df[TEXT_COL].astype(str), df["label"], test_size=TEST_SIZE, random_state=42, stratify=df["label"]
)
print(f"📊 Train size: {len(X_train)}, Test size: {len(X_test)}")
label_names = ["NEGATIVE", "POSITIVE", "NEUTRAL"]

# ---------------------------------------------------------------------------
# 3  Naïve Bayes pipeline
# ---------------------------------------------------------------------------
print("\n=== Training Multinomial Naïve Bayes ===")
# Create a full pipeline
nb_pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer(max_features=5000, ngram_range=(1, 2), stop_words="english")),
    ('classifier', MultinomialNB())
])
nb_pipeline.fit(X_train, y_train)
nb_probs = nb_pipeline.predict_proba(X_test)
nb_raw_preds = nb_pipeline.predict(X_test)

# ---------------------------------------------------------------------------
# 4  LSTM pipeline
# ---------------------------------------------------------------------------
print("\n=== Training Bidirectional LSTM ===")
MAX_NUM_WORDS = 20_000
MAX_LEN = 60

tokenizer = keras.preprocessing.text.Tokenizer(num_words=MAX_NUM_WORDS, oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)
X_train_pad = pad_sequences(X_train_seq, maxlen=MAX_LEN)
X_test_pad = pad_sequences(X_test_seq, maxlen=MAX_LEN)

model = keras.Sequential([
    keras.layers.Embedding(MAX_NUM_WORDS, 100, input_length=MAX_LEN),
    keras.layers.Bidirectional(keras.layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2)),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(3, activation="softmax"),
])
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X_train_pad, y_train, epochs=10, batch_size=32, validation_split=0.1, verbose=2)

lstm_probs = model.predict(X_test_pad, verbose=0)
lstm_raw_preds = np.argmax(lstm_probs, axis=1)

# ---------------------------------------------------------------------------
# 5  Thresholding helper & evaluation
# ---------------------------------------------------------------------------

def apply_threshold(probs, threshold=0.70, neutral_class=2):
    max_probs = probs.max(axis=1)
    argmaxes = probs.argmax(axis=1)
    return np.where(max_probs < threshold, neutral_class, argmaxes)

nb_thresh_preds = apply_threshold(nb_probs, THRESH)
lstm_thresh_preds = apply_threshold(lstm_probs, THRESH)


def print_report(name, y_true, y_pred):
    print(f"\n🔍 {name} Report:")
    print(classification_report(y_true, y_pred, target_names=label_names))

# Reports (thresholded) -----------------------------------------------------
print_report("Naïve Bayes (threshold)", y_test, nb_thresh_preds)
print_report("LSTM (threshold)", y_test, lstm_thresh_preds)

# Raw prediction reports ----------------------------------------------------
print_report("Naïve Bayes (raw)", y_test, nb_raw_preds)
print_report("LSTM (raw)", y_test, lstm_raw_preds)

# ---------------------------------------------------------------------------
# 6  Confusion matrices
# ---------------------------------------------------------------------------

FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)

for name, preds, cmap in [
    ("nb_thresh", nb_thresh_preds, "Blues"),
    ("lstm_thresh", lstm_thresh_preds, "Greens"),
]:
    cm = confusion_matrix(y_test, preds)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_names)
    disp.plot(cmap=cmap, xticks_rotation="vertical")
    plt.tight_layout()
    path = os.path.join(FIG_DIR, f"cm_{name}.png")
    plt.title(f"Confusion Matrix - {name}")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"🖼️  Saved {path}")

print("\n✅ Done. Reports printed and confusion matrices saved to /figures/.")

# ---------------------------------------------------------------------------
# 7  Save models & tokenizers  (NEW SECTION)
# ---------------------------------------------------------------------------
print("\n=== Saving models and tokenizers to /artifacts/ ===")

# Save Naive Bayes pipeline (vectorizer + model)
nb_path = os.path.join(ARTIFACTS_DIR, 'nb_pipeline.pkl')
with open(nb_path, 'wb') as f:
    pickle.dump(nb_pipeline, f)
print(f"💾 Saved Naive Bayes pipeline to {nb_path}")

# Save LSTM model
lstm_path = os.path.join(ARTIFACTS_DIR, 'lstm_sentiment_model.h5')
model.save(lstm_path)
print(f"💾 Saved LSTM model to {lstm_path}")

# Save LSTM Tokenizer
tokenizer_path = os.path.join(ARTIFACTS_DIR, 'tokenizer.pkl')
with open(tokenizer_path, 'wb') as f:
    pickle.dump(tokenizer, f)
print(f"💾 Saved LSTM tokenizer to {tokenizer_path}")


print("\n✅ Done.")
