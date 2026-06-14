import os
import pandas as pd
import matplotlib.pyplot as plt


# =========================
# Configuration
# =========================

CLEANED_FILE = "data/processed/mudah_properties_cleaned.csv"
OUTPUT_DIR = "images"


# =========================
# Main Function
# =========================

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = pd.read_csv(CLEANED_FILE)

    print("Cleaned dataset loaded.")
    print(df.shape)
    print(df.head())

    # =========================
    # Chart 1: Records by Region
    # =========================
    region_counts = df["Region"].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(region_counts.index, region_counts.values)
    plt.title("Top 10 Regions by Number of Property Listings")
    plt.xlabel("Region")
    plt.ylabel("Number of Listings")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/top_regions_by_listings.png", dpi=300)
    plt.close()

    # =========================
    # Chart 2: Property Type Distribution
    # =========================
    property_counts = df["Property_Type"].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(property_counts.index, property_counts.values)
    plt.title("Top 10 Property Types")
    plt.xlabel("Property Type")
    plt.ylabel("Number of Listings")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/top_property_types.png", dpi=300)
    plt.close()

    # =========================
    # Chart 3: Price Distribution
    # Remove extreme top 1% for clearer visualization
    # =========================
    price_limit = df["Price_RM"].quantile(0.99)
    price_df = df[df["Price_RM"] <= price_limit]

    plt.figure(figsize=(10, 6))
    plt.hist(price_df["Price_RM"], bins=50)
    plt.title("Property Price Distribution")
    plt.xlabel("Price (RM)")
    plt.ylabel("Number of Listings")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/price_distribution.png", dpi=300)
    plt.close()

    # =========================
    # Chart 4: Size Distribution
    # Remove extreme top 1% for clearer visualization
    # =========================
    size_limit = df["Size_sqft"].quantile(0.99)
    size_df = df[df["Size_sqft"] <= size_limit]

    plt.figure(figsize=(10, 6))
    plt.hist(size_df["Size_sqft"], bins=50)
    plt.title("Property Size Distribution")
    plt.xlabel("Size (sqft)")
    plt.ylabel("Number of Listings")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/size_distribution.png", dpi=300)
    plt.close()

    # =========================
    # Dataset Summary
    # =========================
    summary = {
        "Total Cleaned Records": len(df),
        "Total Columns": len(df.columns),
        "Unique Property IDs": df["Property_ID"].nunique(),
        "Average Price RM": round(df["Price_RM"].mean(), 2),
        "Median Price RM": round(df["Price_RM"].median(), 2),
        "Average Size sqft": round(df["Size_sqft"].mean(), 2),
        "Median Size sqft": round(df["Size_sqft"].median(), 2),
        "Total Regions": df["Region"].nunique(),
        "Total Property Types": df["Property_Type"].nunique()
    }

    summary_file = "data/processed/dataset_analysis_summary.txt"

    with open(summary_file, "w", encoding="utf-8") as file:
        file.write("Mudah.my Cleaned Dataset Analysis Summary\n")
        file.write("=" * 50 + "\n")
        for key, value in summary.items():
            file.write(f"{key}: {value}\n")

    print("\nDataset Analysis Summary")
    print("=" * 50)
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\nCharts generated successfully:")
    print(f"- {OUTPUT_DIR}/top_regions_by_listings.png")
    print(f"- {OUTPUT_DIR}/top_property_types.png")
    print(f"- {OUTPUT_DIR}/price_distribution.png")
    print(f"- {OUTPUT_DIR}/size_distribution.png")
    print(f"\nSummary saved to: {summary_file}")


if __name__ == "__main__":
    main()