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
from time import sleep
GeoSensorX = 'https://staging.geosensorx.ai'

# Scenarios

scenarios('../features/dc400_configuration.feature')


# Fixtures

@pytest.fixture
def browser():
    logger.info("Create driver")
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
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
def select_Device_DevicesList(browser, deviceID):
    with step(f"Search device with device id: '{deviceID}'"):
        logger.info(f"Search device with device id: '{deviceID}'")
        dashBoardGroup = DashBroardGroup(browser)
        dashBoardGroup.selectDeviceLandingPage(deviceID)
        dashBoardGroup.selectDeviceInList()


# @then('Click on "-" button on the map widget and verify the map is zoomed out')
# def clickZoomOutButton(browser):
    # with step("Click on '-' button on the map widget and verify the map is zoomed out"):
        # logger.info("Click on '-' button on the map widget")
        # dashBoardGroup = DashBroardGroup(browser)
        # before = dashBoardGroup.getValueStyleCurent()
        # after = dashBoardGroup.clickZoomOutButton()
        # assert before != after
@then(parsers.parse("Expected: Device: '{deviceID}' is displayed"))
def verifyDeviceNameIsDisplayed(browser, deviceID):
    with step(f"Expected: Device: '{deviceID}' is displayed"):
        logger.info(f"Expected: Device: '{deviceID}' is displayed")
        dashBoardGroup = DashBroardGroup(browser)
        assert dashBoardGroup.verifyIsDisplayedDeviceName(deviceID) == True


@when(parsers.parse("Click (Go to configuration) icon in device item '{deviceID}'"))
def goToConfiguration(browser, deviceID):
    with step(f"Click (Go to configuration) icon in device item '{deviceID}'"):
        logger.info(f"Click (Go to configuration) icon in device item '{deviceID}'")
        dashBoardGroup = DashBroardGroup(browser)
        dashBoardGroup.go_to_configuration_page(deviceID)

@then(parsers.parse("Device '{deviceID}' configuration page is displayed"))
def verify_configuration_device_page_displayed(browser, deviceID):
    with step(f"Device '{deviceID}' configuration page is displayed"):
        logger.info(f"Device '{deviceID}' configuration page is displayed")
        dashBoardGroup = DashBroardGroup(browser)
        assert dashBoardGroup.is_displayed_label_device_configuration_wiget() == True
        assert dashBoardGroup.is_displayed_device_id_in_configuration_page(deviceID) == True