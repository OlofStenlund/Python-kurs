import pyodbc
db_server_name = "LAPTOP-8N1NGN33\SQLEXPRESS"
db_name = "lesson_todo"
db_driver = "ODBC Driver 17 for SQL Server"

# no spaces between
connection_string = f"""
DRIVER={db_driver};
SERVER={db_server_name};
DATABASE={db_name};
trusted_connection=yes;
"""




class DB:

    def init_db(self):
        # Add if not exists-statement
        init_db_query = """
        IF OBJECT_ID('dbo.todo', 'U') IS NULL
        CREATE TABLE todo (
        id INTEGER IDENTITY(1,1) PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL
        ) 
        """
        insert_start_query = """INSERT INTO todo (title, description)
        VALUES ('Do this!', 'Dont do this please?')
        """
        con = pyodbc.connect(connection_string)
        con.execute(init_db_query)
        con.execute(insert_start_query)
        con.commit()
        con.close()

        # self.call_db(init_db_query)
        # self.call_db(insert_start_query)

    def call_db(self, query, *args):
        data = None
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor()
        # Cursor  should not be created whening select?
        if "SELECT" in query:
            res = cur.execute(query, args)
            data = res.fetchall()
            cur.commit()
            cur.close()
        else:
            conn.execute(query, args)
        conn.commit()
        conn.close()
        return data

if __name__ == '__main__':

    db = DB()
    db.init_db()
