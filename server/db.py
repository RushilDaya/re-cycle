import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()
fd = open('schema.sql','r')
script = fd.read()
fd.close()
cursor.executescript(script)
fd = open('init_data.sql','r')
script = fd.read()
fd.close()
cursor.executescript(script)
db.close()
