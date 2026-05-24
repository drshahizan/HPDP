"""Operational workloads benchmarked across four engines.

Each public function is named ``<workload>_<engine>`` and returns a
deterministic result (DataFrame, Polars frame, Spark frame, or scalar count)
so the benchmark harness can read ``len(result)`` or call ``.count()``.

Naming:
- pandas:  take a pandas DataFrame
- polars:  take a path; read inside the function (lazy reads aren't free, so
           this gives Polars its real cost)
- mp:      take a pandas DataFrame; chunk internally
- spark:   take a path

A dispatch dict ``WORKLOADS`` at the bottom makes the notebook loop trivial.
"""

from __future__ import annotations

from functools import partial
from multiprocessing import Pool, cpu_count
from typing import Any

import numpy as np
import pandas as pd

KEYWORD_REGEX = r"(?i)gaming|laptop|phone|ssd|ram"
HOT_PRICE_LO, HOT_PRICE_HI = 100.0, 10000.0
HOT_LIKES_MIN = 5
HOT_CONDITIONS = ("brand new", "like new")
TOP_N = 10


# ---------------------------------------------------------------------------
# 1. agg_category — heavy multi-key groupby with 13 aggregations
# ---------------------------------------------------------------------------
# Group key: (category, condition). For each group we compute:
#   listing_count, mean/median/p25/p75/p90/min/max/std of price,
#   mean/max/sum of likes, unique sellers, unique products.
#
# This exercises hash aggregation (multi-key), sort-based reductions
# (percentiles, median), distinct-set kernels (nunique x 2), and SIMD float
# reductions (std, sum, mean, min, max) simultaneously across all engines.

AGG_GROUP_KEYS = ["category", "condition"]
AGG_OUTPUT_COLUMNS = [
    "category", "condition", "listing_count",
    "mean_price", "median_price", "p25_price", "p75_price", "p90_price",
    "min_price", "max_price", "std_price",
    "mean_likes", "max_likes", "sum_likes",
    "unique_sellers", "unique_products",
]


