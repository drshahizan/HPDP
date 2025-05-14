import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service # Optional: For specifying driver path
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException # Added WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from supabase import create_client, Client
import socket # Import socket for specific error checking

# --- Supabase Configuration ---
SUPABASE_URL = "https://ugjwigpcopmtjgylopwf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVnandpZ3Bjb3BtdGpneWxvcHdmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU4MjgxMjIsImV4cCI6MjA2MTQwNDEyMn0.oFcP1wCt1upByqTU8NgD4FpJUdv9I8sG1ECWMX1wz8I"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

driver = webdriver.Chrome(options=chrome_options)

# --- List of Base URLs ---
base_urls = [
    'https://www.mudah.my/malaysia/cars-for-sale/4-wheels',
    'https://www.mudah.my/malaysia/cars-for-sale/coupe',
    'https://www.mudah.my/malaysia/cars-for-sale/hatchback?price=-40000',
    'https://www.mudah.my/malaysia/cars-for-sale/hatchback?price=40000-',
    'https://www.mudah.my/malaysia/cars-for-sale/mpvs?price=-90000',
    'https://www.mudah.my/malaysia/cars-for-sale/mpvs?price=90000-',
    'https://www.mudah.my/malaysia/cars-for-sale/pick-up',
    'https://www.mudah.my/malaysia/cars-for-sale/sedan?price=-20000',
    'https://www.mudah.my/malaysia/cars-for-sale/price-from-20000-below-30000-sedan',
    'https://www.mudah.my/malaysia/cars-for-sale/sedan?price=30000-60000',
    'https://www.mudah.my/malaysia/cars-for-sale/sedan?price=60000-180000',
    'https://www.mudah.my/malaysia/cars-for-sale/sedan?price=180000-',
    'https://www.mudah.my/malaysia/cars-for-sale/sports',
    'https://www.mudah.my/malaysia/cars-for-sale/suvs?price=-70000',
    'https://www.mudah.my/malaysia/cars-for-sale/suvs?price=70000-210000',
    'https://www.mudah.my/malaysia/cars-for-sale/suvs?price=210000-',
    'https://www.mudah.my/malaysia/cars-for-sale/others'
]
max_pages = 1000
wait_time_per_page = 1.5
max_retries = 3 # Max retries for network operations
retry_delay = 5 # Seconds to wait before retrying

total_items_inserted = 0

print(f"Starting scraping process for {len(base_urls)} base URLs, up to {max_pages} pages each...")

