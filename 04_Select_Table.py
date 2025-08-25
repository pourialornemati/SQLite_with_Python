import sqlite3
from sqlite3 import Error

def sql_conncetor(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    return con, cur

# Selecting all part of a database table:
def select_data(con, cur):
    cur.execute("SELECT * FROM registration")
    return cur.fetchall()

# Selecting a specific part of a database table:
# def select_data(con, cur):
#     cur.execute("SELECT name, age FROM registration  WHERE age < 30")
#     return cur.fetchall()

con, cur = sql_conncetor('mydatabase.db')
data = select_data(con, cur)

for item in data:
    print(item)
