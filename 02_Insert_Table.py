import sqlite3
from sqlite3 import Error

def sql_conncetor(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    return con, cur

# Static Values: 
# def insert_data(con, cur):
#     cur.execute("""INSERT INTO registration 
#                 VALUES(1, 'Pouria', 'Nemati', 30)""")
#     con.commit()


# Dynamic Values: 
def insert_data(con, cur, entity):
    cur.execute("""INSERT INTO registration 
                VALUES(?, ?, ?, ?)""", entity)
    con.commit()

con, cur = sql_conncetor('mydatabase.db')
entity = (2, 'Parsa', 'Zarvandi', 29)
insert_data(con, cur, entity)
