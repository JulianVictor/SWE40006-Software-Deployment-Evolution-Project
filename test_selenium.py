from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

options = Options()
options.add_argument('--headless')  # Run Chrome without GUI
options.add_argument('--no-sandbox')  # Required for some Linux environments like Docker or Jenkins
options.add_argument('--disable-dev-shm-usage')  # Use /tmp instead of /dev/shm to avoid limited space errors

try:
    driver = webdriver.Chrome(options=options)
    driver.get("https://example.com")
    print("Title:", driver.title)
finally:
    driver.quit()
