import pytest


@pytest.fixture
def mocked_wit_response(mocker):
    wit_json = {
        "text":"turn the temperature to 62 degrees",
        "intents":[
            {
                "id":"240369317812131",
                "name":"temperature_get",
                "confidence":0.9963
            }
        ],
        "entities":{
            "wit$temperature:temperature":[
                {
                    "id":"305684514486650",
                    "name":"wit$temperature",
                    "role":"temperature",
                    "start":24,
                    "end":34,
                    "body":"62 degrees",
                    "confidence":0.9787,
                    "entities":[
                        
                    ],
                    "unit":"degree",
                    "type":"value",
                    "value":62
                }
            ]
        },
        "traits":{
            "test": [
                {
                    "value":62
                }
            ]
        }
    }

    return mocker.patch("wit_core.chatbot.get_user_input", return_value=wit_json)


@pytest.fixture
def mocked_domain(mocker):
    domain_dict = {
        "greet": {
            "response": {
                "text": "Hello, World!"
            }
        },
        "temperature_get": {
            "action": "action_deafult",
            "response": {
                "text": "The weather is pleasant in {action_return}"
            }
        },
        "temperature_set":{
            "action": "action_deafult",
            "response": {
                "template": "template_default"
            }
        }
    }

    return mocker.patch("wit_core.core.utils.load_yaml", return_value=domain_dict)


@pytest.fixture
def mocked_resource(mocker):
    resource = {
        "resource":{
            "latest_message":{
                "text":"turn the temperature to 62 degrees",
                "intents": [{
                    "id":"240369317812131",
                    "name":"temperature_get",
                    "confidence":0.9963
                }],
                "entities":
                    {
                        "wit$temperature":[
                            {
                                "id":"305684514486650",
                                "name":"wit$temperature",
                                "role":"temperature",
                                "start":24,
                                "end":34,
                                "body":"62 degrees",
                                "confidence":0.9787,
                                "entities":[
                                    
                                ],
                                "unit":"degree",
                                "type":"value",
                                "value":62
                            }
                        ]
                    }
                ,
                "traits":
                    {
                        "test": [
                            {
                                "value":62
                            }
                        ]
                    }
            }
        }
    }

    return mocker.patch("wit_core.core.domain.prepare_resource", return_value=resource)
