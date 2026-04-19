from pydantic import BaseModel


class Query(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    type: str
    sources: list[str] = []