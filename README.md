# web-scraping-for-Jumia-
# 📦 Jumia Phones & Tablets Scraper

This Python script scrapes **phones & tablets** product data from [Jumia Egypt](https://www.jumia.com.eg/phones-tablets/) and saves it into a CSV file.

---

## 🚀 Features

- Scrapes **multiple pages** of products (configurable).
- Extracts:
  - 🏷 **Product Name**
  - 💰 **Price**
  - ⭐ **Rating**
  - 🎯 **Discount**
  - 🔗 **Product Link**
- Saves data into a **UTF-8 encoded CSV file**.
- Includes error handling for missing data.

---

## 📂 Output

The script generates a CSV file:

`jumia_products.csv`

| website | name          | price     | rating          | discount    | link |
|---------|--------------|-----------|----------------|-------------|------|
| Jumia   | Product Name | EGP 5,999 | No rating found | -15%        | https://... |

---

## ⚙️ Requirements

Install the required libraries before running:

```bash
pip install requests beautifulsoup4 pandas
