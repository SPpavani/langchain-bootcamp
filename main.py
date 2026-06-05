
# backend/main.py
from fastapi import FastAPI
from services import get_briefing, manage_tasks, get_standup

app = FastAPI()

@app.get("/briefing")
def briefing():
    return get_briefing()

@app.post("/tasks")
def tasks(task: dict):
    return manage_tasks(task)

@app.get("/standup")
def standup():
    return get_standup()
