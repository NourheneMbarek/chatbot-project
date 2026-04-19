from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import Query, ChatResponse
from app.router import detect_intent
from app.tools import get_vacation_days
from app.rag import initialize_documents, search_documents


app = FastAPI(
    title="Simple Chatbot API",
    description="Chatbot using static documents and a mocked external service",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
def startup_event():
    initialize_documents("data")

@app.get("/")
def root():
    return {"message": "Backend running"}


@app.post("/chat", response_model=ChatResponse)
def chat(query: Query):
    intent = detect_intent(query.question)

    if intent == "TOOL_VACATION":
        data = get_vacation_days("user_1")
        return ChatResponse(
            answer=f"You have {data['remaining_days']} vacation days left.",
            type="tool",
            sources=[]
        )

    doc_result = search_documents(query.question)
    return ChatResponse(
        answer=doc_result["answer"],
        type="document",
        sources=doc_result["sources"]
    )