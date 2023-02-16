from fastapi import FastAPI
from models import Person
from db import DB


app = FastAPI()
db = DB("people.db")

@app.get ("/")
def root():
    return "Root"

@app.get("/people")
def get_people():
    get_people_query = """
    SELECT * FROM people
    """
    data = db.call_db(get_people_query)
    return data

@app.post("/create_person")
def create_person(person: Person):
    create_person_query = """
    INSERT INTO people (
        name,
        title,
        mail,
        tel
        ) VALUES (
        ?, ?, ?, ?
        )
    """
    # person refers to the argument of create_person() which is a person object created or line 97 main.py
    db.call_db(create_person_query, person.name, person.title, person.mail, person.tel)
    return person
    

@app.get(f"/people/{id}")
def get_person_by_id(id: int):
    get_person_by_id_query = """
    SELECT * FROM people
    WHERE id = ?
    """
    data = db.call_db(get_person_by_id_query, id)
    return data

@app.delete("/delete_duplicates")
def delete_duplicates():
    remove_duplicates_query = """
    DELETE FROM people
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM people
        GROUP BY name
        )
    """
    db.call_db(remove_duplicates_query)
    print("Removed")