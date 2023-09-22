from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
from main.pages.rpc_multiple_device_page import RPCMultipleDevicePage
import time
import logging
logger = logging.getLogger(__name__)


class DashBroardGroup(BasePage):
    def __int__(self, driver):
        super().__int__(driver)

    ICON_SEARCH = (
        By.XPATH, "//div[@fxlayoutalign='start center']//mat-icon[.='search']")
    INPUT_DEVICE = (By.XPATH, "//input[@data-placeholder='Search entities']")
    CURRENT_DEVICE = (By.XPATH, "//table//mat-row/mat-cell")
    ICON_CONFIGURATION = (
        By.XPATH, "//div[@fxlayoutalign='end']//mat-icon[.='settings']")
    BUTTON_ZOOM_OUT = (By.XPATH, "//a[@title='Zoom out']")
    BUTTON_ZOOM_IN = (By.XPATH, "//a[@title='Zoom in']")
    INTRERNAL_LED_ENABLE = (
        By.XPATH, "//mat-form-field[contains(.,'Internal LED Enable')]")
    STYLE = (By.XPATH, "//div[@class='leaflet-proxy leaflet-zoom-animated']")
    OPTION_FALSE = (
        By.XPATH, "//span[@class='mat-option-text' and contains(.,'False')]")
    OPTION_TRUE = (
        By.XPATH, "//span[@class='mat-option-text' and contains(.,'True')]")
    VALUE = (
        By.XPATH, "//mat-form-field[contains(.,'Internal LED Enable')]//span[contains(@class,'mat-select-value-text')]")
    LOADING = (
        By.XPATH, "//mat-spinner[contains(@class,'mat-primary')]//[local-name()='svg']//[local-name()='circle']")
    SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Save')]")

    LBL_DEVICE_CONFIGURATION_WIGET = (
        By.XPATH, "//div/span[normalize-space(text())='Device configuration widget']")

    def selectDeviceLandingPage(self, deviceName):
        self.wait_for_element_clickable(self.ICON_SEARCH)
        self.do_click(self.ICON_SEARCH)
        self.do_sendKeys(self.INPUT_DEVICE, deviceName)

    def selectDeviceInList(self):
        # self.wait_for_element_clickable(self.CURRENT_DEVICE)
        # self.wait_for_element_clickable(self.CURRENT_DEVICE)
        # self.do_click(self.CURRENT_DEVICE)

        # xpath = "//mat-cell[text()='{0}']/preceding-sibling::mat-cell/mat-checkbox".format(value)
        # chk_device = (By.XPATH, xpath)
        self.wait_for_element_visible(self.CURRENT_DEVICE)
        self.wait_for_element_clickable(self.CURRENT_DEVICE)
        loop = 10
        while loop > 0:
            class_value = self.getAttribute(self.CURRENT_DEVICE, "class")
            if "mat-checkbox-checked" not in class_value:
                try:
                    self.do_click(self.CURRENT_DEVICE)
                except:
                    pass
                    # self.select_entity_checkbox_by_name(name)
            else:
                break
            time.sleep(1)
            loop -= 1
        # self.do_click(chk_device)

    def getValueStyleCurent(self):
        # self.wait_for_element_clickable(self.BUTTON_ZOOM_IN)
        # self.do_click(self.BUTTON_ZOOM_IN)

        logger.info("attribute01: " + self.getAttribute(self.STYLE, "style"))
        return self.getAttribute(self.STYLE, "style")

    def clickZoomOutButton(self):
        self.wait_for_element_clickable(self.BUTTON_ZOOM_IN)
        self.do_click(self.BUTTON_ZOOM_IN)
        logger.info("attribute: " + self.getAttribute(self.STYLE, "style"))
        return self.getAttribute(self.STYLE, "style")

    def clickConfiguration(self):
        self.wait_for_element_clickable(self.ICON_CONFIGURATION)
        self.do_click(self.ICON_CONFIGURATION)

    # def selectIntrernalLedEnable(self):
        # pass
        # time.sleep(4)
        # self.do_click(self.INTRERNAL_LED_ENABLE)

    def selectDifferentValue(self):
        self.get_ElementText(self.VALUE)
        self.do_click(self.INTRERNAL_LED_ENABLE)
        logger.info("value000000000000000000: " +
                    self.get_ElementText(self.VALUE))
        if self.get_ElementText(self.VALUE) == "True":
            self.do_click(self.OPTION_FALSE)
        else:
            self.do_click(self.OPTION_TRUE)

    def clickSaveButton(self):
        logger.info("clickSaveButton")
        self.wait_for_element_clickable(self.SAVE_BUTTON)
        self.click(self.SAVE_BUTTON)
        time.sleep(4)

    def verifyColor(self):
        blueColor_Chrome = "rgba(150, 225, 255, 1)"
        blueColor_Firefox = "rgb(150, 225, 255)"
        self.wait_for_element_visible(self.INTRERNAL_LED_ENABLE)
        # self.wait_for_element_invisible(self.LOADING)
        logger.info(
            "AAAAAAAAAA :" + self.getCSSPropertyName(self.INTRERNAL_LED_ENABLE, "background-color"))
        colorChange = self.getCSSPropertyName(
            self.INTRERNAL_LED_ENABLE, "background-color")
        assert (blueColor_Chrome == colorChange) or (
            blueColor_Firefox == colorChange)

    def verifyIsDisplayedDeviceName(self, deviceID):
        DEVICE_NAME = (
            By.XPATH, f"//mat-row/mat-cell[contains(text(),'{deviceID}')]")
        self.wait_for_element_visible(DEVICE_NAME)
        return self.isDisplayed(DEVICE_NAME)

    def goToConfigration(self, configration):
        self.wait_for_element_visible(self.ICON_CONFIGURATION)
        self.do_click(self.ICON_CONFIGURATION)

    def is_displayed_label_device_configuration_wiget(self):
        self.wait_for_element_visible(self.LBL_DEVICE_CONFIGURATION_WIGET)
        return self.isDisplayed(self.LBL_DEVICE_CONFIGURATION_WIGET)

    def is_displayed_device_id_in_configuration_page(self, deviceId):
        DEVICE_NAME = (
            By.XPATH, f"//section/span[normalize-space(text())='{deviceId}']")
        self.wait_for_element_visible(DEVICE_NAME)
        return self.isDisplayed(DEVICE_NAME)
