from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def test_cat_facts_ui():
    driver = webdriver.Chrome(options=options)
    driver.get("http://54.91.115.194:5000")

    assert "Cat Facts" in driver.title

    fact = driver.find_element("id", "fact-box").text
    assert len(fact) > 0

    driver.quit()
