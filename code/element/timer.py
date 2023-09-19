from core.element.element import Element
from core.config import constants
import datetime


class Timer(Element):
    
    def __init__(self, locator):
        self.timer = Element(locator)
        self.clock = Element("//mat-datetimepicker-calendar")
        self.dynamic_hour = Element("//div[contains(@class,'mat-datetimepicker-clock-hours')]//div[text()='{0}']")
        self.dynamic_minute = Element("//div[contains(@class,'mat-datetimepicker-clock-minutes')]//div[text()='{0}']")
    
    def _open_timer(self, timeout=constants.SELENPY_WAIT_TIMEOUT):
        is_datetime_picker_displayed = self.clock.return_wait_until_element_is_visible()
        while is_datetime_picker_displayed == False:
            if timeout > 0:
                self.timer.wait_until_element_is_clickable()
                self.timer.click_element_by_js()
                is_datetime_picker_displayed = self.clock.return_wait_until_element_is_visible()
                timeout -= 1
            else:
                break
            
    def select_hour(self, hour):
        datetime_object = datetime.datetime.strptime(hour, "%H")
        hour_number = datetime_object.hour
        self.dynamic_hour.arguments = [hour_number]
        self.dynamic_hour.click_element()
        self.dynamic_hour.wait_until_element_is_not_visible()
            
    def select_minute(self, minute):
        datetime_object = datetime.datetime.strptime(minute, "%M")
        minute_number = datetime_object.minute
        if str(minute_number) == "0":
            minute_number = "00"
        self.dynamic_minute.arguments = [minute_number]
        self.dynamic_minute.click_element()
            
    def pick_time(self, time):
        """ Using time with format %-H:%-M """
        time_arr = time.split(":")
        hour = time_arr[0]
        minute = time_arr[1]
        self._open_timer()
        self.select_hour(hour)
        self.select_minute(minute)
        is_datetime_picker_displayed = self.clock.return_wait_until_element_is_visible()
        while is_datetime_picker_displayed == True:
            self.select_minute(minute)
            is_datetime_picker_displayed = self.clock.return_wait_until_element_is_visible()
    