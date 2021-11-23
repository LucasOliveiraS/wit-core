from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ..core.process import process_intent


class Message(BaseModel):
    message: str


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/message")
async def message(message: Message):
    if not message.message:
        raise HTTPException(status_code=500, detail="Not allowed empty string")

    try:
        response = process_intent(message.message)
        return {"res": response}
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Error processing message" + str(error)
        )
