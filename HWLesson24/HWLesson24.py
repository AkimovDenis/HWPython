# Задание №1 
# а) Получить курс валют с динамического сайта, используя selenium. 

print("\n====== Task1 A ======")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def fetch_currency_rates_from_xrates():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.x-rates.com/table/?from=USD&amount=1")

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ratesTable tbody tr"))
        )
        rows = driver.find_elements(By.CSS_SELECTOR, ".ratesTable tbody tr")

        print("Курсы валют относительно USD:")
        for row in rows:
            currency_name = row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
            exchange_rate = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text        
            print(f"{currency_name}: {exchange_rate}")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()

fetch_currency_rates_from_xrates()

# б) Получить все цены с динамического сайта маркетплейса, используя 
# selenium

print("\n====== Task1 B ======")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def fetch_goods_from_olx():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.olx.kz/elektronika/igry-i-igrovye-pristavki/?utm_source=olx&utm_medium=own&utm_campaign=december_promo")

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-l9drzq"))
        )
        
        goods_elements = driver.find_elements(By.CLASS_NAME, "css-l9drzq")

        print("Наименования товаров/работ/услуг:")

        for goods in goods_elements:
            try:

                goods_name = goods.find_element(By.CLASS_NAME, "css-1s3qyje").text
                goods_price = goods.find_element(By.CLASS_NAME, "css-13afqrm").text

                print(f"Наименование: {goods_name}, Цена: {goods_price}")

            except Exception as e:
                print(f"Ошибка при извлечении наименования товара: {e}")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()

fetch_goods_from_olx()
