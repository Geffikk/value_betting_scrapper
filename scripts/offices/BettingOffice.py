from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


class BettingOffice:
    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(url)

    def get_live_score_page(self):
        self.browser.get(self.url)

    def close_browser(self):
        self.browser.close()
