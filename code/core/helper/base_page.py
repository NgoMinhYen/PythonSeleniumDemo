from element import element_factory
from core.helper import page_object_helper

class BasePage():
        
    @classmethod
    def get_classname(cls):
        return cls.__name__

    @classmethod
    def get_parent_classname(cls):
        """
        Return the classname of the first parent class
        """
        return cls.__bases__[0].get_classname()
    
    def __init__(self):
        self._page_names = [ self.get_classname(), self.get_parent_classname() ]
        page_object_helper.load_locators_for_pages(self._page_names)
    
    def element(self, locator_name, target_class=None):
        return element_factory.get_defined_element(self._page_names, locator_name, target_class)
    