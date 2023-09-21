import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)
from selenium.webdriver.common.by import By
TIME_OUT = 30

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, byLocator):
        logger.info('get_element')
        return self.driver.find_element(byLocator)
    
    def click(self, byLocator):
        logger.info("Click in locator")
        logger.info(byLocator)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(byLocator)).click()

    def do_click(self, byLocator):
        logger.info(f"Click in locator {byLocator}")
        WebDriverWait(self.driver, TIME_OUT).until(
            EC.visibility_of_element_located(byLocator)).click()

    def getCSSPropertyName(self,byLocator, property_name):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(byLocator)).value_of_css_property(property_name)    

    def click_by_js(self, byLocator):
        logger.info("click_by_js")
        logger.info(byLocator)
        self.execute_script('arguments[0].click();', byLocator)

    def do_sendKeys(self, byLocator, text):
        WebDriverWait(self.driver, TIME_OUT).until(
            EC.visibility_of_element_located(byLocator)).send_keys(text)

    def clear_text(self, byLocator):
        WebDriverWait(self.driver, TIME_OUT).until(
            EC.visibility_of_element_located(byLocator)).clear()

    def get_ElementText(self, byLocator):
        element = WebDriverWait(self.driver, TIME_OUT).until(
            EC.visibility_of_element_located(byLocator))
        return element.text

    def isEnabled(self, byLocator):
        element = WebDriverWait(self.driver, TIME_OUT).until(EC.visibility_of_element_located(byLocator))
        return bool(element)
    
    def getAttribute(self, byLocator, attribute):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(byLocator)).get_attribute(attribute)
    
    #def getAttribute(self, byLocator, attribute):
        #return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(byLocator)).get_attribute(attribute)

    def isEnabled(self, byLocator):
        element = WebDriverWait(self.driver, TIME_OUT).until(EC.visibility_of_element_located(byLocator))
        return bool(element)

    def getTitle(self, title):
        WebDriverWait(self.driver, 1).until(EC.title_is(title))
        return self.driver.title

    def wait_for_element_visible(self, byLocator):
        WebDriverWait(self.driver, TIME_OUT).until(EC.visibility_of_element_located(byLocator))

    def wait_for_element_clickable(self, byLocator):
        WebDriverWait(self.driver, TIME_OUT).until(EC.element_to_be_clickable(byLocator))

    def wait_for_element_present_in_element_attribute(self, byLocator, attr, text):
        logger.info(f"wait_for_element_present_in_element_attribute {attr} {text}")
        WebDriverWait(self.driver, TIME_OUT).until(EC.text_to_be_present_in_element_attribute(byLocator, attr, text))

    def wait_for_loading_complete(self):
        LOADING = (By.XPATH, "//span[text()='Loading...']")
        WebDriverWait(self.driver, TIME_OUT).until(EC.invisibility_of_element(LOADING))

    def wait_for_spinner_invisible(self):
        logger.info("wait_for_spinner_invisible")
        SPINNING = (By.XPATH, "//gridster-item//div[mat-spinner[@role='progressbar']][contains(@style, 'display: none')]")
        WebDriverWait(self.driver, TIME_OUT).until(EC.visibility_of_element_located(SPINNING))
    
    def execute_script(self, script, byLocator):
        logger.info(f"execute_script {script}")
        self.driver.execute_script(script,
                                   WebDriverWait(self.driver, TIME_OUT).until(EC.presence_of_element_located(byLocator)))

    def wait_until_text_box_has_value(self, xpath, value):
        wait = WebDriverWait(self.driver, TIME_OUT)
        # wait.until(self.check_value_locator_contains_value(xpath, value))

    def check_value_locator_contains_value(self, xpath, value):
        logger.info('check_value_locator_contains_value')
        element = self.driver.find_element(By.XPATH, xpath)
        logger.info(element)
        if element is not None:
            text_value = element.get_attribute('value')
            logger.info('text value1')
            logger.info(text_value)
            logger.info('text value2')
            if value in text_value:
                logger.info('value contains')
                return element
            return False
        return False
