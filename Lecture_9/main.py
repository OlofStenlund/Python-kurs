# from fastapi import FastAPI
# import sqlite3

# from pydantic import BaseModel

# app = FastAPI()

# def call_db(query: str, *args):
#     connection = sqlite3.connect("api.db")
#     cursor = connection.cursor()
#     res = cursor.execute(query, args) 
#     data = res.fetchall()
#     cursor.close() 
#     connection.commit() 
#     connection.close() 
#     return data
    
# def populate_database():
#     connection = sqlite3.connect("api.db")
#     cur = connection.cursor()
#     cur.execute(
#             "CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL)"
#     )
#     cur.execute("INSERT INTO person (name) VALUES ('Olof')")
#     cur.execute("INSERT INTO person (name) VALUES ('Anna')")
#     cur.execute("INSERT INTO person (name) VALUES ('Linus')")
#     cur.execute("INSERT INTO person (name) VALUES ('Walid')")
#     cur.close
#     connection.commit()
#     connection.close()


# @app.get("/")
# def root():
#     return "Hello World"



# @app.get("/test")
# def root():
#     print("Update works?")
#     return "Hello Test no workie? give me food"

# @app.get("/test2")
# def root():
#     return "Hello Testare? See this!"

# @app.get("/test2/populate")
# def root():
#     populate_database()
#     return "Kan vi får detta att funk?"



# @app.get("/person")
# def get_person():
#     person_query = """
#     SELECT * FROM person
#     """
   
#     people = call_db(person_query)
#     print(people)
#     return people

# # introduce variableS, dynamic parameter
# @app.get("/person/{id}")
# def get_person_by_id(id: int):
#     get_person_query = """
#     SELECT * FROM person WHERE id = ?
#     """
#     data = call_db(get_person_query, id)
#     return data

# # routes are evaluated top to bottom. First one first.
# # Since the above has person/{dynamic}, we will be directed there.
# # If we follow this with person/{dynamic}, intending to get something else, it will not work.
# # Instead, we create a different rouse
# @app.get("/person/name/{name}")
# def get_person_by_name(name: str):
#     get_person_query = """
#     SELECT * FROM person WHERE name = ?
#     """
#     data = call_db(get_person_query, name)
#     return data

# # Send in multiple arguments/parameter
# @app.get("/person/getperson/") # must use / after? Because we sent in parameters?
# def get_person(name: str = None, age: int = None):
#     print("vad vill du?", name, age)
#     return name, age

# # person/getperson/?name=olof&age=3 
# # Prints name (olof) and age(33) in terminal, and returns to route
# # By setting default values (= None) all value are not required
# # Get requests are not meant to insert data into the database, for that we use post.
# # (if we want to keep track of get requests, we can use then to insert data though.)

# # post data (as opposed to getting data as we did before)
# # Can reuse a URL ("route") because they do different things???

# # We will use the extension thunder client, which is based on Pydantic 
# # So we will need to create a class which is an extension of the BaseModel from Pydantic
# # For reasons?

# class Person(BaseModel):
#     name: str = None # These are the attributes of the object. Set default to avoid errors
#     age: int = None
#     mail: str = None


# @app.post("/person/getperson/")
# def post_person(person: Person): # take person object (of class Person) as argument
#     print(person)
#     return "Hallo", person
    
