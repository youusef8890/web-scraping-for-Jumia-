import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

products_details = []

def jumia_scraper(base_url, max_pages=5, delay=2):
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Scraping page {page}...")

        try:
            pages = requests.get(url, timeout=10)
            soup = BeautifulSoup(pages.text, 'html.parser')
            products_list = soup.find_all('article', {'class': 'prd'})
            
            if not products_list:
                print("No more products found. Stopping.")
                break

            for product in products_list:
                try:
                    name = product.find('h3', {'class': 'name'}).text.strip()
                except:
                    name = "No name found"

                try:
                    price = product.find('div', {'class': 'prc'}).text.strip()
                except:
                    price = "No price found"

                try:
                    rating = product.find('div', {'class': 'stars'}).text
                except:
                    rating = "No rating found"

                try:
                    discount = product.find('div', {'class': 'bdg'}).text.strip()
                except:
                    discount = "No discount found"

                try:
                    link = f"https://www.jumia.com.eg{product.find('a', {'class': 'core'}).get('href')}"
                except:
                    link = "No link found"

                products_details.append({
                    'website': 'Jumia',
                    'name': name,
                    'price': price,
                    'rating': rating,
                    'discount': discount,
                    'link': link
                })

            time.sleep(delay)  

        except Exception as e:
            print(f"Oops, something went wrong on page {page}: {e}")
            break

jumia_scraper("https://www.jumia.com.eg/phones-tablets/", max_pages=20)

df = pd.DataFrame(products_details)
df.to_csv("jumia_products.csv", index=False, encoding="utf-8-sig")

print(f"Scraping complete! {len(products_details)} products saved to jumia_products.csv")
