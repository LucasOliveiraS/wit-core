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
