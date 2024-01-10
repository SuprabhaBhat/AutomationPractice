import inspect
import logging
import os
if not os.path.exists("Logs"):
    os.makedirs("Logs")
class LogGen:
    @staticmethod
    def loggen():
        #Retrieves the name of the calling function. Index 1-frame of the calling function/index 3 within that frame to function name.
        loggerName= inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("D:\\ApplicationDemoProject\\AutomationApp\\Logs\\automation.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        #to receive logging messages
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger