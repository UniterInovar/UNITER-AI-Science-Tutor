from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.ai.tutor import Tutor

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


class ChatRequest(BaseModel):
    subject: str
    message: str


@router.post("/ask")
def ask_ai(request: ChatRequest):
    """
    Ask the AI Tutor a science question.
    """

    return Tutor.ask(request.message)
