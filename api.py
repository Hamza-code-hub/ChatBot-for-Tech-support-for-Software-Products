from fastapi import FastAPI
from pydantic import BaseModel, Field

from supportgpt.engine import (
    SupportEngine,
)


app = FastAPI(
    title="SupportGPT AI API",
    description=(
        "Technical-support assistant "
        "for software products."
    ),
    version="1.0.0",
)

engine = SupportEngine()


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=5000,
    )


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "SupportGPT AI",
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return engine.answer(
        request.message
    )
