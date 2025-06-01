# test_playwright.py
from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        print("Title:", page.title())
        assert "Example Domain" in page.title()
        browser.close()

if __name__ == "__main__":
    test_example()
