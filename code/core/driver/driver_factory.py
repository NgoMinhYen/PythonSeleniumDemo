from importlib import import_module
from core import browserManagementKeywords
from core.driver.config.driver_config import DriverConfig
from selenium import webdriver
from core.driver import driver

class DriverFactory:
    driver_factory = None
    #module_path = "core.driver.browser.chrome_driver"
    
    @classmethod
    def get_instance(cls):
        if cls.driver_factory is None:
            cls.driver_factory = DriverFactory()
        return cls.driver_factory
    
    def __init__(self):
        self._driverConfig = DriverConfig.get_driver_config()
        
    def start_driver(self, alias=None):
        modulePath = "core.driver.browser.chrome_driver"
        className = "ChromeDriver"
        
        # if self._driverConfig.mode == "local":
        #     modulePath = "%s.%s_driver" % (self.module_path, self._driverConfig.browser.lower())
        #     className = "%sDriver" % self._driverConfig.browser.capitalize()
        # elif self._driverConfig.platform == "mobile":
        #     modulePath = "%s.mobile_driver" % self.module_path
        #     className = "MobileDriver"
        # else:
        #     modulePath = "%s.remote_driver" % self.module_path
        #     className = "RemoteDriver"
            
        module = import_module(modulePath)
        driverClass = getattr(module, className)
        driverClass.create_driver(self._driverConfig, alias)

    def start_ChromeDriver(url):
        browserManagementKeywords.create_webdriver("Chrome")
        browserManagementKeywords.go_to(url)
        # driver.get(url)

    def close_browser():
        browserManagementKeywords.close_browser()
    

