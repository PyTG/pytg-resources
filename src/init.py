import logging

from modules.pytg.ModulesLoader import ModulesLoader

from .YamlResourcesManager import YamlResourcesManager

MANAGER_CLASS = None

def initialize():
    logging.info("Initializing resources module...")

    config_manager = ModulesLoader.load_manager("config")

    settings = config_manager.load_settings_file("resources")
    
    MANAGER_CLASS = __get_manager_class(settings["format"])

    MANAGER_CLASS.initialize()

def connect():
    pass

def load_manager():
    return MANAGER_CLASS.load()

def __get_manager_class(format):
    if format == "yaml":
        return YamlResourcesManager

    return None

def depends_on():
    return ["config"]