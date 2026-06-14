"""
Data Quality Check Script
==========================
Runs a set of common data quality checks on a CSV or Excel dataset
before performing data cleaning.

Usage:
    python data_quality_check.py path/to/your_file.csv
"""

import sys
import pandas as pd
import numpy as np


def load_data(filepath):
    if filepath.endswith('youtube_comments_raw.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith(('.xlsx', '.xls')):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")


def basic_overview(df):
    print("=" * 60)
    print("1. BASIC OVERVIEW")
    print("=" * 60)
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print("\nColumn data types:")
    print(df.dtypes)
    print()


def missing_values_check(df):
    print("=" * 60)
    print("2. MISSING VALUES")
    print("=" * 60)
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    result = pd.DataFrame({'missing_count': missing, 'missing_pct': missing_pct})
    result = result[result['missing_count'] > 0].sort_values('missing_pct', ascending=False)
    if result.empty:
        print("No missing values found.")
    else:
        print(result)
    print()


def duplicate_check(df):
    print("=" * 60)
    print("3. DUPLICATE ROWS")
    print("=" * 60)
    dup_count = df.duplicated().sum()
    print(f"Total duplicate rows: {dup_count}")
    if dup_count > 0:
        print(f"Percentage of dataset: {dup_count / len(df) * 100:.2f}%")
    print()


def unique_values_check(df):
    print("=" * 60)
    print("4. UNIQUE VALUES PER COLUMN")
    print("=" * 60)
    for col in df.columns:
        n_unique = df[col].nunique()
        print(f"{col}: {n_unique} unique values")
        if n_unique == 1:
            print("   - constant column, consider dropping")
        if n_unique == len(df):
            print("   - likely an identifier column")
    print()


def outlier_check(df):
    print("=" * 60)
    print("5. OUTLIER DETECTION (numeric columns, IQR method)")
    print("=" * 60)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) == 0:
        print("No numeric columns found.")
        return
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        if len(outliers) > 0:
            print(f"{col}: {len(outliers)} outliers "
                  f"({len(outliers) / len(df) * 100:.2f}%) "
                  f"outside [{lower:.2f}, {upper:.2f}]")
    print()


def text_consistency_check(df):
    print("=" * 60)
    print("6. TEXT / CATEGORICAL CONSISTENCY")
    print("=" * 60)
    text_cols = df.select_dtypes(include=['object']).columns
    if len(text_cols) == 0:
        print("No text columns found.")
        return
    for col in text_cols:
        series = df[col].dropna().astype(str)
        if series.empty:
            continue
        has_leading_trailing_space = series.str.strip().ne(series).any()
        has_mixed_case = series.str.lower().nunique() != series.nunique()
        issues = []
        if has_leading_trailing_space:
            issues.append("leading/trailing whitespace")
        if has_mixed_case:
            issues.append("inconsistent casing")
        if issues:
            print(f"{col}: {', '.join(issues)}")
    print()


def summary_statistics(df):
    print("=" * 60)
    print("7. SUMMARY STATISTICS (numeric columns)")
    print("=" * 60)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) == 0:
        print("No numeric columns found.")
    else:
        print(df[numeric_cols].describe().T)
    print()


def run_data_quality_check(filepath):
    df = load_data(filepath)
    basic_overview(df)
    missing_values_check(df)
    duplicate_check(df)
    unique_values_check(df)
    outlier_check(df)
    text_consistency_check(df)
    summary_statistics(df)
    print("=" * 60)
    print("Data quality check complete.")
    print("=" * 60)
    return df


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python data_quality_check.py <path_to_dataset>")
        sys.exit(1)
    run_data_quality_check(sys.argv[1])
