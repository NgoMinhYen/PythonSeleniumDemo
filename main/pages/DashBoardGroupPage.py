from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
import time

class DashBroardGroup(BasePage):
    def __int__(self, driver):
      super().__int__(driver)

    ICON_SEARCH = (By.XPATH,"//div[@fxlayoutalign='start center']//mat-icon[.='search']")
    INPUT_DEVICE = (By.XPATH,"//input[@data-placeholder='Search entities']")
    CURRENT_DEVICE = (By.XPATH,"//table//mat-row/mat-cell")
    ICON_CONFIGURATION = (By.XPATH,"//div[@fxlayoutalign='end']//mat-icon[.='settings']")
    BUTTON_ZOOM_OUT = (By.XPATH,"//a[@title='Zoom out']")
    INTRERNAL_LED_ENABLE = (By.XPATH,"//mat-label[contains(.,'Internal LED Enable')]")
    ABC = (By.XPATH,"//div[@class='leaflet-proxy leaflet-zoom-animated']")
    

    def selectDeviceLandingPage(self):
       self.do_click(self.ICON_SEARCH)
       time.sleep(2)
       self.do_sendKeys(self.INPUT_DEVICE,"0203030521054067")
      

    def selectDeviceInList(self):
       time.sleep(10)
       self.do_click(self.CURRENT_DEVICE)

    def clickZoomOutButton(self):
       print("attribute: " + self.getAttribute(self.ABC,"style"))
       self.do_click(self.BUTTON_ZOOM_OUT)

    def clickConfiguration(self):
       self.do_click(self.ICON_CONFIGURATION)      
          
    def selectIntrernalLedEnable(self):
       time.sleep(10)
       self.do_click(self.INTRERNAL_LED_ENABLE)      

