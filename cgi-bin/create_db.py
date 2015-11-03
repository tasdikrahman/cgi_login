#!/usr/bin/env python3.4

import sqlite3
import os

db_name = "user_base.db"

if db_name in os.listdir():
    print("removing the user_base.db and creating a fresh copy of it")
    os.system("rm user_base.db")

print("Creating the database")
conn = sqlite3.connect(db_name)
cur = conn.cursor()

user_table = "CREATE TABLE users(reg_no INTEGER PRIMARY KEY, user_name TEXT, pass TEXT)"

new_users = (
    (1081310251, 'admin', 'admin'),
    (1081310234, 'foo', 'admin123')
)

cur.execute(user_table)
print("table created")
cur.executemany('INSERT INTO users VALUES(?, ?, ?)', new_users)
conn.commit()
print("default users created \n\ndisplaying them")

cur.execute('SELECT * FROM users')
print(cur.fetchall())