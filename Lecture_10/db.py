import sqlite3

class DB:
    db_url: str

    def __init__(self, db_url: str):
        self.db_url = db_url

    def call_db(self, query, *args):
        con = sqlite3.connect(self.db_url)
        cur = con.cursor()
        res = cur.execute(query, args)
        data = res.fetchall()
        cur.close()
        con.commit()
        con.close()
        return data