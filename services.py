# backend/services.py
def get_briefing():
    return {"message": "Morning briefing goes here"}

def manage_tasks(task):
    return {"message": f"Task received: {task}"}

def get_standup():
    return {"message": "Standup summary goes here"}

