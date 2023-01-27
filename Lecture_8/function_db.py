import sqlite3

def call_db(query: str):
    connection = sqlite3.connect("test.db") # create a connection to the database
    cursor = connection.cursor() # create cursor to perform query
    res = cursor.execute(query) # execute query, save result as res
    data = res.fetchall() # get all from res, save in "data"
    cursor.close() # end query
    connection.commit() # commit, actually execute the thing?
    connection.close() # Close connection to database
    return data # return the result from the query
    
query = """
CREATE TABLE IF NOT EXISTS person(
    id INTEGER PRIMARY KEY,
    firstname VARCHAR(80),
    lastname VARCHAR(80),
    motto VARCHAR(80)
)
"""

query ="""
SELECT name FROM test
"""

data = call_db(query)
print(data)
