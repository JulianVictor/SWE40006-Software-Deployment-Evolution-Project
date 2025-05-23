from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://54.226.89.1")
assert "Expected Page Title" in driver.title
driver.quit()
