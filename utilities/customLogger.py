import inspect
import logging
import os
if not os.path.exists("Logs"):
    os.makedirs("Logs")
class LogGen:
    @staticmethod
    def loggen():
        loggerName= inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("D:\\ApplicationDemoProject\\AutomationApp\\Logs\\automation.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger