import yaml, os

from modules.pytg.Manager import Manager

from modules.pytg.ModulesLoader import ModulesLoader

class ResourcesManager(Manager):
    def load_resource(self, module, resource_id, path=""):
        raise NotImplementedError

    def save_resource(self, module, resource_id, data, path=""):
        raise NotImplementedError