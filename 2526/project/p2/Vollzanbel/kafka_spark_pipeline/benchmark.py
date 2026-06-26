"""Batch-vs-streaming comparison (brief section 6.4).

BATCH mode: classify the whole dataset in one shot with the saved model and
measure total processing time, throughput and accuracy.

STREAMING mode: aggregated from `streaming_metrics.csv`, which spark_streaming.py
writes one row per micro-batch while the live pipeline runs.

    uv run python kafka_spark_pipeline/benchmark.py
"""
import json
import time
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
METRICS_CSV = Path(__file__).resolve().parent / "streaming_metrics.csv"
FIG_DIR = ROOT / "reports" / "figures"


def run_batch():
    """Batch mode classifies the whole dataset with the deployed model
    (Logistic Regression), matching the streaming job, so the throughput/latency
    comparison is apples-to-apples."""
    tfidf = joblib.load(MODELS / "tfidf_vectorizer.joblib")
    clf = joblib.load(MODELS / "logistic_regression.joblib")
    id2label = {int(k): v for k, v in
                json.loads((MODELS / "label_map.json").read_text())["id2label"].items()}

    df = pd.read_csv(ROOT / "data" / "cleaned_data.csv")
    df = df[df["cleaned_text"].notna()].copy()
    texts = df["cleaned_text"].tolist()

    t0 = time.time()
    lr_preds = clf.predict(tfidf.transform(texts))            # deployed: LogReg
    dt = time.time() - t0

    pred_labels = [id2label[int(p)] for p in lr_preds]
    acc = accuracy_score(df["sentiment_label"], pred_labels)
    f1 = f1_score(df["sentiment_label"], pred_labels, average="macro")
    return {
        "records": len(texts),
        "total_sec": round(dt, 3),
        "throughput": round(len(texts) / dt, 1),
        "accuracy": round(acc, 4),
        "macro_f1": round(f1, 4),
    }


def summarize_streaming():
    if not METRICS_CSV.exists():
        return None
    m = pd.read_csv(METRICS_CSV)
    if m.empty:
        return None
    total_records = int(m["num_records"].sum())
    total_sec = float(m["process_sec"].sum())
    acc = m["batch_accuracy"].dropna()
    return {
        "records": total_records,
        "total_sec": round(total_sec, 3),
        "throughput": round(total_records / total_sec, 1) if total_sec else 0.0,
        "accuracy": round(acc.mean(), 4) if len(acc) else "n/a",
        "num_batches": len(m),
        "avg_latency_sec": round(m["avg_latency_sec"].dropna().mean(), 4)
        if m["avg_latency_sec"].notna().any() else "n/a",
    }


def save_plot(batch, stream):
    """Save the batch-vs-streaming throughput chart from the measured numbers."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    FIG_DIR.mkdir(parents=True, exist_ok=True)
    modes = ["Batch", "Streaming"]
    throughput = [batch["throughput"], stream["throughput"]]
    fig, ax = plt.subplots(figsize=(5.5, 4))
    bars = ax.bar(modes, throughput, color=["#1f77b4", "#ff7f0e"])
    ax.set_title("Throughput: Batch vs Streaming")
    ax.set_ylabel("Records / second")
    for b, v in zip(bars, throughput):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:,.0f}", ha="center", va="bottom")
    fig.tight_layout()
    out = FIG_DIR / "fig_batch_vs_streaming.png"
    fig.savefig(out, dpi=130)
    plt.close(fig)
    print(f"Saved figure: {out}")


def main():
    print("Running BATCH benchmark ...")
    batch = run_batch()
    stream = summarize_streaming()

    print("\n================ BATCH vs STREAMING ================")
    print(f"{'Metric':<22}{'Batch':>15}{'Streaming':>15}")
    print("-" * 52)
    rows = [
        ("Records processed", batch["records"], stream["records"] if stream else "-"),
        ("Total time (s)", batch["total_sec"], stream["total_sec"] if stream else "-"),
        ("Throughput (rec/s)", batch["throughput"], stream["throughput"] if stream else "-"),
        ("Accuracy", batch["accuracy"], stream["accuracy"] if stream else "-"),
    ]
    for name, b, s in rows:
        print(f"{name:<22}{str(b):>15}{str(s):>15}")
    if stream:
        print(f"{'Avg latency (s)':<22}{'-':>15}{str(stream['avg_latency_sec']):>15}")
        print(f"{'Micro-batches':<22}{'-':>15}{str(stream['num_batches']):>15}")
    else:
        print("\n(No streaming_metrics.csv yet - run the live pipeline first.)")
    print("=" * 52)

    if stream:
        save_plot(batch, stream)


if __name__ == "__main__":
    main()
