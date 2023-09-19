from core.driver.driver_factory import DriverFactory
from core import SL

def start_driver(alias=None):
    DriverFactory.get_instance().start_driver(alias)

   
def start_ChromeDriver(url):
    DriverFactory.start_ChromeDriver(url)

def close_browser():
    DriverFactory.close_browser()

def maximize():
    SL.driver.maximize_window()



