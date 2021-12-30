import configparser
from os.path import exists

class ConfigHandler:
    """
    Handles the configuration files and the parsing for the file
    """

    def __init__(self):
        self.configFile = "config.ini"
        self.DbFile = self.getDbFile()

    def getDbFile(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config["DB"]["DatabaseFileName"]    
    
    def fileExists(self):
        if exists(self.configFile):
            return True
        return False
        

