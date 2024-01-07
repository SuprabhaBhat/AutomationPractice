#Utility: get data from ini and provide it to testcases
import configparser

config=configparser.RawConfigParser()
config.read(".\\Confgurations\\config.ini")

class ReadConfig:
    # can access dirctly using class name without object
    @staticmethod
    def getApplicationURL():
        url = config.get('common data','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common data','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data','password')
        return password