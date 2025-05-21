from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://34.203.249.140")
assert "Expected Page Title" in driver.title
driver.quit()
