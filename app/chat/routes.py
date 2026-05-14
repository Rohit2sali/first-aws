from fastapi import APIRouter

from app.chat.schemas import ChatRequest
from app.chat.service import process_chat

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def chat(data: ChatRequest):

    response = process_chat(data.prompt)

    return {
        "response": response,
    }