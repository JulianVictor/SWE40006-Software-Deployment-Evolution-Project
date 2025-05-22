from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configure headless Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://54.165.71.97")
    time.sleep(2)  # wait for JS to load

    assert "Cat Facts" in driver.page_source, "❌ Title not found"
    assert "Get Another Fact" in driver.page_source, "❌ Button not found"
    print("✅ UI Elements loaded successfully")

finally:
    driver.quit()
