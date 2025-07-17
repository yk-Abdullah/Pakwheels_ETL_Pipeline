# run_etl.py
import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Setup headless browser for scraping
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Function to clean and transform scraped data
def clean_data(df):
    def clean_price(x):
        try:
            digits = ''.join(filter(str.isdigit, str(x)))
            return int(digits) if digits else None
        except:
            return None

    def clean_mileage(x):
        try:
            digits = ''.join(filter(str.isdigit, str(x)))
            return int(digits) if digits else None
        except:
            return None

    def clean_engine(x):
        try:
            digits = ''.join(filter(str.isdigit, str(x)))
            return int(digits) if digits else None
        except:
            return None

    df['Price (PKR)'] = df['Price'].apply(clean_price)
    df['Mileage (km)'] = df['Mileage'].apply(clean_mileage)
    df['Engine (cc)'] = df['Engine'].apply(clean_engine)
    df['Year'] = pd.to_numeric(df['Model Year'], errors='coerce')
    df['City'] = df['Location'].str.split(',').str[0].str.strip()
    df.dropna(subset=['Price (PKR)', 'Mileage (km)', 'Engine (cc)', 'Year', 'City'], inplace=True)
    return df

# Scrape listings
all_data = []
for page in range(1, 3):  # First 2 pages for faster refresh
    url = f"https://www.pakwheels.com/used-cars/search/-/?page={page}"
    driver.get(url)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    listings = driver.find_elements(By.CSS_SELECTOR, "li.classified-listing")
    for listing in listings:
        try:
            title = listing.find_element(By.CSS_SELECTOR, "a.car-name").text
            price = listing.find_element(By.CSS_SELECTOR, ".price-details").text
            location = listing.find_element(By.CSS_SELECTOR, "ul.search-vehicle-info li").text
            specs = listing.find_elements(By.CSS_SELECTOR, "ul.search-vehicle-info-2 li")
            year = specs[0].text if len(specs) > 0 else ""
            mileage = specs[1].text if len(specs) > 1 else ""
            engine = specs[3].text if len(specs) > 3 else ""
            url = listing.find_element(By.CSS_SELECTOR, "a.car-name").get_attribute("href")
            img = listing.find_element(By.CSS_SELECTOR, "li.total-pictures-bar-outer img").get_attribute("src")
            all_data.append([title, price, location, mileage, engine, year, url, img])
        except Exception as e:
            print(f"Skipping a listing: {e}")
            continue

driver.quit()

# Save to DataFrame
columns = ["Title", "Price", "Location", "Mileage", "Engine", "Model Year", "Listing URL", "Image URL"]
df = pd.DataFrame(all_data, columns=columns)
df = clean_data(df)
df.to_csv("cleaned_pakwheels_listings.csv", index=False)

print(f"[✓] Scraped {len(df)} cleaned listings.")
