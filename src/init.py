import logging

from modules.pytg.ModulesLoader import ModulesLoader

from .ResourcesManager import ResourcesManager

def initialize():
    logging.info("Initializing resources module...")

    ResourcesManager.initialize()

def connect():
    logging.info("Connecting resources module...")

    load_manager().create_loaders()

def load_manager():
    return ResourcesManager.load()

def depends_on():
    return ["config"]