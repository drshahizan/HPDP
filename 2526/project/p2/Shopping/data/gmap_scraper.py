"""
================================================================================
Google Maps Review Scraper
================================================================================
SETUP INSTRUCTIONS:
    1. Install dependencies:
       pip install selenium pandas webdriver-manager

    2. Ensure Google Chrome is installed on your system.

    3. Add your Google Maps place URLs to the PLACE_URLS list below.

    4. Run:
       python gmap_scraper.py

OUTPUT FILES:
    - google_reviews.csv   : All scraped reviews (UTF-8, appended incrementally)
    - progress.json        : Resume state (completed URLs, review counts)
    - scraper.log          : Detailed execution log

NOTES:
    - Up to 300 reviews are scraped per place.
    - If interrupted, re-run the script to resume from last saved state.
    - Duplicate reviews are automatically skipped.
================================================================================
"""

# ── Dependency install reminder ──────────────────────────────────────────────
# pip install selenium pandas webdriver-manager

import csv
import json
import logging
import os
import random
import time
from pathlib import Path

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION — Edit this list with up to 10 Google Maps place URLs
# ─────────────────────────────────────────────────────────────────────────────
PLACE_URLS = [
    # Paste your Google Maps place URLs here, e.g.:
    "https://maps.app.goo.gl/sws8cpK7E1f77P1y6", #batu caves
    "https://maps.app.goo.gl/mcvu2yWnC2iujtuu8", #mossy forest
    "https://maps.app.goo.gl/yzwbZnH24MKuUHeB9", #pulau simpadan
    "https://maps.app.goo.gl/cUejB9icyXMEBfHw8", #cheong fatt tze mansion
    "https://maps.app.goo.gl/TQG5jugDdzYYn9wN7", #kundasng sabah
    "https://maps.app.goo.gl/PmgzdjYb6vNNorZJA", #pulau lang tengah
    "https://maps.app.goo.gl/yGD6VsFMr46bmnTv8", #pulau redang
    "https://maps.app.goo.gl/VVqL99B8z8ExqzpH9", #kek lok si temple
    "https://maps.app.goo.gl/NeyrjniAvdA7Tm3p9", #niah national park
    "https://maps.app.goo.gl/JWY9pWdvGqgUHuQc9", #kwang chai hong
    "https://maps.app.goo.gl/UQwEMK536rqxJA1E9", #taman negara national park
    "https://maps.app.goo.gl/iA88tPiYSBuyY3XE6", #petronas twin towers
    "https://maps.app.goo.gl/ukAHEqD5kuqztymG9", #genting skyworld
]

# ── Runtime constants ─────────────────────────────────────────────────────────
MAX_REVIEWS_PER_PLACE = 600
OUTPUT_CSV = "google_reviews.csv"
PROGRESS_FILE = "progress.json"
LOG_FILE = "scraper.log"

# Delay ranges (seconds) for human-like pacing
SCROLL_DELAY_MIN = 1.2
SCROLL_DELAY_MAX = 2.8
ACTION_DELAY_MIN = 0.8
ACTION_DELAY_MAX = 1.8
PAGE_LOAD_TIMEOUT = 30
ELEMENT_TIMEOUT = 15

# ─────────────────────────────────────────────────────────────────────────────
# LOGGING SETUP
# ─────────────────────────────────────────────────────────────────────────────

def setup_logging() -> logging.Logger:
    """Configure file + console logging."""
    logger = logging.getLogger("gmap_scraper")
    logger.setLevel(logging.DEBUG)

    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler (DEBUG and above)
    fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    # Console handler (INFO and above)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


logger = setup_logging()

# ─────────────────────────────────────────────────────────────────────────────
# PROGRESS / RECOVERY
# ─────────────────────────────────────────────────────────────────────────────

