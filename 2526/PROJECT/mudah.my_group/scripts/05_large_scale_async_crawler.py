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

OUTPUT_FILE = "data/raw/mudah_properties_large_raw.csv"

CATEGORY = 2000
REGION_IDS = list(range(1, 16))  # Malaysia regions used by Mudah
MAX_PAGES_PER_REGION = 400
BATCH_SIZE = 10
CONCURRENT_REQUESTS = 5
DELAY_SECONDS = 0.5

TARGET_RECORDS = 110000  # Aim above 100k because cleaning will remove some rows


# =========================
# Helper Functions
# =========================

def extract_property(prop):
    """
    Extract public listing information only.
    Phone numbers and private contact info are intentionally excluded.
    """
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


async def fetch_page(session, region_id, page, semaphore):
    params = {
        "category": CATEGORY,
        "type": "sell",
        "region": region_id,
        "o": page
    }

    async with semaphore:
        await asyncio.sleep(DELAY_SECONDS)

        try:
            async with session.get(BASE_URL, headers=HEADERS, params=params, timeout=20) as response:
                if response.status == 200:
                    data = await response.json()
                    ads = data["pageProps"]["initialStore"]["ads"]

                    rows = [extract_property(prop) for prop in ads]

                    print(f"Region {region_id} | Page {page}: {len(rows)} records")
                    return rows

                print(f"Failed Region {region_id} | Page {page}. Status: {response.status}")
                return None

        except Exception as e:
            print(f"Error Region {region_id} | Page {page}: {e}")
            return None


def initialize_csv():
    os.makedirs("data/raw", exist_ok=True)

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


def append_rows(rows):
    with open(OUTPUT_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


# =========================
# Main Large-Scale Crawler
# =========================

async def main():
    print("Starting large-scale Mudah.my async crawler...")
    print(f"Target records: {TARGET_RECORDS}")

    initialize_csv()

    start_time = time.time()
    total_records = 0
    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)

    async with aiohttp.ClientSession() as session:
        for region_id in REGION_IDS:
            print("\n" + "=" * 60)
            print(f"Starting Region {region_id}")
            print("=" * 60)

            region_records = 0

            for batch_start in range(1, MAX_PAGES_PER_REGION + 1, BATCH_SIZE):
                batch_end = min(batch_start + BATCH_SIZE, MAX_PAGES_PER_REGION + 1)

                tasks = [
                    fetch_page(session, region_id, page, semaphore)
                    for page in range(batch_start, batch_end)
                ]

                results = await asyncio.gather(*tasks)

                batch_rows = []
                empty_page_found = False

                for page_rows in results:
                    # None means request error, not necessarily empty page
                    if page_rows is None:
                        continue

                    # Empty list means no more inventory for this region
                    if len(page_rows) == 0:
                        empty_page_found = True
                        continue

                    batch_rows.extend(page_rows)

                if batch_rows:
                    append_rows(batch_rows)
                    total_records += len(batch_rows)
                    region_records += len(batch_rows)

                    print(
                        f"Saved batch {batch_start}-{batch_end - 1}: "
                        f"{len(batch_rows)} records | Total: {total_records}"
                    )

                if total_records >= TARGET_RECORDS:
                    print("\nTarget reached. Stopping crawler.")
                    break

                if empty_page_found:
                    print(f"No more listings for Region {region_id}. Moving to next region.")
                    break

                await asyncio.sleep(1)

            print(f"Finished Region {region_id}. Region records: {region_records}")

            if total_records >= TARGET_RECORDS:
                break

    end_time = time.time()
    total_time = end_time - start_time

    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / (1024 * 1024)
    cpu_percent = psutil.cpu_percent(interval=1.0)
    throughput = total_records / total_time if total_time > 0 else 0

    print("\n" + "=" * 60)
    print("LARGE-SCALE CRAWLER COMPLETE")
    print("=" * 60)
    print(f"Total records collected: {total_records}")
    print(f"Total time: {round(total_time, 2)} seconds")
    print(f"Throughput: {round(throughput, 2)} records/second")
    print(f"Memory usage: {round(memory_mb, 2)} MB")
    print(f"CPU usage: {round(cpu_percent, 2)} %")
    print(f"Output file: {OUTPUT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())