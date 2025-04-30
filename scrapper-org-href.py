from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.itewiki.fi/yritykset/oulu")

wait = WebDriverWait(driver, 10)
base_url = "https://www.itewiki.fi"
hrefs = set()

while True:
    # Wait until company blocks are loaded
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "search_result")))

    # Find all <a> elements with class 'no_link' inside company blocks
    a_tags = driver.find_elements(By.CSS_SELECTOR, ".col-md-4.col-sm-6 > a.no_link")
    for a in a_tags:
        href = a.get_attribute("href")
        if href:
            hrefs.add(href)

    # Try to go to the next page
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Seuraava")
        next_button.click()
        time.sleep(2)
    except:
        break

# Print collected URLs
for url in sorted(hrefs):
    print(url)

driver.quit()
