import os
import pandas as pd
import matplotlib.pyplot as plt


# =========================
# Configuration
# =========================

PERFORMANCE_FILE = "data/performance/performance_results.csv"
OUTPUT_DIR = "images"


# =========================
# Main Function
# =========================

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load performance results
    df = pd.read_csv(PERFORMANCE_FILE)

    print("Performance data loaded:")
    print(df)

    # =========================
    # Chart 1: Total Time
    # =========================
    plt.figure(figsize=(8, 5))
    plt.bar(df["Method"], df["Total_Time_Seconds"])
    plt.title("Total Processing Time Comparison")
    plt.xlabel("Crawler Method")
    plt.ylabel("Time (Seconds)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/total_time_comparison.png", dpi=300)
    plt.close()

    # =========================
    # Chart 2: Throughput
    # =========================
    plt.figure(figsize=(8, 5))
    plt.bar(df["Method"], df["Throughput_Records_Per_Second"])
    plt.title("Throughput Comparison")
    plt.xlabel("Crawler Method")
    plt.ylabel("Records per Second")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/throughput_comparison.png", dpi=300)
    plt.close()

    # =========================
    # Chart 3: Memory Usage
    # =========================
    plt.figure(figsize=(8, 5))
    plt.bar(df["Method"], df["Memory_Usage_MB"])
    plt.title("Memory Usage Comparison")
    plt.xlabel("Crawler Method")
    plt.ylabel("Memory Usage (MB)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/memory_usage_comparison.png", dpi=300)
    plt.close()

    # =========================
    # Chart 4: CPU Usage
    # =========================
    plt.figure(figsize=(8, 5))
    plt.bar(df["Method"], df["CPU_Usage_Percent"])
    plt.title("CPU Usage Comparison")
    plt.xlabel("Crawler Method")
    plt.ylabel("CPU Usage (%)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/cpu_usage_comparison.png", dpi=300)
    plt.close()

    # =========================
    # Performance Summary
    # =========================
    baseline = df[df["Method"] == "Baseline Sequential"].iloc[0]
    optimized = df[df["Method"] == "Optimized Async"].iloc[0]

    speedup = baseline["Total_Time_Seconds"] / optimized["Total_Time_Seconds"]
    throughput_improvement = (
        optimized["Throughput_Records_Per_Second"]
        / baseline["Throughput_Records_Per_Second"]
    )

    print("\n" + "=" * 50)
    print("PERFORMANCE IMPROVEMENT SUMMARY")
    print("=" * 50)
    print(f"Speedup: {speedup:.2f}x faster")
    print(f"Throughput improvement: {throughput_improvement:.2f}x higher")
    print("=" * 50)

    print("\nCharts generated successfully:")
    print(f"- {OUTPUT_DIR}/total_time_comparison.png")
    print(f"- {OUTPUT_DIR}/throughput_comparison.png")
    print(f"- {OUTPUT_DIR}/memory_usage_comparison.png")
    print(f"- {OUTPUT_DIR}/cpu_usage_comparison.png")


if __name__ == "__main__":
    main()