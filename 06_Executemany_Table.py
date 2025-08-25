import sqlite3
from sqlite3 import Error

def sql_conncetor(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    return con, cur

def insert_many(con, cur, entity):
    cur.executemany("""INSERT INTO registration 
                VALUES(?, ?, ?, ?)""", entity)
    con.commit()

con, cur = sql_conncetor('mydatabase.db')
entity = [(4, 'Andy', 'Maleki', 35), 
          (5, 'Maryam', 'Azad', 18),
          (6, 'Nastaran', 'Sam', 20),
          (7, 'Veronika', 'Azad', 21)]
insert_many(con, cur, entity)

