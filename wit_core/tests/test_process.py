import pytest

from wit_core.core.process import process_intent, process_domain
from wit_core.actions.actions import execute_action_function
from wit_core.templates.templates import execute_template_function
from wit_core.core.domain import prepare_resource

from . import utilities


def test_execute_action_function(mocker):
    action = mocker.patch("wit_core.actions.actions.execute_action_function", return_value="result action")

    assert action("action_default") == "result action"


def test_execute_action_function_error(mocker):
    mocker.patch("wit_core.actions.actions.load_module", return_value="actions")
    with pytest.raises(AttributeError, match=r".*Not found action to execute*"):
        executed_function = execute_action_function("not_existent_function")


def test_execute_template_function(mocker):
    teste = mocker.patch("wit_core.templates.templates.execute_template_function", return_value="result template")

    assert teste("template_default") == "result template"


def test_execute_template_function_error(mocker):
    mocker.patch("wit_core.templates.templates.load_module", return_value="templates")
    with pytest.raises(AttributeError, match=r".*Not found template to execute*"):
        executed_function = execute_template_function("not_existent_template")


def test_process_domain(mocker, mocked_wit_response):
    wit_response = mocked_wit_response("What’s the weather like?")
    action_result = mocker.patch("wit_core.core.process.execute_action_function", return_value="42")
    mocker.patch("wit_core.core.process.execute_template_function", return_value="Response is " + action_result())

    resource = prepare_resource(wit_response)

    case_2 = process_domain(("action_default", {"text": "Response is {action_return}"}), resource)
    case_3 = process_domain(("action_default", {"template": "template_default"}), resource)

    assert case_2 == "Response is 42"
    assert case_3 == "Response is 42"


def test_process_intent_case_1(mocker, mocked_domain):
    mocker.patch("wit_core.core.process.get_user_input", return_value=utilities.greet)
    response = process_intent("Hello, good morning!")

    assert response == "Hello, World!"


def test_process_intent_case_2(mocker, mocked_domain):
    mocker.patch("wit_core.core.process.get_user_input", return_value=utilities.temperature_get)
    mocker.patch("wit_core.core.process.execute_action_function", return_value="São Paulo")

    response = process_intent("What is the weather like in São Paulo")

    assert response == "The weather is pleasant in São Paulo"


def test_process_intent_case_3(mocker, mocked_domain):
    mocker.patch("wit_core.core.process.get_user_input", return_value=utilities.temperature_set)
    result_action = mocker.patch("wit_core.core.process.execute_action_function", return_value="62")
    mocker.patch("wit_core.core.process.execute_template_function", return_value="Turned temperature to " + result_action() + " degrees")

    response = process_intent("Turn the temperature to 62 degrees")

    assert response == "Turned temperature to 62 degrees"
