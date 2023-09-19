
# from tests.base_test import BaseTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import constants
from core.driver import driver

from pages.gsx_login_page import LoginPage

login_page = LoginPage().open_gsx().login_to_gsx()


