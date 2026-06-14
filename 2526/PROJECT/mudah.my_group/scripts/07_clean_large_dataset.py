import os
import re
import pandas as pd


# =========================
# Configuration
# =========================

RAW_FILE = "data/raw/mudah_properties_partitioned_raw.csv"
OUTPUT_FILE = "data/processed/mudah_properties_cleaned.csv"
SUMMARY_FILE = "data/processed/cleaning_summary.txt"


# =========================
# Cleaning Helper Functions
# =========================

def clean_price(value):
    """
    Convert price text like 'RM 450 000' or 'RM450,000' into numeric value.
    Invalid values return None.
    """
    if pd.isna(value):
        return None

    value = str(value)

    # Keep digits only
    digits = re.sub(r"[^\d]", "", value)

    if digits == "":
        return None

    return int(digits)


def clean_size(value):
    """
    Convert size text like '1200 sq.ft.' into numeric sqft value.
    Invalid values return None.
    """
    if pd.isna(value):
        return None

    value = str(value)

    # Keep digits only
    digits = re.sub(r"[^\d]", "", value)

    if digits == "":
        return None

    return int(digits)


def is_valid_property_id(value):
    """
    Property_ID should be numeric.
    """
    if pd.isna(value):
        return False

    return str(value).strip().isdigit()


# =========================
# Main Cleaning Process
# =========================

def main():
    print("Starting data cleaning process...")

    os.makedirs("data/processed", exist_ok=True)

    df = pd.read_csv(RAW_FILE)

    initial_rows = len(df)

    print(f"Initial raw rows: {initial_rows}")

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove invalid Property_ID rows
    df = df[df["Property_ID"].apply(is_valid_property_id)]

    # Remove duplicate records by Property_ID
    before_duplicates = len(df)
    df = df.drop_duplicates(subset=["Property_ID"], keep="first")
    duplicates_removed = before_duplicates - len(df)

    # Clean Price_RM and Size_sqft
    df["Price_RM"] = df["Price_RM"].apply(clean_price)
    df["Size_sqft"] = df["Size_sqft"].apply(clean_size)

    # Remove rows with invalid price or size
    before_valid_numeric = len(df)
    df = df.dropna(subset=["Price_RM", "Size_sqft"])
    invalid_numeric_removed = before_valid_numeric - len(df)

    # Convert numeric columns to integer
    df["Price_RM"] = df["Price_RM"].astype(int)
    df["Size_sqft"] = df["Size_sqft"].astype(int)

    # Remove unreasonable values
    before_reasonable_filter = len(df)

    df = df[
        (df["Price_RM"] >= 1000) &
        (df["Price_RM"] <= 100000000) &
        (df["Size_sqft"] >= 50) &
        (df["Size_sqft"] <= 1000000)
    ]

    unreasonable_removed = before_reasonable_filter - len(df)

    # Clean text columns
    text_columns = [
        "Title",
        "Region",
        "Subarea",
        "Property_Type",
        "Title_Type",
        "Bedrooms",
        "Bathrooms",
        "Agent_Firm",
        "Listing_URL",
        "Scraped_At"
    ]

    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")
            df[col] = df[col].astype(str).str.strip()

    # Replace blank fields
    df = df.replace("", "Unknown")

    # Reorder columns
    final_columns = [
        "Property_ID",
        "Title",
        "Price_RM",
        "Region",
        "Subarea",
        "Property_Type",
        "Title_Type",
        "Size_sqft",
        "Bedrooms",
        "Bathrooms",
        "Agent_Firm",
        "Listing_URL",
        "Scraped_At"
    ]

    df = df[final_columns]

    final_rows = len(df)
    total_removed = initial_rows - final_rows

    # Save cleaned file
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    # Save summary
    with open(SUMMARY_FILE, "w", encoding="utf-8") as file:
        file.write("Mudah.my Dataset Cleaning Summary\n")
        file.write("=" * 40 + "\n")
        file.write(f"Initial raw rows: {initial_rows}\n")
        file.write(f"Duplicate Property_ID rows removed: {duplicates_removed}\n")
        file.write(f"Invalid price/size rows removed: {invalid_numeric_removed}\n")
        file.write(f"Unreasonable value rows removed: {unreasonable_removed}\n")
        file.write(f"Total rows removed: {total_removed}\n")
        file.write(f"Final cleaned rows: {final_rows}\n")
        file.write(f"Final columns: {len(df.columns)}\n")

    print("\n" + "=" * 50)
    print("DATA CLEANING COMPLETE")
    print("=" * 50)
    print(f"Initial raw rows: {initial_rows}")
    print(f"Duplicate rows removed: {duplicates_removed}")
    print(f"Invalid price/size rows removed: {invalid_numeric_removed}")
    print(f"Unreasonable value rows removed: {unreasonable_removed}")
    print(f"Final cleaned rows: {final_rows}")
    print(f"Cleaned dataset saved to: {OUTPUT_FILE}")
    print(f"Cleaning summary saved to: {SUMMARY_FILE}")

    if final_rows >= 100000:
        print("✅ Requirement met: cleaned dataset has at least 100,000 records.")
    else:
        print("⚠️ Requirement not met: cleaned dataset has fewer than 100,000 records.")

    print("=" * 50)


if __name__ == "__main__":
    main()