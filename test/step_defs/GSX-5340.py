import pytest
import logging
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
from allure import step
logger = logging.getLogger(__name__)
# Constants
 
GeoSensorX = 'https://staging.geosensorx.ai'
 
# Scenarios
 
scenarios('../features/GSX-5340.feature')
 

# Fixtures

@pytest.fixture
def browser():
    logger.info("Create driver")
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get(GeoSensorX)
    driver.maximize_window()
    yield driver
    driver.quit()
# Given Steps

@given(parsers.parse("Login GSX Cloud with email '{username}' and password '{password}'"))
def login_page(browser, username, password):
    logger.info("Login")
    with step("Login GSX Cloud"):
        browser.get(GeoSensorX)
        loginPage = LoginPage(browser)
        loginPage.doLoginPage(username, password)

@when('Go to Dashboard groups > DC400 > RPC Multiple Devices DC400')
def select_DC400(browser):
    with step("Go to Dashboard groups > DC400 > RPC Multiple Devices DC400"):
        logger.info("Open daskboard link")
        homePage = HomePage(browser)
        homePage.select_DC400()
       

@when(parsers.parse("Search device with device id: '{deviceID}'"))
def select_Device_DevicesList(browser,deviceID):
    with step("Search device with device id: '{deviceID}'"):
        logger.info("Search device with device id: '{deviceID}'")
        dashBoardGroup = DashBroardGroup(browser)
        dashBoardGroup.selectDeviceLandingPage(deviceID)
        dashBoardGroup.selectDeviceInList()
  

#@then('Click on "-" button on the map widget and verify the map is zoomed out')
#def clickZoomOutButton(browser):
    #with step("Click on '-' button on the map widget and verify the map is zoomed out"):
        #logger.info("Click on '-' button on the map widget")
        #dashBoardGroup = DashBroardGroup(browser)
        #before = dashBoardGroup.getValueStyleCurent()
        #after = dashBoardGroup.clickZoomOutButton()
        #assert before != after
@then(parsers.parse("Expected: Device: '{deviceID}' is displayed"))
def verifyDeviceNameIsDisplayed(browser):
    with step("Expected: Device: '{deviceID}' is displayed"):
           logger.info("Expected: Device: '{deviceID}' is displayed")
           dashBoardGroup = DashBroardGroup(browser)
           assert dashBoardGroup.verifyIsDisplayedDeviceName() == True

@when(parsers.parse("Click '{configration}' icon in device item"))
def goToConfigration(browser):
    with step("Click '{configration}' icon in device item"):
           logger.info("Click '{configration}' icon in device item")
           dashBoardGroup = DashBroardGroup(browser)







    