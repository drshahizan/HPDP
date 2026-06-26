from cProfile import label
from pathlib import Path
import os
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR.parent / "saved_models"

MODEL_PATH = MODEL_DIR / "lstm_model.keras"
TOKENIZER_PATH = MODEL_DIR / "lstm_tokenizer.pkl"
CONFIG_PATH = MODEL_DIR / "lstm_config.pkl"

print("MODEL_PATH =", MODEL_PATH)
print("Exists =", MODEL_PATH.exists())

# load model
model = load_model(MODEL_PATH)

# load tokenizer
with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

# load config
with open(CONFIG_PATH, "rb") as f:
    config = pickle.load(f)

MAX_LEN = config.get("max_len", 100)


def preprocess(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding="post")
    return padded


def predict(text):
    x = preprocess(text)

    probs = model.predict(x, verbose=0)[0]

    pred_id = int(np.argmax(probs))
    confidence = float(np.max(probs))

    label = ['negative', 'neutral', 'positive'][pred_id]

    return label, confidence