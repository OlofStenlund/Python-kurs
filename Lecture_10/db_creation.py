from db import DB

db = DB("people.db")

create_query = """
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY,
    name TEXT,
    title TEXT,
    mail TEXT,
    tel TEXT
    )
"""

db.call_db(create_query)