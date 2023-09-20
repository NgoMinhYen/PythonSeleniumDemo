import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logger = logging.getLogger(__name__)
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, byLocator):
        logger.info("Click in locator")
        logger.info(byLocator)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(byLocator)).click()

    def do_sendKeys(self, byLocator, text):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(byLocator)).send_keys(text)

    def get_ElementText(self, byLocator):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(byLocator))
        return element.text

    def isEnabled(self, byLocator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(byLocator))
        return bool(element)
        
    def getAttribute(self,byLocator, attribute):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(byLocator)).get_attribute(attribute)
                      
    def isEnabled(self, byLocator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(byLocator))
        return bool(element)

    def getTitle(self, title):
        WebDriverWait(self.driver, 1).until(EC.title_is(title))
        return self.driver.title
    
    def wait_for_element_visible(self, byLocator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(byLocator))

    def wait_for_element_clickable(self, byLocator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(byLocator))


    def wait_for_loading_complete(self):
        LOADING = (By.XPATH, "//span[text()='Loading...']")
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element(LOADING))