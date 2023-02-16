from fastapi import FastAPI
from requests import request
from pydantic import BaseModel
from typing import List
# from db import DB
from sql_server_db import DB
# Inherits so we don't need __init__
# Basically makes this a dataclass
class Todo(BaseModel):
    id: int = None
    title: str
    description: str

app = FastAPI()
# db = DB("todo.db")
db = DB()


@app.get("/")
def root():
    data = db.call_db()
    return data

@app.get("/get_todos")
def get_todos():
    get_todos_query = """
    SELECT * FROM todo
    """
    data = db.call_db(get_todos_query)
    todos = []
    for i in data:
        id, title, description = i
        todos.append(Todo(id=id, title=title, description=description))
    print(data)
    return todos

@app.get("/todo/{id}")
def get_todo_by_id(id: int):
    return "Returns a single task: " + str(id)

#When running in TC to check if it works, make sure the right CRUD is used
@app.post("/add_todo")
def add_todo(todo: Todo):

    insert_into_query = """
    INSERT INTO todo (title, description)
    VALUES (?, ?)
    """
    db.call_db(insert_into_query, todo.title, todo.description)


    return "Adds a task "

@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    delete_query = """
    DELETE FROM todo WHERE id = ?
    """
    db.call_db(delete_query, id)
    return True

@app.put("/update_todo/{id}")
def update_todo(id: int, new_todo: Todo):

    update_query = """
    UPDATE todo
    SET title = ?, description = ?
    WHERE id = ?
    """
    db.call_db(update_query, new_todo.title, new_todo.description, id)
    return "Will update task with id: " + str(id)