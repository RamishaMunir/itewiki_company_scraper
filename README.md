# itewiki_company_scraper

A Python-based web scraper using Selenium that extracts company profile links and email addresses from [itewiki.fi](https://www.itewiki.fi/yritykset/oulu), specifically for IT and software companies in Oulu, Finland.

## 🔧 Features

- Navigates through all paginated results
- Extracts:
  - Company profile URLs
  - Email addresses from each company page
- Supports saving and extending for CSV/JSON export

## 🚀 Requirements

- Python 3.x
- Google Chrome
- [ChromeDriver](https://chromedriver.chromium.org/) (automatically managed via `webdriver-manager`)

## 📦 Installation

```bash
pip install -r requirements.txt
```

## Required packages:

selenium
webdriver-manager

## 🧪 Usage
python scraper.py

The script will:

1. Visit each page on the search results.
2. Collect company links.
3. Visit each company profile and extract visible email addresses.

## 📁 Output

Each result is printed in this format:

https://www.itewiki.fi/digia -> info@digia.fi

https://www.itewiki.fi/innofactor -> contact@innofactor.com


## 🙋‍♀️ Author

Ramisha Munir
