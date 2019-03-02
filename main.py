import sqlite3
from flask import Flask, render_template, jsonify


app = Flask(__name__)


class Ranking:
    def __init__(self, args):
        self.id = args[0]
        self.name = args[1]
        self.userdiscount = args[1]


class Discount:
    def __init__(self, args):
        self.name = args[0]
        self.url = args[1]
        self.img = args[2]
        self.userdiscount = args[3]


class User:
    def __init__(self, args):
        self.id = args[0]
        self.name = args[1]
        self.surname = args[2]
        self.age = args[3]
        self.budget = args[4]
        self.discount_diff = args[5]
        self.company = args[6]
        self.city = args[7]


class Route:
    def __init__(self, args):
        self.route_date = args[0]
        self.km = args[1]


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/api/user/<int:id>')
def get_user(user_id):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM user WHERE id = ?;', (user_id,))
    objUser = User(cursor.fetchone())
    json_out = jsonify(objUser.__dict__)
    db.close()
    return json_out


@app.route('/api/user/km/<int:user_id>')
def get_user_routes(user_id):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('SELECT route_date, total_km FROM route '
                   'WHERE user_id = ?;', (user_id,))
    dates = []
    kms = []
    for row in cursor.fetchall():
        dates.append(row[0])
        kms.append(row[1])
    db.close()
    return jsonify({'dates': dates, 'kms': kms})


@app.route('/api/city/<int:id>')
def city(id):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM city WHERE id = ?;', (id,))
    objCity = Discount(cursor.fetchone())
    json_out = jsonify(objCity.__dict__)
    db.close()
    return json_out
