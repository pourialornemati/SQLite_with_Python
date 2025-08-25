import sqlite3
from sqlite3 import Error

def sql_conncetor(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    return con, cur

def delete_data(con, cur):
    cur.execute("""DELETE FROM registration WHERE id == 2""")
    con.commit()

con, cur = sql_conncetor('mydatabase.db')
delete_data(con, cur)

