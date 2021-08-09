from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser: WebDriver = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)