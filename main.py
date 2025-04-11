from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from genai_utils import summarize_reviews, answer_question

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReviewInput(BaseModel):
    reviews: str

class QAInput(BaseModel):
    reviews: str
    question: str

@app.post("/api/summarize")
def summarize_endpoint(data: ReviewInput):
    summary = summarize_reviews(data.reviews)
    return {"summary": summary}

@app.post("/api/chat")
def chat_endpoint(data: QAInput):
    answer = answer_question(data.reviews, data.question)
    return {"answer": answer}