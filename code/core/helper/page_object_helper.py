import json
from core import root
import os,sys

mPageLocators = {}


def load_locators_for_pages(pages):
    for page in pages:
        load_locator_for_page(page)

    
def load_locator_for_page(sPage):
    
    if sPage in mPageLocators:
        return True

    if "win" in sys.platform:
        locatorFile = os.path.join(os.path.abspath(root), "py_modules","gsx_cloud","locators", "{}.json".format(sPage))
    else:
        locatorFile = os.path.join("py_modules","gsx_cloud","locators", "{}.json".format(sPage))

    if not os.path.exists(locatorFile):
        return False
    
    try:
        lstLocators = None
        with open(locatorFile) as f:
            lstLocators = json.load(f)
            
        isLocatorLoaded = lstLocators is not None
        if isLocatorLoaded:
            mPageLocators[sPage] = lstLocators
        else:
            raise Exception("%s file is invalid syntax or empty" % locatorFile)
        return True
    except Exception:
        return False


def get_page_locators(sPage):
    if mPageLocators is None: return None
    
    return mPageLocators[sPage] if sPage in mPageLocators else None

