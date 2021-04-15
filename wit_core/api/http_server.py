from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ..core.process import process_intent


class Message(BaseModel):
    message: str


app = FastAPI()


@app.post("/message")
async def message(message: Message):
    if not message.message:
        raise HTTPException(status_code=500, detail="Not allowed empty string")

    try:
        response = process_intent(message.message)
        return {"res": response}
    except Exception:
        raise HTTPException(status_code=500, detail="Error processing message")
