"""
Data Cleaning Script
=====================
Cleans the YouTube comments dataset based on the data quality check
findings:
  - Drops rows with missing comment_text
  - Converts date columns to proper datetime
  - Strips whitespace and normalizes spacing in text columns
  - Optionally lowercases text columns
  - Saves the cleaned dataset to a new CSV

Usage:
    python data_cleaning.py path/to/your_file.csv
    python data_cleaning.py path/to/your_file.csv --lowercase
"""

import sys
import pandas as pd


DATE_COLUMNS = ['video_published_at', 'published_at', 'updated_at']
TEXT_COLUMNS = ['comment_text', 'author', 'video_title']


def load_data(filepath):
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith(('.xlsx', '.xls')):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")


def handle_missing_values(df):
    before = len(df)
    df = df.dropna(subset=['comment_text'])
    dropped = before - len(df)
    print(f"Dropped {dropped} row(s) with missing comment_text.")
    return df


def convert_dates(df):
    for col in DATE_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            n_failed = df[col].isna().sum()
            print(f"Converted '{col}' to datetime ({n_failed} unparseable value(s) set to NaT).")
    return df


def clean_text_columns(df, lowercase=False):
    present_cols = [c for c in TEXT_COLUMNS if c in df.columns]
    for col in present_cols:
        # strip leading/trailing whitespace and collapse internal whitespace
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
        if lowercase:
            df[col] = df[col].str.lower()
    print(f"Cleaned whitespace/spacing in: {', '.join(present_cols)}")
    if lowercase:
        print("Lowercased the columns above.")
    return df


def run_cleaning(filepath, output_path=None, lowercase_text=False):
    df = load_data(filepath)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns.\n")

    df = handle_missing_values(df)
    df = convert_dates(df)
    df = clean_text_columns(df, lowercase=lowercase_text)

    print(f"\nFinal shape: {df.shape[0]} rows, {df.shape[1]} columns.")

    if output_path is None:
        if filepath.endswith('.csv'):
            output_path = filepath.replace('.csv', '_cleaned.csv')
        else:
            output_path = 'cleaned_data.csv'

    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to: {output_path}")
    return df


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python data_cleaning.py <path_to_dataset> [--lowercase]")
        sys.exit(1)

    filepath = sys.argv[1]
    lowercase_flag = '--lowercase' in sys.argv
    run_cleaning(filepath, lowercase_text=lowercase_flag)
