import time
import random
import csv
from datetime import datetime
from pathlib import Path

import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "https://www.iproperty.com.my/property-for-sale"
RAW_DATA_PATH = Path("data/raw/iproperty_raw_test.csv")
LOG_PATH = Path("data/logs/crawling_log.csv")


def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


def save_records(records):
    if not records:
        return

    df = pd.DataFrame(records)

    file_exists = RAW_DATA_PATH.exists()

    df.to_csv(
        RAW_DATA_PATH,
        mode="a",
        index=False,
        header=not file_exists,
        encoding="utf-8-sig"
    )


def save_log(page_number, status, records_collected, error_message=""):
    file_exists = LOG_PATH.exists()

    with open(LOG_PATH, mode="a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "page",
                "status",
                "records_collected",
                "time",
                "error"
            ])

        writer.writerow([
            page_number,
            status,
            records_collected,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            error_message
        ])


def scrape_page(driver, page_number):
    url = f"{BASE_URL}?page={page_number}"
    print(f"\nOpening: {url}")

    driver.get(url)

    # wait for page body to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    time.sleep(random.uniform(4, 7))

    soup = BeautifulSoup(driver.page_source, "lxml")

    records = []
    seen_links = set()

    # collect all links first, then filter possible property listing links
    links = soup.find_all("a", href=True)

    for link in links:
        raw_text = " ".join(link.get_text(" ", strip=True).split())
        href = link.get("href", "")

        if not raw_text:
            continue

        # filter likely property listing cards
        is_property_text = "RM" in raw_text and ("sqft" in raw_text.lower() or "bed" in raw_text.lower())
        is_property_link = "/property/" in href or "/sale/" in href

        if is_property_text and is_property_link:
            if href in seen_links:
                continue

            seen_links.add(href)

            if href.startswith("/"):
                full_url = "https://www.iproperty.com.my" + href
            else:
                full_url = href

            records.append({
                "page": page_number,
                "raw_text": raw_text,
                "listing_url": full_url,
                "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    return records


def main():
    driver = start_driver()

    total_records = 0

    try:
        for page in range(5001, 5201):  # test page 2001 to 4000
            try:
                records = scrape_page(driver, page)
                save_records(records)
                save_log(page, "success", len(records))

                total_records += len(records)

                print(f"Page {page}: {len(records)} records collected")
                print(f"Total so far: {total_records}")

                time.sleep(random.uniform(3, 6))

            except Exception as e:
                print(f"Error on page {page}: {e}")
                save_log(page, "failed", 0, str(e))

    finally:
        driver.quit()

    print("\nCrawling completed.")
    print(f"Total records collected: {total_records}")
    print(f"Raw data saved to: {RAW_DATA_PATH}")
    print(f"Log saved to: {LOG_PATH}")


if __name__ == "__main__":
    main()