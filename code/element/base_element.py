from abc import ABCMeta

class BaseElement():
    
    __metaclass__ = ABCMeta

    def __init__(self, locator, parent=None):
        self._locator = locator
        self._args = []
        self.parent = parent
    
    @property
    def arguments(self):
        return self._args
    
    @arguments.setter
    def arguments(self, args):
        self._args = args
    
    def locator(self):
        if self.parent:
            return self.parent.locator() + self._locator.format(*self._args)
        return self._locator.format(*self._args)

