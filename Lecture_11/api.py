from fastapi import FastAPI
from requests import request
from pydantic import BaseModel
from typing import List

# Inherits so we don't need __init__
# Basically makes this a dataclass
class Todo(BaseModel):
    id: int = None
    title: str
    description: str

app = FastAPI()

app.curr_id = 1 # Makes curr_id an atribute of the app
# When we connect to database, this list and shit will not be needed
app.todos: List[Todo] = []



@app.get("/")
def root():
    return "General Kenobi!"

@app.get("/get_todos")
def get_todos():
    return app.todos

@app.get("/todo/{id}")
def get_todo_by_id(id: int):
    return "Returns a single task: " + str(id)

#When running in TC to check if it works, make sure the right CRUD is used
@app.post("/add_todo")
def add_todo(todo: Todo):
    print(todo)
    todo.id = app.curr_id
    app.todos.append(todo)
    app.curr_id += 1
    return "Adds a task "

@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    # app.todos refers to the list we store that objects in.
    # Lambda function does something, only keeps the todos with id other thatn the entered
    app.todos = list(filter(lambda x: x.id != id, app.todos))   

    return True

@app.put("/update_todo/{id}")
def update_todo(id: int, todo: Todo):
    return "Will update task with id: " + str(id)