from time import sleep
from core.config import constants
from core.helper.base_page import BasePage
import pytest
from core.util import utils

from core.driver import driver

class GeneralPage(BasePage):

    def __init__(self):
        BasePage.__init__(self)
        self.logger = utils.get_logger("GSX")
        #self._is_repeat_mode = pytest.repeat_mode
        self.icon_user_menu = self.element("icon_user_menu")
        self.btn_user_menu = self.element("btn_user_menu")
        self.dynamic_menu_item = self.element("dynamic_menu_item")
        self.dynamic_entity = self.element("dynamic_entity")
        self.tb_current_entity_state_controller = self.element("tb_current_entity_state_controller")
        self.span_entity_section = self.element("span_entity_section")
        self.div_rpc_widget_disable = self.element("div_rpc_widget_disable")
        self.btn_search = self.element("btn_search")
        self.btn_close = self.element("btn_close")
        self.dynamic_checkbox_rpc_multiple_devices = self.element("dynamic_checkbox_rpc_multiple_devices")
        self.txt_search_entity = self.element("txt_search_entity")
        self.btn_zoom_in = self.element("btn_zoom_in")
        self.btn_zoom_out = self.element("btn_zoom_out")
        self.map_panel_leaflet_zoom_animated = self.element("map_panel_leaflet_zoom_animated")
        self.lbl_item_per_page = self.element("lbl_item_per_page")
        self.lbl_paginator_range = self.element("lbl_paginator_range")
        self.realtime_tab = self.element("realtime_tab")
        self.tb_timeinterval = self.element("tb_timeinterval")
        self.tb_timeinterval_option = self.element("tb_timeinterval_option")
        self.tb_timeinterval_update_button = self.element("tb_timeinterval_update_button")
        self.timeseries_rows_by_dynamic_column = self.element("timeseries_rows_by_dynamic_column")
        self.btn_edit_mode = self.element("btn_edit_mode")
        self.btn_close_toast_message = self.element("btn_close_toast_message")
        self.timeseries_full_screen_btn = self.element("timeseries_full_screen_btn")
        
    def is_user_menu_displayed(self):
        return self.icon_user_menu.is_element_displayed()
    
    def select_menu_item(self, item, subItem=None):
        self.dynamic_menu_item.arguments = [item]
        self.dynamic_menu_item.wait_until_element_is_visible()
        self.dynamic_menu_item.wait_until_element_is_clickable()
        self.dynamic_menu_item.click_element()
        if subItem is not None:
            self.dynamic_menu_item.arguments = [subItem]
            self.dynamic_menu_item.wait_until_element_is_visible()
            self.dynamic_menu_item.wait_until_element_is_clickable()
            self.dynamic_menu_item.click_element()
            sleep(1)

    def select_entity_by_name(self, name):
        self.dynamic_entity.arguments = [name]
        self._search(name)
        self.dynamic_entity.wait_until_element_is_visible()
        self.dynamic_entity.wait_until_element_is_clickable()
        self.dynamic_entity.click_element_by_js()
        
    def select_entity_checkbox_by_name(self, name):
        self.dynamic_entity.arguments = [name]
        self._search(name)
        sleep(1)
        attemp = 3
        while self.dynamic_entity.return_wait_until_element_is_visible() is False and attemp > 0:
            driver.reload_page()
            self._search(name)
            attemp -= 1
        self.dynamic_checkbox_rpc_multiple_devices.arguments = [name] 
        self.dynamic_checkbox_rpc_multiple_devices.wait_until_element_is_visible()
        self.dynamic_checkbox_rpc_multiple_devices.wait_until_element_is_enabled()
        loop = 10
        while loop > 0:
            class_value = self.dynamic_checkbox_rpc_multiple_devices.get_element_attribute("class")
            if "mat-checkbox-checked" not in class_value:
                try:
                    self.dynamic_checkbox_rpc_multiple_devices.click_element()
                except:
                    self.select_entity_checkbox_by_name(name)
            else:
                break
            sleep(1)
            loop-=1
        
    def get_entity_section_value(self):
        self.span_entity_section.wait_until_element_is_visible()
        value = self.span_entity_section.get_text()
        return value
    
    def get_current_page_title(self):
        self.tb_current_entity_state_controller.wait_until_element_is_visible()
        return self.tb_current_entity_state_controller.get_text()
    
    def click_zoom_in_button(self, repeat=1):
        self.btn_zoom_in.wait_until_element_is_visible()
        while(repeat > 0):
            self.btn_zoom_in.click_element_by_js()
            repeat-=1
        sleep(constants.SELENPY_WAIT_TIMEOUT)
        
    def click_zoom_out_button(self, repeat=1):
        self.btn_zoom_out.wait_until_element_is_visible()
        while(repeat > 0):
            self.btn_zoom_out.click_element_by_js()
            repeat-=1
        sleep(constants.SELENPY_WAIT_TIMEOUT)
    
    def is_widget_disabled(self):
        return self.div_rpc_widget_disable.return_wait_until_element_is_visible()
    
    def get_disabled_widget_message(self):
        return self.div_rpc_widget_disable.get_text()

    def _search(self, entity_name):
        if self.btn_close.is_element_displayed():
            self.btn_close.click_element()
        self.btn_search.wait_until_element_is_clickable()
        self.btn_search.click_element()
        self.txt_search_entity.input_text(entity_name)
        
    def get_background_color_from_style(self, value):
        rgb = ((((value.split("background-color:"))[1]).split(";"))[0]).strip()
        self.logger.info("background-color: %s" % rgb)
        return rgb
    
    def get_scale_value_of_map_panel(self):
        value = self.map_panel_leaflet_zoom_animated.get_element_attribute("style")
        scale_value = (value.split('scale(')[1].split(');')[0]).strip()
        self.logger.info("scale: %s" % scale_value)
        return scale_value
    
    def get_item_per_page_value(self):
        self.lbl_item_per_page.wait_until_element_is_visible()
        self.logger.info("Get Item per page value")
        return self.lbl_item_per_page.get_text()

    def get_paginator_range_label(self):
        self.lbl_paginator_range.wait_until_element_is_visible()
        self.lbl_paginator_range.get_text()
        
    def click_realtime_tab(self):
        self.realtime_tab.click_element()
        
    def select_timeinterval_option(self, value):
        self.tb_timeinterval.wait_until_element_is_clickable()
        self.tb_timeinterval.click_element()
        self.tb_timeinterval_option.arguments = [value]
        self.tb_timeinterval_option.click_element_by_js()
        
    def click_timeinterval_update_btn(self):
        self.tb_timeinterval_update_button.wait_until_element_is_clickable()
        self.tb_timeinterval_update_button.click_element()

    def config_timeinterval(self, value):
        self.click_realtime_tab()
        self.select_timeinterval_option(value)
        self.click_timeinterval_update_btn()
        sleep(constants.SELENPY_DEFAULT_TIMEOUT)
        
    def open_full_screen_timeseries_table(self):
        self.timeseries_full_screen_btn.click_element()
        
    def get_data_in_timeseries_by(self, table_header):
        self.timeseries_rows_by_dynamic_column.arguments = [table_header]
        elements = self.timeseries_rows_by_dynamic_column.get_webelements()
        data = []
        for e in elements:
            try:
                value = e.text
                data.append(value)
            except:
                data.append('')
        self.logger.info(data)
        return data

    
    def wait_for_event_displayed(self, expected_event=None, timeout=720):
        # Wait for build download to complete (Need to Go to Driving Data Page and wait for the event (FW-OTA) displayed)
        # Wait for upgrade/downgrade done (Need to Go to Driving Data Page and wait for the event (Power ON) displayed)
        time_sleepwait = 3
        result = True
        while timeout > 0:
            sleep(time_sleepwait)
            timeout-=time_sleepwait
            result = self.is_event_dispayed_on_map_wiget(expected_event)
            if result:
                break
            
        return result
   

           
    
    