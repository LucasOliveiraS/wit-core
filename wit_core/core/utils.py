import yaml

from ..decorators import dot_notation


@dot_notation
def extract_wit_response(wit_response: dict) -> dict:
    text: str = wit_response["text"]
    intent: str = wit_response["intents"][0]["name"]
    entities: list = wit_response["entities"]
    traits: dict = wit_response["traits"]

    return {
        "text": text,
        "intent": intent,
        "entities": entities,
        "traits": traits
    }


@dot_notation
def load_yaml(file: str) -> dict:
    file = open(file, 'r')
    return yaml.load(file, Loader=yaml.FullLoader)


def rename_entities_keys(dict_arg: dict) -> dict:
    for i in list(dict_arg["entities"]):
        new_name = dict_arg["entities"][i][0]["name"]
        dict_arg["entities"][new_name] = dict_arg["entities"].pop(i)

    return dict_arg
