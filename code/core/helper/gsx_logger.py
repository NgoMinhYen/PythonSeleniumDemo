
import logging

class Logger():
    LOGGER = logging.getLogger("Waiter")
    
    @staticmethod
    def info(message):
        Logger.LOGGER.info(message)
    
    @staticmethod
    def warn(message):
        Logger.LOGGER.warn(message)
        
    @staticmethod
    def error(message):
        Logger.LOGGER.error(message)