from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://54.165.71.97")
assert "Expected Page Title" in driver.title
driver.quit()
