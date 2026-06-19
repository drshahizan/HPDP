"""
batch_benchmark.py
==================
Produces the BATCH side of the "batch vs streaming" comparison the brief
requires (Section 6.4): total processing time, throughput (records/sec),
and classification accuracy.

It classifies a fixed set of N comments all at once and reports the
numbers. You compare these against the STREAMING numbers printed by
spark_streaming.py (the "rec/s" line for each micro-batch).

Usage:
    python batch_benchmark.py --csv youtube_comments_cleaned_roberta.csv --limit 500

Tip: run the producer with the SAME --limit so both modes process the
same volume, giving a fair comparison.
"""

import argparse
import time

import numpy as np
import pandas as pd

from sentiment_model import predict_batch


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="youtube_comments_cleaned_roberta.csv")
    ap.add_argument("--text-col", default="cleaned_text")
    ap.add_argument("--label-col", default="sentiment")
    ap.add_argument("--limit", type=int, default=500)
    args = ap.parse_args()

    df = pd.read_csv(args.csv).dropna(subset=[args.text_col])
    if args.limit:
        df = df.head(args.limit)
    texts = df[args.text_col].astype(str).tolist()
    n = len(texts)
    print(f"Benchmarking BATCH mode on {n:,} records...\n")

    # warm up the model so loading time is not counted in throughput
    predict_batch(texts[:1])

    t0 = time.time()
    preds, _ = predict_batch(texts)
    elapsed = time.time() - t0

    rps = n / elapsed if elapsed > 0 else float("inf")

    print("=" * 48)
    print("  BATCH MODE RESULTS")
    print("=" * 48)
    print(f"  Records processed : {n:,}")
    print(f"  Total time        : {elapsed:.3f} s")
    print(f"  Throughput        : {rps:.1f} records/sec")

    if args.label_col in df.columns:
        truth = df[args.label_col].astype(str).tolist()
        acc = np.mean([p == t for p, t in zip(preds, truth)])
        print(f"  Accuracy          : {acc:.4f}")
    print("=" * 48)

    # Save a row you can paste into your report's comparison table.
    out = pd.DataFrame([{
        "mode": "batch",
        "records": n,
        "total_time_s": round(elapsed, 3),
        "throughput_rec_s": round(rps, 1),
    }])
    out.to_csv("benchmark_batch.csv", index=False)
    print("Saved -> benchmark_batch.csv")
    print("\nNow read the 'rec/s' line in spark_streaming.py's output for "
          "the streaming side, and put both rows in one table.")


if __name__ == "__main__":
    main()