def agg_category_pandas(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby(AGG_GROUP_KEYS, dropna=False)
    out = g.agg(
        listing_count=("listing_id", "size"),
        mean_price=("price", "mean"),
        median_price=("price", "median"),
        p25_price=("price", lambda s: s.quantile(0.25)),
        p75_price=("price", lambda s: s.quantile(0.75)),
        p90_price=("price", lambda s: s.quantile(0.90)),
        min_price=("price", "min"),
        max_price=("price", "max"),
        std_price=("price", "std"),
        mean_likes=("likes", "mean"),
        max_likes=("likes", "max"),
        sum_likes=("likes", "sum"),
        unique_sellers=("seller", "nunique"),
        unique_products=("product", "nunique"),
    ).reset_index()
    return out[AGG_OUTPUT_COLUMNS]


def agg_category_polars(path: str):
    import polars as pl
    df = pl.read_csv(path, ignore_errors=True)
    return (
        df.group_by(AGG_GROUP_KEYS)
          .agg([
              pl.len().alias("listing_count"),
              pl.col("price").mean().alias("mean_price"),
              pl.col("price").median().alias("median_price"),
              pl.col("price").quantile(0.25).alias("p25_price"),
              pl.col("price").quantile(0.75).alias("p75_price"),
              pl.col("price").quantile(0.90).alias("p90_price"),
              pl.col("price").min().alias("min_price"),
              pl.col("price").max().alias("max_price"),
              pl.col("price").std().alias("std_price"),
              pl.col("likes").mean().alias("mean_likes"),
              pl.col("likes").max().alias("max_likes"),
              pl.col("likes").sum().alias("sum_likes"),
              pl.col("seller").n_unique().alias("unique_sellers"),
              pl.col("product").n_unique().alias("unique_products"),
          ])
          .select(AGG_OUTPUT_COLUMNS)
    )


def _agg_chunk(df: pd.DataFrame) -> pd.DataFrame:
    """Per-chunk partial state: enough to reconstruct mean/median/percentiles/std/nunique."""
    g = df.groupby(AGG_GROUP_KEYS, dropna=False)
    out = g.agg(
        listing_count=("listing_id", "size"),
        sum_price=("price", "sum"),
        sum_sq_price=("price", lambda s: float((s.astype(float) ** 2).sum())),
        min_price=("price", "min"),
        max_price=("price", "max"),
        prices=("price", list),
        sum_likes=("likes", "sum"),
        max_likes=("likes", "max"),
        sellers=("seller", lambda s: set(s.dropna())),
        products=("product", lambda s: set(s.dropna())),
    ).reset_index()
    return out


def agg_category_mp(df: pd.DataFrame, n_workers: int | None = None) -> pd.DataFrame:
    n = n_workers or cpu_count()
    size = (len(df) + n - 1) // n
    chunks = [df.iloc[i:i + size] for i in range(0, len(df), size)]
    with Pool(processes=n) as pool:
        parts = pool.map(_agg_chunk, chunks)

    merged = pd.concat(parts, ignore_index=True)
    final = (
        merged.groupby(AGG_GROUP_KEYS, dropna=False)
        .agg(
            listing_count=("listing_count", "sum"),
            sum_price=("sum_price", "sum"),
            sum_sq_price=("sum_sq_price", "sum"),
            min_price=("min_price", "min"),
            max_price=("max_price", "max"),
            prices=("prices", lambda lists: [v for sub in lists for v in sub]),
            sum_likes=("sum_likes", "sum"),
            max_likes=("max_likes", "max"),
            sellers=("sellers", lambda sets: set().union(*sets)),
            products=("products", lambda sets: set().union(*sets)),
        )
        .reset_index()
    )

    n_rows = final["listing_count"].astype(float)
    final["mean_price"]  = final["sum_price"] / n_rows
    final["median_price"] = final["prices"].map(lambda xs: float(np.median(xs)) if xs else np.nan)
    final["p25_price"]    = final["prices"].map(lambda xs: float(np.quantile(xs, 0.25)) if xs else np.nan)
    final["p75_price"]    = final["prices"].map(lambda xs: float(np.quantile(xs, 0.75)) if xs else np.nan)
    final["p90_price"]    = final["prices"].map(lambda xs: float(np.quantile(xs, 0.90)) if xs else np.nan)
    # Sample standard deviation (matches pandas / Polars default ddof=1)
    var = (final["sum_sq_price"] - n_rows * final["mean_price"] ** 2) / (n_rows - 1).where(n_rows > 1, 1)
    final["std_price"]  = var.clip(lower=0).pow(0.5)
    final["mean_likes"] = final["sum_likes"] / n_rows
    final["unique_sellers"]  = final["sellers"].map(len)
    final["unique_products"] = final["products"].map(len)

    return final[AGG_OUTPUT_COLUMNS]


def agg_category_spark(path: str):
    from pyspark.sql import functions as F
    df = _spark_read(path)
    quantiles = F.percentile_approx("price", [0.25, 0.5, 0.75, 0.90])
    return (
        df.groupBy(*AGG_GROUP_KEYS)
          .agg(
              F.count(F.lit(1)).alias("listing_count"),
              F.mean("price").alias("mean_price"),
              quantiles.alias("_price_quantiles"),
              F.min("price").alias("min_price"),
              F.max("price").alias("max_price"),
              F.stddev("price").alias("std_price"),
              F.mean("likes").alias("mean_likes"),
              F.max("likes").alias("max_likes"),
              F.sum("likes").alias("sum_likes"),
              F.countDistinct("seller").alias("unique_sellers"),
              F.countDistinct("product").alias("unique_products"),
          )
          .withColumn("p25_price",   F.col("_price_quantiles").getItem(0))
          .withColumn("median_price", F.col("_price_quantiles").getItem(1))
          .withColumn("p75_price",   F.col("_price_quantiles").getItem(2))
          .withColumn("p90_price",   F.col("_price_quantiles").getItem(3))
          .drop("_price_quantiles")
          .select(*AGG_OUTPUT_COLUMNS)
    )


# ---------------------------------------------------------------------------
# 2. filter_hot — predicate filter + count
# ---------------------------------------------------------------------------

def filter_hot_pandas(df: pd.DataFrame) -> pd.DataFrame:
    m = (
        df["price"].between(HOT_PRICE_LO, HOT_PRICE_HI)
        & (df["likes"] >= HOT_LIKES_MIN)
        & df["condition"].isin(HOT_CONDITIONS)
    )
    return df.loc[m, ["listing_id", "product", "price", "likes", "condition"]].reset_index(drop=True)


def filter_hot_polars(path: str):
    import polars as pl
    df = pl.read_csv(path, ignore_errors=True)
    return (
        df.filter(
            pl.col("price").is_between(HOT_PRICE_LO, HOT_PRICE_HI)
            & (pl.col("likes") >= HOT_LIKES_MIN)
            & pl.col("condition").is_in(list(HOT_CONDITIONS))
        )
        .select(["listing_id", "product", "price", "likes", "condition"])
    )


def _filter_chunk(df: pd.DataFrame) -> pd.DataFrame:
    return filter_hot_pandas(df)


def filter_hot_mp(df: pd.DataFrame, n_workers: int | None = None) -> pd.DataFrame:
    n = n_workers or cpu_count()
    size = (len(df) + n - 1) // n
    chunks = [df.iloc[i:i + size] for i in range(0, len(df), size)]
    with Pool(processes=n) as pool:
        parts = pool.map(_filter_chunk, chunks)
    return pd.concat(parts, ignore_index=True)


def filter_hot_spark(path: str):
    from pyspark.sql import functions as F
    df = _spark_read(path)
    return (
        df.filter(
            (F.col("price").between(HOT_PRICE_LO, HOT_PRICE_HI))
            & (F.col("likes") >= HOT_LIKES_MIN)
            & (F.col("condition").isin(list(HOT_CONDITIONS)))
        )
        .select("listing_id", "product", "price", "likes", "condition")
    )


# ---------------------------------------------------------------------------
# 3. top_n — top N per category by likes desc, price desc
# ---------------------------------------------------------------------------

def top_n_pandas(df: pd.DataFrame, n: int = TOP_N) -> pd.DataFrame:
    return (
        df.sort_values(["category", "likes", "price"], ascending=[True, False, False])
          .groupby("category", dropna=False)
          .head(n)
          .reset_index(drop=True)
    )


def top_n_polars(path: str, n: int = TOP_N):
    import polars as pl
    df = pl.read_csv(path, ignore_errors=True)
    return (
        df.sort(["category", "likes", "price"], descending=[False, True, True])
          .group_by("category", maintain_order=True)
          .head(n)
    )


def _top_n_chunk(df_n: tuple[pd.DataFrame, int]) -> pd.DataFrame:
    df, n = df_n
    return top_n_pandas(df, n)


def top_n_mp(df: pd.DataFrame, n: int = TOP_N, n_workers: int | None = None) -> pd.DataFrame:
    nw = n_workers or cpu_count()
    size = (len(df) + nw - 1) // nw
    chunks = [(df.iloc[i:i + size], n) for i in range(0, len(df), size)]
    with Pool(processes=nw) as pool:
        parts = pool.map(_top_n_chunk, chunks)
    merged = pd.concat(parts, ignore_index=True)
    return top_n_pandas(merged, n)


def top_n_spark(path: str, n: int = TOP_N):
    from pyspark.sql import functions as F
    from pyspark.sql.window import Window
    df = _spark_read(path)
    w = Window.partitionBy("category").orderBy(F.col("likes").desc(), F.col("price").desc())
    return (
        df.withColumn("rn", F.row_number().over(w))
          .filter(F.col("rn") <= n)
          .drop("rn")
    )


# ---------------------------------------------------------------------------
# 4. keyword_search — regex contains on `product`
# ---------------------------------------------------------------------------

def keyword_search_pandas(df: pd.DataFrame) -> pd.DataFrame:
    m = df["product"].astype(str).str.contains(KEYWORD_REGEX, regex=True, na=False)
    return df.loc[m, ["listing_id", "product", "price"]].reset_index(drop=True)


def keyword_search_polars(path: str):
    import polars as pl
    df = pl.read_csv(path, ignore_errors=True)
    return (
        df.filter(pl.col("product").cast(pl.Utf8).str.contains(KEYWORD_REGEX))
          .select(["listing_id", "product", "price"])
    )


def _keyword_chunk(df: pd.DataFrame) -> pd.DataFrame:
    return keyword_search_pandas(df)


def keyword_search_mp(df: pd.DataFrame, n_workers: int | None = None) -> pd.DataFrame:
    n = n_workers or cpu_count()
    size = (len(df) + n - 1) // n
    chunks = [df.iloc[i:i + size] for i in range(0, len(df), size)]
    with Pool(processes=n) as pool:
        parts = pool.map(_keyword_chunk, chunks)
    return pd.concat(parts, ignore_index=True)


def keyword_search_spark(path: str):
    from pyspark.sql import functions as F
    df = _spark_read(path)
    return (
        df.filter(F.col("product").rlike(KEYWORD_REGEX))
          .select("listing_id", "product", "price")
    )


# ---------------------------------------------------------------------------
# 5. seller_enrich — self-join with derived seller stats
# ---------------------------------------------------------------------------

def _seller_stats_pandas(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("seller", dropna=False)
          .agg(avg_price=("price", "mean"),
               total_listings=("listing_id", "size"),
               total_likes=("likes", "sum"))
          .reset_index()
    )


def seller_enrich_pandas(df: pd.DataFrame) -> pd.DataFrame:
    stats = _seller_stats_pandas(df)
    return df.merge(stats, on="seller", how="inner")


def seller_enrich_polars(path: str):
    import polars as pl
    df = pl.read_csv(path, ignore_errors=True)
    stats = df.group_by("seller").agg([
        pl.col("price").mean().alias("avg_price"),
        pl.len().alias("total_listings"),
        pl.col("likes").sum().alias("total_likes"),
    ])
    return df.join(stats, on="seller", how="inner")


def _seller_enrich_chunk(args: tuple[pd.DataFrame, pd.DataFrame]) -> pd.DataFrame:
    chunk, stats = args
    return chunk.merge(stats, on="seller", how="inner")


def seller_enrich_mp(df: pd.DataFrame, n_workers: int | None = None) -> pd.DataFrame:
    stats = _seller_stats_pandas(df)
    n = n_workers or cpu_count()
    size = (len(df) + n - 1) // n
    chunks = [(df.iloc[i:i + size], stats) for i in range(0, len(df), size)]
    with Pool(processes=n) as pool:
        parts = pool.map(_seller_enrich_chunk, chunks)
    return pd.concat(parts, ignore_index=True)


def seller_enrich_spark(path: str):
    from pyspark.sql import functions as F
    df = _spark_read(path)
    stats = df.groupBy("seller").agg(
        F.mean("price").alias("avg_price"),
        F.count(F.lit(1)).alias("total_listings"),
        F.sum("likes").alias("total_likes"),
    )
    return df.join(F.broadcast(stats), on="seller", how="inner")


# ---------------------------------------------------------------------------
# Spark session helper (single shared SparkSession across workloads)
# ---------------------------------------------------------------------------

_spark = None


def _get_spark():
    global _spark
    if _spark is None:
        from pyspark.sql import SparkSession
        _spark = (
            SparkSession.builder
            .master("local[*]")
            .appName("hpdp_workloads")
            .config("spark.sql.shuffle.partitions", "8")
            .getOrCreate()
        )
        _spark.sparkContext.setLogLevel("ERROR")
    return _spark


def _spark_read(path: str):
    """Single CSV reader so all *_spark workloads parse the file identically.

    `multiLine=True` + `escape='"'` mirror the pandas/Polars/Multiprocessing
    parsers, which means Spark no longer treats embedded `\\n` inside quoted
    cells as record separators.
    """
    return _get_spark().read.csv(
        path,
        header=True,
        inferSchema=True,
        multiLine=True,
        escape='"',
        quote='"',
    )


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

WORKLOADS: dict[str, dict[str, Any]] = {
    "agg_category": {
        "pandas": agg_category_pandas, "polars": agg_category_polars,
        "mp": agg_category_mp, "spark": agg_category_spark,
    },
    "filter_hot": {
        "pandas": filter_hot_pandas, "polars": filter_hot_polars,
        "mp": filter_hot_mp, "spark": filter_hot_spark,
    },
    "top_n": {
        "pandas": top_n_pandas, "polars": top_n_polars,
        "mp": top_n_mp, "spark": top_n_spark,
    },
    "keyword_search": {
        "pandas": keyword_search_pandas, "polars": keyword_search_polars,
        "mp": keyword_search_mp, "spark": keyword_search_spark,
    },
    "seller_enrich": {
        "pandas": seller_enrich_pandas, "polars": seller_enrich_polars,
        "mp": seller_enrich_mp, "spark": seller_enrich_spark,
    },
}

PANDAS_ENGINES = {"pandas", "mp"}   # take a DataFrame
PATH_ENGINES = {"polars", "spark"}  # take a CSV path
