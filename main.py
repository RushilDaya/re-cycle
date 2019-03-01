import sqlite3
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello World!"

@app.route('/list')
def list():
	db = sqlite3.connect('database.db')
	#db.row_factory = sql.Row
	cursor = db.cursor()

	cursor.execute('''SELECT * FROM user LIMIT 1;''')
	#rows = cur.fetchall(); 
	
	return str(cursor.fetchone())#render_template("list.html",rows = rows)