import csv
import time
from queue import Queue
import threading  # ✅ Optimization: Enables multithreading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver():
    options = Options()

    # ✅ Optimization: Use headless mode and disable unnecessary resources for faster loading
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=1920,1080")

    # ✅ Optimization: Block images, stylesheets, and fonts to speed up page load
    options.add_experimental_option("prefs", {
        "profile.managed_default_content_settings.images": 2,
        "profile.managed_default_content_settings.stylesheets": 2,
        "profile.managed_default_content_settings.fonts": 2
    })

    options.add_argument("user-agent=Mozilla/5.0 ... Safari/537.36")

    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def scrape_with_driver(driver, page_num):
    url = f"https://www.nst.com.my/business?page={page_num}"
    results = []

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".article-teaser"))
        )

        articles = driver.find_elements(By.CSS_SELECTOR, ".article-teaser")

        for article in articles:
            try:
                # ✅ Data Cleaning: Remove whitespace and validate non-empty headline
                headline = article.find_element(By.CSS_SELECTOR, ".field-title").text.strip()
                if not headline:
                    continue

                category = article.find_element(By.CSS_SELECTOR, ".field-category").text.strip()
                date = article.find_element(By.CSS_SELECTOR, ".created-ago").text.strip()

                # ✅ Data Cleaning: Extract summary text only from specific element
                try:
                    summary_elem = article.find_element(By.CSS_SELECTOR, ".field-body")
                    summary = summary_elem.text.strip()
                except NoSuchElementException:
                    summary = ""  # ✅ Data Cleaning: Fallback if summary is missing

                results.append({
                    "category": category,
                    "headline": headline,
                    "summary": summary,
                    "date": date
                })

            except NoSuchElementException:
                continue

        print(f"✅ Page {page_num}: {len(results)} articles scraped.")
    except Exception as e:
        print(f"❌ Error on page {page_num}: {e}")
    return results


def worker(queue, output_list):
    driver = create_driver()
    while not queue.empty():
        page = queue.get()
        result = scrape_with_driver(driver, page)
        output_list.extend(result)
        queue.task_done()
    driver.quit()


def main():
    total_pages = 10
    num_threads = 4
    q = Queue()
    results = []

    # ---------- START TIMER ----------
    start_time = time.time()
    # ---------------------------------

    # ✅ Optimization: Queue used to distribute workload across threads
    for page in range(1, total_pages + 1):
        q.put(page)

    threads = []
    for _ in range(num_threads):
        # ✅ Optimization: Multithreading implementation to speed up scraping
        t = threading.Thread(target=worker, args=(q, results))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    # ✅ Data Output: Save the cleaned and structured data to CSV
    with open("nst_articles_optimized.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["category", "headline", "summary", "date"])
        writer.writeheader()
        writer.writerows(results)

    # ---------- END TIMER & REPORT ----------
    elapsed = time.time() - start_time
    print(f"\n✅ Finished: {len(results)} articles from {total_pages} pages.")
    print(f"⏱️ Total time: {elapsed:.2f} seconds")
    # ----------------------------------------


if __name__ == "__main__":
    main()
