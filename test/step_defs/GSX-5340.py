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

@given('Login GSX Cloud')
def login_page(browser):
    logger.info("Login")
    with step("Login GSX Cloud"):
        browser.get(GeoSensorX)
        loginPage = LoginPage(browser)
        loginPage.doLoginPage("phat.ngo+tenant-admin@logigear.com", "Y9!ynp7GY-XHEKWN")

@when('Go to Dashboard groups > DC400 > RPC Multiple Devices DC400')
def select_DC400(browser):
    with step("Go to Dashboard groups > DC400 > RPC Multiple Devices DC400"):
        logger.info("Open daskboard link")
        homePage = HomePage(browser)
        homePage.select_DC400()
    
@when(parsers.parse("Select an active Device '{deviceName}' on the DC400 devices list"))
def select_Device_LandingPage(browser,deviceName):
    with step("Select an active Device {deviceName} on the DC400 devices list"):
        logger.info("Select any device in Landing page to go to Driving Data page")
        dashBoardGroup = DashBroardGroup(browser)
        dashBoardGroup.wait_for_loading_complete
        dashBoardGroup.selectDeviceLandingPage(deviceName)
    

@when('Select any device in Devices list of Driving Data page')
def select_Device_DevicesList(browser):
    with step("Select any device in Devices list of Driving Data page"):
        logger.info("Select any device in Devices list of Driving Data page")
        dashBoardGroup = DashBroardGroup(browser)
        dashBoardGroup.selectDeviceInList()
  

@then('Click on "-" button on the map widget and verify the map is zoomed out')
def clickZoomOutButton(browser):
    with step("Click on '-' button on the map widget and verify the map is zoomed out"):
        logger.info("Click on '-' button on the map widget")
        dashBoardGroup = DashBroardGroup(browser)
        before = dashBoardGroup.clickZoomInButton()
        after = dashBoardGroup.clickZoomOutButton()
        assert before != after





    