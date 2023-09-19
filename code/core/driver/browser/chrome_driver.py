from core.driver.base_driver import BaseDriver
from selenium import webdriver

class ChromeDriver(BaseDriver):
    def create_driver(self, config, alias=None):
        chrome = webdriver.Chrome()
        # for argument in config.arguments:
        #     chrome.add_argument(argument)

  