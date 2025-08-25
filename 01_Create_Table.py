import sqlite3
from sqlite3 import Error


try:
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()
    cur.execute(
    """CREATE TABLE IF NOT EXISTS registration
    (
    id integer PRIMARY KEY,
    name TEXT,
    family_name TEXT,
    age integer
    )"""
    )
    con.commit()
except Error:
    print(Error)

finally:
    con.close()
