"""
batch_resource_benchmark.py
===========================
Runs batch-mode classification AND measures the CPU and memory the
process uses, so you can fill in requirement 6.4(d) for batch mode with
real numbers instead of "minimal".

Usage (from the activated venv):
    pip install psutil
    $env:MODEL_OVERRIDE="lr"
    python batch_resource_benchmark.py --limit 3349
"""

import argparse
import os
import time
import threading

import numpy as np
import pandas as pd
import psutil

from sentiment_model import predict_batch


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="youtube_comments_cleaned_roberta.csv")
    ap.add_argument("--text-col", default="cleaned_text")
    ap.add_argument("--label-col", default="sentiment")
    ap.add_argument("--limit", type=int, default=3349)
    args = ap.parse_args()

    df = pd.read_csv(args.csv).dropna(subset=[args.text_col])
    if args.limit:
        df = df.head(args.limit)
    texts = df[args.text_col].astype(str).tolist()
    n = len(texts)

    proc = psutil.Process(os.getpid())
    proc.cpu_percent(interval=None)        # prime the CPU meter

    # warm up the model so loading time isn't counted in throughput
    predict_batch(texts[:1])

    # --- sample memory in the background while we classify ---
    peak_mem = {"val": 0.0}
    stop = {"flag": False}

    def sample_mem():
        while not stop["flag"]:
            mb = proc.memory_info().rss / (1024 * 1024)
            peak_mem["val"] = max(peak_mem["val"], mb)
            time.sleep(0.005)

    t = threading.Thread(target=sample_mem)
    t.start()

    t0 = time.time()
    preds, _ = predict_batch(texts)
    elapsed = time.time() - t0

    stop["flag"] = True
    t.join()

    cpu = proc.cpu_percent(interval=None)   # CPU% used since priming
    rps = n / elapsed if elapsed > 0 else float("inf")

    print("\n" + "=" * 50)
    print("  BATCH MODE — PERFORMANCE + RESOURCES")
    print("=" * 50)
    print(f"  Records processed : {n:,}")
    print(f"  Total time        : {elapsed:.3f} s")
    print(f"  Throughput        : {rps:.1f} records/sec")
    if args.label_col in df.columns:
        truth = df[args.label_col].astype(str).tolist()
        acc = np.mean([p == t for p, t in zip(preds, truth)])
        print(f"  Accuracy          : {acc:.4f}")
    print(f"  CPU usage         : {cpu:.1f}%  (of one core)")
    print(f"  Peak memory (RSS) : {peak_mem['val']:.1f} MB")
    print("=" * 50)
    print("Note: CPU% is relative to a single core, so values above 100%")
    print("mean multiple cores were used. Memory is this process only.")


if __name__ == "__main__":
    main()