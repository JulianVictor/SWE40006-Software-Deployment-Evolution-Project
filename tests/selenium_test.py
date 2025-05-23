from selenium import webdriver
import time

# Create a new browser session (auto-detects driver with Selenium 4.6+)
driver = webdriver.Firefox()

# Go to your deployed app
driver.get("http://44.220.158.67:5000")

# Give it some time to load (adjust if needed)
time.sleep(2)

# Check the page title contains expected text
assert "Cat Facts" in driver.title

# Close the browser
driver.quit()
