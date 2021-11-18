import os
import json
import requests
from decouple import config
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
from flask_bcrypt import Bcrypt
from cs50 import SQL
from flask_session import Session
from tempfile import mkdtemp
from flask_helper import login_required
# from flask_wtf.csrf import CSRFProtect
from helper import forecast_api_request, get_city
import pdb


app = Flask(__name__)


# App Configs

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
bcrypt = Bcrypt(app)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# CSRF
# csrf = CSRFProtect()
# csrf.init_app(app)

# API key
API_KEY = config('API_KEY')

# DB
db = SQL("sqlite:///temp.db")

# Assets
with open('updated_city.list.json') as f:
    CITY_DATA = json.load(f)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def index_test():
    return render_template('index_test.html')


@app.route('/filter_cities', methods=['GET', 'POST'])
def filter_cities():
    # breakpoint()
    input_city = request.json['city'].lower()

    filtered = []
    for city in CITY_DATA:
        if city['name'].lower().startswith(input_city):
            filtered.append(city)
    filtered = filtered[:10]
    return jsonify(filtered)


@app.route('/fetch', methods=['POST', 'GET'])
def fetch():

    city_id = request.json['id']
    # city_name = request.json['name'].lower()
    url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}'

    # OpenWeather response
    response = requests.get(url).json()
    if response.get('cod') != 200:
        message = response.get('message', '')
        return jsonify({'error': message})
    else:
        weather_dict = forecast_api_request(response, API_KEY)
        city = get_city(CITY_DATA, city_id)
        if city:
            weather_dict['current']['state'] = city['state']

    # Populate save/unsave button
    if session.get("user_id"):
        user_cities = db.execute("select * from cities where user_id = ?", session["user_id"])
        if int(city_id) in [int(c['city_id']) for c in user_cities]:
            weather_dict['saved'] = True
        else:
            weather_dict['saved'] = False
        weather_dict['session'] = session["user_id"]

    return jsonify(weather_dict)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(username) == 0 or len(request.form.get('password')) == 0:
            flash("Must fill in username and password", 'danger')
        if len(rows) > 0:
            flash("Username already existed", 'info')
        elif request.form.get('password') != request.form.get('confirm_password'):
            flash("Passwords not matching", 'danger')
        elif len(request.form.get('password')) < 8 or not any(c.isdigit() for c in request.form.get('password')) or not any(c.isalpha() for c in request.form.get('password')):
            flash("Passwords has to be at least 8 charaters and contain at least one number and one letter", "info")
        else:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, bcrypt.generate_password_hash(request.form.get('password')))
            rows = db.execute("SELECT * FROM users WHERE username = ?", username)
            session["user_id"] = rows[0]["id"]

            flash(f'Account created for {username}! You are now able to save favorite cities', 'success')
            return redirect('/')
    return render_template('register.html', title='Register')



@app.route('/login', methods=['GET', 'POST'])
def login():

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        if True: # check for validation
            username = request.form.get("username")
            if len(username) == 0 or len(request.form.get('password')) == 0:
                flash("Must fill in username and password", 'danger')

            rows = db.execute("SELECT * FROM users WHERE username = ?", username)
            if len(rows) < 1:
                flash("No username found", 'danger')
            elif bcrypt.check_password_hash(rows[0]["hash"], request.form.get("password")):
                # save user session
                session["user_id"] = rows[0]["id"]

                flash('You have been logged in!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Unsuccessful.', 'danger')
    return render_template('login.html', title='Login')


@app.route('/logout')
@login_required
def logout():
    # Forget any user_id
    session.clear()
    return redirect(url_for('index'))


@app.route('/account')
@login_required
def account():
    cities = db.execute("select * from cities where user_id = ?", session["user_id"])
    #cities = [i["name"].title() for i in user_cities]
    print(cities)
    return render_template('account.html', title='Account', cities=cities)


@app.route('/save_city', methods=['GET', 'POST'])
@login_required
def save_city():
    if session.get("user_id"):
    # check if city was added
        city_id = request.json['id']
        city = get_city(CITY_DATA, city_id)

        if city:
            name = city['name'].lower()
            state = city['state'].lower()
            country = city['country'].lower()
            user_cities = db.execute("select * from cities where user_id = ?", session["user_id"])
            if city_id not in [c['city_id'] for c in user_cities]:
                db.execute("INSERT into cities (user_id, city_id, name, state, country) VALUES (?, ?, ?, ?, ?)",
                session["user_id"], city_id, name, state, country)
    else:
        #return jsonify({'error': "error"})
        print('failed here')
        return redirect(url_for('login'))

    return jsonify({'status': True})


@app.route('/unsave_city', methods=['GET', 'POST'])
@login_required
def unsave_city():

    if session.get("user_id"):
    # check if city is saved
        city_id = request.json['id']
        city = get_city(CITY_DATA, city_id)
        if city:
            name = city['name'].lower()
            state = city['state'].lower()
            country = city['country'].lower()
            user_cities = db.execute("select * from cities where user_id = ?", session["user_id"])
            if city_id not in [c['city_id'] for c in user_cities]:
                db.execute("delete from cities where user_id = ? and city_id = ?", session["user_id"], city_id)
    else:
      flash('Please Login First', 'danger')
      print('failed here')
      return jsonify({'status': False})
    return jsonify({'status': True})



def init_db():

    query1 = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER ,
        username TEXT NOT NULL,
        hash TEXT NOT NULL,
        PRIMARY KEY(id)
        )"""
    db.execute(query1)
    query2 = """CREATE TABLE IF NOT EXISTS cities (name TEXT NOT NULL
    , state TEXT
    , country TEXT
    , city_id INTEGER NOT NULL
    , user_id INTEGER NOT NULL
    , FOREIGN KEY (user_id) REFERENCES users (id))
    """
    db.execute(query2)

    print('ran this')
    # Create a test user
    rows = db.execute("select * from users where username = ?", 'u123')
    if len(rows) == 0:
        test_user = "INSERT into users (username, hash) VALUES (?, ?)"
        test_cities = "INSERT into cities (name, user_id, city_id) VALUES (?, ?, ?)"
        db.execute(test_user, "u123", bcrypt.generate_password_hash('aaaaaaaa'))
        db.execute(test_cities, "boston", 1, 4930956)
        print(db.execute("select * from users")[0])
        print(db.execute("select * from cities")[0])
    return None


if __name__ == '__main__':
    init_db()
    app.run(debug=False)
