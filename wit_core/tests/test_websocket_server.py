import pytest
from fastapi.testclient import TestClient

from wit_core.api.websocket_server import app

client = TestClient(app)


def test_send_and_receive_message(mocker):
    process_intent = mocker.patch("wit_core.api.websocket_server.process_intent", return_value="Message processed")

    with client.websocket_connect("/message") as websocket:
        websocket.send_text("Test message")
        data = websocket.receive_text()

        process_intent.assert_called_with("Test message")
        assert data == "Message processed"


def test_receive_message_error(mocker):
    mocker.patch("wit_core.api.websocket_server.process_intent", side_effect=Exception("Some exception"))

    with client.websocket_connect("/message") as websocket:
        websocket.send_text("Test message")
        data = websocket.receive_text()

        assert data == "Some exception"
