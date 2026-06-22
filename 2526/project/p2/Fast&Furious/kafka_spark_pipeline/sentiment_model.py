"""
sentiment_model.py
==================
Loads the model artefacts saved by the NLP/Model Engineer's notebook
(the `saved_models/` folder) and exposes ONE batch-prediction function:

    predict_batch(texts) -> (labels, confidences)

Why batch instead of the notebook's row-at-a-time predict_sentiment()?
Tokenising / vectorising a whole micro-batch at once is far faster than
one row at a time, which keeps streaming throughput reasonable.

The model is loaded once (lazily, on first call) and cached, so Spark's
foreachBatch reuses the same in-memory model for every micro-batch.

Environment variables:
    MODEL_DIR        path to saved_models/   (default: "saved_models")
    MODEL_OVERRIDE   force a model: "lr" | "nb" | "xlm"  (default: use best_model.pkl)
                     -> set MODEL_OVERRIDE=lr for a fast, lightweight live demo.
"""

import os
import joblib
import numpy as np

MODEL_DIR = os.environ.get("MODEL_DIR", "saved_models")
OVERRIDE = os.environ.get("MODEL_OVERRIDE", "").strip().lower()

# Cache populated on first predict_batch() call.
_state = {}


def _load():
    if _state:
        return

    le = joblib.load(os.path.join(MODEL_DIR, "label_encoder.pkl"))
    tfidf = joblib.load(os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"))
    config = joblib.load(os.path.join(MODEL_DIR, "xlm_roberta_config.pkl"))
    label_names = config["LABEL_NAMES"]
    max_len = config["MAX_LEN"]

    # ---- decide which model to use -------------------------------------
    if OVERRIDE == "xlm":
        kind = "xlm"
    elif OVERRIDE in ("lr", "nb"):
        kind = OVERRIDE
    else:
        best_ptr = joblib.load(os.path.join(MODEL_DIR, "best_model.pkl"))
        if isinstance(best_ptr, dict) and best_ptr.get("best") == "xlm_roberta":
            kind = "xlm"
        else:
            kind = "sklearn"          # best_ptr IS the sklearn model object
            _state["clf"] = best_ptr

    # ---- load the chosen model -----------------------------------------
    if kind in ("lr", "nb"):
        fname = "lr_model.pkl" if kind == "lr" else "nb_model.pkl"
        _state["clf"] = joblib.load(os.path.join(MODEL_DIR, fname))
        kind = "sklearn"

    if kind == "xlm":
        # Heavy imports only happen if we actually use the transformer.
        import torch
        from transformers import (AutoTokenizer,
                                   AutoModelForSequenceClassification)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        tok = AutoTokenizer.from_pretrained(os.path.join(MODEL_DIR, "xlm_roberta_tokenizer"))
        mdl = AutoModelForSequenceClassification.from_pretrained(
            os.path.join(MODEL_DIR, "xlm_roberta_model"))
        mdl.to(device)
        mdl.eval()
        _state.update(torch=torch, tok=tok, mdl=mdl, device=device)

    _state.update(kind=kind, le=le, tfidf=tfidf,
                  label_names=label_names, max_len=max_len)
    print(f"[sentiment_model] loaded '{kind}' "
          f"({'XLM-RoBERTa' if kind == 'xlm' else 'classical'}) "
          f"from {MODEL_DIR}")


def predict_batch(texts):
    """
    texts: list[str]
    returns: (labels: list[str], confidences: list[float])
    """
    _load()
    texts = ["" if t is None else str(t) for t in texts]

    if _state["kind"] == "sklearn":
        X = _state["tfidf"].transform(texts)
        clf = _state["clf"]
        pred_ids = clf.predict(X)
        try:
            conf = clf.predict_proba(X).max(axis=1)
        except Exception:
            conf = np.ones(len(texts))            # NB/LR without proba
        labels = _state["le"].inverse_transform(pred_ids)
        return list(labels), [float(c) for c in conf]

    # ---- XLM-RoBERTa (processed in chunks to bound memory) -------------
    torch = _state["torch"]
    tok, mdl, device = _state["tok"], _state["mdl"], _state["device"]
    label_names, max_len = _state["label_names"], _state["max_len"]

    labels, confs = [], []
    CHUNK = 32
    for i in range(0, len(texts), CHUNK):
        chunk = texts[i:i + CHUNK]
        enc = tok(chunk, truncation=True, padding="max_length",
                  max_length=max_len, return_tensors="pt")
        enc = {k: v.to(device) for k, v in enc.items()}
        with torch.no_grad():
            logits = mdl(**enc).logits
        probs = torch.softmax(logits, dim=1).cpu().numpy()
        ids = probs.argmax(axis=1)
        labels.extend(label_names[int(j)] for j in ids)
        confs.extend(float(probs[r, ids[r]]) for r in range(len(chunk)))
    return labels, confs
