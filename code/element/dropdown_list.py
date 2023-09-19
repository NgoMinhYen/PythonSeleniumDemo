from core.element.element import Element


class DropDownList(Element):
    
    def __init__(self, locator):
        self.dropdown_list = Element(locator)

    def _get_select_option(self, option):
        locator = "//mat-option[normalize-space(span)='%s']" % option
        select_option = Element(locator)
        return select_option
    
    def _expand_dropdown_list(self):
        self.dropdown_list.wait_until_element_is_clickable()
        self.dropdown_list.click_element_by_js()
    
    def select_by_text(self, text):
        is_selected = self.is_option_selected(text)
        select_option = self._get_select_option(text)
        while is_selected == False:
            if select_option.return_wait_until_element_is_visible() == False:
                self._expand_dropdown_list()
                select_option.wait_until_element_is_visible()
                select_option.click_element_by_js()
                is_selected = self.is_option_selected(text)
        
    def get_selected_value(self):
        locator = "{0}//span[text()]".format(self.dropdown_list.locator())
        selected = Element(locator)
        selected.wait_until_element_is_visible()
        value = selected.get_text()
        return value
    
    def is_option_selected(self, option):
        current_value = self.get_selected_value()
        if current_value == option:
            return True
        else:
            return False