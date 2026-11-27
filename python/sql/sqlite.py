import sqlite3

con = sqlite3.connect('my_database.db')
cur = con.cursor()

tab = '''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)'''
                   
cur.execute(tab)



sel = "SELECT * FROM users"
cur.execute(sel)

rows = cur.fetchall()
for row in rows:
    print(row)
    
"""Insert data into the table"""
#cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")


"""Inserting multiple records using executemany()"""

users_data = [
    ('Bob', 25),
    ('Charlie', 35),
    ('David', 28)
]

#cur.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_data)


sel = "SELECT * FROM users"
#cur.execute(sel)

rows = cur.fetchall()
for row in rows:
    print(row)


con.commit()
con.close()
