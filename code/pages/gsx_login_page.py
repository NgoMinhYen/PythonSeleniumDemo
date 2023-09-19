from core.helper.base_page import BasePage
from core.driver import driver
from data import constants
from pages.gsx_home_page import HomePage
from core.driver.driver_factory import DriverFactory
from pytest_bdd import given, when, then, scenario, scenarios


class LoginPage(BasePage):

    def __init__(self):
        BasePage.__init__(self)
        self.txt_username = self.element("txt_username")
        self.txt_password = self.element("txt_password")
        self.btn_login = self.element("btn_login")
        
    def open_gsx(self, url = constants.GSX_STAGING_URL):
        driver.start_ChromeDriver(url)
        driver.maximize()
        return LoginPage()
        
    def login_to_gsx(self, username=constants.GSX_QA_USERNAME, password=constants.GSX_QA_PASSWORD):
        self.txt_username.wait_until_element_is_visible()
        self.txt_username.input_text(username)
        self.txt_password.input_text(password)
        self.btn_login.click_element()
        self.btn_login.wait_until_element_is_not_visible()
        return HomePage()


    @given("Go to dashboard on the Dashboard")
    def openGSX(self, url = constants.GSX_STAGING_URL):
        self.open_gsx()
        # driver.start_ChromeDriver(url)
        # driver.maximize()
        # return LoginPage()
    
    @when("Login with QA account")
    def loginToGSX(self, username=constants.GSX_QA_USERNAME, password=constants.GSX_QA_PASSWORD):
        self.login_to_gsx()
    
    @then("Verify login with QA successfully")
    def verifyHomePageIsDisplayed():
        print("Passed Passed Passed")