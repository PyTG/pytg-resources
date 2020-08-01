import logging, yaml, os

from modules.pytg.ModulesLoader import ModulesLoader

from .ResourcesManager import ResourcesManager

logger = logging.getLogger(__name__)

class YamlResourcesManager(ResourcesManager):
    @staticmethod
    def initialize():
        YamlResourcesManager.__instance = YamlResourcesManager()

        return

    @staticmethod
    def load():
        return YamlResourcesManager.__instance

    def load_resource(self, module, resource_id, path=""):
        module_folder = ModulesLoader.get_module_content_folder(module)

        try:
            return yaml.safe_load(open("{}/{}/{}.yaml".format(module_folder, path, resource_id), "r"))
        except FileNotFoundError:
            logger.warn("Trying to access missing resource '{}/{}' in module {}".format(path, resource_id, module))

            return None

    def save_resource(self, module, resource_id, data, path=""):
        module_folder = ModulesLoader.get_module_content_folder(module)

        yaml.safe_dump(data, open("{}/{}/{}.yaml".format(module_folder, path, resource_id), "w"))