from typing import Any
from pathlib import Path

from .domain import search_intent, match_domain, prepare_resource, \
    response_text
from ..actions import actions
from ..templates import templates
from ..chatbot import get_user_input
from . import utils


def process_intent(user_input: str) -> str:
    wit_response = get_user_input(user_input)

    domain = utils.load_yaml(Path("wit_core/") / "domain.yaml")

    intent_properties = search_intent(
        wit_response["intents"][0]["name"], domain)

    result = match_domain(intent_properties)

    if isinstance(result, str):
        return result

    resource = prepare_resource(wit_response)

    response = process_domain(result, resource)

    return response


def execute_action_function(func, arg=None) -> Any:
    if getattr(actions, func, None) is None:
        raise AttributeError("Not found action to execute")

    try:
        return getattr(actions, func)(arg)
    except Exception as error:
        return error


def execute_template_function(func, arg=None) -> Any:
    if getattr(templates, func, None) is None:
        raise AttributeError("Not found template to execute")

    try:
        return getattr(templates, func)(arg)
    except Exception as error:
        return error


def process_domain(x: tuple, resource: dict) -> str:
    action_domain = x[0]
    response_domain = x[1]

    result_action = execute_action_function(action_domain, resource)

    if "text" in response_domain:
        return response_text(response_domain["text"], result_action)

    if "template" in response_domain:
        result_template = execute_template_function(
            response_domain["template"], result_action)

        return result_template
