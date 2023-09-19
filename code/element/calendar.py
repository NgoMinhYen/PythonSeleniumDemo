from core.element.element import Element
from core.config import constants
import datetime
from enum import Enum


class CalendarEnum(Enum):
    PREVIOUS = "Previous"
    NEXT = "Next"


class Calendar(Element):
    
    def __init__(self, locator):
        self.calendar = Element(locator)
        self.dynamic_day_element = Element("//div[normalize-space(text())='{0}']")
        self.lbl_calendar = Element("//div[contains(@class,'mat-datetimepicker-calendar-period-button')]/strong")
        self.datetime_picker_element = Element("//mat-datetimepicker-content")
        self.dynamic_btn_navigate = Element("//div[@aria-label='{0} month']")
        self.lbl_year = Element("//div[contains(@class,'mat-datetimepicker-calendar-header-year')]")
    
    def _navigate(self, button):
        self.dynamic_btn_navigate.arguments = [button]
        self.dynamic_btn_navigate.wait_until_element_is_clickable()
        self.dynamic_btn_navigate.click_element()
        
    def _open_calendar(self, timeout=constants.SELENPY_WAIT_TIMEOUT):
        is_datetime_picker_displayed = self.datetime_picker_element.return_wait_until_element_is_visible()
        while is_datetime_picker_displayed == False:
            if timeout > 0:
                self.calendar.wait_until_element_is_clickable()
                self.calendar.click_element_by_js()
                is_datetime_picker_displayed = self.datetime_picker_element.return_wait_until_element_is_visible()
                timeout -= 1
            else:
                break
            
    def _get_current_label(self):
        self.lbl_calendar.wait_until_element_is_visible()
        label = self.lbl_calendar.get_text()
        return label
    
    def get_current_year(self):
        self.lbl_year.wait_until_element_is_visible()
        year = self.lbl_year.get_text()   
        return year     
            
    def get_current_month(self):
        month = self._get_current_label()
        datetime_object = datetime.datetime.strptime(month, "%B")
        month_number = datetime_object.month
        return month_number
            
    def select_day(self, day):
        datetime_object = datetime.datetime.strptime(day, "%d")
        day = datetime_object.day
        self.dynamic_day_element.arguments = [day]
        self.dynamic_day_element.click_element()
        
    def select_month(self, month):
        month = int(month)
        current_month = self.get_current_month()
        if month != current_month:
            while month < self.get_current_month():
                self._navigate(CalendarEnum.PREVIOUS.value)
            while month > self.get_current_month():
                self._navigate(CalendarEnum.NEXT.value)
        
    def select_year(self, year):
        year = int(year)
        current_year = int(self.get_current_year())
        if year != current_year:
            while year < int(self._get_current_label()):
                self._navigate(CalendarEnum.PREVIOUS.value)
            while year > int(self._get_current_label()):
                self._navigate(CalendarEnum.NEXT.value)
            
    def pick_date(self, date):
        """ Using date with format %m/%d/%Y """
        date_arr = date.split("/")
        month = date_arr[0]
        day = date_arr[1]
        year = date_arr[2]
        self._open_calendar()
        self.select_year(year)
        self.select_month(month)
        self.select_day(day)
        is_datetime_picker_displayed = self.datetime_picker_element.return_wait_until_element_is_visible()
        while is_datetime_picker_displayed == True:
            self.select_day(day)
            is_datetime_picker_displayed = self.datetime_picker_element.return_wait_until_element_is_visible()
        
