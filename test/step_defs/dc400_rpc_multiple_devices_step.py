import logging
import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from main.pages.LoginPage import LoginPage
from main.pages.HomePage import HomePage
from main.pages.DashBoardGroupPage import DashBroardGroup
from main.pages.rpc_multiple_device_page import RPCMultipleDevicePage
# Constants
logger = logging.getLogger(__name__)
from time import sleep

GeoSensorX = 'https://staging.geosensorx.ai'

# Scenarios

scenarios('../features/dc400_rpc_multiple_devices.feature')


# Fixtures


@pytest.fixture
def browser():
    logger.info("Create driver")
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait = 30
    driver.maximize_window()
    driver.get(GeoSensorX)
    yield driver
    # driver.quit()
# Given Steps


@given('Login GSX Cloud')
def login_page(browser):
    logger.info("Login")
    browser.get(GeoSensorX)
    loginPage = LoginPage(browser)
    loginPage.doLoginPage(
        "phat.ngo+tenant-admin@logigear.com", "Y9!ynp7GY-XHEKWN")

@given("Go to Dashboard groups > DC400 > RPC Multiple Devices DC400")
def go_to_rpc_multiple_device(browser):
    multiplePage = RPCMultipleDevicePage(browser)
    sleep(10)
    logger.info("Open daskboard link")
    multiplePage.clickDashBoardGroupLink()

    sleep(10)
    logger.info("Click dc400 link")
    multiplePage.clickOnLink()

    sleep(15)
    logger.info("Open dc400 dasboard button")
    multiplePage.openDashboardDC400()

@given(parsers.parse("Select an active Device {string} on the DC400 devices list"))
def select_device(browser, deviceName):
  multiplePage = RPCMultipleDevicePage(browser)
  logger.info("Click search device button")
  multiplePage.wait_for_loading_complete()
  multiplePage.clickButtonSearchDevice()

  logger.info('Enter device name')
  multiplePage.inputDeviceName(deviceName)

  logger.info('Select device')
  multiplePage.selectDevice(deviceName)


@given("Select {string} on RPC Method Description list")
def select_rpc_method(browser, method):
  multiplePage = RPCMultipleDevicePage(browser)
  logger.info('Select RPC Method Description')
  multiplePage.selectRPCMethod(method)


@given('Enter {string} on RPC parameters')
def select_rpc_method(browser, params):
  multiplePage = RPCMultipleDevicePage(browser)
  logger.info('Enter on RPC parameters')
  multiplePage.inputRPCParameter(params)

@given("Uncheck Clear selection after RPC ?")
def uncheck_clear_selecttion_rpc(browser):
   multiplePage = RPCMultipleDevicePage(browser)
   logger.info("Uncheck Clear selection after RPC ?")
   multiplePage.uncheck_clear_selection_after_rpc()


@given("Click Send RPC button")
def clickSendRPCButton(browser):
   multiplePage = RPCMultipleDevicePage(browser)
   logger.info("Click Send RPC button")
   multiplePage.clickSendRPCButton()


@given("Clear response history")
def clear_response_history():
    multiplePage = RPCMultipleDevicePage(browser)
    logger.info("Clear response history")
    multiplePage.clickClearRPCHistoryResponseButton();
