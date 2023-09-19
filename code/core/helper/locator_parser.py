from selenium.webdriver.common.by import By

class LocatorParser():
    
    @staticmethod
    def parse_string_to_locator(locator_string):
        by = None
        value = None
        
        arr = locator_string.split("=", 1)
        if( len(arr) == 2):            
            tp = arr[0]
            if tp == 'xpath':
                by = By.XPATH
            elif tp  == 'class-name':
                by = By.CLASS_NAME
            elif tp  == 'css':
                by = By.CSS_SELECTOR
            elif tp  == 'id':
                by = By.ID
            elif tp  == 'name':
                by = By.NAME
            elif tp  == 'tag-name':
                by = By.TAG_NAME
            elif tp  == 'link-text':
                by = By.LINK_TEXT
            elif tp  == 'partial-link-text':
                by = By.PARTIAL_LINK_TEXT
            else:
                by = By.XPATH
                
            if by is not None:
                value = arr[1]
                return [by, value]
        
        return None
        