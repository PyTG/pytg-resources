import logging

from pytg.load import manager

from .ResourcesManager import ResourcesManager

def connect():
    logging.info("Connecting resources module...")

    manager("bot").create_loaders()

def initialize_manager():
    return ResourcesManager()

def depends_on():
    return ["config"]