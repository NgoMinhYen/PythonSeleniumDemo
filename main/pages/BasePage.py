from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
        def __init__(self, driver):
          self.driver = driver

        def do_click(self, byLocator):
          WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator)).click()

        def do_sendKeys(self, byLocator, text):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator)).send_keys(text)

        def get_ElementText(self, byLocator):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator))
            return element.text

        def isEnabled(self, byLocator):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator))
            return bool(element)

        def getTitle(self, title):
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
            return self.driver.title  