import sqlite3
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__,
            static_folder="./frontend/dist/static",
            template_folder="./frontend/dist")
CORS(app)


class Ranking:
    def __init__(self, args):
        self.id = args[0]
        self.name = args[1]
        self.totalkm = args[2]


class Discount:
    def __init__(self, args):
        self.name = args[0]
        self.url = args[1]
        self.img = args[2]
        self.tax = args[3]
        self.company_rate = args[4]
        self.user_rate = args[5]


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
        self.total_kms = args[8]


class Route:
    def __init__(self, args):
        self.route_date = args[0]
        self.km = args[1]


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")


#@app.route("/")
#def hello():
#    return "Hello World!"


@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute(
        'SELECT user.id, user.name, surname, age, budget, discount_percent, company.name, city.name, sum(route.total_km) '
        'FROM user '
        'INNER JOIN company ON user.id = company.id '
        'INNER JOIN city ON user.id = city.id '
        'INNER JOIN route ON user.id = route.user_id '
        'WHERE user.id = ? '
        'GROUP BY user.id;', (user_id,))

    obj_user = User(cursor.fetchone())
    json_out = jsonify(obj_user.__dict__)

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


@app.route('/api/topfive/<request_type>')
def topfive(request_type):
    json_out = []
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    if request_type == 'users':
        sql_txt = 'SELECT user.id, (user.name || " " || user.surname) AS name, sum(total_km) as total ' \
                  'FROM user ' \
                  'LEFT JOIN route ON user.id = user_id ' \
                  'GROUP BY user.id ' \
                  'ORDER BY total ' \
                  'DESC LIMIT 5;'
    elif request_type == 'cities':
        sql_txt = 'SELECT city.id, city.name, sum(total_km)/COUNT(DISTINCT user.id) as avg ' \
                  'FROM user JOIN city ON user.city_id=city.id ' \
                  'LEFT JOIN route ON user.id = user_id ' \
                  'GROUP BY user.city_id ' \
                  'ORDER BY avg ' \
                  'DESC LIMIT 5;'
    elif request_type == 'companies':
        sql_txt = 'SELECT company.id, company.name, sum(total_km)/COUNT(DISTINCT user.id) as avg ' \
                  'FROM user JOIN company ON user.company_id=company.id ' \
                  'LEFT JOIN route ON user.id = user_id ' \
                  'GROUP BY user.company_id ' \
                  'ORDER BY avg ' \
                  'DESC LIMIT 5;'

    cursor.execute(sql_txt)
    for row in cursor.fetchall():
        objRank = Ranking(row)
        json_out.append(objRank.__dict__)
    db.close()
    return jsonify(json_out)


@app.route('/api/discount/<int:id>')
def discount(id):
    json_out = []
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute(
        'SELECT discount.name, url, img, tax, discount_rate, discount_percent ' \
        'FROM user JOIN discount ' \
        'WHERE user.id = ?;', \
        (id,))
    for row in cursor.fetchall():
        objDiscount = Discount(row)
        json_out.append(objDiscount.__dict__)
    db.close()
    return jsonify(json_out)
