from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:
    def __init__(self, browser='chrome'):
        self.browser = browser.lower()
        self.driver = None

    def create_driver(self, maximize_window=True, detach=True):
        if self.browser == 'chrome':
            chrome_options = ChromeOptions()
            if maximize_window:
                chrome_options.add_argument('--start-maximized')
            if detach:
                chrome_options.add_experimental_option('detach', True)
            self.driver = webdriver.Chrome(options=chrome_options)
        elif self.browser == 'firefox':
            firefox_options = FirefoxOptions()
            if maximize_window:
                firefox_options.add_argument('--start-maximized')
            if detach:
                firefox_options.add_argument('--detach')
            self.driver = webdriver.Firefox(options=firefox_options)
        elif self.browser == 'edge':
            edge_options = EdgeOptions()
            if maximize_window:
                edge_options.add_argument('--start-maximized')
            if detach:
                edge_options.add_argument('--browser.detachUrl')
            self.driver = webdriver.Edge(options=edge_options)
        else:
            raise ValueError(f"Invalid browser: {self.browser}")
        return self.driver
