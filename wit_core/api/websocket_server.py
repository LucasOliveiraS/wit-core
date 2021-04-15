from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from ..core.process import process_intent


app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)


manager = ConnectionManager()


@app.websocket("/message")
async def message(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            response = process_intent(data)

            await manager.send_personal_message(response, websocket)
    except Exception as error:
        await manager.send_personal_message(str(error), websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.send_personal_message(
            "Disconnected from server",
            websocket
        )
