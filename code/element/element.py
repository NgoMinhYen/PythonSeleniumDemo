from core import elementKeywords, formElementKeywords, waitingKeywords, selectElementKeywords, \
    tableElementKeywords
from element.base_element import BaseElement
from core.driver import driver
from core.config import constants
import time
from selenium.common.exceptions import StaleElementReferenceException, \
    ElementNotInteractableException, \
    NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from core.helper.waiter import Waiter
from core.helper.gsx_logger import Logger


class Element(BaseElement):

    def get_webelement(self):
        try:
            return elementKeywords.get_webelement(self.locator())
        except NoSuchElementException:
            Logger.error("Element with locator: %s is not found" % self.locator())

    def get_webelements(self):
        return elementKeywords.get_webelements(self.locator())

    def get_element_attribute(self, attribute, timeout=constants.SELENPY_WAIT_TIMEOUT):
        elapse_time = 1
        try:
            if (timeout > 0):
                return elementKeywords.get_element_attribute(self.locator(), attribute)
        except StaleElementReferenceException or ElementNotInteractableException or NoSuchElementException:
            elapse_time += 1
            self.get_element_attribute(attribute, (timeout - elapse_time))

    def get_horizontal_position(self):
        return elementKeywords.get_horizontal_position(self.locator())

    def get_element_size(self):
        return elementKeywords.get_element_size(self.locator())

    def cover_element(self):
        elementKeywords.cover_element(self.locator())

    def get_value(self, timeout=constants.SELENPY_WAIT_TIMEOUT):
        elapse_time = 1
        try:
            if (timeout > 0):
                return elementKeywords.get_value(self.locator())
        except StaleElementReferenceException or ElementNotInteractableException:
            elapse_time += 1
            self.get_value((timeout - elapse_time))

    def get_text(self, timeout=constants.SELENPY_WAIT_TIMEOUT):
        elapse_time = 1
        try:
            if (timeout > 0):
                return elementKeywords.get_text(self.locator())
        except StaleElementReferenceException or ElementNotInteractableException:
            elapse_time += 1
            self.get_text((timeout - elapse_time))

    def clear_element_text(self):
        elementKeywords.clear_element_text(self.locator())

    def get_vertical_position(self):
        return elementKeywords.get_vertical_position(self.locator())

    def click_button(self, modifier=False):
        elementKeywords.click_button(self.locator(), modifier)

    def click_image(self, modifier=False):
        elementKeywords.click_image(self.locator(), modifier)

    def click_link(self, modifier=False):
        elementKeywords.click_link(self.locator(), modifier)

    def click_element(self, modifier=False, action_chain=False, timeout=constants.SELENPY_WAIT_TIMEOUT):
        elapse_time = 1
        try:
            if (timeout > 0):
                elementKeywords.click_element(self.locator(), modifier, action_chain)
        except StaleElementReferenceException or ElementNotInteractableException:
            elapse_time += 1
            self.click_element(modifier, action_chain, (timeout - elapse_time))

    def click_element_by_js(self, timeout=constants.SELENPY_WAIT_TIMEOUT):
        Logger.info("Clicking element {0}".format(self.locator()))
        elapse_time = 1
        try:
            if (timeout > 0):
                driver.execute_javascript("arguments[0].click();", self.get_webelement())
        except StaleElementReferenceException or ElementNotInteractableException:
            elapse_time += 1
            self.click_element_by_js((timeout - elapse_time))

    def double_click_element(self, timeout=constants.SELENPY_WAIT_TIMEOUT):
        elapse_time = 1
        try:
            if (timeout > 0):
                elementKeywords.double_click_element(self.locator())
        except StaleElementReferenceException or ElementNotInteractableException:
            elapse_time += 1
            self.double_click_element(timeout - elapse_time)

    def removeAttribute(self, attribute):
        Logger.info("Remove attribute {0} on element {1}".format(attribute, self.locator()))
        driver.execute_javascript("arguments[0].removeAttribute('{0}')".format(attribute), self.get_webelement())

    def is_element_visible(self):
        try:
            return driver.execute_javascript("function isVisible(e){var t=e.getBoundingClientRect(),"
                                             + "n=document.elementFromPoint(t.x+t.width/2,t.y+t.height/2),"
                                             + "i=!1;for(let t=0;t<3;t++)e==n?i=!0:n=n.parentElement;return i}"
                                             + "return isVisible(arguments[0]);", self.get_webelement())

        except:
            return False

    def is_element_present(self):
        try:
            return self.get_webelement() is not None
        except:
            return False

    def is_element_displayed(self):
        return elementKeywords.is_visible(self.locator())

    def is_element_enabled(self):
        if self.get_element_attribute("disabled") == "true":
            return False
        else:
            return True

    def is_element_disabled(self):
        if self.is_element_enabled():
            return False
        else:
            return True

    def get_element_count(self):
        return elementKeywords.get_element_count(self.locator())

    def set_focus_to_element(self):
        elementKeywords.set_focus_to_element(self.locator())

    def scroll_element_into_view(self):
        elementKeywords.scroll_element_into_view(self.locator())

    def drag_and_drop(self, target):
        elementKeywords.drag_and_drop(self.locator(), target)

    def drag_and_drop_by_offset(self, xOffSet, yOffSet):
        elementKeywords.drag_and_drop_by_offset(self.locator(), xOffSet, yOffSet)

    def mouse_over(self, timeout=constants.SELENPY_DEFAULT_TIMEOUT):
        elapse_time = 1
        try:
            if (timeout > 0):
                action = ActionChains(driver.get_driver())
                web_element = self.get_webelement()
                size = self.get_element_size()
                width = size[0]
                height = size[1]
                action.move_to_element_with_offset(web_element, 1, 1).move_by_offset(int(width / 2),
                                                                                     int(height / 2)).perform()
        except StaleElementReferenceException:
            elapse_time += 1
            self.mouse_over((timeout - elapse_time))

    def mouse_down(self):
        elementKeywords.mouse_down(self.locator())

    def mouse_out(self):
        elementKeywords.mouse_out(self.locator())

    def mouse_up(self):
        elementKeywords.mouse_up(self.locator())

    def open_context_menu(self):
        elementKeywords.open_context_menu(self.locator())

    def simulate_event(self, event):
        elementKeywords.simulate_event(self.locator(), event)

    def press_keys(self, *keys):
        elementKeywords.press_keys(self.locator(), keys)

    def press_key(self, key):
        elementKeywords.press_key(self.locator(), key)

    def get_all_links(self):
        return elementKeywords.get_all_links()

    def mouse_down_on_link(self):
        elementKeywords.mouse_down_on_link(self.locator())

    def mouse_down_on_image(self):
        elementKeywords.mouse_down_on_image(self.locator())

    def add_location_strategy(self, strategy_name, strategy_keyword, persist=False):
        elementKeywords.add_location_strategy(strategy_name, strategy_keyword, persist)

    def remove_location_strategy(self, strategy_name):
        elementKeywords.remove_location_strategy(strategy_name)

    def parse_modifier(self, modifier):
        elementKeywords.parse_modifier(modifier)

    def get_element_size_and_position(self):
        """return an array including [top,left,width,height]"""
        top = self.get_vertical_position()
        left = self.get_horizontal_position()
        width = self.get_element_size()[0]
        height = self.get_element_size()[1]

        return [top, left, width, height]

    def drag_left_border(self, changedWidth=0):
        action = ActionChains(driver.get_driver())
        web_element = self.get_webelement()
        size = self.get_element_size()
        width = size[0]
        height = size[1]
        xOffset = width - changedWidth

        action.move_to_element_with_offset(web_element, 0, int(height / 2)).perform()
        action.click_and_hold().move_by_offset(xOffset, 0).perform()
        action.release(web_element).perform()
        action.reset_actions()

    def select_area(self, sourceCoordinate, destinationCoordinate):
        action = ActionChains(driver.get_driver())
        web_element = self.get_webelement()
        action.move_to_element_with_offset(web_element, sourceCoordinate[0], sourceCoordinate[1]).perform()
        action.key_down(Keys.ALT).click_and_hold().move_by_offset(destinationCoordinate[0] - sourceCoordinate[0],
                                                                  destinationCoordinate[1] - sourceCoordinate[
                                                                      1]).key_up(Keys.ALT).perform()
        action.release().perform()
        action.reset_actions()

    def _return_running_method(self, functionName, *args):
        try:
            functionName(*args)
            return True
        except:
            return False

    def return_wait_until_element_is_visible(self, timeout=constants.SELENPY_SHORT_TIMEOUT):
        return self._return_running_method(self.wait_until_element_is_visible, timeout)
    
    def return_wait_until_element_is_clickable(self, timeout=constants.SELENPY_SHORT_TIMEOUT):
        return self._return_running_method(self.wait_until_element_is_clickable, timeout)

    def return_wait_until_element_is_not_visible(self, timeout=constants.SELENPY_SHORT_TIMEOUT):
        return self._return_running_method(self.wait_until_element_is_not_visible, timeout)

    def return_wait_until_element_contains(self, text, timeout=constants.SELENPY_SHORT_TIMEOUT):
        return self._return_running_method(self.wait_until_element_contains, text, timeout)

    def return_wait_until_element_does_not_contain(self, text, timeout=constants.SELENPY_SHORT_TIMEOUT):
        return self._return_running_method(self.wait_until_element_does_not_contain, text, timeout)

    def return_wait_until_element_value_contains(self, value, timeout=constants.SELENPY_SHORT_TIMEOUT):
        return self._return_running_method(self.wait_until_element_attribute_contains, "value", str(value), timeout)

    def return_wait_until_element_value_does_not_contain(self, value, timeout=constants.SELENPY_SHORT_TIMEOUT):
        return self._return_running_method(self.wait_until_element_attribute_does_not_contain, "value", str(value),
                                           timeout)

    def return_wait_until_element_attribute_contains(self, attribute, value, timeout=constants.SELENPY_SHORT_TIMEOUT):
        return self._return_running_method(self.wait_until_element_attribute_contains, attribute, str(value), timeout)

    def return_wait_until_element_attribute_does_not_contain(self, attribute, value,
                                                             timeout=constants.SELENPY_SHORT_TIMEOUT):
        return self._return_running_method(self.wait_until_element_attribute_does_not_contain, attribute, str(value),
                                           timeout)

    def wait_until_element_contains(self, text, timeout=constants.SELENPY_SHORT_TIMEOUT):
        Logger.info("Waiting for element {0} contains text '{1}'".format(self.locator(), text))
        #         waitingKeywords.wait_until_element_contains(self.locator(), text, timeout, error)
        timeoutMil = time.time() + timeout
        while time.time() <= timeoutMil:
            element_text = self.get_text()
            if str(text) in str(element_text):
                break
            time.sleep(constants.SELENPY_WAIT_TIMEOUT)

    def wait_until_element_does_not_contain(self, text, timeout=constants.SELENPY_SHORT_TIMEOUT, error=None):
        Logger.info("Waiting for element {0} does not contain text '{1}'".format(self.locator(), text))
        #         waitingKeywords.wait_until_element_does_not_contain(self.locator(), text, timeout, error)
        timeoutMil = time.time() + timeout
        while time.time() <= timeoutMil:
            element_text = self.get_text()
            if str(text) not in str(element_text):
                break
            time.sleep(constants.SELENPY_WAIT_TIMEOUT)

    def wait_until_element_is_visible(self, timeout=constants.SELENPY_SHORT_TIMEOUT, error=None):
        Logger.info("Waiting for element {0} to be visible".format(self.locator()))
        waitingKeywords.wait_until_element_is_visible(self.locator(), timeout, error)

    def wait_until_element_is_not_visible(self, timeout=constants.SELENPY_SHORT_TIMEOUT, error=None):
        Logger.info("Waiting for element {0} to be not visible".format(self.locator()))
        waitingKeywords.wait_until_element_is_not_visible(self.locator(), timeout, error)

    def wait_until_element_is_enabled(self, timeout=constants.SELENPY_SHORT_TIMEOUT, error=None):
        Logger.info("Waiting for element {0} to be enable".format(self.locator()))
        waitingKeywords.wait_until_element_is_enabled(self.locator(), timeout, error)

    def wait_until_element_is_disabled(self, timeout=constants.SELENPY_SHORT_TIMEOUT, error=None):
        Logger.info("Waiting for element {0} to be disable".format(self.locator()))
        waitingKeywords._wait_until(
            lambda: not waitingKeywords.is_element_enabled(self.locator()),
            "Element '%s' was not disabled in <TIMEOUT>." % self.locator(),
            timeout, error
        )

    def wait_until_page_contains_element(self, timeout=constants.SELENPY_SHORT_TIMEOUT, error=None):
        Logger.info("Waiting for element {0} to be displayed on DOM".format(self.locator()))
        waitingKeywords.wait_until_page_contains_element(self.locator(), timeout, error)

    def wait_until_page_does_not_contain_element(self, timeout=constants.SELENPY_SHORT_TIMEOUT, error=None):
        Logger.info("Waiting for element {0} to be not displayed on DOM".format(self.locator()))
        waitingKeywords.wait_until_page_does_not_contain_element(self.locator(), timeout, error)

    def wait_until_element_attribute_contains(self, attribute, value, timeout=constants.SELENPY_SHORT_TIMEOUT):
        Logger.info("Waiting for element {0} attribute '{1}' to contain '{2}'".format(self.locator(), attribute, value))
        timeoutMil = time.time() + timeout
        while time.time() <= timeoutMil:
            attValue = self.get_element_attribute(attribute)
            if str(value) in str(attValue):
                break
            time.sleep(constants.SELENPY_WAIT_TIMEOUT)

    def wait_until_element_attribute_does_not_contain(self, attribute, value,
                                                      timeout=constants.SELENPY_SHORT_TIMEOUT):
        Logger.info(
            "Waiting for element {0} attribute '{1}' to not contain '{2}'".format(self.locator(), attribute, value))
        timeoutMil = time.time() + timeout
        while time.time() <= timeoutMil:
            attValue = self.get_element_attribute(attribute)
            if str(value) not in str(attValue):
                break
            time.sleep(constants.SELENPY_WAIT_TIMEOUT)

    def wait_until_element_text_displays(self, text, timeout=constants.SELENPY_SHORT_TIMEOUT):
        Waiter.wait_for_element_text_displayed(driver.get_driver(), self.locator(), text, timeout)

    def wait_until_element_is_clickable(self, timeout=constants.SELENPY_SHORT_TIMEOUT):
        Waiter.wait_for_element_to_be_clickable(driver.get_driver(), self.locator(), timeout)

    def input_text(self, text, clear=True, timeout=constants.SELENPY_WAIT_TIMEOUT):
        elapse_time = 0
        try:
            if timeout > 0:
                if text is not None:
                    if text != "":
                        formElementKeywords.input_text(self.locator(), text, clear)
                    else:
                        self.set_focus_to_element()
                        self.press_key("\\1")
                        self.press_key("\\127")
        except StaleElementReferenceException:
            elapse_time += 1
            self.input_text(text, clear, (timeout - elapse_time))

    def input_password(self, password, clear=True):
        formElementKeywords.input_password(self.locator(), password, clear)

    def submit_form(self, locator=None):
        formElementKeywords.submit_form(locator)

    def select_checkbox(self):
        formElementKeywords.select_checkbox(self.locator())

    def unselect_checkbox(self):
        formElementKeywords.unselect_checkbox(self.locator())

    def select_radio_button(self, group_name, value):
        formElementKeywords.select_radio_button(group_name, value)

    def choose_file(self, file_path):
        formElementKeywords.choose_file(self.locator(), file_path)

    def is_selected(self):
        webElement = formElementKeywords._get_checkbox(self.locator())
        return webElement.is_selected()

    def get_list_items(self, values=False):
        return selectElementKeywords.get_list_items(self.locator(), values)

    def get_selected_list_label(self):
        return selectElementKeywords.get_selected_list_label(self.locator())

    def get_selected_list_labels(self):
        return selectElementKeywords.get_selected_list_labels(self.locator())

    def get_selected_list_value(self):
        return selectElementKeywords.get_selected_list_value(self.locator())

    def get_selected_list_values(self):
        return selectElementKeywords.get_selected_list_values(self.locator())

    def select_all_from_list(self):
        selectElementKeywords.select_all_from_list(self.locator())

    def select_from_list_by_index(self, *indexes):
        selectElementKeywords.select_from_list_by_index(self.locator(), indexes)

    def select_from_list_by_value(self, *values):
        selectElementKeywords.select_from_list_by_value(self.locator(), values)

    def select_from_list_by_label(self, label):
        selectElementKeywords.select_from_list_by_label(self.locator(), str(label))

    def unselect_all_from_list(self):
        selectElementKeywords.unselect_all_from_list(self.locator())

    def unselect_from_list_by_index(self, *indexes):
        selectElementKeywords.unselect_from_list_by_index(self.locator(), indexes)

    def unselect_from_list_by_value(self, *values):
        selectElementKeywords.unselect_from_list_by_value(self.locator(), values)

    def unselect_from_list_by_label(self, *labels):
        selectElementKeywords.unselect_from_list_by_label(self.locator(), labels)

    def get_table_cell(self, row, column, loglevel='TRACE'):
        return tableElementKeywords.get_table_cell(self.locator(), row, column, loglevel)

    def does_table_contain(self, expected, loglevel='TRACE'):
        return self._return_running_method(
            tableElementKeywords.table_should_contain(self.locator(), expected, loglevel))