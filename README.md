# amazon-webscraper
Amazon Best Sellers Scraper

This project is a Python-based web scraper that uses Selenium to extract information from Amazon's "Best Sellers" section. It logs in using valid credentials and collects details of products with discounts greater than 50% in the top 10 categories, limited to the top 1500 best-selling products per category.

Features

Authentication: Automates login to Amazon using valid credentials.

Data Collection: Scrapes product details from the top 10 categories, focusing on items with significant discounts.

Data Points Extracted:

Product Name

Product Price

Sale Discount

Best Seller Rating

Ship From

Sold By

Product Description

Number Bought in the Past Month (if available)

Category Name

All Available Images

Data Storage: Stores the extracted data in structured formats (CSV or JSON).

Error Handling: Robust exception handling for seamless scraping.

Compliance: Ensures adherence to Amazon’s terms of service.

Requirements

Python Packages:

selenium

python-dotenv

Other Dependencies:

Chrome browser

ChromeDriver (compatible with your Chrome version)

Setup:

Clone this repository:

git clone <repository-url>

Install the required Python packages:

pip install -r requirements.txt

Ensure you have a valid .env file with the following structure:

AMAZON_EMAIL=your_email@example.com
AMAZON_PASSWORD=your_password

Usage

1. Run the Script

Execute the script with:

python main.py

2. Output

The scraped data will be saved in either output.json or output.csv in the project directory.

Important Notes

CAPTCHA Handling:

The script does not handle CAPTCHA challenges.

If a CAPTCHA appears, manually resolve it and rerun the script.

Compliance:

This project is intended for educational purposes.

Ensure compliance with Amazon's terms of service when using the scraper.

Browser Compatibility:

Verify that your ChromeDriver matches your installed Chrome browser version.

Update both Chrome and ChromeDriver if necessary.

Troubleshooting

Common Errors:

NoSuchElementException:

Ensure that the webpage structure matches the element locators in the script.

Update the locators by inspecting the Amazon page source.

Invalid Session ID:

Restart the script and ensure no other browser instances are open.

Page Load Issues:

Check your internet connection.

Increase wait times in the script using WebDriverWait.

Future Improvements

Add CAPTCHA-solving integration.

Implement proxy rotation to avoid detection.

Enhance scraping for dynamically loaded content
