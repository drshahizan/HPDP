from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import random

class ScrapeLazada():

    def Scrape(self, urls):

        options = webdriver.ChromeOptions()
        options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36")
        
        driver = webdriver.Chrome(options=options)
        products=[]

        for url in urls:
            driver.get(url)

            # Wait for page to load
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#root")))
            time.sleep(random.uniform(2.5, 4.5))

            # Get total number of pages
            soup = BeautifulSoup(driver.page_source, "html.parser")
            pagination = soup.select(".ant-pagination-item")
            total_pages = int(pagination[-1].text) if pagination else 1
            print(f"Scraping {total_pages} pages from: {url}")

            for page in range(total_pages):
                print(f"Scraping page {page+1} of {total_pages}")
                try:
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.ID, "captcha"))  # Adjust if Lazada uses different selector
                    )
                    input("⚠️ CAPTCHA detected. Please solve it manually in the browser, then press Enter to continue...")
                except:
                    pass

                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#root")))
                # time.sleep(random.uniform(2.5, 4.5))

                # driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

                soup = BeautifulSoup(driver.page_source, "html.parser")
                
                for item in soup.findAll('div', class_='Bm3ON'):
                    product_name = item.find('div', class_='RfADt').text
                    price = float(item.find('span', class_='ooOxS').text.replace('RM', '').replace(',', ''))
                    location = item.find('span', class_='oa6ri').text
                    numbersold = item.find('span', class_='_1cEkb')
                    numbersold = numbersold.text.strip() if numbersold else 'N/A'
                    reviews = item.find('span', class_='qzqFw')
                    reviews = reviews.text.strip() if reviews else 'N/A'
                    
                    products.append((product_name, price, location, numbersold, reviews))

                # Click next page button
                try:
                    next_button = driver.find_element(By.CSS_SELECTOR, ".ant-pagination-next > button")
                    time.sleep(random.uniform(3, 5))  # Simulate reading delay
                    next_button.click()
                except:
                    print("Next button not found or last page reached.")
                    break

        df = pd.DataFrame(products, columns=['Product Name', 'Price', 'Location', 'Quantity Sold', 'Total Reviews'])

        df.to_excel("Lazada (Stationery).xlsx", index=False)
        print("Data saved in local disk")


        driver.close()


urls = [
    'https://www.lazada.com.my/catalog/?q=Women%27s%20Fashion&price=0-25',
    'https://www.lazada.com.my/catalog/?q=Women%27s%20Fashion&price=25-40',
    'https://www.lazada.com.my/catalog/?q=Women%27s%20Fashion&price=40-84',
    'https://www.lazada.com.my/catalog/?q=Women%27s%20Fashion&price=84-',
    'https://www.lazada.com.my/catalog/?q=Beauty%20Skincare&price=0-7',
    'https://www.lazada.com.my/catalog/?q=Beauty%20Skincare&price=7-12',
    'https://www.lazada.com.my/catalog/?q=Beauty%20Skincare&price=12-16',
    'https://www.lazada.com.my/catalog/?q=Beauty%20Skincare&price=16-22',
    'https://www.lazada.com.my/catalog/?q=Beauty%20Skincare&price=22-31',
    'https://www.lazada.com.my/catalog/?q=Beauty%20Skincare&price=31-47',
    'https://www.lazada.com.my/catalog/?q=Beauty%20Skincare&price=47-78',
    'https://www.lazada.com.my/catalog/?q=Beauty%20Skincare&price=78-191',
    'https://www.lazada.com.my/catalog/?q=Beauty%20Skincare&price=191-',
    'https://www.lazada.com.my/catalog/?q=Health%20Wellness&price=0-15',
    'https://www.lazada.com.my/catalog/?q=Health%20Wellness&price=15-31',
    'https://www.lazada.com.my/catalog/?q=Health%20Wellness&price=31-53',
    'https://www.lazada.com.my/catalog/?q=Health%20Wellness&price=53-81',
    'https://www.lazada.com.my/catalog/?q=Health%20Wellness&price=81-124',
    'https://www.lazada.com.my/catalog/?q=Health%20Wellness&price=124-219',
    'https://www.lazada.com.my/catalog/?q=Health%20Wellness&price=219-',
    'https://www.lazada.com.my/catalog/?q=Home%20Living&price=0-16',
    'https://www.lazada.com.my/catalog/?q=Home%20Living&price=16-40',
    'https://www.lazada.com.my/catalog/?q=Home%20Living&price=40-135',
    'https://www.lazada.com.my/catalog/?q=Home%20Living&price=135-',
    'https://www.lazada.com.my/catalog/?q=Home%20Appliances&price=0-46',
    'https://www.lazada.com.my/catalog/?q=Home%20Appliances&price=46-109',
    'https://www.lazada.com.my/catalog/?q=Home%20Appliances&price=109-380',
    'https://www.lazada.com.my/catalog/?q=Home%20Appliances&price=380-',
    'https://www.lazada.com.my/catalog/?q=Mother%20Baby',
    'https://www.lazada.com.my/catalog/?q=Stationery&price=0-1',
    'https://www.lazada.com.my/catalog/?q=Stationery&price=1-3',
    'https://www.lazada.com.my/catalog/?q=Stationery&price=3-5',
    'https://www.lazada.com.my/catalog/?q=Stationery&price=5-8',
    'https://www.lazada.com.my/catalog/?q=Stationery&price=8-13',
    'https://www.lazada.com.my/catalog/?q=Stationery&price=13-26',
    'https://www.lazada.com.my/catalog/?q=Stationery&price=26-'
]

sl = ScrapeLazada()
sl.Scrape(urls)
