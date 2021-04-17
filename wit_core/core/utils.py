import importlib.util
import pathlib
import yaml

from ..decorators import dot_notation


@dot_notation
def load_yaml(file: str) -> dict:
    file = open(file, 'r')
    return yaml.load(file, Loader=yaml.FullLoader)


def rename_entities_keys(dict_arg: dict) -> dict:
    for i in list(dict_arg["entities"]):
        new_name = dict_arg["entities"][i][0]["name"]
        dict_arg["entities"][new_name] = dict_arg["entities"].pop(i)

    return dict_arg


def load_module(module_name, file_path):
    module_name = str(pathlib.Path().absolute()) + "/" + module_name
    file_path = module_name + "/" + file_path

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
