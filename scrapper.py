import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.itewiki.fi/yritykset/oulu")
base_url = "https://www.itewiki.fi"
company_urls = set()

# Step 1: Collect all company URLs from all pages
while True:
    time.sleep(2)
    company_links = driver.find_elements(By.CSS_SELECTOR, ".col-md-4.col-sm-6 > a.no_link")
    for a in company_links:
        href = a.get_attribute("href")
        if href:
            company_urls.add(href)

    # Move to next page
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Seuraava")
        next_button.click()
    except:
        break

# Step 2: Visit each company page and extract email addresses
results = []

for url in sorted(company_urls):
    driver.get(url)
    time.sleep(2)

    # Search entire page source for emails using regex
    page_source = driver.page_source
    emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", page_source))

    # Store result
    results.append((url, list(emails)))

# Close the browser
driver.quit()

# Step 3: Print results
for url, email_list in results:
    print(f"{url} -> {', '.join(email_list) if email_list else 'No email found'}")
