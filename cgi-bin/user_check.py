#!/usr/bin/env python3.4

import cgi, cgitb
import os
import sqlite3

cgitb.enable()

form = cgi.FieldStorage()
register_no = form.getvalue('register_no')
username = form.getvalue('username')
passwd = form.getvalue('password')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("</head>")
print("<body>")
print('<div style = "text-align:center ; "')
print("<h1><b>Login page</b></h1>")

## making a connection to the sqlite3 database
conn = sqlite3.connect('/home/tasdik/Downloads/souvik_refactoring/cgi-bin/user_base.db')
cur = conn.cursor()

## now to check whether the entered data is for
## -> new user 
## -> an old user

query = "SELECT * FROM users"
cur.execute(query)
print("<p>" , cur.fetchall, "</p>")
cur.execute('SELECT user_name FROM users WHERE reg_no = ?', (register_no,))
rows = cur.fetchall()

## mind you that the above variable "rows" is a list and stores all the entries, grouped together in
## a row. So if the user with the particular "register_no" does not exist in the database. "rows" will
## be an empty list 

print("<br><br>")
if len(rows) == 0:  ### if list is empty, we could also have done a "if not a:" but that is not that intuitive
    print("<p>User : <b>", username , "</b> does not exist.</p>")
    cur.execute('INSERT INTO users VALUES(?, ?, ?)', (register_no, username, passwd))
    conn.commit()
    print("<p>User was created successfully</p>")
    print("Done")
    print("</div>")
    
else:
    print("<p>Welcome<b>", username ,"</b>. Good to have you back")
    print("<br><p>Your account details</p>")
    print("<p><b>Register number : </b>", register_no, " </p>")
    print("<p><b>Username : </b> " , username, "</p>")
    print("</div>")