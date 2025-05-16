import pandas as pd
import dask.dataframe as dd
import polars as pl
import numpy as np
import time
import psutil
import threading
import matplotlib.pyplot as plt

def monitor_resources(stop_flag, cpu_list, mem_list):
    while not stop_flag.is_set():
        cpu_list.append(psutil.cpu_percent(interval=0.5))
        mem_list.append(psutil.virtual_memory().percent)

def monitor_performance(func):
    def wrapper(*args, **kwargs):
        stop_flag = threading.Event()
        cpu_usage = []
        mem_usage = []

        monitor_thread = threading.Thread(target=monitor_resources, args=(stop_flag, cpu_usage, mem_usage))
        monitor_thread.start()

        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time

        stop_flag.set()
        monitor_thread.join()

        avg_cpu = sum(cpu_usage) / len(cpu_usage) if cpu_usage else 0
        peak_mem = max(mem_usage) if mem_usage else 0
        throughput = len(result) / elapsed if elapsed > 0 else 0

        print(f"{func.__name__} results:")
        print(f"Time elapsed: {elapsed:.2f} seconds")
        print(f"Avg CPU usage: {avg_cpu:.2f}%")
        print(f"Peak Memory Usage: {peak_mem:.2f}%")
        print(f"Records processed: {len(result):,}")
        print(f"Throughput: {throughput:.2f} records/sec\n")

        return result, elapsed, avg_cpu, peak_mem, throughput
    return wrapper

def parse_and_clean_dates(df, date_col='date'):
    df[date_col] = pd.to_datetime(
        df[date_col].str.replace('@', '', regex=False).str.strip(),
        format='%b %d, %Y %I:%M%p',
        errors='coerce'
    )
    return df

@monitor_performance
def clean_pandas(file_path):
    df = pd.read_csv(file_path, encoding='latin1')

    df['headline'] = df['headline'].astype(str).str.strip()
    df = df[df['headline'] != ""]
    df['summary'] = df['summary'].fillna("").astype(str).str.strip()
    df['category'] = df['category'].astype(str).str.strip()

    df = parse_and_clean_dates(df, 'date')

    df['place'] = df['summary'].str.extract(r'^([A-Z\s]+):')[0]
    df['place'] = df['place'].where(df['place'].notnull(), np.nan)
    df['place'] = df['place'].str.strip().str.title()

    df['summary'] = df['summary'].str.replace(r'^[A-Z\s]+:\s*', '', regex=True)
    df['category'] = df['category'].str.title()

    df = df.drop_duplicates()
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    return df

@monitor_performance
def clean_dask(file_path):
    df = dd.read_csv(file_path, encoding='latin1')

    df['headline'] = df['headline'].astype(str).str.strip()
    df = df[df['headline'] != ""]
    df['summary'] = df['summary'].fillna("").astype(str).str.strip()
    df['category'] = df['category'].astype(str).str.strip()

    df = df.compute()
    df = parse_and_clean_dates(df, 'date')

    df['place'] = df['summary'].str.extract(r'^([A-Z\s]+):')[0]
    df['place'] = df['place'].where(df['place'].notnull(), np.nan)
    df['place'] = df['place'].str.strip().str.title()

    df['summary'] = df['summary'].str.replace(r'^[A-Z\s]+:\s*', '', regex=True)
    df['category'] = df['category'].str.title()

    df = df.drop_duplicates()
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    return df

@monitor_performance
def clean_polars(file_path):
    df = pl.read_csv(file_path, encoding='latin1')

    df = df.with_columns([
        pl.col('headline').str.strip_chars(),
        pl.col('summary').fill_null("").cast(pl.Utf8).str.strip_chars(),
        pl.col('category').str.strip_chars(),
        pl.col('date').str.strip_chars()
    ])

    df = df.filter(pl.col('headline') != "")

    # Clean date string and rename to 'date_cleaned'
    df = df.with_columns([
        pl.col('date').str.replace('@', '', literal=False).str.strip_chars().alias('date_cleaned'),
    ])

    # Parse 'date_cleaned' into datetime, rename to 'date' and drop intermediate column
    df = df.with_columns([
        pl.col('date_cleaned').str.strptime(pl.Datetime, format="%b %d, %Y %I:%M%p", strict=False).alias('date')
    ]).drop('date_cleaned')

    place = (
        df.select(pl.col('summary').str.extract(r'^([A-Z\s]+):'))
          .to_series()
          .str.strip_chars()
          .str.to_titlecase()
    )

    # Replace empty strings with null (missing)
    place = place.map_elements(lambda x: None if x == "" else x)

    df = df.with_columns([place.alias('place')])

    df = df.with_columns(
        df['summary'].str.replace(r'^[A-Z\s]+:\s*', '', literal=False).alias('summary')
    )

    df = df.with_columns(
        (
            pl.col('category').str.to_lowercase()
            .str.slice(0, 1).str.to_uppercase()
            + pl.col('category').str.slice(1, None)
        ).alias('category')
    )

    df = df.unique()

    df = df.with_columns([
        pl.col('date').dt.year().alias('year'),
        pl.col('date').dt.month().alias('month')
    ])

    return df

def plot_results(results):
    tools = ['Pandas', 'Dask', 'Polars']
    times = [r[1] for r in results]
    cpu = [r[2] for r in results]
    mem = [r[3] for r in results]
    throughput = [r[4] for r in results]

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.bar(tools, times)
    plt.ylabel('Seconds')
    plt.title('Processing Time')

    plt.subplot(2, 2, 2)
    plt.bar(tools, cpu)
    plt.ylabel('% CPU Usage')
    plt.title('Average CPU Usage')

    plt.subplot(2, 2, 3)
    plt.bar(tools, mem)
    plt.ylabel('% Memory Usage')
    plt.title('Peak Memory Usage')

    plt.subplot(2, 2, 4)
    plt.bar(tools, throughput)
    plt.ylabel('Records/sec')
    plt.title('Throughput')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = r"C:\Users\User\Documents\UTM data engineering\s6\HPDP\nst_articles_final.csv"

    print("Starting Pandas cleaning...")
    pandas_df, pandas_time, pandas_cpu, pandas_mem, pandas_throughput = clean_pandas(file_path)
    pandas_df.to_csv("cleaned_pandas.csv", index=False, encoding="utf-8")

    print("Starting Dask cleaning...")
    dask_df, dask_time, dask_cpu, dask_mem, dask_throughput = clean_dask(file_path)
    dask_df.to_csv("cleaned_dask.csv", index=False, encoding="utf-8")

    print("Starting Polars cleaning...")
    polars_df, polars_time, polars_cpu, polars_mem, polars_throughput = clean_polars(file_path)
    polars_df.write_csv("cleaned_polars.csv")

    plot_results([
        (pandas_df, pandas_time, pandas_cpu, pandas_mem, pandas_throughput),
        (dask_df, dask_time, dask_cpu, dask_mem, dask_throughput),
        (polars_df, polars_time, polars_cpu, polars_mem, polars_throughput),
    ])
