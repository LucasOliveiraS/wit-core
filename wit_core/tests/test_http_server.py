import pytest
from fastapi.testclient import TestClient

from wit_core.api.http_server import app

client = TestClient(app)


def test_http_message_response(mocker):
    process_intent = mocker.patch("wit_core.api.http_server.process_intent", return_value="Message processed")

    response = client.post("/message", json={"message": "Message input"})

    process_intent.assert_called_with("Message input")
    assert response.status_code == 200
    assert response.json() == {"res": "Message processed"}


def test_http_message_response_error(mocker):
    mocker.patch("wit_core.api.http_server.process_intent", side_effect=Exception("No intents were found for the question"))

    response = client.post("/message", json={"message": "Message input"})

    assert response.status_code == 500
    assert response.json() == {"detail": "Error processing message"}


def test_http_message_response_empty_string(mocker):
    response = client.post("/message", json={"message": ""})

    assert response.status_code == 500
    assert response.json() == {"detail": "Not allowed empty string"}
