"""
Scraper for carlist.my — Playwright-only (no BeautifulSoup)
Output: carlist_100k_pw.csv

Run full:  python carlist_scraper_pw.py
Run test:  python carlist_scraper_pw.py --test   (scrapes ~50 records)
"""

import asyncio
import csv
import json
import re
import sys
import time
from pathlib import Path

from playwright.async_api import async_playwright, Browser

BASE_URL   = "https://www.carlist.my"
LIST_URL   = f"{BASE_URL}/cars-for-sale/malaysia"
OUTPUT_CSV = Path(__file__).parent / "carlist_100k_pw.csv"
STATE_FILE = Path(__file__).parent / "carlist_pw_state.json"

TARGET      = 100_000
CONCURRENCY = 4
PAGE_DELAY  = 1.5
MAX_RETRIES = 3
PAGE_SIZE   = 25

CSV_FIELDS = [
    "id", "title", "year", "price", "monthly_payment",
    "mileage", "transmission", "seller_type",
    "location", "condition", "url",
]

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

INIT_SCRIPT = "Object.defineProperty(navigator,'webdriver',{get:()=>undefined})"


# ── Page extraction using Playwright evaluate only ────────────────────────────

async def extract_page_pw(page) -> list[dict]:
    """Extract all listing cards via a single JS evaluate — no BeautifulSoup."""
    return await page.evaluate(r'''(baseUrl) => {
        const articles = document.querySelectorAll('article[class~="listing"]');
        const results  = [];
        const seen     = new Set();

        function getSpecByIcon(container, iconClass) {
            if (!container) return "";
            const icon = container.querySelector('i[class*="' + iconClass + '"]');
            if (!icon) return "";
            const parent = icon.parentElement;
            if (!parent) return "";
            const clone = parent.cloneNode(true);
            clone.querySelectorAll("i").forEach(i => i.remove());
            return clone.textContent.replace(/\s+/g, " ").trim();
        }

        for (const art of articles) {
            const link = art.querySelector(
                'a[href*="/used-cars/"], a[href*="/new-cars/"], a[href*="/recon-cars/"]'
            );
            if (!link) continue;

            let href = link.getAttribute("href") || "";
            if (!href.startsWith("http")) href = baseUrl + href;

            const parts    = href.split("/");
            const lastPart = parts[parts.length - 1];
            if (!/^\d+$/.test(lastPart)) continue;
            const id = lastPart;
            if (seen.has(id)) continue;
            seen.add(id);

            let condition = "";
            if (href.includes("/used-cars/"))  condition = "USED";
            else if (href.includes("/new-cars/"))   condition = "NEW";
            else if (href.includes("/recon-cars/")) condition = "RECON";

            const titleEl = art.querySelector('[class*="listing__title"]');
            const title   = titleEl ? titleEl.innerText.trim() : "";
            const yearMatch = title.match(/^\d{4}/);
            const year    = yearMatch ? yearMatch[0] : "";

            const priceEl = art.querySelector('[class*="listing__price"]');
            const price   = priceEl ? priceEl.innerText.trim() : "";

            let monthly = "";
            const walker = document.createTreeWalker(art, NodeFilter.SHOW_TEXT);
            let node;
            while ((node = walker.nextNode())) {
                if (node.textContent.toLowerCase().includes("/ month")) {
                    monthly = node.textContent.trim();
                    break;
                }
            }

            const specsEl    = art.querySelector('[class*="listing__specs"]');
            const mileage      = getSpecByIcon(specsEl, "icon--meter");
            const transmission = getSpecByIcon(specsEl, "icon--transmission");
            const seller_type  = getSpecByIcon(specsEl, "icon--user-formal");
            const location     = getSpecByIcon(specsEl, "icon--location");

            results.push({
                id, title, year, price,
                monthly_payment: monthly,
                mileage, transmission, seller_type,
                location, condition, url: href,
            });
        }

        return results;
    }''', BASE_URL)


# ── Per-page scraper ───────────────────────────────────────────────────────────

async def scrape_page(
    browser: Browser,
    page_num: int,
    semaphore: asyncio.Semaphore,
) -> list[dict]:
    async with semaphore:
        for attempt in range(1, MAX_RETRIES + 1):
            ctx = await browser.new_context(
                user_agent=USER_AGENT,
                viewport={"width": 1280, "height": 900},
            )
            pg = await ctx.new_page()
            await pg.add_init_script(INIT_SCRIPT)
            await pg.route("**/*.{woff,woff2,ttf,eot,svg,gif}", lambda r: r.abort())
            await pg.route(
                re.compile(r'(google-analytics|doubleclick|googlesyndication|facebook|tiktok)', re.I),
                lambda r: r.abort(),
            )
            try:
                url  = f"{LIST_URL}?page_number={page_num}&page_size={PAGE_SIZE}"
                resp = await pg.goto(url, timeout=60_000, wait_until="domcontentloaded")
                if resp and resp.status in (403, 429):
                    raise RuntimeError(f"HTTP {resp.status} on page {page_num}")
                await asyncio.sleep(PAGE_DELAY)
                rows = await extract_page_pw(pg)
                return rows
            except Exception as exc:
                print(f"  page {page_num} attempt {attempt} failed: {exc}", file=sys.stderr)
                if attempt < MAX_RETRIES:
                    await asyncio.sleep(3 * attempt)
            finally:
                await ctx.close()
    return []


