from wit_core.core.domain import search_intent, prepare_resource, resource_interface, response_text


def test_search_intent(mocked_domain):
    domain = mocked_domain("domain.yaml")
    
    result_search_1 = search_intent("greet", domain)
    result_search_2 = search_intent("temperature_get", domain)
    result_search_3 = search_intent("temperature_set", domain)

    assert set(["response"]).issubset(list(result_search_1.keys()))
    assert set(["action", "response"]).issubset(list(result_search_2.keys()))
    assert set(["action", "response"]).issubset(list(result_search_3.keys()))


def test_search_intent_error(mocked_domain):
    domain = mocked_domain("domain.yaml")
    intent = "not_existent_intent"
    
    result_search = search_intent(intent, domain)

    assert result_search == "Not found intent in domain"


def test_resource_interface(mocked_wit_response):
    wit_response = mocked_wit_response("What’s the weather like?")

    interface = prepare_resource(wit_response)

    assert interface.get_latest_message == "turn the temperature to 62 degrees"
    assert list(interface.get_intent.keys()) == ["id", "name", "confidence"]
    assert list(interface.get_entity("wit$temperature:temperature").keys()) == ["id", "name", "role", "start", "end", "body", "confidence", "entities", "unit", "type", "value"]
    assert list(interface.get_traits("test").keys()) == ["value"]


def test_response_text():
    text = response_text(text="Response text")
    text_action = response_text("This is a {action_return}", "Super test!")

    assert text == "Response text"
    assert text_action == "This is a Super test!"
