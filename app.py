from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from typing import List

from models import User, Feedback

app = FastAPI()

# хранилище для отзывов
feedbacks: List[Feedback] = []

# задание 1.1
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

# задание 1.2
@app.get("/html", response_class=HTMLResponse)
async def read_html():
    return FileResponse("index.html")

# задание 1.4
@app.get("/users")
async def get_users():
    user = User(name="Александра Казакова", id=1)
    return user

# задание 2.1
@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}