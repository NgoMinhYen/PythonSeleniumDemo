from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
import time

class DashBroardGroup(BasePage):
    def __int__(self, driver):
      super().__int__(driver)

    ICON_SEARCH = (By.XPATH,"(//span[contains(.,'search')]//parent::button)[2]")
    INPUT_DEVICE = (By.XPATH,"//input[@data-placeholder='Search entities']")
    CURRENT_DEVICE = (By.XPATH,"//table//mat-row/mat-cell")


    def selectDeviceLandingPage(self):
       self.do_click(self.ICON_SEARCH)
       time.sleep(2)
       self.do_sendKeys(self.INPUT_DEVICE,"0203030521054067")
       self.do_click(self.CURRENT_DEVICE)

    def selectDeviceInList(self):
       self.do_click(self.CURRENT_DEVICE)
          

