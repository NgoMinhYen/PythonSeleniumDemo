from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

class HomePage(BasePage):
    def __int__(self, driver):
      super().__int__(driver)

    DASHBOARD_GROUP = (By.XPATH,"//li[contains(.,'Dashboard groups')]")
    DC400 = (By.XPATH, "//a[contains(.,'DC400')]")
    FMS_DASHBOARD = (By.XPATH,"//span[contains(.,'DC400 FMS Dashboard')]//parent::mat-cell//following-sibling::mat-cell//span")
    ICON_SEARCH = (By.XPATH,"(//span[contains(.,'search')]//parent::button)[2]")

    def select_DC400(self):
       self.do_click(self.DASHBOARD_GROUP)
       self.do_click(self.DC400)
       self.do_click(self.FMS_DASHBOARD)

