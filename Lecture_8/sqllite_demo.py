import sqlite3

# connection is a variable
# if no database exists, sqllite will create one
connection = sqlite3.connect("test.db")
# Creates a database IN THE FOLDER WHICH YOU ARE IN IN THE TERMINAL
# If the database exists, it will not create one but connect to it.
# Will it only connect if it's in the same folder?

# Install extension sqllite viewer

# Cursor points a t things to excecute
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name VARCHAR(80));")
cursor.execute("CREATE TABLE IF NOT EXISTS test2 (id INTEGER PRIMARY KEY, name VARCHAR(80));")
cursor.execute("CREATE TABLE IF NOT EXISTS test3 (id INTEGER PRIMARY KEY, name VARCHAR(80));")
# Right klick on database and chose open with sqllite viewer

# sqllite is auto incrementing PK
# Insert info into table "test"
cursor.execute("INSERT INTO test (name) VALUES ('Olof')")
# Must commit the changes before it's updated
# connection.commit()
cursor.execute("INSERT INTO test (name) VALUES ('Grisen')")
cursor.execute("INSERT INTO test (name) VALUES ('Leffe')")
cursor.execute("INSERT INTO test (name) VALUES ('Omar')")
# use string stored in variable
person_insert = """
INSERT INTO test(
    name
) VALUES (
    'Tove'
)
"""
cursor.execute(person_insert)

# Each time you runt the file, these names will be added again

# Drop table:
cursor.execute("DROP TABLE test2")
cursor.execute("DROP TABLE test3")


res = cursor.execute("SELECT name FROM test")
# res is cursor object, menaing we can use res.fetchall() etc.
data = res.fetchone() # Fetchone "returns the first as an iterator, then if I call it again, the next object that fits"
# In the above example, we selected name from "master" (all?) and iot will fetch the first result. Next time we run it will fetch the second.
print(data)
data = res.fetchone()
print(data)
data = res.fetchone()
print(data)
# Returns None if we run out of results to fetch 

alldata = res.fetchall() # Fetches all that has not been fetched yet?
# print(alldata)






# Committhe changes
connection.commit()

# Close the connection before exiting
cursor.close()
connection.close()