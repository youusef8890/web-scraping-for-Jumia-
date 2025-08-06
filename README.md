# web-scraping-for-Jumia-
# 📦 Jumia Mobile Phones Scraper

This Python script scrapes **mobile phone product data** from [Jumia Egypt](https://www.jumia.com.eg/mobile-phones/) and saves it into a CSV file.

---

## 🚀 Features

- Scrapes **multiple pages** of products (configurable).
- Extracts:
  - 🌍 **Website**
  - 🏷 **Brand** 
  - 📄 **Product Name**
  - 💰 **Product Price**
  - ⭐ **Product Rating**
  - 🎯 **Product Discount**
  - 🔗 **Product Link**
- Saves data into a **UTF-8 encoded CSV file**.
- Includes error handling for missing data.

---

## 📂 Output

The script generates a CSV file:

`jumia_products.csv`

| website | brand | product name | product price | product rating | product discount | product link |
|---------|-------|--------------|---------------|----------------|------------------|--------------|
| Jumia   | Samsung | Samsung Galaxy A15 4GB RAM 128GB ROM | EGP 5,999 | No rating found | -15% | https://www.jumia.com.eg/... |

---

## ⚙️ Requirements

Install the required libraries before running:

```bash
pip install requests beautifulsoup4 pandas