# ── Discover total pages ───────────────────────────────────────────────────────

async def get_total_pages(browser: Browser) -> int:
    ctx = await browser.new_context(
        user_agent=USER_AGENT, viewport={"width": 1280, "height": 900}
    )
    pg = await ctx.new_page()
    await pg.add_init_script(INIT_SCRIPT)
    await pg.route("**/*.{woff,woff2,ttf,eot,svg,gif}", lambda r: r.abort())
    try:
        await pg.goto(LIST_URL, timeout=60_000, wait_until="domcontentloaded")
        await asyncio.sleep(4)
        nums = await pg.evaluate(r'''() => {
            const pag = document.querySelector('[class*="pagination"]');
            if (!pag) return [];
            return Array.from(pag.querySelectorAll('a[href*="page_number="]'))
                .map(a => {
                    const m = a.href.match(/page_number=(\d+)/);
                    return m ? parseInt(m[1]) : 0;
                })
                .filter(n => n > 0);
        }''')
        return max(nums) if nums else 1
    except Exception as e:
        print(f"  Could not get total pages: {e}", file=sys.stderr)
        return 7142
    finally:
        await ctx.close()


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_existing_ids(path: Path) -> tuple[set[str], int]:
    seen: set[str] = set()
    if not path.exists():
        return seen, 0
    with path.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            seen.add(row["id"])
    return seen, len(seen)


def load_state() -> int:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())["last_page"]
        except Exception:
            pass
    return 0


def save_state(last_page: int) -> None:
    STATE_FILE.write_text(json.dumps({"last_page": last_page}))


# ── Main ──────────────────────────────────────────────────────────────────────

async def main(target: int = TARGET) -> None:
    global_seen, already = load_existing_ids(OUTPUT_CSV)
    total_written = [already]
    write_lock    = asyncio.Lock()
    stop_flag     = asyncio.Event()

    if already:
        print(f"Resuming: {already:,} entries already in {OUTPUT_CSV.name}")

    if total_written[0] >= target:
        print(f"Target of {target:,} already met — nothing to do.")
        return

    print(f"Target: {target:,} | Have: {total_written[0]:,} | Need: {target - total_written[0]:,}")

    t0        = time.time()
    file_mode = "a" if OUTPUT_CSV.exists() and already > 0 else "w"

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"],
        )

        print("\nDiscovering total pages...")
        total_pages = await get_total_pages(browser)
        last_page   = load_state()
        start_page  = max(1, last_page - 2) if last_page else 1
        extra_pages = (target - total_written[0] + PAGE_SIZE - 1) // PAGE_SIZE + 100
        end_page    = min(total_pages, start_page + extra_pages)
        print(f"Total pages on site: {total_pages:,} | Resuming from page: {start_page:,} to {end_page:,}")

        sem        = asyncio.Semaphore(CONCURRENCY)
        pages_done = [0]

        async def process(pg_num: int) -> None:
            if stop_flag.is_set():
                return
            rows = await scrape_page(browser, pg_num, sem)
            pages_done[0] += 1

            new = [r for r in rows if r["id"] not in global_seen]
            if new:
                async with write_lock:
                    if stop_flag.is_set():
                        return
                    new2 = [r for r in new if r["id"] not in global_seen]
                    for r in new2:
                        global_seen.add(r["id"])
                    writer.writerows(new2)
                    total_written[0] += len(new2)
                    if total_written[0] >= target:
                        stop_flag.set()

            done = pages_done[0]
            if done % 10 == 0 or stop_flag.is_set():
                elapsed = time.time() - t0
                rate    = total_written[0] / elapsed * 60 if elapsed else 0
                eta_min = (target - total_written[0]) / rate if rate else 0
                print(
                    f"  page {done} | "
                    f"{total_written[0]:,}/{target:,} entries | "
                    f"{rate:.0f}/min | ETA {eta_min:.0f} min"
                )

        with OUTPUT_CSV.open(file_mode, newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            if file_mode == "w":
                writer.writeheader()

            BATCH = 200
            for batch_start in range(start_page, end_page + 1, BATCH):
                if stop_flag.is_set():
                    break
                batch_end = min(batch_start + BATCH, end_page + 1)
                tasks = [asyncio.create_task(process(p))
                         for p in range(batch_start, batch_end)]
                await asyncio.gather(*tasks)
                f.flush()
                save_state(batch_end - 1)
                if stop_flag.is_set():
                    break

        await browser.close()

    elapsed = time.time() - t0
    print(f"\n{'='*60}")
    print(f"Done!  {total_written[0]:,} total entries in {OUTPUT_CSV.name}")
    print(f"Elapsed: {elapsed/60:.1f} min")


if __name__ == "__main__":
    test_mode = "--test" in sys.argv
    asyncio.run(main(target=50 if test_mode else TARGET))
