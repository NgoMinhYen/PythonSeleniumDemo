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
logger = logging.getLogger(__name__)
# Constants
 
GeoSensorX = 'https://staging.geosensorx.ai'
 
# Scenarios
 
scenarios('../features/GSX-13874.feature')
 

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
    browser.get(GeoSensorX)
    loginPage = LoginPage(browser)
    loginPage.doLoginPage("phat.ngo+tenant-admin@logigear.com", "Y9!ynp7GY-XHEKWN")


@when('Go to Dashboard groups - DC400 - FMS Dashboard')
def select_DC400(browser):
    logger.info("Open daskboard link")
    homePage = HomePage(browser)
    homePage.select_DC400()

@when('Select any device then go to Configuration page')
def selectDeviceAndGoToConfig(browser):
    logger.info("Select any device then go to Configuration page")
    dashBoardGroup = DashBroardGroup(browser)
    dashBoardGroup.selectDeviceLandingPage()
    dashBoardGroup.selectDeviceInList()
    dashBoardGroup.clickConfiguration()

@when('Select the Intrernal LED Enable configuration with a different value')
def selectInternalLed(browser):
    logger.info("Select the Intrernal LED Enable configuration with a different value")
    dashBoardGroup = DashBroardGroup(browser)
    dashBoardGroup.selectIntrernalLedEnable()
