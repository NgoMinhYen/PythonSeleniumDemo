import logging
from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
from time import sleep
logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    def __int__(self, driver):
      super().__int__(driver)

    EMAIL = (By.ID, "username-input")
    PASSWORD = (By.ID, "password-input")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")



    def getLoginPageTitle(self, title):
        return self.getTitle(title)

    def doLoginPage(self, userName, password):
        logger.info("doLoginPage")
        #self.wait_for_element_visible(self.EMAIL)
        self.do_sendKeys(self.EMAIL, userName)
        self.do_sendKeys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)