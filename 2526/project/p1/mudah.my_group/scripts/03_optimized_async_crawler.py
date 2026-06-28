import aiohttp
import asyncio
import csv
import time
import os
import psutil
from datetime import datetime


# =========================
# Configuration
# =========================

BASE_URL = "https://www.mudah.my/_next/data/ZZIvdMD681zu5P-pSGeHT/list.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://www.mudah.my/malaysia/properties-for-sale"
}

OUTPUT_FILE = "data/raw/optimized_mudah_properties.csv"
PERFORMANCE_FILE = "data/performance/performance_results.csv"

CATEGORY = 2000
TOTAL_PAGES = 50
CONCURRENT_REQUESTS = 5
DELAY_SECONDS = 0.5


# =========================
# Helper Functions
# =========================

def extract_property(prop):
    attr = prop.get("attributes", {})

    agent_firm = "Private Seller"
    agent_data = attr.get("agentData", {})

    if isinstance(agent_data, dict):
        firm_data = agent_data.get("data", {})
        if isinstance(firm_data, dict):
            agent_firm = firm_data.get("storeParamsCompanyName", "Private Seller")

    property_id = prop.get("id", "")
    listing_url = f"https://www.mudah.my/view?ad_id={property_id}"

    return [
        property_id,
        attr.get("subject", ""),
        attr.get("priceAlias", ""),
        attr.get("regionName", ""),
        attr.get("subareaName", ""),
        attr.get("propertyTypeName", ""),
        attr.get("titleTypeName", ""),
        attr.get("size", ""),
        attr.get("roomsName", ""),
        attr.get("bathroomName", ""),
        agent_firm,
        listing_url,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ]


async def fetch_page(session, page, semaphore):
    params = {
        "category": CATEGORY,
        "type": "sell",
        "o": page
    }

    async with semaphore:
        await asyncio.sleep(DELAY_SECONDS)

        try:
            async with session.get(BASE_URL, headers=HEADERS, params=params, timeout=15) as response:
                if response.status == 200:
                    data = await response.json()
                    ads = data["pageProps"]["initialStore"]["ads"]

                    rows = [extract_property(prop) for prop in ads]

                    print(f"Fetched page {page}/{TOTAL_PAGES}: {len(rows)} records")
                    return rows

                print(f"Failed page {page}. Status code: {response.status}")
                return []

        except Exception as e:
            print(f"Error on page {page}: {e}")
            return []


def write_performance(method, pages, records, total_time, memory_mb, cpu_percent):
    os.makedirs("data/performance", exist_ok=True)

    file_exists = os.path.exists(PERFORMANCE_FILE)
    throughput = records / total_time if total_time > 0 else 0

    with open(PERFORMANCE_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Method",
                "Pages_Crawled",
                "Records_Collected",
                "Total_Time_Seconds",
                "Throughput_Records_Per_Second",
                "Memory_Usage_MB",
                "CPU_Usage_Percent"
            ])

        writer.writerow([
            method,
            pages,
            records,
            round(total_time, 2),
            round(throughput, 2),
            round(memory_mb, 2),
            round(cpu_percent, 2)
        ])


# =========================
# Main Optimized Crawler
# =========================

async def main():
    print("Starting optimized async crawler...")

    os.makedirs("data/raw", exist_ok=True)

    start_time = time.time()
    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)

    all_rows = []

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_page(session, page, semaphore)
            for page in range(1, TOTAL_PAGES + 1)
        ]

        results = await asyncio.gather(*tasks)

        for page_rows in results:
            all_rows.extend(page_rows)

    total_records = len(all_rows)

    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
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
        ])

        writer.writerows(all_rows)

    end_time = time.time()
    total_time = end_time - start_time

    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / (1024 * 1024)
    cpu_percent = psutil.cpu_percent(interval=1.0)

    write_performance(
        method="Optimized Async",
        pages=TOTAL_PAGES,
        records=total_records,
        total_time=total_time,
        memory_mb=memory_mb,
        cpu_percent=cpu_percent
    )

    throughput = total_records / total_time if total_time > 0 else 0

    print("\n" + "=" * 50)
    print("OPTIMIZED ASYNC CRAWLER COMPLETE")
    print("=" * 50)
    print(f"Total records collected: {total_records}")
    print(f"Total time: {round(total_time, 2)} seconds")
    print(f"Throughput: {round(throughput, 2)} records/second")
    print(f"Memory usage: {round(memory_mb, 2)} MB")
    print(f"CPU usage: {round(cpu_percent, 2)} %")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Performance saved to: {PERFORMANCE_FILE}")
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())