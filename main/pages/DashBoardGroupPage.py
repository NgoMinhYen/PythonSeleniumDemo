from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
import time

class DashBroardGroup(BasePage):
    def __int__(self, driver):
      super().__int__(driver)

    ICON_SEARCH = (By.XPATH,"(//span[contains(.,'search')]//parent::button)[2]")
    INPUT_DEVICE = (By.XPATH,"//input[@data-placeholder='Search entities']")
    CURRENT_DEVICE = (By.XPATH,"//table//mat-row/mat-cell")


    def selectDevice(seff):
       seff.do_click(seff.ICON_SEARCH)
       time.sleep(2)
       seff.do_sendKeys(seff.INPUT_DEVICE,"0203030521054067")
       seff.do_click(seff.CURRENT_DEVICE)

