from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
import time


class RPCMultipleDevicePage(BasePage):
    def __int__(self, driver):
        super().__int__(driver)

    ICON_SEARCH = (
        By.XPATH, "//div[@fxlayoutalign='start center']//mat-icon[.='search']")
    INPUT_DEVICE = (By.XPATH, "//input[@data-placeholder='Search entities']")
    CURRENT_DEVICE = (By.XPATH, "//table//mat-row/mat-cell")
    ICON_CONFIGURATION = (
        By.XPATH, "(//span[contains(.,'settings')]/parent::button)[2]")
    BUTTON_ZOOM_OUT = (By.XPATH, "//a[@title='Zoom out']")
    dashboardGroups = (By.XPATH, "//a[@href='/dashboardGroups']")
    dc400 = (By.XPATH, "//tb-menu-link/a[span//span[.='DC400']]")
    BUTTON_DC400_DASBOARD = (
        By.XPATH, "//mat-cell[span[text()='DC400 RPC Multiple Devices']]/following-sibling::mat-cell//button[.=' dashboard']")

    def selectDeviceLandingPage(self):
        self.do_click(self.ICON_SEARCH)
        time.sleep(2)
        self.do_sendKeys(self.INPUT_DEVICE, "0203030521054067")

    def selectDeviceInList(self):
        self.do_click(self.CURRENT_DEVICE)

    def clickZoomOutButton(self):
        self.do_click(self.BUTTON_ZOOM_OUT)

    def clickDashBoardGroupLink(self):
        self.wait_for_element_visible(self.dashboardGroups)
        self.do_click(self.dashboardGroups)

    def clickOnLink(self):
        # time.sleep(2000)
        self.wait_for_loading_complete()
        self.wait_for_element_clickable(self.dc400)
        self.do_click(self.dc400)

    def openDashboardDC400(self):
        self.wait_for_loading_complete()
        self.wait_for_element_clickable(self.BUTTON_DC400_DASBOARD)
        self.do_click(self.BUTTON_DC400_DASBOARD)

    btn_search_device = (
        By.XPATH, "//div[contains(@class, 'tb-widget-actions')]/button[span/mat-icon[text()='search']]")

    def clickButtonSearchDevice(self):
        time.sleep(10)
        self.wait_for_element_visible(self.btn_search_device)
        self.do_click(self.btn_search_device)

    txt_search = (
        By.XPATH, "//mat-form-field//input[@data-placeholder='Search entities']")

    def inputDeviceName(self, value):
        self.wait_for_element_visible(self.txt_search)
        self.do_sendKeys(self.txt_search, value)

    def selectDevice(self, value):
        xpath = "//mat-cell[text()='{0}']/preceding-sibling::mat-cell/mat-checkbox//input".format(value)
        chk_device = (By.XPATH, xpath)
        self.wait_for_element_visible(chk_device)
        self.do_click(chk_device)

    select_rpc_emthod = (
        By.XPATH, "//mat-form-field//span[.='RPC Method Description']/preceding-sibling::mat-select")

    def selectRPCMethod(self, value):
        self.do_click(self.select_rpc_emthod)
        xpath = "//div[@role='listbox']/mat-option[span[normalize-space(text()) = '{0}']]".format(
            value)
        option = (By.XPATH, xpath)
        self.do_click(option)

    txt_rpc_parameter = (
        By.XPATH, "//div[contains(@class, 'mat-form-field-wrapper')]//span[label/mat-label[text()='RPC parameters']]/preceding-sibling::input")

    def inputRPCParameter(self, value):
        self.wait_for_element_visible(self.txt_rpc_parameter)
        self.do_sendKeys(self.txt_rpc_parameter, value)

    chk_clear_selection_after_rpc = (
        By.XPATH, "//mat-checkbox/label/span[contains(text(), 'Clear selection after RPC ?')]/preceding-sibling::span//input")

    def uncheck_clear_selection_after_rpc(self):
        self.do_click(self.chk_clear_selection_after_rpc)

    btn_send_rpc = (
        By.XPATH, "//button[span[normalize-space(text()) = 'Send RPC']]")

    def clickSendRPCButton(self):
        self.do_click(self.btn_send_rpc)

    btn_clear_response_history = (
        By.XPATH, "//button[span[normalize-space(text()) = 'Clear response history']]")

    def clickClearRPCHistoryResponseButton(self):
        self.do_click(self.btn_clear_response_history)
