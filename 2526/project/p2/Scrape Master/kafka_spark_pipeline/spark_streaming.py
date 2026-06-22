"""
================================================================================
 Spark Structured Streaming consumer  —  FUZZ CHANNEL Sentiment Pipeline
 SECP3133 Project 2 · Member 3 (Pipeline & Visualization)
================================================================================

Reads JSON messages from the Kafka topic written by `producer.py`, classifies
each message with whichever model `models/best_model_info.json` points to
(supports the LogReg+DistilBERT ensemble Member 2 produced), and bulk-indexes
the enriched records into Elasticsearch where Kibana visualises them.

────────────────────────────────────────────────────────────────────────────────
 Data flow
────────────────────────────────────────────────────────────────────────────────

  Kafka topic                 Spark Structured Streaming                ES index
  ─────────────               ──────────────────────────                ────────
  youtube-comments-raw  ───▶  readStream (kafka source)
                              from_json(value, schema)
                              foreachBatch(process_batch)  ───▶  youtube_sentiment
                                ├─ batch_df.toPandas()
                                ├─ predict_ensemble(clean_text, tokens)
                                ├─ attach sentiment_label, sentiment_score,
                                │  per-class probabilities, model_used,
                                │  processed_at
                                └─ helpers.bulk(es, actions)

────────────────────────────────────────────────────────────────────────────────
 Why foreachBatch and not a pandas UDF?
────────────────────────────────────────────────────────────────────────────────
We run Spark in local[*] mode (single JVM), so all rows naturally land in one
process. foreachBatch lets us:
  • Load the models exactly once in the driver Python process (no UDF pickling)
  • Use the Elasticsearch python client directly with helpers.bulk
  • Print clear per-batch progress lines for the demo

────────────────────────────────────────────────────────────────────────────────
 Usage
────────────────────────────────────────────────────────────────────────────────
  python pipeline/spark_streaming.py
  python pipeline/spark_streaming.py --starting-offsets earliest
  python pipeline/spark_streaming.py --single-model       # skip ensemble
  python pipeline/spark_streaming.py --verbose            # show all Spark logs

  By default the script runs in "quiet mode" — only our own startup banner and
  one [batch N] line per micro-batch are printed. Spark/JVM/transformers chatter
  is silenced. Pass --verbose to see the full firehose (useful for debugging).

  On first run, Spark downloads the Kafka connector JAR from Maven Central.
  Takes ~1-2 min the first time, instant after.
================================================================================
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ── Quiet down everything except our own batch prints ──────────────────────
# These env vars MUST be set before importing pyspark / transformers, so they
# live at the very top of the file. Toggle via --verbose if you ever need the
# full chatter back.
_QUIET = "--verbose" not in sys.argv
if _QUIET:
    os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
    os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import joblib
import numpy as np
import pandas as pd
import torch
from elasticsearch import Elasticsearch, helpers
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import (
    IntegerType, StringType, StructField, StructType,
)
from transformers import AutoModelForSequenceClassification, AutoTokenizer

if _QUIET:
    logging.getLogger("py4j").setLevel(logging.ERROR)
    logging.getLogger("pyspark").setLevel(logging.ERROR)
    logging.getLogger("elasticsearch").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logging.getLogger("kafka").setLevel(logging.ERROR)

# ── Paths and runtime config ───────────────────────────────────────────────
PROJECT_ROOT   = Path(__file__).resolve().parent.parent
MODELS_DIR     = PROJECT_ROOT / "models"
MODEL_INFO_FP  = MODELS_DIR / "best_model_info.json"
CHECKPOINT_DIR = PROJECT_ROOT / "checkpoints" / "spark_streaming"

KAFKA_BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "localhost:9092")
KAFKA_TOPIC     = os.environ.get("KAFKA_TOPIC",     "youtube-comments-raw")
ES_HOST         = os.environ.get("ES_HOST",         "http://localhost:9200")
ES_INDEX        = os.environ.get("ES_INDEX",        "youtube_sentiment")

# Pick the Kafka connector that matches the local pyspark install.
# pyspark's bundled JARs are compiled against a specific Scala major version
# (2.12 for Spark <= 3.x, 2.13 for Spark 4.x). The connector artefact id
# encodes both, so we derive it dynamically rather than hard-coding.
def _kafka_connector_pkg() -> str:
    import pyspark
    v = pyspark.__version__               # e.g. "4.1.1" or "3.5.3"
    scala = "2.13" if v.split(".")[0] >= "4" else "2.12"
    return f"org.apache.spark:spark-sql-kafka-0-10_{scala}:{v}"

SPARK_KAFKA_PKG = _kafka_connector_pkg()


def _cached_jars_or_packages() -> tuple[str | None, str | None]:
    """If the connector JARs are already in Ivy's local cache, point Spark at
    them via --jars (zero Ivy chatter). Otherwise return the Maven coordinate
    so Spark resolves it from the network on first run."""
    import pyspark
    v = pyspark.__version__
    scala = "2.13" if v.split(".")[0] >= "4" else "2.12"
    ivy_cache = Path.home() / ".ivy2.5.2" / "jars"
    needed = [
        f"org.apache.spark_spark-sql-kafka-0-10_{scala}-{v}.jar",
        f"org.apache.spark_spark-token-provider-kafka-0-10_{scala}-{v}.jar",
    ]
    if not all((ivy_cache / n).exists() for n in needed):
        return (None, SPARK_KAFKA_PKG)
    # Include all the transitive deps that the connector pulls in. We grab
    # everything matching kafka-clients / hadoop-client / lz4 / snappy / etc
    # rather than enumerate exact versions, so a Spark upgrade just works.
    # Ivy stores jars as e.g. "org.apache.spark_spark-sql-kafka-0-10_2.13-4.1.1.jar",
    # so each pattern needs a leading wildcard for the groupId prefix.
    glob_patterns = ["*spark-sql-kafka*.jar", "*spark-token-provider-kafka*.jar",
                     "*kafka-clients*.jar", "*lz4-java*.jar", "*snappy-java*.jar",
                     "*slf4j-api*.jar", "*hadoop-client*.jar", "*commons-pool*.jar",
                     "*jsr305*.jar", "*scala-parallel-collections*.jar"]
    # Ivy keeps every version that's ever been resolved (e.g. kafka-clients
    # 3.4.1 next to 3.9.1). Loading both into Spark's classpath causes runtime
    # version conflicts, so we dedupe to one JAR per artifact, preferring the
    # highest version. The "artifact" key strips the trailing "-X.Y.Z" version.
    import re
    candidates: dict[str, tuple[tuple[int, ...], Path]] = {}
    for pat in glob_patterns:
        for p in ivy_cache.glob(pat):
            if scala == "2.13" and "_2.12-" in p.name:
                continue
            if scala == "2.12" and "_2.13-" in p.name:
                continue
            # Match the LAST `-<numeric>.<numeric>.<numeric>` before `.jar`.
            # This dodges the `kafka-0-10` portion in connector filenames.
            m = re.match(r"^(.+?)-(\d+(?:\.\d+){1,3})\.jar$", p.name)
            if not m:
                # Filename without a parseable version — include it unconditionally
                candidates.setdefault(p.name, ((0,), p))
                continue
            artifact, ver_str = m.group(1), m.group(2)
            try:
                ver = tuple(int(x) for x in ver_str.split("."))
            except ValueError:
                candidates.setdefault(p.name, ((0,), p))
                continue
            prev = candidates.get(artifact)
            if prev is None or ver > prev[0]:
                candidates[artifact] = (ver, p)
    jars = [str(t[1]) for t in candidates.values()]
    return (",".join(jars), None)

LABELS    = ["negative", "neutral", "positive"]
LABEL_ARR = np.array(LABELS)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# ── Schema of the Kafka message body (matches producer.py PAYLOAD_COLS) ────
KAFKA_VALUE_SCHEMA = StructType([
    StructField("comment_id",   StringType()),
    StructField("video_id",     StringType()),
    StructField("video_title",  StringType()),
    StructField("comment_text", StringType()),
    StructField("clean_text",   StringType()),
    StructField("tokens",       StringType()),
    StructField("like_count",   IntegerType()),
    StructField("reply_count",  IntegerType()),
    StructField("published_at", StringType()),
    StructField("ingested_at",  StringType()),
])


# ────────────────────────────────────────────────────────────────────────────
# Model loading — done once in the driver process
# ────────────────────────────────────────────────────────────────────────────

class SentimentScorer:
    """Wraps either an ensemble (LogReg + DistilBERT) or a single model.

    Single source of truth is models/best_model_info.json — written by
    model_training.ipynb. The Spark job doesn't need to know which model
    won; it just calls scorer.predict_proba(clean_texts, tokens_list).
    """

    def __init__(self, info: dict, force_single: bool = False):
        self.info = info
        kind = info["kind"]

        if kind == "ensemble" and not force_single:
            print(f"[scorer] loading ensemble: {info['best_model']}")
            self.mode = "ensemble"
            self.weights = []
            self.logreg, self.bert_tok, self.bert_model = None, None, None
            for comp in info["components"]:
                if comp["kind"] == "sklearn-pipeline":
                    self.logreg = joblib.load(comp["path"])
                    self.logreg_w = comp["weight"]
                elif comp["kind"] == "huggingface":
                    self.bert_tok   = AutoTokenizer.from_pretrained(comp["path"])
                    self.bert_model = (
                        AutoModelForSequenceClassification
                        .from_pretrained(comp["path"]).to(DEVICE).eval()
                    )
                    self.bert_w = comp["weight"]
        else:
            # Fall back to a single model — either ensemble fallback or
            # the natively-single winner.
            single = info.get("fallback_single_model") if (kind == "ensemble") else info
            print(f"[scorer] loading single model: {single['kind']}")
            self.mode = "single-" + single["kind"]
            if single["kind"] == "sklearn-pipeline":
                self.logreg = joblib.load(single["path"])
            else:
                self.bert_tok = AutoTokenizer.from_pretrained(single["path"])
                self.bert_model = (
                    AutoModelForSequenceClassification
                    .from_pretrained(single["path"]).to(DEVICE).eval()
                )

        print(f"[scorer] mode={self.mode}  device={DEVICE}")

    # ── Probability helpers ────────────────────────────────────────────────
    def _logreg_proba(self, tokens_list):
        p = self.logreg.predict_proba(tokens_list)
        order = [list(self.logreg.classes_).index(l) for l in LABELS]
        return p[:, order]

    @torch.no_grad()
    def _bert_proba(self, texts, batch_size=32, max_len=128):
        out = []
        for i in range(0, len(texts), batch_size):
            enc = self.bert_tok(
                texts[i:i+batch_size], truncation=True, max_length=max_len,
                padding=True, return_tensors="pt",
            ).to(DEVICE)
            logits = self.bert_model(**enc).logits
            out.append(torch.softmax(logits, dim=-1).cpu().numpy())
        p = np.vstack(out)
        order = [self.bert_model.config.id2label[i] for i in range(p.shape[1])]
        idx   = [order.index(l) for l in LABELS]
        return p[:, idx]

    def predict_proba(self, clean_texts, tokens_list):
        """Return an (N, 3) array of probabilities aligned to LABELS."""
        if self.mode == "ensemble":
            p_lr = self._logreg_proba(tokens_list)
            p_bt = self._bert_proba(clean_texts)
            return self.logreg_w * p_lr + self.bert_w * p_bt
        if self.mode == "single-sklearn-pipeline":
            return self._logreg_proba(tokens_list)
        return self._bert_proba(clean_texts)


# ────────────────────────────────────────────────────────────────────────────
# foreachBatch handler — runs in the driver process for each micro-batch
# ────────────────────────────────────────────────────────────────────────────

def make_batch_handler(scorer: SentimentScorer, es: Elasticsearch):
    """Returns the foreachBatch callback closed over scorer + es."""

    def process_batch(batch_df, batch_id: int) -> None:
        n = batch_df.count()
        if n == 0:
            return

        t0  = time.time()
        pdf = batch_df.toPandas()

        # Defensive defaults — empty tokens hurts LogReg, empty clean_text hurts BERT
        pdf["clean_text"] = pdf["clean_text"].fillna("").astype(str)
        pdf["tokens"]     = pdf["tokens"].fillna("").astype(str)

        probs = scorer.predict_proba(
            pdf["clean_text"].tolist(),
            pdf["tokens"].tolist(),
        )
        pdf["prob_negative"]   = probs[:, 0]
        pdf["prob_neutral"]    = probs[:, 1]
        pdf["prob_positive"]   = probs[:, 2]
        pdf["sentiment_label"] = LABEL_ARR[probs.argmax(axis=1)]
        pdf["sentiment_score"] = probs.max(axis=1)
        pdf["model_used"]      = scorer.info.get("best_model", "unknown")
        pdf["processed_at"]    = datetime.now(timezone.utc).isoformat()

        # Build bulk-index actions
        actions = [
            {
                "_index":  ES_INDEX,
                "_id":     row["comment_id"],
                "_source": {k: (None if pd.isna(v) else v) for k, v in row.items()},
            }
            for row in pdf.to_dict(orient="records")
        ]
        ok, errs = helpers.bulk(es, actions, raise_on_error=False, stats_only=True)

        elapsed = time.time() - t0
        rps     = n / max(elapsed, 1e-6)
        dist    = pdf["sentiment_label"].value_counts().to_dict()
        print(
            f"[batch {batch_id:>4}]  rows={n:>4}  "
            f"{elapsed*1000:>6.0f} ms  ({rps:>6.1f} rec/s)  "
            f"es_ok={ok} es_err={errs}  dist={dist}"
        )

    return process_batch


# ────────────────────────────────────────────────────────────────────────────
# Main
# ────────────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Spark Structured Streaming sentiment job")
    p.add_argument("--bootstrap", default=KAFKA_BOOTSTRAP)
    p.add_argument("--topic",     default=KAFKA_TOPIC)
    p.add_argument("--es-host",   default=ES_HOST)
    p.add_argument("--starting-offsets", choices=["earliest", "latest"],
                   default="latest",
                   help="where to start reading from (default: latest)")
    p.add_argument("--single-model", action="store_true",
                   help="skip the ensemble, use the fallback single model")
    p.add_argument("--trigger-seconds", type=int, default=5,
                   help="micro-batch trigger interval (default: 5s)")
    p.add_argument("--verbose", action="store_true",
                   help="show full Spark/transformers/py4j logs (default: only batch lines)")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    # Make our prints visible immediately instead of buffered behind Spark's
    # JVM stdout writes.
    sys.stdout.reconfigure(line_buffering=True)

    print("=" * 78)
    print("  FUZZ CHANNEL Sentiment Pipeline · Spark Structured Streaming")
    print("=" * 78)
    print(f"  kafka bootstrap : {args.bootstrap}")
    print(f"  topic           : {args.topic}")
    print(f"  elasticsearch   : {args.es_host} (index: {ES_INDEX})")
    print(f"  starting offset : {args.starting_offsets}")
    print(f"  trigger         : {args.trigger_seconds}s micro-batches")
    print(f"  device          : {DEVICE}")
    print(f"  checkpoint dir  : {CHECKPOINT_DIR}")
    print("=" * 78)

    if not MODEL_INFO_FP.exists():
        print(f"ERROR: {MODEL_INFO_FP} not found. Run model_training.ipynb first.")
        return 2

    with open(MODEL_INFO_FP) as f:
        info = json.load(f)
    scorer = SentimentScorer(info, force_single=args.single_model)

    es = Elasticsearch(args.es_host, request_timeout=30)
    if not es.ping():
        print(f"ERROR: cannot reach Elasticsearch at {args.es_host}")
        return 2

    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

    jars_csv, pkg = _cached_jars_or_packages()
    builder = (
        SparkSession.builder
        .appName("FuzzSentimentStream")
        .master("local[*]")
        .config("spark.sql.session.timeZone", "UTC")
        .config("spark.sql.shuffle.partitions", "4")
        .config("spark.ui.showConsoleProgress", "false")
    )
    if jars_csv:
        # Local JARs path — no Ivy noise on startup
        builder = builder.config("spark.jars", jars_csv)
    else:
        # First run — let Spark resolve from Maven Central
        builder = builder.config("spark.jars.packages", pkg)
    spark = builder.getOrCreate()
    spark.sparkContext.setLogLevel("ERROR" if _QUIET else "WARN")

    raw = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", args.bootstrap)
        .option("subscribe", args.topic)
        .option("startingOffsets", args.starting_offsets)
        .option("failOnDataLoss", "false")
        .load()
    )

    parsed = (
        raw.selectExpr("CAST(value AS STRING) AS json")
        .select(from_json(col("json"), KAFKA_VALUE_SCHEMA).alias("d"))
        .select("d.*")
    )

    query = (
        parsed.writeStream
        .foreachBatch(make_batch_handler(scorer, es))
        .outputMode("update")
        .trigger(processingTime=f"{args.trigger_seconds} seconds")
        .option("checkpointLocation", str(CHECKPOINT_DIR))
        .start()
    )

    print(f"[stream] started. waiting for messages on '{args.topic}' ...")
    print(f"[stream] Ctrl-C to stop.\n")
    try:
        query.awaitTermination()
    except KeyboardInterrupt:
        print("\n[stream] Ctrl-C — stopping cleanly ...")
        query.stop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
