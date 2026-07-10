from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.ai.tutor import Tutor

router = APIRouter(prefix="/ai", tags=["AI"])


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_ai(request: QuestionRequest):
    """
    Ask the AI tutor a science question.
    """

    answer = Tutor.ask(request.question)

    return answer