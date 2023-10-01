"""
create and connect to a SQLite database
"""

import sqlite3

# create a db
connection = sqlite3.connect("sample.db")

# query to create a table
table = 'CREATE TABLE people (id integer primary key, name TEXT, surname TEXT)'
# create cursor to execute query
cursor = connection.cursor()
# execute query
cursor.execute(table)
# commit execute
connection.commit()
