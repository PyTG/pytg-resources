import logging

from modules.resources.YamlResourcesManager import YamlResourcesManager

def initialize():
    logging.info("Initializing resources module...")

    YamlResourcesManager.initialize()

def connect():
    pass

def load_manager():
    return YamlResourcesManager.load()

def depends_on():
    return []