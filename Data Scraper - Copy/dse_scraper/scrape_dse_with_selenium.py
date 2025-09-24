from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time

# Set up the Selenium WebDriver (assuming you have ChromeDriver installed)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (without opening a browser window)
options.add_argument('--disable-extensions')  # Disable unnecessary extensions

# Set the WebDriver timeout
driver = webdriver.Chrome(options=options)

# Open the URL in the browser
url = 'https://www.dsebd.org/day_end_archive.php?startDate=2025-01-01&endDate=2025-07-08&inst=All%20Instrument&archive=data'
driver.get(url)

# Wait for the table to load (adjust the time if needed)
try:
    WebDriverWait(driver, 120).until(  # Increased timeout to 120 seconds
        EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )  # Wait for the table to load
except Exception as e:
    print(f"Error while waiting for the page to load: {e}")
    driver.quit()
    exit()

# Ensure that the page loaded fully before scraping
time.sleep(3)  # Wait for any JavaScript to finish execution, if needed

# Get the page source after JavaScript is executed
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the table by looking for the <table> tag
table = soup.find('table')

if table:
    # Create a CSV file to store the data
    with open('output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Trading Code', 'LTP', 'High', 'Low', 'OpenP', 'CloseP', 'YCP', 'Trade', 'Value', 'Volume'])  # Write the header row

        # Loop through all the rows in the table body
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) == 11:  # Ensure there are exactly 11 columns in the row
                data = [column.text.strip() for column in columns]
                writer.writerow(data)  # Write the row data to the CSV file
else:
    print("Table not found on the page.")

# Close the browser window
driver.quit()

print("Scraping completed and saved to output.csv.")
