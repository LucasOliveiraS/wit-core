from typing import Any
from pathlib import Path

from .domain import search_intent, match_domain, prepare_resource, \
    resource_interface, response_text
from ..chatbot import get_user_input
from . import utils


def process_intent(user_input: str) -> str:
    wit_response = get_user_input(user_input)

    domain = utils.load_yaml(Path.cwd() / "domain.yaml")

    intent_properties = search_intent(
        wit_response["intents"][0]["name"], domain)

    result_match = match_domain(intent_properties)

    if isinstance(result_match, str):
        return result_match

    resource = prepare_resource(wit_response)

    interface = resource_interface(resource)

    response = process_domain(result_match, interface)

    return response


def process_domain(x: tuple, resource: dict) -> str:
    action_domain = x[0]
    response_domain = x[1]

    result_action = execute_function("actions", action_domain, resource)

    if "text" in response_domain:
        return response_text(response_domain["text"], result_action)

    if "template" in response_domain:
        result_template = execute_function(
            "templates", response_domain["template"], result_action)

        return result_template


def execute_function(module: str, func, arg=None) -> Any:
    module = utils.load_module(module, module + ".py")

    if getattr(module, func, None) is None:
        raise AttributeError("Not found function to execute: " + module)

    try:
        if not arg:
            return getattr(module, func)()
        else:
            return getattr(module, func)(arg)
    except Exception as error:
        return error
