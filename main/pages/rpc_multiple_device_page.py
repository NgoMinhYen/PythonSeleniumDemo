import logging
from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
import time
logger = logging.getLogger(__name__)


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
        By.XPATH,
        "//mat-cell[span[text()='DC400 RPC Multiple Devices']]/following-sibling::mat-cell//button[.=' dashboard']/span[@class='mat-button-wrapper']")

    txt_rpc_response = (By.XPATH, "//textarea[@formcontrolname='rpcResponse']")
    btn_clear_response_history = (
        By.XPATH, "//button/span[normalize-space(.)='Clear response history']")
    btn_search_device = (
        By.XPATH, "//div[contains(@class, 'tb-widget-actions')]/button[span/mat-icon[text()='search']]")

    txt_search = (
        By.XPATH, "//mat-form-field//input[@data-placeholder='Search entities']")
    select_rpc_emthod = (
        By.XPATH, "//mat-form-field//span[normalize-space(.)='RPC Method Description']/preceding-sibling::mat-select")
    txt_rpc_parameter = (
        By.XPATH,
        "//div[contains(@class, 'mat-form-field-wrapper')]//span[label/mat-label[text()='RPC parameters']]/preceding-sibling::input")
    chk_clear_selection_after_rpc = (
        By.XPATH, "//mat-checkbox/label/span[contains(text(), 'Clear selection after RPC ?')]/preceding-sibling::span")
    btn_send_rpc = (
        By.XPATH, "//button[span[normalize-space(text()) = 'Send RPC']]")

    def selectDeviceLandingPage(self):
        self.do_click(self.ICON_SEARCH)
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

    def clickButtonSearchDevice(self):
        # self.wait_for_spinner_invisible()
        self.wait_for_element_clickable(self.btn_search_device)
        self.do_click(self.btn_search_device)

    def inputDeviceName(self, value):
        self.wait_for_element_visible(self.txt_search)
        self.do_sendKeys(self.txt_search, value)
        xpath = (By.XPATH, f"//mat-cell[normalize-space(.)='{value}']/parent::mat-row")
        # self.wait_for_element_visible(xpath)

    def selectDevice(self, value):
        xpath = "//mat-cell[text()='{0}']/preceding-sibling::mat-cell/mat-checkbox".format(value)
        chk_device = (By.XPATH, xpath)
        self.wait_for_element_visible(chk_device)
        self.wait_for_element_clickable(chk_device)
        loop = 10
        while loop > 0:
            class_value = self.getAttribute(chk_device, "class")
            if "mat-checkbox-checked" not in class_value:
                try:
                    self.do_click(chk_device)
                except:
                    pass
                    # self.select_entity_checkbox_by_name(name)
            else:
                break
            time.sleep(1)
            loop-=1
        # self.do_click(chk_device)

    def selectRPCMethod(self, value):
        self.wait_for_element_clickable(self.select_rpc_emthod)

        # loop = 10
        # while loop > 0:
        #     class_value = self.getAttribute(self.select_rpc_emthod, "aria-expanded")
        #     logger.info(f'value class {class_value}')
        #     if class_value is "false":
        #         self.do_click(self.select_rpc_emthod)
        #         self.wait_for_element_present_in_element_attribute(self.select_rpc_emthod, "aria-expanded", "true")
        #     else:
        #         break
        #     time.sleep(1)
        #     loop-=1

        self.do_click(self.select_rpc_emthod)
        self.wait_for_element_present_in_element_attribute(self.select_rpc_emthod, "aria-expanded", "true")
        xpath = "//div[@role='listbox']/mat-option[span[normalize-space(text()) = '{0}']]".format(
            value)
        option = (By.XPATH, xpath)
        try:
            self.wait_for_element_visible(option)
            self.do_click(option)
        except:
            self.click_by_js(option)
            

    def inputRPCParameter(self, value):
        self.wait_for_element_visible(self.txt_rpc_parameter)
        self.clear_text(self.txt_rpc_parameter)
        self.do_sendKeys(self.txt_rpc_parameter, value)

    def uncheck_clear_selection_after_rpc(self):
        self.do_click(self.chk_clear_selection_after_rpc)

    def clickSendRPCButton(self):
        self.do_click(self.btn_send_rpc)

    def clickClearRPCHistoryResponseButton(self):
        script = "arguments[0].click();"
        # self.execute_script(script, self.btn_clear_response_history)
        self.do_click(self.btn_clear_response_history)

    def get_value_rpc_response(self):
        script = "arguments[0].removeAttribute('disabled')"
        self.execute_script(script, self.txt_rpc_response)
        self.wait_until_text_box_has_value(self.txt_rpc_response, 'status: SUCCESSFUL')
        loop = 10
        while loop > 0:
            response = self.getAttribute(self.txt_rpc_response, "value")
            if "status: SUCCESSFUL" in response:
                return response
            else:
                time.sleep(1)
                loop-=1
        return self.getAttribute(self.txt_rpc_response, "value")
