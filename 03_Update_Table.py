import sqlite3
from sqlite3 import Error

def sql_conncetor(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    return con, cur

def update_data(con, cur):
    cur.execute("UPDATE registration SET name = 'Paria' WHERE id= 2")
    con.commit()

con, cur = sql_conncetor('mydatabase.db')
update_data(con, cur)