import pytest

from wit_core.core.process import process_intent, process_domain, execute_function
from wit_core.core.domain import prepare_resource

from . import utilities


def test_execute_function(mocker):
    action = mocker.patch("wit_core.core.process.execute_function", return_value="result function")

    assert action("function_default") == "result function"


def test_execute_function_error(mocker):
    mocker.patch("wit_core.core.process.utils.load_module", return_value="module")
    with pytest.raises(AttributeError, match=r".*Not found function to execute: module*"):
        executed_function = execute_function("module", "not_existent_function")


def test_process_domain(mocker, mocked_wit_response):
    wit_response = mocked_wit_response("What’s the weather like?")
    mocker.patch("wit_core.core.process.execute_function", return_value="42")

    resource = prepare_resource(wit_response)

    case_2 = process_domain(("action_default", {"text": "{action_return}"}), resource)
    case_3 = process_domain(("action_default", {"template": "template_default"}), resource)

    assert case_2 == "42"
    assert case_3 == "42"


def test_process_intent_case_1(mocker, mocked_domain):
    mocker.patch("wit_core.core.process.get_user_input", return_value=utilities.greet)
    response = process_intent("Hello, good morning!")

    assert response == "Hello, World!"


def test_process_intent_case_2(mocker, mocked_domain):
    mocker.patch("wit_core.core.process.get_user_input", return_value=utilities.temperature_get)
    mocker.patch("wit_core.core.process.execute_function", return_value="São Paulo")

    response = process_intent("What is the weather like in São Paulo")

    assert response == "The weather is pleasant in São Paulo"


def test_process_intent_case_3(mocker, mocked_domain):
    mocker.patch("wit_core.core.process.get_user_input", return_value=utilities.temperature_set)
    mocker.patch("wit_core.core.process.execute_function", return_value="Turned temperature to 62 degrees")

    response = process_intent("Turn the temperature to 62 degrees")

    assert response == "Turned temperature to 62 degrees"
