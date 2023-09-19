from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from core.helper.gsx_logger import Logger
from core.helper.locator_parser import LocatorParser
    
class Waiter:
    @staticmethod
    def wait_for_element_text_displayed(driver, locator_string, text, timeout):
        Logger.info("Waiting for element text displayed " + locator_string)
        locator = LocatorParser.parse_string_to_locator(locator_string)
        print(locator[0] + " >> "+ locator[1])
        if locator is not None:
            try:
                WebDriverWait(driver, timeout).until(
                    expected_conditions.text_to_be_present_in_element( (locator[0], locator[1]), text))
                Logger.info("Waiting completed.")
            except:
                return False
    
    @staticmethod
    def wait_for_element_to_be_clickable(driver, locator_string, timeout):
        Logger.info("Waiting for element to be clickable " + locator_string)
        locator = LocatorParser.parse_string_to_locator(locator_string)
        print(locator[0] + " >> "+ locator[1])
        if locator is not None:
            WebDriverWait(driver, timeout).until(
                expected_conditions.element_to_be_clickable( (locator[0], locator[1])))
            Logger.info("Waiting completed.")
            
    @staticmethod
    def wait_for_element_visibility(driver, locator_string, timeout):
        Logger.info("Waiting for element to be visible " + locator_string)
        locator = LocatorParser.parse_string_to_locator(locator_string)
        print(locator[0] + " >> "+ locator[1])
        if locator is not None:
            WebDriverWait(driver, timeout).until(
                expected_conditions.visibility_of_element_located( (locator[0], locator[1])))
            Logger.info("Waiting completed.")