import json
import joblib

MODEL_PATH = "models/best_model.pkl"
VECTORIZER_PATH = "models/best_tfidf_vectorizer.pkl"
CONFIG_PATH = "models/deployment_config.json"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

classes = config["classes"]

sample_reviews = [
    "Very good service and easy to use.",
    "The driver cancelled my booking and refund is very slow.",
    "The app is okay but sometimes loading is slow."
]

X = vectorizer.transform(sample_reviews)
predictions = model.predict(X)
probabilities = model.predict_proba(X)

for text, pred, prob in zip(sample_reviews, predictions, probabilities):
    label = classes[int(pred)]
    confidence = max(prob)

    print("Review:", text)
    print("Prediction:", label)
    print("Confidence:", round(confidence, 4))
    print("-" * 50)