from wit_core.core.domain import get_entity, get_intent, match_domain, search_intent, prepare_resource, resource_interface, response_text, get_latest_message


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


def test_match_domain(mocked_domain):
    domain = mocked_domain("domain.yaml")

    result_match_case_1 = match_domain(domain["greet"])
    result_match_case_2 = match_domain(domain["temperature_get"])
    result_match_case_3 = match_domain(domain["temperature_set"])

    assert result_match_case_1 == "Hello, World!"
    assert result_match_case_2 == ("action_deafult", {"text": "The weather is pleasant in {action_return}"})
    assert result_match_case_3 == ("action_deafult", {"template": "template_default"})


def test_prepare_resource(mocked_wit_response):
    wit_response = mocked_wit_response("What’s the weather like?")

    resource = prepare_resource(wit_response)

    assert list(resource["resource"]["latest_message"].keys()) == ["text", "intents", "entities", "traits"]


def test_resource_interface(mocked_resource):
    interface = resource_interface(mocked_resource())

    assert interface.get_latest_message == "turn the temperature to 62 degrees"
    assert list(interface.get_intent.keys()) == ["id", "name", "confidence"]
    assert list(interface.get_entity("wit$temperature").keys()) == ["id", "name", "role", "start", "end", "body", "confidence", "entities", "unit", "type", "value"]
    assert list(interface.get_traits("test").keys()) == ["value"]


def test_get_latest_message(mocked_resource):
    latest_message = get_latest_message(mocked_resource())

    assert latest_message == "turn the temperature to 62 degrees"


def test_get_intent(mocked_resource):
    intent = get_intent(mocked_resource())

    assert list(intent.keys()) == ["id", "name", "confidence"]


def test_get_entity(mocked_resource):
    entity = get_entity(mocked_resource())

    assert list(entity("wit$temperature").keys())== ["id", "name", "role", "start", "end", "body", "confidence", "entities", "unit", "type", "value"]


def get_trait(mocked_resource):
    traits = get_trait(mocked_resource())

    assert list(traits("test").keys()) == ["value"]


def test_response_text():
    text = response_text(text="Response text")
    text_action = response_text("This is a {action_return}", "Super test!")

    assert text == "Response text"
    assert text_action == "This is a Super test!"