class ProgressTracker:
    """
    Persist scraping state to disk so the script can resume after a crash.

    Schema of progress.json:
    {
        "completed_urls": ["url1", "url2", ...],
        "review_counts":  {"url1": 247, ...}
    }
    """

    def __init__(self, path: str = PROGRESS_FILE):
        self.path = Path(path)
        self.state: dict = {"completed_urls": [], "review_counts": {}}
        self._load()

    def _load(self):
        if self.path.exists():
            try:
                with self.path.open("r", encoding="utf-8") as f:
                    self.state = json.load(f)
                logger.info("Loaded progress from %s", self.path)
                logger.info(
                    "Completed URLs: %d | Partial counts: %s",
                    len(self.state["completed_urls"]),
                    self.state["review_counts"],
                )
            except (json.JSONDecodeError, KeyError) as exc:
                logger.warning("Corrupt progress file, starting fresh. (%s)", exc)
                self.state = {"completed_urls": [], "review_counts": {}}

    def _save(self):
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)

    def is_completed(self, url: str) -> bool:
        return url in self.state["completed_urls"]

    def mark_completed(self, url: str):
        if url not in self.state["completed_urls"]:
            self.state["completed_urls"].append(url)
        self._save()
        logger.info("Marked as completed: %s", url)

    def update_count(self, url: str, count: int):
        self.state["review_counts"][url] = count
        self._save()

    def get_count(self, url: str) -> int:
        return self.state["review_counts"].get(url, 0)


# ─────────────────────────────────────────────────────────────────────────────
# CSV OUTPUT
# ─────────────────────────────────────────────────────────────────────────────

class CSVWriter:
    """
    Incremental CSV writer.  Writes the header once and appends rows
    as they are collected, so data is safe even if the script crashes.
    """

    FIELDNAMES = ["place_url", "review_text"]

    def __init__(self, path: str = OUTPUT_CSV):
        self.path = Path(path)
        self._ensure_header()

    def _ensure_header(self):
        """Write header row only if the file is new or empty."""
        if not self.path.exists() or self.path.stat().st_size == 0:
            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
                writer.writeheader()
            logger.debug("CSV header written to %s", self.path)

    def append_reviews(self, rows: list[dict]):
        """Append a list of review dicts to the CSV."""
        if not rows:
            return
        with self.path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
            writer.writerows(rows)
        logger.debug("Appended %d rows to CSV.", len(rows))

    def load_existing_texts(self, url: str) -> set[str]:
        """
        Return a set of already-saved review texts for a given URL so we
        can avoid duplicates when resuming.
        """
        existing: set[str] = set()
        if not self.path.exists():
            return existing
        try:
            df = pd.read_csv(self.path, encoding="utf-8")
            subset = df[df["place_url"] == url]["review_text"].dropna()
            existing = set(subset.tolist())
            logger.debug(
                "Loaded %d existing reviews for dedup from CSV.", len(existing)
            )
        except Exception as exc:
            logger.warning("Could not read existing CSV for dedup: %s", exc)
        return existing


# ─────────────────────────────────────────────────────────────────────────────
# BROWSER MANAGEMENT
# ─────────────────────────────────────────────────────────────────────────────

def build_driver() -> webdriver.Chrome:
    """
    Construct a resource-efficient, headless Chrome WebDriver instance.
    Images, GPU, and unnecessary rendering are disabled.
    """
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-infobars")
    opts.add_argument("--disable-popup-blocking")
    opts.add_argument("--blink-settings=imagesEnabled=false")
    opts.add_argument("--window-size=1280,900")
    opts.add_argument("--lang=en-US,en;q=0.9")
    opts.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
    # Suppress Chrome logging noise
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    opts.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.notifications": 2,
            "profile.managed_default_content_settings.images": 2,
        },
    )

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    logger.info("Chrome WebDriver initialised (headless).")
    return driver


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def human_delay(min_s: float = ACTION_DELAY_MIN, max_s: float = ACTION_DELAY_MAX):
    """Sleep for a random interval to mimic human interaction speed."""
    time.sleep(random.uniform(min_s, max_s))


