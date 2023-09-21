from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
import time
import logging
logger = logging.getLogger(__name__)

class DashBroardGroup(BasePage):
    def __int__(self, driver):
      super().__int__(driver)

    ICON_SEARCH = (By.XPATH,"//div[@fxlayoutalign='start center']//mat-icon[.='search']")
    INPUT_DEVICE = (By.XPATH,"//input[@data-placeholder='Search entities']")
    CURRENT_DEVICE = (By.XPATH,"//table//mat-row/mat-cell")
    ICON_CONFIGURATION = (By.XPATH,"//div[@fxlayoutalign='end']//mat-icon[.='settings']")
    BUTTON_ZOOM_OUT = (By.XPATH,"//a[@title='Zoom out']")
    BUTTON_ZOOM_IN = (By.XPATH,"//a[@title='Zoom in']")
    INTRERNAL_LED_ENABLE = (By.XPATH,"//mat-form-field[contains(.,'Internal LED Enable')]")
    ABC = (By.XPATH,"//div[@class='leaflet-proxy leaflet-zoom-animated']")
    OPTION_FALSE = (By.XPATH,"//span[@class='mat-option-text' and contains(.,'False')]")
    OPTION_TRUE = (By.XPATH,"//span[@class='mat-option-text' and contains(.,'True')]")
    VALUE = (By.XPATH,"//mat-form-field[contains(.,'Internal LED Enable')]//span[contains(@class,'mat-select-value-text')]")

    SAVE_BUTTON = (By.XPATH,"//button[contains(.,'Save')]")
    

    def selectDeviceLandingPage(self):
       self.do_click(self.ICON_SEARCH)
       #time.sleep(2)
       self.do_sendKeys(self.INPUT_DEVICE,"0203030521054067")
      

    def selectDeviceInList(self):
       self.wait_for_element_clickable(self.CURRENT_DEVICE)
       #time.sleep(10)
       self.do_click(self.CURRENT_DEVICE)
       #time.sleep(20)

    def clickZoomInButton(self):
       self.do_click(self.BUTTON_ZOOM_IN)
       logger.info("attribute: " + self.getAttribute(self.ABC,"style"))
       return self.getAttribute(self.ABC,"style")

    def clickZoomOutButton(self):
       self.do_click(self.BUTTON_ZOOM_OUT)
       logger.info("attribute: " + self.getAttribute(self.ABC,"style"))
       return self.getAttribute(self.ABC,"style")
        

    def clickConfiguration(self):
       
       self.do_click(self.ICON_CONFIGURATION)      
          
    def selectIntrernalLedEnable(self):
       pass
       time.sleep(4)
       #self.do_click(self.INTRERNAL_LED_ENABLE)

    def selectDifferentValue(self):
       self.get_ElementText(self.VALUE)
       self.do_click(self.INTRERNAL_LED_ENABLE)
       logger.info("value000000000000000000: " + self.get_ElementText(self.VALUE))
       if self.get_ElementText(self.VALUE) == "True": 
        self.do_click(self.OPTION_FALSE)
       else: self.do_click(self.OPTION_TRUE)
       time.sleep(1)
       
    def clickSaveButton(self):
       self.click(self.SAVE_BUTTON)

    def verifyColor(self):
       self.getCSSPropertyName(self.INTRERNAL_LED_ENABLE, "background-color")
                   

