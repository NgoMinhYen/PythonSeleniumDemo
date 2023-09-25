from time import sleep
import logging
import pytest
from pytest_bdd import scenarios, given, parsers, when, then
from selenium import webdriver
import allure
from main.pages.LoginPage import LoginPage
from main.pages.rpc_multiple_device_page import RPCMultipleDevicePage
from allure import step

# Constants
logger = logging.getLogger(__name__)

GeoSensorX = 'https://staging.geosensorx.ai'

# Scenarios


from datetime import datetime

# Fixtures

scenarios('../features/dc400_rpc_multiple_devices.feature')


@pytest.fixture
def browser():
    logger.info("Create driver")
    driver = webdriver.Chrome()
    # driver.implicitly_wait = 30
    driver.maximize_window()
    driver.get(GeoSensorX)
    yield driver
    driver.quit()


# Given Steps


@given(parsers.parse("Login GSX Cloud with email {email} and password {password}"))
def login_page(browser, email, password):
    # logger.info(datetime.now())
    with step("Login GSX Cloud"):
        logger.info("Login GSX Cloud")
        browser.get(GeoSensorX)
        loginPage = LoginPage(browser)
        loginPage.doLoginPage(email, password)


@given("Go to Dashboard groups > DC400 > RPC Multiple Devices DC400")
def go_to_rpc_multiple_device(browser):
    with step("Go to Dashboard groups > DC400 > RPC Multiple Devices DC400"):
        multiplePage = RPCMultipleDevicePage(browser)
        logger.info("Open daskboard link")
        multiplePage.clickDashBoardGroupLink()

        logger.info("Click dc400 link")
        multiplePage.clickOnLink()

        logger.info("Open dc400 dasboard button")
        multiplePage.openDashboardDC400()


@given(parsers.parse("Select an active Device {deviceName} on the DC400 devices list"))
def select_device(browser, deviceName):
    with step(f"Select an active Device {deviceName} on the DC400 devices list"):
        multiplePage = RPCMultipleDevicePage(browser)
        multiplePage.wait_for_loading_complete()

        logger.info("Click search device button")
        multiplePage.clickButtonSearchDevice()

        logger.info('Enter device name')
        multiplePage.inputDeviceName(deviceName)

        logger.info('Select device')
        multiplePage.selectDevice(deviceName)


@when(parsers.parse("Select {rpc_method} on RPC Method Description list"))
def select_rpc_method(browser, rpc_method):
    with step(f"Select '{rpc_method}' on RPC Method Description list"):
        multiplePage = RPCMultipleDevicePage(browser)
        logger.info('Select RPC Method Description')
        multiplePage.selectRPCMethod(rpc_method)


@when(parsers.parse("Enter {params} on RPC parameters"))
def select_rpc_method(browser, params):
    multiplePage = RPCMultipleDevicePage(browser)
    logger.info(f'Enter {params} on RPC parameters')
    multiplePage.inputRPCParameter(params)


@when("Uncheck Clear selection after RPC")
def uncheck_clear_selecttion_rpc(browser):
    multiplePage = RPCMultipleDevicePage(browser)
    logger.info("Uncheck Clear selection after RPC ?")
    multiplePage.uncheck_clear_selection_after_rpc()


@then(parsers.parse("Verify RPC command response device: {device_name}, parameters: {params}"))
def verify_response_config_set(browser, device_name, params):
    with step(f"Verify RPC command response device: {device_name}, parameters: {params}"):
        logger.info('verify_response_config_set')
        multiplePage = RPCMultipleDevicePage(browser)
        response = multiplePage.get_value_rpc_response()
        logger.info(response)

        logger.info("Verify response device name")
        assert f'name: {device_name}' in response, 'Verify fail device name'

        logger.info("Verify response status")
        assert 'response: {"status":"success"}' in response, 'Verify fail status'

        logger.info("Verify response method")
        assert f'method: config-set, params: {params}' in response, 'Verify fail method'

        logger.info("Verify response status")
        assert 'status: SUCCESSFUL' in response, 'Verify fail status'


@when("Click Send RPC button")
def click_send_rpc_button(browser):
    with step("Click Send RPC button"):
        multiplePage = RPCMultipleDevicePage(browser)
        logger.info("Click Send RPC button")
        multiplePage.clickSendRPCButton()


@when("Clear response history")
def clear_response_history(browser):
    with step("Clear response history"):
        multiplePage = RPCMultipleDevicePage(browser)
        logger.info("Clear response history")
        multiplePage.click_clear_rpc_history_response_button()


@then(parsers.parse("Verify RPC command get response device: {device_name}, params: {params}, value: {value}"))
def verify_response_config_get(browser, device_name, params, value):
    with step(f"Verify RPC command get response device: '{device_name}', params: '{params}', value: '{value}'"):
        logger.info('verify_response_config_set')
        multiplePage = RPCMultipleDevicePage(browser)
        response = multiplePage.get_value_rpc_response()
        logger.info(response)

        logger.info("Verify response device name")
        assert f'name: {device_name}' in response, 'Verify fail device name'

        logger.info("Verify response data")
        response_data = 'response: {"data":' + value + '}'
        logger.info(response_data)
        # logger.info(datetime.now())
        assert response_data in response, 'Verify fail data'
        # logger.info(datetime.now())

        logger.info("Verify response method")
        logger.info(f'method: config-get, params: "{params}"')
        assert f'method: config-set, params: {params}' in response, 'Verify fail method'

        logger.info("Verify response status")
        assert 'status: SUCCESSFUL' in response, 'Verify fail status'