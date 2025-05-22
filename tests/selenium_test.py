from selenium import webdriver
import time

driver = webdriver.Firefox()  # Or Chrome if installed
driver.get("http://localhost:5000")

assert "Cat Facts" in driver.title
time.sleep(3)
driver.quit()
