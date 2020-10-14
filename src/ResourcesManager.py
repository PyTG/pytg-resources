import yaml, os, logging

from modules.pytg.Manager import Manager

from modules.pytg.load import manager

from .loaders.YamlResourcesLoader import YamlResourcesLoader
from .loaders.JsonResourcesLoader import JsonResourcesLoader
from .loaders.PlainResourcesLoader import PlainResourcesLoader

class ResourcesManager(Manager):
    @staticmethod
    def initialize():
        ResourcesManager.__instance = ResourcesManager()

    @staticmethod
    def load():
        return ResourcesManager.__instance

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.__loaders = {}

    def create_loaders(self):
        settings = manager("config").load_settings("resources")

        self.__loaders = {}

        for loader_id in settings["loaders"]:
            self.__loaders[loader_id] = self.__build_loader(loader_id)

        self.__loaders["default"] = self.__loaders[settings["default_loader"]]

    def load_resource(self, module, resource_id, path="", loader = "default"):
        return self.__loaders[loader].load_resource(module, resource_id, path)

    def save_resource(self, module, resource_id, data, path="", loader = "default"):
        return self.__loaders[loader].save_resource(module, resource_id, data, path)

    def __build_loader(self, loader_id):
        if loader_id == "yaml":
            return YamlResourcesLoader()

        if loader_id == "json":
            return JsonResourcesLoader()

        if loader_id == "plain":
            return PlainResourcesLoader()

        self.logger.warning("Unknown loader id '{}'".format(loader_id))

        return None