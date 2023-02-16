import sqlite3

def call_db(query: str, *args):
    connection = sqlite3.connect("test.db") # create a connection to the database
    cursor = connection.cursor() # create cursor to perform query
    res = cursor.execute(query, args) # execute query, save result as res. Args to take in values for wuery later
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

# query ="""
# SELECT name FROM test
# """
call_db(query)
# data = call_db(query)
# print(data)

insertquery = """
    INSERT INTO person(
    firstname,
    lastname,
    motto
    )
    VALUES(
    ?,
    ?,
    ?
    )
"""
# ? are used as placeholders. We take in values as arguments when calling th function using the query

# call_db(insertquery)

query_person = """
SELECT * FROM person
"""

data = call_db(insertquery, "Jack", "Sparrow", "Why is the rum gone?") # insertquery takes arguments

people = call_db(query_person)
print(people)