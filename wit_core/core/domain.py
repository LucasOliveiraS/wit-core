from pampy import match, _

from ..decorators import dot_notation


def search_intent(intent: str, domain_dict: dict) -> dict:
    if intent in domain_dict:
        return domain_dict[intent]

    return "Not found intent in domain"


def match_domain(intent_properties):
    result = match(intent_properties,
                   {"action": _, "response": {"template": _}},
                   lambda action, template: (action, {"template": template}),
                   {"action": _, "response": {"text": _}},
                   lambda action, text: (action, {"text": text}),
                   {"response": {"text": _}}, lambda text: text,
                   )

    return result


@dot_notation
def prepare_resource(wit_response: dict) -> dict:
    resource: dict = {"resource": {"latest_message": {}}}

    (resource["resource"]
        ["latest_message"]["text"]) = wit_response["text"]
    (resource["resource"]
        ["latest_message"]["intents"]) = wit_response["intents"]
    (resource["resource"]
        ["latest_message"]["entities"]) = wit_response["entities"]
    (resource["resource"]
        ["latest_message"]["traits"]) = wit_response["traits"]

    return resource


@dot_notation
def resource_interface(resource):
    return {
        "get_latest_message": get_latest_message(resource),
        "get_intent": get_intent(resource),
        "get_entity": get_entity(resource),
        "get_traits": get_trait(resource),
    }


def get_latest_message(resource: dict) -> str:
    return resource["resource"]["latest_message"]["text"]


@dot_notation
def get_intent(resource: dict) -> dict:
    return resource["resource"]["latest_message"]["intents"][0]


def get_entity(resource: dict):
    @dot_notation
    def execute(entity_name: str) -> dict:
        return (resource["resource"]["latest_message"]
                ["entities"][entity_name][0])

    return execute


def get_trait(resource: dict):
    @dot_notation
    def execute(trait_name: str) -> dict:
        return resource["resource"]["latest_message"]["traits"][trait_name][0]

    return execute


def response_text(text: str, result_action: str = None) -> str:
    if result_action:
        return text.format(action_return=result_action)

    return text