def exponential_backoff(attempt: int, base: float = 2.0, cap: float = 30.0) -> float:
    """Return a capped exponential back-off delay with jitter."""
    delay = min(base ** attempt + random.uniform(0, 1), cap)
    return delay


def safe_click(driver: webdriver.Chrome, element, retries: int = 3) -> bool:
    """
    Attempt a click, falling back to JavaScript click on interception.
    Returns True if the click succeeded.
    """
    for attempt in range(retries):
        try:
            element.click()
            return True
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", element)
            return True
        except StaleElementReferenceException:
            logger.debug("Stale element on click attempt %d.", attempt + 1)
            human_delay(0.5, 1.0)
        except WebDriverException as exc:
            logger.debug("Click failed (attempt %d): %s", attempt + 1, exc)
            human_delay(*exponential_backoff(attempt), *[None][:0])
    return False


# ─────────────────────────────────────────────────────────────────────────────
# CORE SCRAPER
# ─────────────────────────────────────────────────────────────────────────────

class GoogleMapsReviewScraper:
    """
    Scrapes reviews from a list of Google Maps place URLs.

    Features:
    - Resumable via ProgressTracker + CSVWriter dedup
    - Incremental CSV saves after every batch
    - Exponential back-off retries
    - Human-like scrolling with randomised delays
    - Stale-element recovery
    """

    # CSS / XPath selectors (may need updating if Google changes its DOM)
    SEL_REVIEWS_TAB = 'button[aria-label*="Reviews"]'
    SEL_SORT_BUTTON = 'button[aria-label*="Sort reviews"]'
    SEL_REVIEW_CARD = "div.jftiEf"          # individual review card container
    SEL_REVIEW_TEXT = "span.wiI7pd"         # review body text
    SEL_MORE_BUTTON = "button.w8nwRe"       # "More" expand button
    SEL_SCROLLABLE  = "div.m6QErb[tabindex]"  # scrollable reviews panel

    BATCH_SIZE = 10  # save to CSV every N new reviews

    def __init__(self):
        self.progress = ProgressTracker()
        self.csv_writer = CSVWriter()
        self.driver: webdriver.Chrome | None = None

    # ── Driver lifecycle ──────────────────────────────────────────────────────

    def _start_driver(self):
        if self.driver is None:
            self.driver = build_driver()

    def _quit_driver(self):
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
            self.driver = None
            logger.info("Browser closed.")

    def _restart_driver(self):
        logger.warning("Restarting browser…")
        self._quit_driver()
        human_delay(2, 4)
        self._start_driver()

    # ── Navigation ────────────────────────────────────────────────────────────

    def _load_url(self, url: str, retries: int = 3) -> bool:
        """Navigate to a URL with retries and exponential back-off."""
        for attempt in range(retries):
            try:
                self.driver.get(url)
                human_delay(2.0, 3.5)
                return True
            except TimeoutException:
                logger.warning(
                    "Page load timeout (attempt %d/%d): %s", attempt + 1, retries, url
                )
                if attempt < retries - 1:
                    time.sleep(exponential_backoff(attempt))
                    self._restart_driver()
            except WebDriverException as exc:
                logger.error("WebDriver error loading %s: %s", url, exc)
                if attempt < retries - 1:
                    time.sleep(exponential_backoff(attempt))
                    self._restart_driver()
        return False

    # ── Review panel setup ────────────────────────────────────────────────────

    def _open_reviews_tab(self) -> bool:
        """Click the 'Reviews' tab to open the reviews panel."""
        try:
            wait = WebDriverWait(self.driver, ELEMENT_TIMEOUT)
            tab = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.SEL_REVIEWS_TAB))
            )
            safe_click(self.driver, tab)
            human_delay(1.5, 2.5)
            logger.debug("Reviews tab opened.")
            return True
        except TimeoutException:
            logger.warning("Reviews tab not found within timeout.")
            return False

    def _sort_by_newest(self):
        """
        Attempt to sort reviews by 'Newest' to get a stable ordering.
        Silently skips if the sort button is unavailable.
        """
        try:
            wait = WebDriverWait(self.driver, 8)
            sort_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.SEL_SORT_BUTTON))
            )
            safe_click(self.driver, sort_btn)
            human_delay(0.8, 1.5)

            # Select "Newest" option from the dropdown
            newest = WebDriverWait(self.driver, 6).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//li[@data-index="1"]')
                )
            )
            safe_click(self.driver, newest)
            human_delay(1.5, 2.5)
            logger.debug("Reviews sorted by Newest.")
        except (TimeoutException, NoSuchElementException):
            logger.debug("Sort button not available; using default order.")

    # ── Scrolling ─────────────────────────────────────────────────────────────

    def _get_scroll_panel(self):
        """Return the scrollable reviews panel element, or None."""
        try:
            panels = self.driver.find_elements(By.CSS_SELECTOR, self.SEL_SCROLLABLE)
            # The reviews panel is typically the last matching element
            return panels[-1] if panels else None
        except Exception:
            return None

    def _scroll_panel(self, panel) -> bool:
        """
        Scroll the reviews panel by a random amount to load more reviews.
        Returns True if a scroll was performed.
        """
        try:
            scroll_amount = random.randint(600, 1200)
            self.driver.execute_script(
                "arguments[0].scrollTop += arguments[1];", panel, scroll_amount
            )
            human_delay(SCROLL_DELAY_MIN, SCROLL_DELAY_MAX)
            return True
        except (StaleElementReferenceException, WebDriverException) as exc:
            logger.debug("Scroll failed: %s", exc)
            return False

    # ── Review extraction ─────────────────────────────────────────────────────

    def _expand_review_texts(self):
        """Click all visible 'More' buttons to expand truncated reviews."""
        try:
            more_buttons = self.driver.find_elements(
                By.CSS_SELECTOR, self.SEL_MORE_BUTTON
            )
            for btn in more_buttons:
                try:
                    safe_click(self.driver, btn)
                    human_delay(0.1, 0.3)
                except Exception:
                    pass
        except Exception:
            pass

    def _extract_reviews_from_page(self) -> list[str]:
        """
        Return all review text strings currently rendered in the DOM.
        Expands truncated reviews first.
        """
        self._expand_review_texts()
        texts: list[str] = []
        try:
            cards = self.driver.find_elements(By.CSS_SELECTOR, self.SEL_REVIEW_CARD)
            for card in cards:
                try:
                    text_el = card.find_element(By.CSS_SELECTOR, self.SEL_REVIEW_TEXT)
                    text = text_el.text.strip()
                    if text:
                        texts.append(text)
                except (NoSuchElementException, StaleElementReferenceException):
                    continue
        except Exception as exc:
            logger.debug("Error extracting reviews: %s", exc)
        return texts

    # ── Main scrape loop for one URL ──────────────────────────────────────────

    def _scrape_place(self, url: str) -> int:
        """
        Scrape up to MAX_REVIEWS_PER_PLACE reviews from a single place URL.
        Returns the total number of new reviews saved.
        """
        logger.info("=== Scraping: %s ===", url)

        # Load existing reviews for dedup (crash-resume)
        existing_texts = self.csv_writer.load_existing_texts(url)
        previously_saved = self.progress.get_count(url)
        logger.info(
            "Resuming from %d previously saved reviews (%d in dedup set).",
            previously_saved,
            len(existing_texts),
        )

        if not self._load_url(url):
            logger.error("Failed to load URL, skipping: %s", url)
            return previously_saved

        if not self._open_reviews_tab():
            logger.error("Could not open reviews tab for: %s", url)
            return previously_saved

        self._sort_by_newest()

        collected_texts: set[str] = set(existing_texts)  # all seen texts
        new_batch: list[dict] = []                        # pending CSV writes
        total_new = 0                                     # new reviews this run
        no_progress_streak = 0                            # scroll stall detector

        while (previously_saved + total_new) < MAX_REVIEWS_PER_PLACE:
            panel = self._get_scroll_panel()
            if panel is None:
                logger.warning("Scrollable panel not found; retrying…")
                human_delay(2, 4)
                panel = self._get_scroll_panel()
                if panel is None:
                    logger.error("Panel still missing; aborting this URL.")
                    break

            current_texts = self._extract_reviews_from_page()
            newly_seen = 0

            for text in current_texts:
                if text not in collected_texts:
                    collected_texts.add(text)
                    new_batch.append({"place_url": url, "review_text": text})
                    total_new += 1
                    newly_seen += 1

                    if len(new_batch) >= self.BATCH_SIZE:
                        self.csv_writer.append_reviews(new_batch)
                        self.progress.update_count(url, previously_saved + total_new)
                        logger.info(
                            "Saved batch | Total new this run: %d | Grand total: %d",
                            total_new,
                            previously_saved + total_new,
                        )
                        new_batch = []

                    if (previously_saved + total_new) >= MAX_REVIEWS_PER_PLACE:
                        break

            if newly_seen == 0:
                no_progress_streak += 1
                logger.debug(
                    "No new reviews on this scroll (streak: %d).", no_progress_streak
                )
                if no_progress_streak >= 5:
                    logger.info(
                        "No new reviews after 5 consecutive scrolls — "
                        "assuming all reviews loaded."
                    )
                    break
            else:
                no_progress_streak = 0

            # Scroll to load more
            self._scroll_panel(panel)

        # Flush remaining batch
        if new_batch:
            self.csv_writer.append_reviews(new_batch)
            self.progress.update_count(url, previously_saved + total_new)

        grand_total = previously_saved + total_new
        logger.info(
            "Finished %s | New this run: %d | Grand total: %d",
            url, total_new, grand_total,
        )
        return grand_total

    # ── Public entry point ────────────────────────────────────────────────────

    def run(self, urls: list[str]):
        """
        Iterate over all place URLs, scraping each one.
        Skips URLs already marked complete.  Continues on per-URL errors.
        """
        if not urls:
            logger.error(
                "PLACE_URLS is empty.  Add your Google Maps URLs to the list."
            )
            return

        self._start_driver()

        try:
            for url in urls:
                if self.progress.is_completed(url):
                    logger.info("Skipping (already completed): %s", url)
                    continue

                for attempt in range(3):
                    try:
                        total = self._scrape_place(url)
                        self.progress.mark_completed(url)
                        logger.info(
                            "✓ Completed: %s (%d reviews total)", url, total
                        )
                        break
                    except KeyboardInterrupt:
                        logger.info("Interrupted by user.  Progress saved.")
                        raise
                    except Exception as exc:
                        wait = exponential_backoff(attempt)
                        logger.error(
                            "Unexpected error on attempt %d for %s: %s  "
                            "(retrying in %.1fs)",
                            attempt + 1, url, exc, wait,
                        )
                        time.sleep(wait)
                        self._restart_driver()
                else:
                    logger.error(
                        "All retries exhausted for %s — skipping.", url
                    )

                # Polite inter-place pause
                human_delay(3.0, 6.0)

        except KeyboardInterrupt:
            logger.info("Scraper stopped by user.  All progress has been saved.")
        finally:
            self._quit_driver()

        logger.info("All done!  Results saved to %s", OUTPUT_CSV)


# ─────────────────────────────────────────────────────────────────────────────
# ENTRYPOINT
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if not PLACE_URLS:
        print(
            "\n[ERROR] No URLs configured.\n"
            "Edit the PLACE_URLS list at the top of this script and re-run.\n"
        )
    else:
        scraper = GoogleMapsReviewScraper()
        scraper.run(PLACE_URLS)