# --- Loop through each base URL ---
for base_url in base_urls:
    print(f"\n--- Starting scrape for base URL: {base_url} ---")
    skip_current_base_url = False # Flag to skip to next base_url on persistent error

    # Determine the starting page number for this base_url
    start_page = 1
    if base_url == 'https://www.mudah.my/malaysia/cars-for-sale/sedan?price=30000-60000':
        start_page = 17
        print(f"Starting from page {start_page} for this specific URL.")

    for page_num in range(start_page, max_pages + 1): 
        if skip_current_base_url:
            break 

        # --- URL Generation ---
        if page_num == 1 and start_page == 1: # Only use base_url directly if starting from page 1
             current_url = base_url
        # elif page_num == start_page and start_page != 1: # If starting from a later page, construct the URL immediately
        #     if '?' in base_url:
        #         current_url = f"{base_url}&o={page_num}"
        #     else:
        #         current_url = f"{base_url}?o={page_num}"
        else: # For all subsequent pages (page > 1 or page > start_page)
            if '?' in base_url:
                current_url = f"{base_url}&o={page_num}"
            else:
                current_url = f"{base_url}?o={page_num}"


        # --- Retry logic for driver.get() ---
        retries = 0
        while retries < max_retries:
            try:
                # Check if it's the very first navigation attempt for a non-page-1 start
                if page_num == start_page and start_page != 1:
                     if '?' in base_url:
                         current_url = f"{base_url}&o={page_num}"
                     else:
                         current_url = f"{base_url}?o={page_num}"

                print(f"Navigating to page {page_num} for {current_url}")
                driver.get(current_url)
                time.sleep(wait_time_per_page)
                break 
            except WebDriverException as e:
                retries += 1
                print(f"Error navigating to {current_url}: {e}")
                if "net::ERR_INTERNET_DISCONNECTED" in str(e) or "net::ERR_CONNECTION_RESET" in str(e):
                    if retries < max_retries:
                        print(f"Internet connection error detected. Retrying in {retry_delay} seconds... (Attempt {retries}/{max_retries})")
                        time.sleep(retry_delay)
                    else:
                        print(f"Max retries reached for navigating to {current_url}. Skipping this base URL.")
                        skip_current_base_url = True # Set flag to skip remaining pages for this base_url
                        break # Exit retry loop
                else:
                    print("Unhandled WebDriverException occurred. Skipping this base URL.")
                    skip_current_base_url = True # Skip on other critical WebDriver errors
                    break # Exit retry loop
            except Exception as e:
                 retries += 1
                 print(f"An unexpected error occurred during navigation: {e}")
                 if retries < max_retries:
                     print(f"Retrying in {retry_delay} seconds... (Attempt {retries}/{max_retries})")
                     time.sleep(retry_delay)
                 else:
                     print(f"Max retries reached for unexpected navigation error. Skipping this base URL.")
                     skip_current_base_url = True
                     break # Exit retry loop

        if skip_current_base_url:
            continue # Go to the next iteration of the page loop (which will then break)

        # --- Error Handling (Keep as is) ---
        while True:
            page_source = driver.page_source
            if "handshake failed" in page_source or "SSL error code" in page_source:
                # ("SSL haprintndshake error detected. Please manually refresh the page in the browser, then press Enter to continue...")
                input()
                driver.get(current_url)
                time.sleep(wait_time_per_page)
            else:
                break

        # print(f"Getting page source for page {page_num}...")
        page_source = driver.page_source

        # --- Check for "No Results Found" text ---
        if "Sorry, No Results Found!" in page_source:
            print(f"Found 'Sorry, No Results Found!' on page {page_num} for {base_url}. Moving to next base URL or stopping scrape.")
            break # Stop scraping for the current base_url

        # print(f"Parsing page source for page {page_num} with BeautifulSoup...")
        soup = BeautifulSoup(page_source, 'html.parser')

        listing_items = soup.find_all('div', attrs={'data-testid': lambda x: x and x.startswith('listing-ad-item-')})

        # print(f"Found {len(listing_items)} potential listing items on page {page_num} for {base_url}.")

        # --- Check if listing_items is empty ---
        if not listing_items:
            print(f"No listing items found on page {page_num} for {base_url} (after checking for 'No Results' text). Continuing to next page.")

        # --- Item Processing Loop (Keep as is, inside the page loop) ---
        for item in listing_items:
            title_element = item.find(class_='flex flex-col flex-1 gap-2 self-center')

            title = None
            price_str = None
            price_int = None
            car_name = None
            condition = None
            mileage = None
            manufactured_year_str = None
            engine_capacity = None 
            location = None
            manufactured_year_int = None

            if title_element:
                title = title_element.text.strip()

                price_element = title_element.find(class_='text-sm text-[#E21E30] font-bold')
                price_str = price_element.text.strip() if price_element else None

                # --- Clean and convert price to integer ---
                if price_str:
                    try:
                        cleaned_price = price_str.replace('RM', '').replace(',', '').strip()
                        price_int = int(cleaned_price)
                    except (ValueError, TypeError):
                        print(f"Warning: Could not convert price '{price_str}' to integer for item: {title}") # Use title if name isn't available yet
                        price_int = None

                # --- Adjust selectors based on what you are scraping ---
                item_name_link = title_element.find('a')
                item_name = item_name_link.text.strip() if item_name_link else title 

                details_container = title_element.find('div', class_='gap-2 grid grid-cols-2 mt-2')

                if details_container:
                    def extract_detail(detail_title):
                        detail_div = details_container.find('div', attrs={'title': detail_title})
                        if detail_div:
                            value_div = detail_div.find('div', class_='text-[11px]')
                            if value_div:
                                return value_div.text.strip()

                        if detail_title == 'Manufactured Year':
                            year_badge_div = details_container.find('div', attrs={'data-testid': 'year-verified-badge'})
                            if year_badge_div:
                                year_text_div = year_badge_div.find('div', class_=lambda x: x and 'text-black' in x and ('text-xs' in x or 'text-[11px]' in x))
                                if year_text_div:
                                    return year_text_div.text.strip()

                        return None


                    condition = extract_detail('Condition')
                    mileage = extract_detail('Mileage')
                    manufactured_year_str = extract_detail('Manufactured Year')
                    engine_capacity = extract_detail('Engine capacity')

            region_span_parent = item.find('span', attrs={'title': 'Region'})
            if region_span_parent:
                img_tag = region_span_parent.find('img')
                if img_tag:
                    location_span = img_tag.find_next_sibling('span')
                    if location_span:
                        location = location_span.text.strip()

            # Attempt to convert year to integer if needed by your Supabase schema
            if manufactured_year_str:
                try:
                    manufactured_year_int = int(manufactured_year_str)
                except (ValueError, TypeError):
                    manufactured_year_int = None # Set to None if conversion fails

            # --- Prepare data for Supabase (Adjust field names if needed) ---
            # Ensure these field names match your Supabase table columns
            item_data = {
                'c_name': item_name,
                'c_price': price_int,
                'c_location': location,
                'c_condition': condition,
                'c_mileage': mileage,
                'c_year': manufactured_year_int,
                'c_engine': engine_capacity
            }

            # --- Insert data into Supabase with Retry ---
            retries = 0
            while retries < max_retries:
                try:
                    data, count = supabase.table('Jiale_cars').insert(item_data).execute()
                    # Check response structure carefully based on actual Supabase client behavior
                    success = False
                    if isinstance(data, tuple) and len(data) > 1 and hasattr(data[1], '__len__') and len(data[1]) > 0: # Check if count is meaningful
                         success = True
                         total_items_inserted += 1
                    elif hasattr(data, 'data') and data.data: 
                         success = True
                         total_items_inserted += 1

                    if success:
                         break # Success, exit retry loop
                    else:
                         print(f"Insertion did not return expected success data for: {item_name}. Response: {data}")
                         break

                except socket.gaierror as e: # Specifically catch DNS errors
                    retries += 1
                    print(f"DNS Error (getaddrinfo failed) inserting data for {item_name}: {e}")
                    if retries < max_retries:
                        print(f"Retrying Supabase insert in {retry_delay} seconds... (Attempt {retries}/{max_retries})")
                        time.sleep(retry_delay)
                    else:
                        print(f"Max retries reached for Supabase insert (DNS error) for {item_name}. Skipping item.")
                        break # Exit retry loop
                except ConnectionError as e: # Catch broader connection errors
                    retries += 1
                    print(f"Connection Error inserting data for {item_name}: {e}")
                    if retries < max_retries:
                        print(f"Retrying Supabase insert in {retry_delay} seconds... (Attempt {retries}/{max_retries})")
                        time.sleep(retry_delay)
                    else:
                        print(f"Max retries reached for Supabase insert (Connection error) for {item_name}. Skipping item.")
                        break # Exit retry loop
                except Exception as e:
                    # Catch other Supabase client errors or unexpected issues
                    print(f"Unexpected error inserting data for {item_name} into Supabase: {e}")
                    break 

    print(f"--- Finished scraping for base URL: {base_url} ---")


print("\nFinished scraping all base URLs. Closing browser...")
driver.quit()

print(f"\nTotal items successfully inserted into Supabase across all URLs: {total_items_inserted}")